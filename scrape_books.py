#!/usr/bin/env python3
"""Scrape the 17 top-level OCI docs books: fetch each book's live home page
(curl + browser UA) and render its full header outline from toc.json.
Output: Fox-OCI/books/<slug>/home.html + outline.md, plus books/index.md."""
import json, subprocess, time, re, os, html

TOC = json.load(open(os.path.join(os.path.dirname(__file__), "toc.json")))
tree, pages = TOC["tree"], TOC["pages"]
BASE = "https://docs.oracle.com/en-us/iaas/"
UA = "Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0"
OUT = os.path.join(os.path.dirname(__file__), "books")


def url_for(path):
    if not path or path.startswith("http"):
        return path
    return BASE + (path if path.startswith("Content/") else "Content/" + path)


def slugify(root_node, idx):
    p = pages.get(root_node["i"], {}).get("p", "")
    m = re.match(r"Content/([^/]+)/", p)
    if m:
        return m.group(1)
    stem = os.path.splitext(os.path.basename(p))[0]
    return f"{idx:02d}-{re.sub(r'[^a-z0-9]+', '-', stem.lower()).strip('-')}"


def count_nodes(subtree):
    n = 0
    for child in subtree:
        n += 1 + count_nodes(child.get("c") or [])
    return n


def render_outline(node, depth, out):
    info = pages.get(node["i"], {})
    title = html.escape(info.get("t", "(untitled)"))
    u = url_for(info.get("p", ""))
    out.append("  " * depth + f"- **{title}** — {u}" if u else "  " * depth + f"- **{title}**")
    for c in (node.get("c") or []):
        render_outline(c, depth + 1, out)


def fetch_curl(url, dest):
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    r = subprocess.run(
        ["curl", "-sS", "--max-time", "45", "-A", UA,
         "-w", "%{http_code}\n%{size_download}", "-o", dest, url],
        capture_output=True, text=True)
    parts = r.stdout.strip().split("\n")
    code = parts[0] if parts else "000"
    size = int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else 0
    title = ""
    if code == "200" and os.path.exists(dest):
        raw = open(dest, "rb").read()
        t = re.search(rb"<title>(.*?)</title>", raw, re.S | re.I)
        if t:
            title = html.unescape(t.group(1).decode("utf-8", "ignore").strip()).replace("\n", " ")
    err = r.stderr.strip()[:120] if r.returncode else ""
    return code, size, title, err


def main():
    os.makedirs(OUT, exist_ok=True)
    used = {}
    index = ["# OCI Books — Home Pages + Header Outlines\n",
             "Source: `docs.oracle.com/en-us/iaas/toc.json` navigation tree + live home fetches",
             "(curl, browser UA, 0.7 s between requests). Folders under `books/<slug>/`.\n"]
    ok = 0
    total_pages = 0
    for i, root in enumerate(tree):
        info = pages.get(root["i"], {})
        title = info.get("t", "?")
        u = url_for(info.get("p", ""))
        slug = slugify(root, i + 1)
        while slug in used:
            slug = f"{i+1:02d}-{slug}"
        used[slug] = True
        if u.startswith("http") and "docs.oracle" not in u:
            index.append(f"## {i+1:2d}. {title}\n\n- External: `{u}` — not an oci-docs book; nothing to crawl.\n")
            print(f"{i+1:2d}. {title[:52]:<52} EXTERNAL")
            continue
        code, size, ptitle, err = fetch_curl(u, f"{OUT}/{slug}/home.html")
        time.sleep(0.7)
        total = count_nodes(root.get("c") or []) + 1
        lines = [f"# {title}", "", f"- Home: `{u}`",
                 (f"- Home fetched: **HTTP {code}** ({size:,} B) — <title>{ptitle}</title>"
                  if code == "200" else f"- Home fetched: **FAILED** ({code}) {err}"),
                 f"- Pages in book (incl. home): {total}"]
        if root.get("c"):
            lines += ["", "## Header outline", ""]
            ol = []
            for c in root["c"]:
                render_outline(c, 0, ol)
            lines += ol
        open(f"{OUT}/{slug}/outline.md", "w").write("\n".join(lines) + "\n")
        if code == "200":
            ok += 1
            total_pages += total
        index.append(f"## {i+1:2d}. {title}\n\n- Home: `{u}` — **HTTP {code}** ({size:,} B)\n"
                     f"- Pages in book (incl. home): {total}\n- Files: `{slug}/outline.md`, `{slug}/home.html`\n")
        print(f"{i+1:2d}. {title[:52]:<52} {code}  pages={total:<6} {slug}")
    open(f"{OUT}/index.md", "w").write("\n".join(index) + "\n")
    print(f"\nok {ok}/16 docs-books ({1} external); pages across OK books: {total_pages:,}")


if __name__ == "__main__":
    main()
