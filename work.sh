#!/usr/bin/env bash
# work.sh — single entry point for agents in a shared-document workspace.
# Agent-agnostic: works for ANY agent that can run bash. One identity arg,
# fixed command set. See the workspace README.md for the full rulebook.
#
# Usage:
#   ./work.sh <agent> sync
#   ./work.sh <agent> claim <task-id>
#   ./work.sh <agent> done  <task-id> "summary"
#   ./work.sh <agent> block <task-id> "reason"
#   ./work.sh <agent> status
#   ./work.sh <agent> log
# Pushes happen automatically when a remote+upstream exist; without them the
# workspace works fully local (quiet no-op, no tracking errors).
set -euo pipefail

AGENT="${1:?usage: work.sh <agent> <sync|claim|done|block|status|log> [task-id] [note]}"
CMD="${2:?missing command (sync|claim|done|block|status|log)}"
REPO="$(cd "$(dirname "$0")" && pwd)"
cd "$REPO"

git config user.name  "$AGENT"
git config user.email "${AGENT}@agents.shared"

has_tracking() { git remote get-url origin >/dev/null 2>&1 && git rev-parse --abbrev-ref '@{upstream}' >/dev/null 2>&1; }
push() { if has_tracking; then git push origin HEAD; else echo "(local-only: no remote/upstream set — commits stay in the repo)"; fi; }
sync_all() { if has_tracking; then git pull --rebase --autostash; else true; fi; }

set_task() { python3 - "$@" <<'PY'
import json, sys, datetime
path = "tasks.json"
data = json.load(open(path))
cmd, task_id, owner = sys.argv[1], sys.argv[2], sys.argv[3]
note  = sys.argv[4] if len(sys.argv) > 4 else None
task = next((t for t in data["tasks"] if t["id"] == task_id), None)
if task is None:
    sys.exit(f"no such task id: {task_id} (known: {[t['id'] for t in data['tasks']]})")
if cmd == "claim" and task["status"] == "in-progress" and task["owner"] not in (None, owner):
    sys.exit(f"CONFLICT: task {task_id} is in-progress under {task['owner']}; back off (rule 3)")
task["owner"] = owner
if note:
    task["note"] = note
if cmd == "claim": task["status"] = "in-progress"
if cmd == "done":  task["status"] = "done"
if cmd == "block": task["status"] = "blocked"
data["updated"] = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
with open(path, "w") as f:
    json.dump(data, f, indent=2)
    f.write("\n")
PY
}

commit_task() {
  local msg="$1"
  git add tasks.json plan.md
  if git commit -q -m "[$AGENT] $msg"; then
    echo "[commit] $msg"
    push
  else
    echo "nothing to commit (no changes)" >&2
    exit 1
  fi
}

task_owner() { python3 -c "import json,sys;d=json.load(open('tasks.json'));print(next(t['owner'] or '' for t in d['tasks'] if t['id']=='$1'))" "$1"; }

case "$CMD" in
  sync)
    sync_all
    echo "synced." ;;
  claim)
    TASK="${3:?usage: work.sh <agent> claim <task-id>}"
    sync_all
    set_task claim "$TASK" "$AGENT" ""
    commit_task "claim $TASK"
    echo "claimed $TASK as $AGENT. Write ONLY that section in plan.md now (rule 2)." ;;
  done)
    TASK="${3:?usage: work.sh <agent> done <task-id> \"summary\"}"
    NOTE="${4:?missing summary — it lands in the audit trail, make it specific}"
    sync_all
    OWNER="$(task_owner "$TASK")"
    if [ "$OWNER" != "$AGENT" ]; then
      echo "REFUSED: $TASK is owned by '${OWNER:-nobody}', not $AGENT (rule 4). Do not take others' tasks (rule 5)." >&2
      exit 1
    fi
    set_task done "$TASK" "$AGENT" "$NOTE"
    commit_task "done $TASK: $NOTE" ;;
  block)
    TASK="${3:?usage: work.sh <agent> block <task-id> \"reason\"}"
    NOTE="${4:?missing reason}"
    sync_all
    OWNER="$(task_owner "$TASK")"
    if [ "$OWNER" != "$AGENT" ]; then
      echo "REFUSED: $TASK is owned by '${OWNER:-nobody}', not $AGENT (rule 4)." >&2
      exit 1
    fi
    set_task block "$TASK" "$AGENT" "$NOTE"
    commit_task "BLOCKED $TASK: $NOTE"
    echo "marked $TASK blocked — also file a GitHub issue with the reason (rule 6)." ;;
  status)
    python3 - <<'PY'
import json
for t in json.load(open("tasks.json"))["tasks"]:
    print(f"{t['status']:<12} {t['id']:<20} owner={t['owner'] or '-':<14} {t['section']}")
    print(f"{'':<12} note: {t.get('note','')[:100]}")
PY
    ;;
  log)
    git log --oneline --format='%an | %s' -20 ;;
  *)
    echo "unknown command: $CMD (sync|claim|done|block|status|log)" >&2
    exit 1 ;;
esac
