#!/usr/bin/env python3
"""Search Masahiro Sakurai's game-design knowledge base.

Examples:
  search.py "hitstop heavy attack"                 # best matches across principles, techniques, lenses
  search.py "boss fight" --domain principles -n 8  # one dataset
  search.py "difficulty" --area balance            # filter by design area
  search.py --review "boss fight with flying phase and fireballs"
  search.py --episode 3                            # print an episode's notes
  search.py --transcript 3                         # print an episode's transcript
  search.py --areas                                # list areas with counts

No third-party dependencies. Ranking is BM25 over each CSV row's text.
"""
import argparse
import csv
import math
import re
import sys
from collections import Counter
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = SKILL_DIR / "data"
REPO_ROOT = SKILL_DIR.parent.parent

DOMAINS = {
    # dataset: (file, title field, fields shown in results, fields searched with extra weight)
    "principles": ("principles.csv", "principle",
                   ["id", "area", "priority", "why", "how_to_apply", "anti_pattern", "example", "review_question", "episodes"],
                   ["principle", "keywords"]),
    "techniques": ("techniques.csv", "technique",
                   ["id", "area", "what", "how", "when", "pitfalls", "episodes"],
                   ["technique", "keywords"]),
    "lenses": ("lenses.csv", "lens",
               ["id", "area", "look_for", "red_flags", "principles", "episodes"],
               ["lens", "keywords"]),
    "episodes": ("episodes.csv", "title",
                 ["ep", "category", "summary", "takeaways", "games", "notes", "url"],
                 ["title", "tags"]),
    "quotes": ("quotes.csv", "quote", ["ep", "title", "time", "theme"], ["quote", "theme"]),
    "glossary": ("glossary.csv", "term", ["meaning", "episodes"], ["term"]),
}
DEFAULT_MIX = ["principles", "techniques", "lenses"]
PRIORITY_ORDER = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3}
MIN_RELATIVE = 0.35  # drop matches scoring below this fraction of the best match
AREA_BOOST = 1.4
# words that hint which design areas a query is about; matching rows get a score boost
AREA_HINTS = {
    "essence": "risk reward fun core loop enemy enemies boss bosses strategy combat shooter puzzle competitive",
    "balance": "difficulty difficult hard easy beginner beginners expert balance stuck fair handicap boss bosses",
    "planning": "concept pacing tutorial onboarding cutscene story structure level levels reward rewards scope prototype jam proposal",
    "feel": "hitstop hit stop shake impact jump jumps responsive lag input camera controls dash cancel knockback weight floaty fly flying aerial air",
    "animation": "animation pose poses windup lead follow-through attack attacks swing frames",
    "visuals": "effect effects particles explosion flash color readability readable silhouette art character lighting fireball fireballs projectile",
    "audio": "sound sounds music audio sfx mix voice reverb",
    "ui": "menu menus hud ui text font icons button buttons remap skip pause loading",
    "team": "team director feedback review meeting playtest playtesting decision decisions",
    "craft": "motivation ideas career habit habits health",
    "marketing": "trailer trailers marketing reveal demo update updates patch",
    "tech": "debug parameters tuning frame rate fps build bug bugs hardware optimization",
}
STOP = set("a an and are as at be but by for from has have how i if in into is it its of on or so that the "
           "their them then there these this to was what when where which who will with you your".split())


def tokenize(text):
    return [t for t in re.findall(r"[a-z0-9]+", text.lower().replace("-", " ")) if t not in STOP]


def stem(t):
    for suf in ("ing", "ies", "es", "ed", "s"):
        if len(t) > len(suf) + 2 and t.endswith(suf):
            return t[: -len(suf)] + ("y" if suf == "ies" else "")
    return t


def load(domain):
    path = DATA_DIR / DOMAINS[domain][0]
    if not path.exists():
        return []
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


class BM25:
    def __init__(self, docs, k1=1.4, b=0.75):
        self.docs = [[stem(t) for t in d] for d in docs]
        self.k1, self.b = k1, b
        self.avg = sum(map(len, self.docs)) / max(len(self.docs), 1)
        df = Counter(t for d in self.docs for t in set(d))
        n = len(self.docs)
        self.idf = {t: math.log(1 + (n - c + 0.5) / (c + 0.5)) for t, c in df.items()}
        self.tf = [Counter(d) for d in self.docs]

    def score(self, query):
        q = [stem(t) for t in tokenize(query)]
        out = []
        for i, tf in enumerate(self.tf):
            s, dl = 0.0, len(self.docs[i])
            for t in q:
                if t in tf:
                    s += self.idf[t] * tf[t] * (self.k1 + 1) / (tf[t] + self.k1 * (1 - self.b + self.b * dl / self.avg))
            out.append(s)
        return out


def hinted_areas(query):
    q = set(tokenize(query))
    return {a for a, words in AREA_HINTS.items() if q & set(words.split())}


def prefer_hinted(results, query, keep=2):
    """Keep only results from areas the query hints at, unless that leaves too few."""
    hinted = hinted_areas(query)
    picked = [x for x in results if x[1].get("area") in hinted]
    return picked if len(picked) >= keep else results


def search(domain, query, n, area=None):
    rows = load(domain)
    if area:
        rows = [r for r in rows if r.get("area", "").lower() == area.lower()
                or area.lower() in r.get("category", "").lower()]
    if not rows:
        return []
    _, title, shown, boosted = DOMAINS[domain]
    docs = []
    for r in rows:
        boost = " ".join(r.get(k, "") for k in boosted)
        docs.append(tokenize(" ".join(r.values()) + (" " + boost) * 2))
    scores = BM25(docs).score(query)
    hinted = hinted_areas(query)
    scores = [s * AREA_BOOST if r.get("area") in hinted else s for s, r in zip(scores, rows)]
    ranked = sorted(zip(scores, rows), key=lambda x: (-x[0], PRIORITY_ORDER.get(x[1].get("priority", ""), 9)))
    top = ranked[0][0] if ranked else 0
    return [(s, r) for s, r in ranked if s > 0 and s >= top * MIN_RELATIVE][:n]


def show(domain, results):
    _, title, shown, _ = DOMAINS[domain]
    print(f"\n## {domain} ({len(results)} match{'es' if len(results) != 1 else ''})")
    for s, r in results:
        head = r.get(title, "")
        tag = r.get("id") or (f"ep {r['ep']}" if r.get("ep") else "")
        print(f"\n### {tag + ' · ' if tag else ''}{head}")
        for k in shown:
            if k in ("id",) or not r.get(k):
                continue
            print(f"- **{k}:** {r[k]}")


def review(query, n):
    print(f"# Sakurai design review: {query}\n")
    print("Work through every lens below against the actual design or build. For each, write what")
    print("the design does now, what Sakurai's principle says, and the concrete change, then rank")
    print("the changes by player impact.")
    lenses = prefer_hinted(search("lenses", query, n * 2), query)[:n]
    principles = search("principles", query, n * 2)
    principles.sort(key=lambda x: (PRIORITY_ORDER.get(x[1].get("priority", ""), 9), -x[0]))
    techniques = prefer_hinted(search("techniques", query, n * 2), query)[:n]
    episodes = search("episodes", query, 5)
    show("lenses", lenses)
    show("principles", principles)
    show("techniques", techniques)
    anti = [r["anti_pattern"] for _, r in principles if r.get("anti_pattern")]
    if anti:
        print("\n## anti-patterns to check for")
        for a in dict.fromkeys(anti):
            print(f"- {a}")
    print("\n## episodes worth reading in full")
    for _, r in episodes:
        print(f"- ep {r['ep']} · {r['title']} ({r['category']}): {r.get('notes', '')}")
    if not (lenses or principles or techniques):
        print("\nNo matches. Retry with 2-5 plainer words (e.g. 'boss difficulty', 'attack impact').")


def episode_file(num, kind):
    for r in load("episodes"):
        if r["ep"] == str(num):
            rel = r["notes"] if kind == "notes" else r["notes"].replace("/notes/", "/transcripts/")
            return REPO_ROOT / rel
    return None


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("query", nargs="?", default="")
    ap.add_argument("--domain", choices=list(DOMAINS), help="search one dataset")
    ap.add_argument("--area", help="filter by design area (essence, balance, feel, planning, ...)")
    ap.add_argument("-n", type=int, default=5, help="results per dataset")
    ap.add_argument("--review", metavar="DESIGN", help="build a design-review brief for a feature or design")
    ap.add_argument("--episode", type=int, help="print an episode's notes")
    ap.add_argument("--transcript", type=int, help="print an episode's transcript")
    ap.add_argument("--areas", action="store_true", help="list design areas with principle counts")
    a = ap.parse_args()

    if a.episode or a.transcript:
        num, kind = (a.episode, "notes") if a.episode else (a.transcript, "transcript")
        path = episode_file(num, kind)
        if not path or not path.exists():
            sys.exit(f"episode {num} not found")
        print(path.read_text(encoding="utf-8"))
    elif a.areas:
        counts = Counter(r["area"] for r in load("principles"))
        for area, c in counts.most_common():
            print(f"{area:12} {c} principles")
    elif a.review:
        review(a.review, a.n)
    elif a.query:
        for d in [a.domain] if a.domain else DEFAULT_MIX:
            show(d, search(d, a.query, a.n, a.area))
    else:
        ap.print_help()


if __name__ == "__main__":
    main()
