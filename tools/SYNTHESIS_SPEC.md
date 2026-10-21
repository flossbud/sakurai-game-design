# Chapter synthesis spec

Second pass: turn per-episode notes into study-guide chapters and the skill's searchable data. Each synthesis agent owns one or two design **areas** (the `domain` values from `NOTES_SPEC.md`).

## Inputs

- `work/areas/<area>.jsonl` holds every principle candidate tagged with your area, one per line, with its episode number.
- `episodes/notes/*.md` holds per-episode notes. Read the notes of every episode that appears in your area files.
- `episodes/transcripts/*.md` holds full transcripts. Read one when a note is thin, or when you need exact numbers, examples or a quote.
- `episodes/index.csv` holds episode titles and categories.
- Also skim notes from other categories that touch your area: `grep -l` the notes directory for your tags. Grab Bag episodes often hide relevant lessons.

## Output 1: study-guide chapter(s), `study-guide/NN-slug.md`

Write for game developers who have never seen the series. Use Sakurai's reasoning, not just his rules. Structure:

```markdown
# NN · Chapter title

> One-paragraph summary: Sakurai's stance on this area and why it matters.

## The big ideas
2–4 short paragraphs that tie the principles together into a way of thinking.

## Principles
### AREA-01 · Imperative principle title
**Why:** his reasoning. **Do:** concrete application. **Watch out:** the anti-pattern.
*Sakurai's example:* … · Episodes: [12](../episodes/notes/012-slug.md), [87](../episodes/notes/087-slug.md)
(Repeat for each principle, most important first.)

## Techniques and numbers
A table: technique | what to do (with any numbers he gives) | when | episodes

## Common mistakes
A bulleted list.

## Review questions
Questions a designer asks of their own build (these become the lenses).

## Exercises
3–6 hands-on drills a small team could do in a day or less on their own game.

## Watch list
Episodes to watch in priority order, each with one line on why.
```

Link episodes with relative links to their notes files. Quote Sakurai sparingly: short verbatim lines only (at most 30 words each), and at most about 8 per chapter. These are Sora Ltd.'s words.

## Output 2: data parts, `work/parts/<area>-<kind>.jsonl`

Merge duplicate candidates across episodes into one consolidated principle that lists every supporting episode. Aim for **12–30 principles per area**: fewer, stronger principles beat many near-duplicates. IDs use the area prefix: `ESS` essence, `BAL` balance, `PLAN` planning, `FEEL` feel, `ANIM` animation, `VIS` visuals, `AUD` audio, `UI` ui, `TEAM` team, `CRAFT` craft, `MKT` marketing, `TECH` tech, `CASE` case-study.

- `<area>-principles.jsonl`: `{"id":"FEEL-01","area":"feel","priority":"CRITICAL|HIGH|MEDIUM|LOW","principle":"<=14 words, imperative","why":"","how_to_apply":"","anti_pattern":"","example":"","review_question":"a yes/no or what-question to ask of a build","episodes":"3;45;120","keywords":"space separated synonyms people might search, e.g. hitstop hit-stop freeze frame impact pause"}`
- `<area>-techniques.jsonl`: concrete, implementable recipes, with numbers where he gives them. `{"id":"FEEL-T01","area":"feel","technique":"","what":"","how":"","when":"","pitfalls":"","episodes":"","keywords":""}`. Some areas, like craft and team, may have few; that's fine.
- `<area>-lenses.jsonl`: 4–10 review questions per area. `{"id":"FEEL-L01","area":"feel","lens":"question","look_for":"what good looks like","red_flags":"what bad looks like","principles":"FEEL-01;FEEL-04","episodes":"","keywords":""}`
- `<area>-glossary.jsonl`: Sakurai's own terms and coinages. `{"term":"","meaning":"","episodes":""}`
- `<area>-quotes.jsonl`: the 5–10 best short quotes. `{"quote":"<=30 words verbatim","ep":12,"title":"","time":"MM:SS","theme":""}`

Priority means:
- **CRITICAL:** getting it wrong breaks the core experience: the fun, fairness, the player's grasp of what's happening, or respect for the player's time.
- **HIGH:** clearly raises quality or game feel in most games.
- **MEDIUM:** polish and craft.
- **LOW:** situational, or specific to one kind of game.

Every field is plain text with no newlines. Write valid JSON, one object per line.
