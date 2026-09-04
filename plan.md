# OCI Docs Migration Plan

> Shared working doc — agents write their own sections, commit per section.

## Contents
- [ ] Survey (agent A)
- [ ] Extraction (agent B)
- [ ] QA (agent C)

## Survey (agent A)
- Scope: 17 top-level OCI book entries; toc.json = 18,937 pages.
- Navigation: sidebar is JS-rendered from /en-us/iaas/toc.json; scrape against that graph.

## Extraction (agent B)
- scraper.py built; tests: seed=HTTP200, traverse down/lateral OK, extraction OK.
- Open question with owner: which 3 scope options for full crawl.
