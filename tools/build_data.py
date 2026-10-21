"""Build the skill's CSV data from the agents' JSONL output.

usage:
  python build_data.py areas   # work/batches/*.jsonl -> data/episodes.csv + work/areas/<area>.jsonl
  python build_data.py data    # work/parts/*.jsonl   -> data/{principles,techniques,lenses,glossary,quotes}.csv

Run from anywhere; paths are relative to the repo root.
"""
import csv
import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORK = ROOT / "work"
DATA = ROOT / "skills" / "sakurai-game-design" / "data"
AREA_PREFIX = {"essence": "ESS", "balance": "BAL", "planning": "PLAN", "feel": "FEEL", "animation": "ANIM",
               "visuals": "VIS", "audio": "AUD", "ui": "UI", "team": "TEAM", "craft": "CRAFT",
               "marketing": "MKT", "tech": "TECH", "case-study": "CASE"}
KINDS = {
    "principles": ["id", "area", "priority", "principle", "why", "how_to_apply", "anti_pattern", "example",
                   "review_question", "episodes", "keywords"],
    "techniques": ["id", "area", "technique", "what", "how", "when", "pitfalls", "episodes", "keywords"],
    "lenses": ["id", "area", "lens", "look_for", "red_flags", "principles", "episodes", "keywords"],
    "glossary": ["term", "meaning", "episodes"],
    "quotes": ["quote", "ep", "title", "time", "theme"],
}
PRIORITY = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3}


def read_jsonl(path):
    out = []
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if line.strip():
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError as e:
                sys.exit(f"{path}:{n}: {e}")
    return out


def flat(v):
    if isinstance(v, list):
        return "; ".join(str(x) for x in v)
    return " ".join(str(v if v is not None else "").split())


def write_csv(path, fields, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow({k: flat(r.get(k, "")) for k in fields})
    print(f"{path.relative_to(ROOT)}: {len(rows)} rows")


def build_areas():
    index = {int(r["ep"]): r for r in csv.DictReader(open(ROOT / "episodes" / "index.csv"))}
    eps, areas = [], defaultdict(list)
    for path in sorted((WORK / "batches").glob("batch-*.jsonl")):
        for row in read_jsonl(path):
            ep = int(row["ep"])
            meta = index[ep]
            notes = meta["transcript"].replace("/transcripts/", "/notes/")
            eps.append({"ep": ep, "title": meta["title"], "category": meta["category"], "url": meta["url"],
                        "summary": row.get("summary", ""), "takeaways": row.get("takeaways", []),
                        "games": row.get("games", []), "tags": " ".join(row.get("tags", [])), "notes": notes})
            for p in row.get("principles", []):
                area = p.get("domain", "").strip()
                if area not in AREA_PREFIX:
                    print(f"ep {ep}: unknown domain {area!r}, filed under craft")
                    area = "craft"
                areas[area].append({"ep": ep, "title": meta["title"], "category": meta["category"], **p})
    eps.sort(key=lambda r: r["ep"])
    missing = sorted(set(index) - {r["ep"] for r in eps})
    if missing:
        print(f"WARNING: no notes row for episodes {missing}")
    write_csv(DATA / "episodes.csv", ["ep", "title", "category", "url", "summary", "takeaways", "games", "tags", "notes"], eps)
    (WORK / "areas").mkdir(parents=True, exist_ok=True)
    for area, rows in sorted(areas.items()):
        with open(WORK / "areas" / f"{area}.jsonl", "w", encoding="utf-8") as f:
            for r in rows:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        print(f"work/areas/{area}.jsonl: {len(rows)} candidates")


def build_data():
    for kind, fields in KINDS.items():
        rows = []
        for path in sorted((WORK / "parts").glob(f"*-{kind}.jsonl")):
            rows += read_jsonl(path)
        if kind == "principles":
            rows.sort(key=lambda r: (list(AREA_PREFIX).index(r.get("area", "craft")) if r.get("area") in AREA_PREFIX else 99,
                                     PRIORITY.get(r.get("priority", ""), 9), r.get("id", "")))
        elif kind == "quotes":
            rows.sort(key=lambda r: int(r.get("ep", 0) or 0))
        elif kind == "glossary":
            seen = {}
            for r in rows:  # same term from two areas: merge episode lists
                key = r["term"].strip().lower()
                if key in seen:
                    seen[key]["episodes"] = ";".join(dict.fromkeys(
                        (flat(seen[key]["episodes"]) + ";" + flat(r.get("episodes", ""))).replace(" ", "").split(";")))
                else:
                    seen[key] = r
            rows = sorted(seen.values(), key=lambda r: r["term"].lower())
        ids = [r.get("id") for r in rows if r.get("id")]
        dupes = {i for i in ids if ids.count(i) > 1}
        if dupes:
            print(f"WARNING: duplicate {kind} ids {sorted(dupes)}")
        write_csv(DATA / f"{kind}.csv", fields, rows)


if __name__ == "__main__":
    {"areas": build_areas, "data": build_data}[sys.argv[1]]()
