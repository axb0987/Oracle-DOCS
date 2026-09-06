#!/usr/bin/env python3
"""Retry pass: re-crawl ONLY the previously-failed rows from a crawl CSV,
re-resolving each URL through the fixed per-book sourceBasepaths routing
and with -L redirect following.

Usage: retry_failed.py <run-tag> <source.csv> [delay] [outdir]

Reads every row with http != 200 from source.csv, maps the failed URL back
to its toc entry (by leaf name), re-resolves it with crawl_shard.abs_url,
fetches it, and writes md into <outdir>/pages/ alongside the corpus.
Outputs <outdir>/retry-<run-tag>.csv with the same columns as the crawler.
"""
import csv
import html as _h
import os
import re
import sys
import time

import crawl_shard as cs


def url_to_leaf(url):
    """Strip the (buggy) base off a failed URL back to its leaf path."""
    u = url.replace("Content//", "Content/")
    if "/Content/" in u:
        return u.split("/Content/", 1)[1]
    if "docs.oracle.com/" in u:
        return u.split("docs.oracle.com/", 1)[1]
    return u


def make_key(p):
    """Mirror crawl_shard's dest key: toc path -> flat .md filename."""
    if not p:
        return None
    k = p.lstrip("/")
    for pre in ("/Content/", "Content/"):
        if k.startswith(pre):
            k = k[len(pre):]
    k = k.replace("/", "__")
    k = re.sub(r"\.(htm|html)$", "", k, flags=re.I)
    return k + ".md"


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(2)
    run_tag = sys.argv[1]
    src_csv = sys.argv[2] if os.path.isabs(sys.argv[2]) else os.path.join(cs.HERE, sys.argv[2])
    delay = float(sys.argv[3]) if len(sys.argv) > 3 else 0.7
    outdir = sys.argv[4] if len(sys.argv) > 4 else os.path.join(cs.HERE, "pages-all")
    pages_dir = os.path.join(outdir, "pages")
    os.makedirs(pages_dir, exist_ok=True)

    tree, pages = cs.load_toc()  # also populates cs._sbp

    # leaf (sans Content/) -> toc info; and full path -> toc info
    pby_leaf, pby_full = {}, {}
    for p in pages.values():
        pp = p.get("p", "")
        leaf = pp[len("Content/"):] if pp.startswith("Content/") else pp
        pby_full[pp.strip("/")] = p
        pby_leaf[leaf.strip("/")] = p

    rows = list(csv.reader(open(src_csv)))
    if not rows or rows[0][0] != "ts":
        rows = list(csv.reader(open(src_csv, newline="")))
    fails = [r for r in rows[1:] if r and r[2] not in ("200",)]
    print(f"retry {run_tag}: {len(fails)} failed rows from {src_csv}")

    log = open(os.path.join(outdir, f"retry-{run_tag}.csv"), "a", newline="")
    w = csv.writer(log)
    if log.tell() == 0:
        w.writerow(["ts", "url", "http", "bytes", "out"])

    new = cached = still = 0
    t0 = time.time()
    for i, r in enumerate(fails, 1):
        old_url = r[1]
        leaf = url_to_leaf(old_url)
        info = pby_leaf.get(leaf.strip("/")) or pby_full.get(leaf.strip("/")) or {}
        url = cs.abs_url(info.get("p", "") or None, info.get("s"))
        if not url:
            # uncatalogued or non-docs.oracle page: refetch the original URL
            url = old_url
        key = make_key(info.get("p")) or make_key(leaf)
        dest = os.path.join(pages_dir, key)
        tmp = dest + ".tmp"
        if os.path.exists(dest) and not os.path.exists(tmp):
            cached += 1
            w.writerow([time.strftime('%H:%M:%S'), url, "cached", 0, key])
            continue
        code, size, err = cs.fetch(url, tmp)
        ts = time.strftime('%H:%M:%S')
        if code == "200":
            body = open(tmp, "rb").read()
            text = body.decode("utf-8", "ignore")
            tm = re.search(r"<title>(.*?)</title>", text, re.S | re.I)
            title = _h.unescape(tm.group(1)).strip() if tm else info.get("t", "")
            am = cs.main_span(text)
            tgt = text[am[0]:am[1]] if am else text
            tgt = re.sub(r"<title>.*?</title>", "", tgt, flags=re.S | re.I)
            mdtext = cs.html_to_md(tgt, url)
            head = f"# {title}\n- Source: {url}\n- Fetched: {time.strftime('%Y-%m-%d %H:%M %Z')}\n\n"
            md = head + re.sub(r"\n{3,}", "\n\n", mdtext).strip() + "\n"
            if len(md.strip()) > 120 and not md.lstrip().startswith("<"):
                with open(dest, "w", encoding="utf-8") as mf:
                    mf.write(md)
                os.remove(tmp)
                new += 1
                w.writerow([ts, url, code, size, key])
            else:
                still += 1
                w.writerow([ts, url, code, size, "BADHTML:" + key])
                if os.path.exists(tmp):
                    os.remove(tmp)
        else:
            still += 1
            w.writerow([ts, url, code, size, err])
            if os.path.exists(tmp):
                os.remove(tmp)
        if i % 100 == 0 or i == len(fails):
            dt = time.time() - t0
            print(f"  [{i}/{len(fails)}] recovered={new} cached={cached} still_failing={still} "
                  f"({dt/max(i,1):.1f}s/page)", flush=True)
        time.sleep(delay)
    log.close()
    dt = time.time() - t0
    print(f"retry {run_tag}: DONE recovered={new} cached={cached} still_failing={still} "
          f"of {len(fails)} in {dt:.0f}s")


if __name__ == "__main__":
    main()
