# Phase-2 Crawl Worker Instructions (peers)

You are a crawl worker for the 15-book OCI docs crawl. Work autonomously;
report back to the dispatcher (your A2A caller) exactly ONCE when done.

## Setup (once)
1. Check for an existing clone: `ls ~/oracle-docs-clone` — if present,
   `cd ~/oracle-docs-clone && ./work.sh <your-agent-id> sync`.
   If absent: `git clone https://github.com/axb0987/Oracle-DOCS.git
   ~/oracle-docs-clone && cd ~/oracle-docs-clone`.
2. Confirm you can reach GitHub: `git pull --rebase` must succeed.
   If git AUTH fails on pull/push (401/403/insufficient permissions):
   STOP. Report the exact error line to your dispatcher and do not
   continue. Do not print the failing credentials in your report.

## Run your shard
```
cd ~/oracle-docs-clone
./work.sh <your-agent-id> sync
mkdir -p pages-all
nohup python3 crawl_shard.py file shards/<your-agent-id>.pages 0.7 > pages-all/run-<your-agent-id>.log 2>&1 &
```
- `<your-agent-id>` is exactly what the dispatcher named in the task
  (tars / plex).
- The crawl logs per-page to `pages-all/crawl-<shardslug>-S-L-of-L.csv`
  and prints a final summary to `pages-all/run-<your-agent-id>.log`.
- It is resumable: restarting it skips pages already in the CSV.
- Expected duration: several hours. Do NOT sit polling in the reply
  path — when the process exits, proceed to the commit step.

## Commit + mark done
Only commit YOUR files (never `git add -A`):
```
git add pages-all/crawl-*.csv pages-all/run-<your-agent-id>.log \
        pages-all/pages/*
git commit -m "[<your-agent-id>] phase-2 shard <your-agent-id> complete:
<fetch summary line from the run log>"
git push origin HEAD
./work.sh <your-agent-id> done <your-task-id> "<fetch summary line>"
```
Where `<your-task-id>` is `crawl-p2-<your-agent-id>`.

If `git push` fails on authentication, retry once after `sync`
(another worker's new commits may have landed). Still failing → mark
the task `blocked` with the error and report to the dispatcher.

## Report format (single message to dispatcher on completion)
```
WORKER <id> done
shard: shards/<id>.pages
fetched=N cached=M failed=F picked=P
commit: <sha> (on origin/main)
task: crawl-p2-<id> -> done
```
Plus the full final summary line from the run log. If the crawl
crashed instead: report the last 20 log lines and the task id; do
not silently give up.
