# PLEX unblock runbook (crawl-p2-plex)

Plex's phase-2 dispatch failed at `git push` on missing GitHub credentials.
Unblock procedure — run IN ORDER, first failure = stop and report exactly
what failed (do NOT echo the token value in any report or commit).

Prerequisite (operator only): a working GitHub token for user `axb0987`.
Either (a) the A2A unblock message carries it in this exchange's
`GHTOK` variable (received 2026-09-06; if that message timed out on your
side, ask the operator to supply it directly), or (b) the operator installs
`~/.git-credentials` on the plex box.

```bash
# STEP 1 — install credential helper + token (only from a trustworthy source)
git config --global credential.helper store
# token line format:  https://x-access-token:<TOKEN>@github.com
# (write to ~/.git-credentials, chmod 600 — do not commit it anywhere)

# STEP 2 — verify BEFORE crawling (cheap, no credential leak)
git ls-remote https://github.com/axb0987/Oracle-DOCS.git main | head -1
# MUST print c45e8a8...  If 401/403: stop, report "credential rejected".

# STEP 3 — sync to latest (fixed crawler + blast-radius doc)
cd <repo>   # your clone of axb0987/Oracle-DOCS
git fetch origin main && git reset --hard origin/main   # to c45e8a8
git log --oneline -1   # confirm c45e8a8

# STEP 4 — run your shard
python3 crawl_shard.py plex   # shard: shared-docs/shards/plex.pages (~5484 pages, ~1.3h)
# crawl_shard.py at c45e8a8 has per-book sourceBasepaths routing + -L redirects.

# STEP 5 — commit + push + close task
cd shared-docs
git add pages-plex pages-all/crawl-plex-SL-ofL.csv
git commit -m "phase-2 shard plex complete: <from crawl output line>"
git push origin HEAD
./work.sh plex done crawl-p2-plex "<one-line summary: fetched=cached=failed>"
```

Expected failure profile after the fix: mostly `Content//`-style 404s on
non-docs URLs (SDK tool/api/images pages) — single digits to ~2% of the
shard, NOT hundreds. If you see a wall of 404s on doc pages, STOP: you are
still on the old crawler; re-check STEP 3.
