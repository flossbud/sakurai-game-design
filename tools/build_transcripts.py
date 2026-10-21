"""Turn OCR'd subtitle JSON into numbered markdown transcripts + an episode index.

usage: python build_transcripts.py <videos.tsv> <ocr_dir> <repo_root>

videos.tsv is `yt-dlp --flat-playlist --print "%(id)s\t%(title)s\t%(duration)s"`
of the channel's /videos tab (newest first). Category compilations are skipped
because they only re-cut earlier episodes.
"""
import csv
import json
import re
import sys
from pathlib import Path

CATEGORY_FIX = {"Planning & Design": "Planning & Game Design"}
PARA_GAP = 2.0  # seconds of silence that starts a new paragraph
PARA_LINES = 4  # after this many lines, break at the next sentence end
SENTENCE_END = (".", "!", "?", "\u201d", '"', "…")


def parse_title(raw):
    m = re.match(r"^(.*?)\s*\[([^\]]+)\]\s*$", raw)
    if m:
        title, cat = m.group(1).strip(), m.group(2).strip()
    else:
        title, cat = raw.strip(), "Special"
    return title, CATEGORY_FIX.get(cat, cat)


def slugify(s, n=60):
    s = re.sub(r"[’']", "", s.lower())
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:n].rstrip("-")


def mmss(t):
    t = int(t)
    return f"{t // 60:02d}:{t % 60:02d}"


def paragraphs(lines):
    paras, cur = [], []
    for ln in lines:
        long_enough = len(cur) >= PARA_LINES and cur[-1]["text"].endswith(SENTENCE_END)
        if cur and (ln["start"] - cur[-1]["end"] > PARA_GAP or long_enough):
            paras.append(cur)
            cur = []
        cur.append(ln)
    if cur:
        paras.append(cur)
    return paras


def main():
    tsv, ocr_dir, root = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
    rows = [r.split("\t") for r in tsv.read_text().splitlines() if r.strip()]
    rows = [r for r in rows if "Compilation" not in r[1]][::-1]  # oldest first
    out_dir = root / "episodes" / "transcripts"
    out_dir.mkdir(parents=True, exist_ok=True)
    index = []
    for n, (vid, raw, dur) in enumerate(rows, 1):
        title, cat = parse_title(raw)
        fname = f"{n:03d}-{slugify(title)}.md"
        url = f"https://www.youtube.com/watch?v={vid}"
        ocr = ocr_dir / f"{vid}.json"
        lines = json.loads(ocr.read_text()) if ocr.exists() else []
        words = sum(len(l["text"].split()) for l in lines)
        body = []
        for p in paragraphs(lines):
            t = p[0]["start"]
            body.append(f"[{mmss(t)}](https://youtu.be/{vid}?t={int(t)}) " + " ".join(l["text"] for l in p))
        md = [
            f"# {n:03d} · {title}",
            "",
            f"- **Category:** {cat}",
            f"- **Video:** {url}",
            f"- **Length:** {mmss(float(dur or 0))}",
            "- **Source:** official English subtitles burned into the video, read by OCR (tools/ocr_subs.py). Expect rare OCR typos.",
            "",
            "---",
            "",
            "\n\n".join(body) if body else "_No subtitle text was found in this video._",
            "",
        ]
        (out_dir / fname).write_text("\n".join(md))
        index.append({"ep": n, "video_id": vid, "title": title, "category": cat,
                      "duration_s": int(float(dur or 0)), "words": words, "url": url,
                      "transcript": f"episodes/transcripts/{fname}"})
    with open(root / "episodes" / "index.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(index[0]))
        w.writeheader()
        w.writerows(index)
    print(f"{len(index)} episodes, {sum(i['words'] for i in index)} words")


if __name__ == "__main__":
    main()
