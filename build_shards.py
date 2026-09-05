#!/usr/bin/env python3
"""Build disjoint page shards for the 3 workers from toc.json root subtrees.

Books per Oracle-Scracper-Doc.txt = the 15 spec'd toc root subtrees
(tools-root excluded). Infrastructure Services (~17k pages) is split
evenly across all three workers; the 14 smaller books are handed out
round-robin by descending size. Output: shards/<worker>.pages, one toc
path per line -> `crawl_shard.py file shards/<worker>.pages`.
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
SPEC = [
    "Oracle Cloud Infrastructure Cloud Adoption Framework",
    "Getting Started",
    "Oracle Cloud's Free Tier",
    "Oracle Multicloud",
    "Oracle Dedicated Cloud",
    "Oracle Cloud Infrastructure Government Cloud",
    "Applications Services",
    "Infrastructure Services",
    "Developer Resources",
    "Security",
    "Marketplace",
    "Partner Offerings: Cloudflare at OCI",
    "More Resources",
    "Glossary",
    "Oracle Cloud Console",
]
WORKERS = ["cheemtos", "tars", "plex"]

d = json.load(open(os.path.join(HERE, "toc.json")))
tree, pages = d["tree"], d["pages"]

def flat(sub, acc):
    for n in sub:
        acc.append(n["i"])
        flat(n.get("c") or [], acc)
    return acc

roots = []
for r in tree:
    t = pages.get(r["i"], {}).get("t", "")
    for spec in SPEC:
        if t.startswith(spec):
            acc = []
            flat([r], acc)
            paths = sorted({pages[i]["p"] for i in acc if i in pages})
            roots.append((len(paths), spec, paths))
            break

assert len(roots) == len(SPEC), f"matched {len(roots)}/{len(SPEC)} spec books"
roots.sort(key=lambda x: -x[0])
big = [roots[0]]
assert len(big) == 1 and big[0][1] == "Infrastructure Services", big
small = roots[1:]

shards = {w: [] for w in WORKERS}
for rank, (n, name, paths) in enumerate(small):
    w = WORKERS[rank % 3]
    shards[w].extend(paths)
    print(f"book {n:5d} -> {w:10s}  {name}")

n, name, svc = big[0]
third, rem = divmod(n, 3)
pos = 0
for i, w in enumerate(WORKERS):
    cnt = third + (1 if i < rem else 0)
    shards[w].extend(svc[pos:pos + cnt])
    pos += cnt
print(f"book {n:5d} split {third}x3+{rem} across workers  {name}")

out = os.path.join(HERE, "shards")
os.makedirs(out, exist_ok=True)
claimed = set()
sets = {}
for w in WORKERS:
    ps, dup = [], 0
    for p in sorted(set(shards[w])):
        if p in claimed:
            dup += 1
            continue
        claimed.add(p)
        ps.append(p)
    open(os.path.join(out, f"{w}.pages"), "w").write("\n".join(ps) + "\n")
    sets[w] = set(ps)
    print(f"shard {w:10s} = {len(ps):6d} pages (dropped {dup} dup)")

ovlp = sum(len(sets[a] & sets[b]) for a in WORKERS for b in WORKERS if a < b)
union = len(set().union(*sets.values()))
print(f"overlap = {ovlp} (must be 0); union = {union}")
assert ovlp == 0
