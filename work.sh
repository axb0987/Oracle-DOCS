#!/usr/bin/env bash
# work.sh — single entry point for agents in the shared-document workspace.
# Usage:
#   ./work.sh <agent> sync
#   ./work.sh <agent> claim <task-id>
#   ./work.sh <agent> done  <task-id> "summary"
#   ./work.sh <agent> block <task-id> "reason"
#   ./work.sh <agent> status
#   ./work.sh <agent> log
# Per-agent git identity is derived from <agent>. Push only succeeds once a
# remote exists (set with: git remote add origin <url>  — see README).
set -euo pipefail

AGENT="${1:?usage: work.sh <agent> <sync|claim|done|block|status|log> [task-id] [note]}"
CMD="${2:?missing command}"
REPO="$(cd "$(dirname "$0")" && pwd)"
cd "$REPO"

git config user.name  "$AGENT"
git config user.email "${AGENT}@agents.shared"

remote="$(git remote get-url origin 2>/dev/null || true)"
push() { [ -n "$remote" ] && git push origin HEAD || echo "(no remote configured; commits local-only)"; }

sync_all() { git pull --rebase --autostash 2>/dev/null || git pull --rebase || true; }

set_task() { python3 - "$@" <<'PY'
import json, sys
path = "tasks.json"
data = json.load(open(path))
cmd, task_id = sys.argv[1], sys.argv[2]
owner = sys.argv[3]
note  = sys.argv[4] if len(sys.argv) > 4 else None
task = next((t for t in data["tasks"] if t["id"] == task_id), None)
if task is None:
    sys.exit(f"no such task id: {task_id}")
conflict = task["status"] == "in-progress" and task["owner"] not in (None, owner)
if conflict and cmd in ("claim",):
    sys.exit(f"CONFLICT: task {task_id} is in-progress under {task['owner']}; back off (protocol rule 2)")
task["owner"] = owner
task["note"] = note or task.get("note", "")
task["updated"] = __import__("datetime").datetime.now(__import__("datetime").timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
if cmd == "claim":  task["status"] = "in-progress"
if cmd == "done":   task["status"] = "done"
if cmd == "block":  task["status"] = "blocked"
json.dump(data, open(path, "w"), indent=2)
open(path, "a").write("\n")
PY
}

commit_task() {
  local msg="$1"
  git add tasks.json plan.md
  git commit -m "[$AGENT] $msg"
  push
}

case "$CMD" in
  sync)
    sync_all
    echo "synced."
    ;;
  claim)
    TASK="${3:?usage: work.sh <agent> claim <task-id>}"
    sync_all
    set_task claim "$TASK" "$AGENT" ""
    commit_task "claim $TASK"
    echo "claimed $TASK as $AGENT. Write to your section in plan.md now."
    ;;
  done)
    TASK="${3:?usage: work.sh <agent> done <task-id> \"summary\"}"
    NOTE="${4:?missing summary}"
    sync_all
    # verify ownership before marking done
    OWNER="$(python3 -c "import json;print(next(t['owner'] for t in json.load(open('tasks.json'))['tasks'] if t['id']=='$TASK'))")"
    if [ "$OWNER" != "$AGENT" ]; then
      echo "REFUSED: $TASK is owned by $OWNER, not $AGENT (protocol rule 4)." >&2
      exit 1
    fi
    set_task done "$TASK" "$AGENT" "$NOTE"
    commit_task "done $TASK: $NOTE"
    echo "marked $TASK done."
    ;;
  block)
    TASK="${3:?usage: work.sh <agent> block <task-id> \"reason\"}"
    NOTE="${4:?missing reason}"
    sync_all
    set_task block "$TASK" "$AGENT" "$NOTE"
    commit_task "BLOCKED $TASK: $NOTE"
    echo "marked $TASK blocked — file a GitHub issue for humans (protocol rule 5)."
    ;;
  status)
    python3 - <<'PY'
import json
for t in json.load(open("tasks.json"))["tasks"]:
    print(f"{t['status']:<12} {t['id']:<16} owner={t['owner'] or '-':<10} {t['section']}  | {t['note'][:70]}")
PY
    ;;
  log)
    git log --oneline --format='%an | %s' -15
    ;;
  *)
    echo "unknown command: $CMD (sync|claim|done|block|status|log)" >&2
    exit 1
    ;;
esac
