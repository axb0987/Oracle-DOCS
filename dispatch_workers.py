#!/usr/bin/env python3
"""Dispatch crawl workers.

Local: runs shards in background (nohup) — no A2A needed; deterministic.
A2A peers (tars/plex): sends ONE task per shard via JSON-RPC to
<A2A_PEER_URL>:9900/ with bearer A2A_PEER_TOKENS[<peer>]. Task = "claim
shard via work.sh in oracle-docs-clone, run python3 crawl_shard.py ...,
commit+push only pages/<book>/S<shard>_shard, mark done". Peer replies
when the job exits (task completes); we do NOT block on the reply here.

Shard assignments:
  1/5/6      -> plex   (5540 pages)
  2/3/4      -> local (11069 pages)
  14/15/16   -> tars   (6907 pages, if tars reachable)
If a peer is DOWN at dispatch, reassign its shards to local so nothing
is left orphaned.

Usage:
  dispatch_workers.py                     # plan + run
  dispatch_workers.py --dryrun            # plan only, don't fire
  dispatch_workers.py --local-only        # skip peer dispatch entirely
  dispatch_workers.py --peer-exclude tars # pretend peer down
"""
import json, os, subprocess, sys, time, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.join(HERE, 'shared-docs')
BASE = "https://docs.oracle.com/en-us/iaas/"
UA = ("Mozilla/5.0 (X11; Linux x86_64; rv=140.0) Gecko/20100101 "
      "Firefox/140.0")

dryrun = "--dryrun" in sys.argv
local_only = "--local-only" in sys.argv
peer_exclude = set()
for a in sys.argv:
    if a.startswith("--peer-exclude"):
        peer_exclude = {a.split("=", 1)[1]} if "=" in a else set()
    elif a.startswith("--peer-exclude="):
        peer_exclude = {a.split("=", 1)[1]}

# --- peers ---
env = {}
for line in open(os.path.expanduser("~/.hermes/.env")):
    if "=" in line and not line.startswith("#"):
        k, v = line.strip().split("=", 1)
        env[k] = v

A2A_TOKENS = env.get("A2A_PEER_TOKENS", "")
PEER_TOKENS = {}
for part in A2A_TOKENS.split(","):
    k, _, v = part.partition(":")
    if v:
        PEER_TOKENS[k.strip()] = v.strip()
PEERS = {
    "plex": "http://plex.seagull-rohu.ts.net:9900/",
    "tars": "http://tars.seagull-rohu.ts.net:9900/",
}

# --- shard plan: peer ownership ---
PEER_SHARDS = {"local": [2, 3, 4], "plex": [1, 5, 6], "tars": [14, 15, 16]}
BOOK_NAME = "Infrastructure Services"

# --- counts to report against ---
d