# -*- coding: utf-8 -*-
"""One-time seed for page_lastmod.json from real git history.

Walks every commit oldest to newest and records, for each indexable route, the
date of the last commit that actually changed the page's <main> region. Commits
that only rewrote shared chrome or bumped an asset version do not count, so the
seeded dates are spread across the site's real editing history instead of
collapsing onto the date of the latest build commit.

Run once from _source/:  python3 backfill_lastmod.py
"""
from pathlib import Path
import json
import subprocess
import sys

from lastmod import fingerprint, guide_slug, REGISTRY
from guide_dates import GUIDE_UPDATED_DATES

ROOT = Path(__file__).resolve().parent.parent


def git(*args):
    result = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True,
                            encoding="utf-8", errors="replace")
    if result.returncode != 0:
        raise SystemExit(f"git {' '.join(args)} failed:\n{result.stderr}")
    return result.stdout


class BlobReader:
    """Stream blobs out of one long-lived `git cat-file --batch` process."""

    def __init__(self):
        self.proc = subprocess.Popen(["git", "cat-file", "--batch"], cwd=ROOT,
                                     stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    def read(self, spec):
        self.proc.stdin.write((spec + "\n").encode("utf-8"))
        self.proc.stdin.flush()
        header = self.proc.stdout.readline().decode("utf-8", "replace").strip()
        if header.endswith(("missing", "ambiguous")):
            return None
        size = int(header.split()[2])
        payload = self.proc.stdout.read(size)
        self.proc.stdout.read(1)
        return payload.decode("utf-8", "replace")

    def close(self):
        self.proc.stdin.close()
        self.proc.wait()


def route_for(relative):
    if relative == "index.html":
        return "/"
    if relative.endswith("/index.html"):
        return "/" + relative[: -len("index.html")]
    return None


def main():
    manifest = json.loads((ROOT / "_source/page_manifest.json").read_text(encoding="utf-8"))
    wanted = {route for route, data in manifest.items() if data["indexable"]}
    history = git("log", "--reverse", "--root", "--format=@%H|%cs", "--name-only", "--", "*index.html")

    reader = BlobReader()
    marks, dates = {}, {}
    sha = day = None
    events = 0
    for line in history.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith("@") and "|" in line:
            sha, day = line[1:].split("|", 1)
            continue
        route = route_for(line)
        if route not in wanted or sha is None:
            continue
        blob = reader.read(f"{sha}:{line}")
        if blob is None:
            continue
        events += 1
        mark = fingerprint(blob)
        if marks.get(route) != mark:
            marks[route] = mark
            dates[route] = day
    reader.close()

    missing = sorted(wanted - set(dates))
    if missing:
        print("Khong tim thay lich su cho cac route sau (se can gan tay):", file=sys.stderr)
        for route in missing:
            print("  " + route, file=sys.stderr)

    registry = {}
    for route in sorted(wanted & set(dates)):
        slug = guide_slug(route)
        lastmod = GUIDE_UPDATED_DATES[slug] if slug else dates[route]
        registry[route] = {"fingerprint": marks[route], "lastmod": lastmod}

    REGISTRY.write_text(json.dumps(registry, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
                        encoding="utf-8")
    spread = {}
    for entry in registry.values():
        spread[entry["lastmod"]] = spread.get(entry["lastmod"], 0) + 1
    print(f"Da doc {events} phien ban trang, ghi {len(registry)} route vao {REGISTRY.name}")
    print(f"So ngay khac nhau: {len(spread)}")
    for day in sorted(spread):
        print(f"  {day}  {spread[day]} trang")


if __name__ == "__main__":
    main()
