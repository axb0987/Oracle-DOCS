#!/usr/bin/env python3
"""OCI page shard crawler — python3 stdlib + curl only (no pip deps).

Walks one book's subtree from toc.json, fetches each page (browser UA, with a
delay), converts the page body to markdown (relative links resolved to
absolute), writes <outdir>/pages/<path with / replaced by __>.md.

Resume-safe: an existing non-empty .md is skipped. Every URL is appended to
the CSV log: <outdir>/crawl-<slug>-S<shard>-of<N>.csv (ts,url,http,bytes,out).

Usage:
  crawl_shard.py <book-substring> <shard> <nshards> [delay] [outdir]
    book-substring: matched on the first segment under Content/ (e.g. GSG)
    shard/nshards : 0-based even interleaving (idx % nshards == shard)

Exit: 0 = all good or fully cached; 1 = some failures (check CSV).
"""
import json, os, re, subprocess, sys, time, csv
from html.parser import HTMLParser
from html import unescape

BASE = "https://docs.oracle.com/en-us/iaas/"
UA = ("Mozilla/5.0 (X11; Linux x86_64; rv=140.0) Gecko/20100101 Firefox/140.0")
HERE = os.path.dirname(os.path.abspath(__file__))
SKIP_TAGS = {"script", "style", "noscript", "template", "nav", "header",
             "footer", "iframe", "form", "button", "select", "svg", "aside"}
HEADING = {t: int(t[1]) for t in ("h1", "h2", "h3", "h4", "h5", "h6")}


def load_toc():
    p = os.path.join(HERE, "toc.json")
    if not os.path.exists(p):
        p = os.path.expanduser("~/toc.json")
    d = json.load(open(p))
    return d["tree"], d["pages"]


def abs_url(path):
    if not path:
        return None
    if path.startswith("http"):
        return path if "docs.oracle" in path else None
    p = path if path.startswith("Content/") else "Content/" + path
    return BASE + p


def md_link_abs(href, page_url):
    """Resolve a doc href to an absolute docs.oracle URL (None = ignore)."""
    href = href.strip()
    if not href:
        return None
    if href.startswith("http://") or href.startswith("https://"):
        return href
    if href.startswith("#"):
        return page_url + href
    if href.startswith("mailto:") or href.startswith("tel:"):
        return href
    if href.startswith("/"):
        # host-absolute on docs.oracle.com (e.g. /en-us/..., /iaas/...)
        return "https://docs.oracle.com" + href
    if href.startswith("Content/"):
        return BASE + href
    # page-relative
    d = page_url.rsplit("/", 1)[0]
    return d.rstrip("/") + "/" + href.strip("/")


class Conv(HTMLParser):
    """HTML -> linear markdown text. Links become [text](absurl)."""

    def __init__(self, page_url):
        super().__init__(convert_charrefs=True)
        self.pu = page_url
        self.out = []
        self.skip = 0
        self.stack = []
        self.mode = None  # None | 'pre' | 'code'
        self.link_href = None

    def md(self):
        if self.skip:
            return ""
        t = " ".join(" ".join(self.out).split())
        return re.sub(r"\s+", " ",
                      t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))

    def flush(self):
        if not self.skip and self.mode is None:
            t = " ".join(" ".join(self.out).split())
            self.out = []
            if t:
                self._emit(t)

    def _emit(self, t):
        self._result.append(self._esc(t))

    @staticmethod
    def _esc(t):
        # escape md special chars that break links
        t = t.replace("![", "[")
        return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if self.skip:
            return
        if tag in SKIP_TAGS:
            self.skip = 1
            return
        self.stack.append(tag)
        if tag == "pre":
            if self.mode is None:
                self.flush()
                self._result.append("\n```\n")
                self.mode = "pre"
        elif tag == "code" and self.mode is None:
            self.flush()
            self._result.append("`")
            self.mode = "code"
        elif tag in HEADING:
            self.flush()
            self._result.append("\n\n" + "#" * HEADING[tag] + " ")
        elif tag == "p":
            self.flush()
            self._result.append("\n\n")
        elif tag == "br":
            self.flush()
            self._result.append("  \n")
        elif tag == "li":
            self.flush()
            self._result.append("\n- ")
        elif tag in ("div", "section", "tr", "table"):
            self.flush()
            self._result.append("\n")
        elif tag == "a" and a.get("href"):
            href = md_link_abs(a["href"], self.pu)
            if href:
                self.flush()
                self._result.append("[")
                self._pending = href
            else:
                self._pending = None
        else:
            self._pending = None

    def handle_endtag(self, tag):
        if self.skip:
            self.skip = max(0, self.skip - 1)
            return
        if tag in SKIP_TAGS:
            return
        # close innermost matching open tag
        while self.stack and self.stack[-1] != tag:
            self.stack.pop()
        if self.stack:
            self.stack.pop()
        if tag == "pre" and self.mode == "pre":
            self._result.append("\n```\n")
            self.out = []
            self.mode = None
        elif tag == "code" and self.mode == "code":
            t = " ".join(" ".join(self.out).split())
            self.out = []
            self._result.append(unescape(t) + "`")
            self.mode = None
        elif tag in HEADING:
            self.flush()
        elif tag == "a" and getattr(self, "_pending", None):
            self.flush()
            t = self._last_text
            self._result.append(f"]({self._pending})")
            self._pending = None

    def handle_data(self, data):
        if self.skip:
            return
        if self.mode == "pre":
            self.out.append(data)
            return
        self.out.append(data)

    # we capture the raw text run since the last flush for link labels
    @property
    def _last_text(self):
        return " ".join(" ".join(self.out).split())

    def _result_get(self):
        r, self._result = self._result, []
        return r


def html_to_md(soup_html, page_url):
    c = Conv(page_url)
    c._result = []
    try:
        c.feed(soup_html)
        c.close()
        s = c._result_get()
    except Exception:
        s = list(c._result)
    if getattr(c, "_result", None):
        s += c._result
    return "".join(s)


def fetch(url, tmp):
    r = subprocess.run(
        ["curl", "-sS", "--max-time", "45", "-A", UA,
         "-w", "%{http_code}\\n%{size_download}", "-o", tmp, url],
        capture_output=True, text=True)
    parts = (r.stdout or "").strip().split("\n")
    code = parts[0] if parts else "000"
    size = int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else 0
    err = r.stderr.strip()[:120] if r.returncode else ""
    return code, size, err


def main_span(body_html):
    """Byte span of the first role=article container, depth-counted across
    nested <article>/</article>. None = not found (caller uses whole body)."""
    opens = list(re.finditer(r'<article\b[^>]*role="article"', body_html, re.I))
    if not opens:
        return None
    start = opens[0].start()
    depth = 0
    for m in re.finditer(r"<article\b|</article>", body_html[start:], re.I):
        if m.group(0)[1].lower() == "/":
            depth -= 1
        else:
            depth += 1
        if depth == 0:
            return (start, start + m.end())
    return (start, len(body_html))


def main():
    if len(sys.argv) < 4:
        print(__doc__)
        sys.exit(2)
    pat, shard, nsh = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    delay = float(sys.argv[4]) if len(sys.argv) > 4 else 0.7
    outdir = sys.argv[5] if len(sys.argv) > 5 else os.path.join(HERE, "pages-all")
    pages_dir = os.path.join(outdir, "pages")
    os.makedirs(pages_dir, exist_ok=True)

    tree, pages = load_toc()
    # build ordered list of (path, title) for this book
    items = []
    def walk(sub):
        for n in sub:
            info = pages.get(n["i"], {})
            p = info.get("p", "")
            if pat.lower() in (p.lower().split("/")[:3]):
                items.append((p, info.get("t", "")))
            walk(n.get("c") or [])
    for root in tree:
        info = pages.get(root["i"], {})
        if pat.lower() in (info.get("p", "").lower().split("/")[:3]):
            items.append((info.get("p", ""), info.get("t", "")))
            walk(root.get("c") or [])

    slug = pat
    log_path = os.path.join(outdir, f"crawl-{slug}-S{shard}-of{nsh}.csv")
    seen = set()
    if os.path.exists(log_path):
        with open(log_path) as f:
            for row in csv.reader(f):
                if row and row[0] != "ts":
                    out = row[4] if len(row) > 4 else ""
                    if out and not out.startswith(("BADHTML:", "EMPTY:")):
                        seen.add(row[1])
    new = cached = failed = 0
    total = len(items)
    picked = [it for i, it in enumerate(items) if i % nsh == shard]
    tstart = time.time()
    with open(log_path, "a", newline="") as log:
        w = csv.writer(log)
        if log.tell() == 0:
            w.writerow(["ts", "url", "http", "bytes", "out"])
        for p, title in picked:
            url = abs_url(p)
            if not url:
                continue
            if url in seen:
                cached += 1
                continue
            key = p.lstrip("/").replace("/", "__")
            key = re.sub(r"\.(htm|html)$", "", key, flags=re.I) + ".md"
            dest = os.path.join(pages_dir, key)
            code, size, err = fetch(url, dest + ".tmp")
            ts = time.strftime("%H:%M:%S")
            if code == "200":
                body = open(dest + ".tmp", "rb").read()
                text = body.decode("utf-8", "ignore")
                tm = re.search(r"<title>(.*?)</title>", text, re.S | re.I)
                page_title = unescape(tm.group(1)).strip() if tm else title
                am = main_span(text)
                tgt = text[am[0]:am[1]] if am else text
                tgt = re.sub(r"<title>.*?</title>", "", tgt, flags=re.S | re.I)
                mdtext = html_to_md(tgt, url)
                head = f"# {page_title}\n"
                head += f"- Source: {url}\n- Fetched: {time.strftime('%Y-%m-%d %H:%M %Z')}\n\n"
                md = head + re.sub(r"\n{3,}", "\n\n", mdtext).strip() + "\n"
                if len(md.strip()) > 120 and not md.lstrip().startswith("<"):
                    with open(dest, "w", encoding="utf-8") as mf:
                        mf.write(md)
                    os.remove(dest + ".tmp")
                    new += 1
                    w.writerow([ts, url, code, size, key])
                else:
                    failed += 1
                    w.writerow([ts, url, code, size, "BADHTML:" + key])
                    if os.path.exists(dest + ".tmp"):
                        os.remove(dest + ".tmp")
            else:
                failed += 1
                w.writerow([ts, url, code, size, err])
            time.sleep(delay)
    dt = time.time() - tstart
    print(f"S{shard}/{nsh} {slug}: fetched={new} cached={cached} "
          f"failed={failed} picked={len(picked)} total_book={total} "
          f"took={dt:.0f}s ({dt/max(len(picked),1):.1f}s/page)")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
