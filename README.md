# Shared Document Workspace — Multi-Agent Protocol

One repo = one shared document. Humans read `shared-docs/plan.md`; agents
coordinate through git.

## Layout
- `shared-docs/plan.md`   the shared document (append-ish, sectioned)
- `shared-docs/tasks.json` claim ledger: {id, section, status(open|in-progress|done|blocked), owner, note}
- `work.sh`               the only entry point agents should use

## Rules (all agents, no exceptions)
1. Claim before writing. `work.sh <agent> claim <task-id>` — commits a task
   row to `in-progress` with your owner. Pull first: `work.sh <agent> sync`.
2. One writer per section. If a claim commit you pulled already sets another
   owner on your task → back off, pick another open task or report to human.
3. Write to your section in `plan.md` (create it if absent, keep the
   `## Section` heading and its `### status` line current).
4. Done = `work.sh <agent> done <task-id> "summary"` — commits status flip
   + note to tasks.json, pushes.
5. Never rewrite another agent's section or their claims. If you spot a
   problem in someone else's section → file it as a GitHub issue with the
   section name, don't edit it.
6. Conflict in `tasks.json` on `sync` → the pull won by git; re-run `claim`
   (your commit will be rejected or you'll see the owner changed). Never
   hand-resolve someone else's claim line.
7. Commits are per-agent identities (work.sh sets user.name/email from the
   agent name), so `git log` is the audit trail.

## Human interface
- `shared-docs/plan.md` is the doc; GitHub issues = the message board.
- Optional: sync `plan.md` → Google Doc / SharePoint for viewers; the git
  repo stays the source of truth (writers never write to the office copies).
