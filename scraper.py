#!/usr/bin/env python3
"""
OCI Documentation scraper per ~/hermes/taildrop/Fox-OCI/Oracle-Scracper-Doc.txt
Site: https://docs.oracle.com/en-us  (Oracle Cloud Infrastructure Documentation)

Key mechanic discovered: the per-page sidebar TOC on docs.oracle.com is NOT in the
static HTML — it is rendered client-side (front-end.js) from the JSON document map
at  /en-us/iaas/toc.json  (keys: tree, pages, sourceBasepaths, sourceFilter).
So "link traversal" between sections is performed against that same authoritative
graph, and "accessing"/"extracting" a page is a real HTTP fetch + parse.
"""
import json, re, html, sys
import urllib.request

BASE      = "https://docs.oracle.com"
LANG_BASE = BASE + "/en-us"
UA        = ("Mozilla/5.0 (X11; Linux x86_64; rv:140.0) "
             "Gecko/20100101 Firefox/140.0")
TOC_URL   = LANG_BASE + "/iaas/toc.json"        # the navigation source the site uses

HTML_RE   = re.compile(r"<[^>]+>")


class OciScraper:
    def __init__(self, toc_json):
        self.toc = json.load(open(toc_json))
        self.pages = self.toc["pages"]
        self.basepaths = self.toc["sourceBasepaths"]
        self.parent = {}
        self.node = {}
        self._build()

    # ---- graph (built from the site's own toc.json) ----
    def _build(self):
        def rec(nodes, par):
            for n in nodes:
                self.parent[n["i"]] = par
                self.node[n["i"]] = n
                if n.get("c"):
                    rec(n["c"], n["i"])
        rec(self.toc["tree"], None)

    def url_of(self, nid):
        p = self.pages.get(nid)
        if not p:
            return None
        return LANG_BASE + self.basepaths.get(str(p["s"]), "/iaas") + "/" + p["p"]

    def title_of(self, nid):
        p = self.pages.get(nid)
        return p.get("t") if p else None

    def children(self, nid):
        return [c["i"] for c in self.node.get(nid, {}).get("c", [])]

    def find_by_title(self, title):
        title = title.strip().lower()
        return [nid for nid in self.parent
                if self.title_of(nid) and self.title_of(nid).strip().lower() == title]

    # ---- actual page access (live HTTP) ----
    def fetch(self, url, timeout=30):
        req = urllib.request.Request(url, headers={
            "User-Agent": UA,
            "Accept-Language": "en-US,en;q=0.9",
            "Accept": "text/html,application/xhtml+xml",
        })
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                body = r.read().decode("utf-8", "ignore")
                return r.getcode(), body
        except Exception as e:                       # noqa: BLE001
            return None, str(e)

    # ==================== the 4 required tests ====================
    def test_link(self, url):
        """Given link -> 'Link Accessed' / 'Denied link'"""
        code, body = self.fetch(url)
        if code == 200 and len(body) > 500:
            return "Link Accessed", code, body
        return "Denied link", code, body

    def test_traverse_down(self, chain_titles):
        """Multicloud -> Get Started -> Multicloud Benefits  (parent->child->child)
           -> 'Traversal Down' / 'Traverse Down Fail'"""
        ids = []
        for t in chain_titles:
            hits = self.find_by_title(t)
            if not ids:
                ids.append(hits[0]); continue
            # the next node must be a direct child of the current one
            child = [h for h in hits if self.parent[h] == ids[-1]]
            if not child:
                return "Traverse Down Fail", None
            ids.append(child[0])
        # verify each is the direct parent of the next
        for a, b in zip(ids, ids[1:]):
            if self.parent[b] != a:
                return "Traverse Down Fail", None
        return "Traversal Down", [self.node[x] and self.title_of(x) + " " + self.url_of(x) for x in ids]

    def test_traverse_lateral(self, from_title, to_title):
        """Multicloud -> Oracle Dedicated Cloud (exit to a sibling)
           -> 'Traversal lateral' / 'Traverse Lateral Fail'"""
        f = self.find_by_title(from_title)
        t = self.find_by_title(to_title)
        if not f or not t:
            return "Traverse Lateral Fail", None
        fid, tid = f[0], t[0]
        # must be siblings: same parent (both top-level here => parent None)
        if self.parent[fid] == self.parent[tid]:
            return "Traversal lateral", [
                f"{self.title_of(fid)} -> {self.title_of(tid)} "
                f"(siblings under {self.title_of(self.parent[fid]) or 'ROOT'})"]
        return "Traverse Lateral Fail", None

    def test_extract(self, title):
        """Extract info from 'Support Requests' -> 'Extracted' / 'Cannot extract'"""
        hits = self.find_by_title(title)
        if not hits:
            return "Cannot extract", None
        nid = hits[0]
        url = self.url_of(nid)
        code, body = self.fetch(url)
        if code != 200:
            return "Cannot extract", f"{code} {url}"
        text = self.extract_article(body)
        if text and len(text) > 40:
            return "Extracted", {"url": url, "text": text}
        return "Cannot extract", None

    @staticmethod
    def extract_article(body):
        """Pull the main <article> body, strip tags, collapse whitespace."""
        m = re.search(r"<article\b.*?>.*?</article>", body, re.S)
        chunk = m.group(0) if m else body
        chunk = re.sub(r"<script.*?</script>", " ", chunk, flags=re.S)
        chunk = HTML_RE.sub(" ", chunk)
        chunk = html.unescape(chunk)
        return re.sub(r"\s+", " ", chunk).strip()


def main():
    s = OciScraper("/home/cheemtos/hermes/taildrop/Fox-OCI/toc.json")
    print("=" * 70)
    # 1. seed link
    r, code, _ = s.test_link("https://docs.oracle.com/en-us/iaas/"
                             "Content/GSG/Concepts/baremetalintro.htm")
    print(f"[TEST 1 seed link]  {r}   (HTTP {code})")

    # 2. traverse down
    r, detail = s.test_traverse_down(["Oracle Multicloud", "Get Started", "Multicloud Benefits"])
    print(f"[TEST 2 traverse down]  {r}")
    if isinstance(detail, list):
        for line in detail: print("      " + line)

    # 3. traverse lateral
    r, detail = s.test_traverse_lateral("Oracle Multicloud", "Oracle Dedicated Cloud")
    print(f"[TEST 3 traverse lateral]  {r}")
    if isinstance(detail, list):
        for line in detail: print("      " + line)

    # 4. extract
    r, detail = s.test_extract("Support Requests")
    print(f"[TEST 4 extract Support Requests]  {r}")
    if isinstance(detail, dict):
        print("      url:", detail["url"])
        print("      snippet:", detail["text"][:320] + "...")
    elif detail:
        print("      ", detail)


if __name__ == "__main__":
    main()
