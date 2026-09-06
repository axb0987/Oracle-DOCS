# Blast-radius readback for TARS (crawl-p2-tars)

Requested by TARS before giving its recon assessment. DATA ONLY — reading
this is not a go. No work without your operator's direct call.

Repo: github.com/axb0987/Oracle-DOCS, branch `main` (latest at commit `023833d`
and the crawler fix `617fe7f`).

## Repo / crawler state
- `crawl_shard.py` is BUG-FIXED (commit `617fe7f`). The early crawler hardcoded
  the docs base to `/en-us/iaas/` and ignored `toc.json sourceBasepaths`, which
  caused 880/6244 failures on the cheemtos shard:
  - 29 URLs with double-slash `Content//` paths
  - 42 301 pages not followed (no `-L`)
  - 809 true 404s from wrong-book bases (`dbms_*` → `pl-sql-sdk/doc/`,
    billing/DR → `autonomous-database-serverless/doc/`, terraform landing)
- Fix: per-page base resolved from `toc.json` `sourceBasepaths` by the page's
  `s` field; curl now uses `-L`.
- Validation: targeted retry of all 880 failures recovered **865/880 (98.3%)**
  in 25.5 min (`pages-all/retry-cheemtos-retry.csv`). The 15 remaining are
  genuine Oracle-side dead links — SDK tool landing/index pages under
  `tools/*/latest`, `api`, and `images` directory URLs. Expect the same
  failure profile on your shard, concentrated in tool/tool-page leaves.
- Corpus at this point: 6,229 pages committed+pushed (`023833d`), of 18,936
  mapped (~33%). plex will pull to this commit before starting (5,484 URLs).

## Expected profile for shards/tars.pages
- 5,973 URLs (disjoint from cheemtos and plex shards — verified by construction)
- Runtime ~2.0 h at 0.7 s spacing (nohup, not in reply path)
- Network egress: docs.oracle.com only, ~0.7 s spacing
- Disk: ~62 MB of markdown into `pages-all/pages/` (cheemtos shard: 5,364 pages
  = 59 MB after retry additions)
- Writes: `crawl-tars-SL-ofL.csv`, `run-tars.log`, `pages-all/pages/*` only;
  commit own files + push + `./work.sh tars done crawl-p2-tars "<summary>"`
- No other box changes, no other remotes, one report at the end.

## Failure-handling contract (same as playbook)
- Any git/auth/config failure: STOP, mark the task blocked, report once with
  the exact error line, do not improvise around it.
- The credential question: TARS should confirm which credential it will use to
  push (its own, or the operator-provided one). If TARS also lacks push creds
  it will hit the same wall plex just hit — say so at recon rather than
  discovering it mid-crawl. plex already has working creds delivered over the
  A2A channel.
