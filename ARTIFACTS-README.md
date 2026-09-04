# Crawl Artifacts

Phase 1 (books + headers) output, copied from `Fox-OCI/books/` on the crawl box.
Live source: `https://docs.oracle.com/en-us/iaas/toc.json` (fetched 2026-09-04).

- `index.md` — all 16 live books: home URL, HTTP status, page count, artifact paths
- `books/<slug>/home.html` — raw home page of each book (browser-UA fetch)
- `books/<slug>/outline.md` — title, home status, page count, full header outline
  (every section/page in the book, with doc URLs)
- Slugs `General` = Partner Offerings: Cloudflare at OCI; `15-General` = More Resources
  (both live under `Content/General/` in the source; de-collided at import)
- Book 17 (Oracle Cloud Console) is an external product link, not an oci-docs book.

Scripts that produced this (kept on the crawl box `Fox-OCI/`): `scraper.py`
(link/traverse/extract tests), `scrape_books.py` (phase-1 home+outline crawl).
Phase 2 (full page crawl of all 18,936 pages) pending scope sign-off.
