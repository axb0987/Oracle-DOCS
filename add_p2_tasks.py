#!/usr/bin/env python3
"""Add phase-2 crawl task rows to tasks.json (open, per worker)."""
import json, datetime, sys
p = "/home/cheemtos/hermes/taildrop/Fox-OCI/shared-docs/tasks.json"
d = json.load(open(p))
ids = {t["id"] for t in d["tasks"]}
note = ("Phase-2 shard run per WORKER-PLAYBOOK.md; "
        "shard file shards/<worker>.pages; disjoint page sets, 15 books")
now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
for tid in ("crawl-p2-tars", "crawl-p2-plex"):
    if tid not in ids:
        d["tasks"].append({
            "id": tid,
            "section": "## Phase-2 Crawl Log (" + tid[-4:] + ")",
            "status": "open",
            "owner": None,
            "note": note,
        })
d["updated"] = now
open(p, "w").write(json.dumps(d, indent=2) + "\n")
print("ok", now)
