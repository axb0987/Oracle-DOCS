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
- Scope decision (user, 2026-09-04): start with the 17 books + their headers (phase 1), full 18,937-page crawl = phase 2 (pending).
- **Phase 1 DONE (2026-09-04, crawl-agent):** `scrape_books.py` fetched all 16 live book home pages (HTTP 200, browser UA, 0.7s spacing) + rendered full header outlines from `toc.json`. Artifacts: `books/<slug>/{home.html,outline.md}` (17 slugs; `General` = Cloudflare partner book, `15-General` = More Resources), plus `books/index.md` summary. Book spans: FreeTier(4) … Infrastructure Services(16,958) … total 18,936 pages. Book 17 (Oracle Cloud Console) is an external non-doc link.


## QA (agent C)
- Verified all 4 task outputs print the spec strings against the live site.
