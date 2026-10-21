"""Expand episode references in markdown files.

usage: python link_eps.py <file.md> [...]

`{{12}}` becomes `[12](../episodes/notes/012-slug.md)`, linked relative to the
file being edited. `{{12|title}}` uses the episode title as the link text.
"""
import csv
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EPS = {int(r["ep"]): r for r in csv.DictReader(open(ROOT / "episodes" / "index.csv"))}


def expand(path):
    path = Path(path).resolve()
    base = path.parent

    def link(m):
        n, mode = int(m.group(1)), m.group(2)
        r = EPS[n]
        target = ROOT / r["transcript"].replace("/transcripts/", "/notes/")
        rel = os.path.relpath(target, base)
        text = f"{n} · {r['title']}" if mode == "title" else str(n)
        return f"[{text}]({rel})"

    text = path.read_text(encoding="utf-8")
    new = re.sub(r"\{\{(\d+)(?:\|(title))?\}\}", link, text)
    path.write_text(new, encoding="utf-8")


if __name__ == "__main__":
    for p in sys.argv[1:]:
        expand(p)
