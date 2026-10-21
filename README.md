# sakurai-game-design

Everything Masahiro Sakurai taught in **all 261 episodes** of [*Masahiro Sakurai on Creating Games*](https://www.youtube.com/@sora_sakurai_en), turned into:

1. **A study guide for developers:** [`study-guide/`](study-guide/README.md) has 14 chapters, checklists, a glossary and an episode index.
2. **A Claude Code plugin for agents:** [`skills/sakurai-game-design`](skills/sakurai-game-design/SKILL.md) is a searchable knowledge base of 302 principles, 291 techniques, 114 review lenses, 130 quotes and 230 glossary terms, with a design-review mode. It's built in the same style as `ui-ux-pro-max`.
3. **The source material:** [`episodes/`](episodes/) holds study notes for every episode plus full transcripts of the official English subtitles.

## What's inside

```
study-guide/            the study guide (start with README.md, then 01-how-sakurai-thinks.md)
skills/sakurai-game-design/
  SKILL.md              the agent skill: priorities, workflows, query contract
  scripts/search.py     BM25 search, --review briefs, episode lookup (no dependencies)
  data/*.csv            principles, techniques, lenses, episodes, quotes, glossary
  references/           quick reference of every principle, every technique
episodes/
  index.csv             episode number, video id, title, category, length, word count
  notes/NNN-*.md        study notes per episode (lesson, key ideas, do/avoid, examples, quote, tags)
  transcripts/NNN-*.md  official English subtitles with timestamped links to the video
tools/                  the pipeline that built all of this (see below)
work/                   intermediate data from the note-taking and chapter-writing passes
.claude-plugin/         plugin and marketplace manifests
```

## Using the plugin

Install it in Claude Code from this repo, either the local clone or GitHub:

```
/plugin marketplace add /srv/projects/sakurai-game-design      # or: flossbud/sakurai-game-design
/plugin install sakurai-game-design@sakurai-game-design
```

The skill triggers on game design work: designing or reviewing mechanics, combat feel, difficulty, bosses, UI, effects, pacing, specs and team process. You can also call it directly:

```bash
S=skills/sakurai-game-design/scripts/search.py
python3 $S "hitstop sword"                          # principles, techniques, lenses
python3 $S "beginner difficulty" --area balance -n 8
python3 $S --review "flying boss that shoots fireballs and stomps"
python3 $S --episode 47                             # notes for "Eight Hit Stop Techniques"
python3 $S --transcript 47
```

## How it was built

1. **Fetch.** `tools/fetch_videos.sh` lists the channel and downloads all 261 non-compilation episodes at 720p, video only (about 8 GB, not committed). Category compilations are skipped because they re-cut earlier episodes.
2. **OCR.** The English subtitles are burned into the video, and YouTube's caption track is only a machine translation. `tools/ocr_subs.py` crops the subtitle bar, splits it into stable segments by diffing text masks, and reads each line once with RapidOCR (recognition only, about 8 seconds per episode). `tools/run_ocr.sh` runs it over every video.
3. **Transcripts.** `tools/build_transcripts.py` numbers the episodes in release order and writes `episodes/transcripts/` plus `episodes/index.csv`: 148k words, a median of about 137 words per minute. Episodes with low counts are footage with no narration (concerts, stage tours, effect reels), not OCR misses.
4. **Notes.** Twelve parallel passes wrote `episodes/notes/` and `work/batches/*.jsonl` to [`tools/NOTES_SPEC.md`](tools/NOTES_SPEC.md). Every quote was checked verbatim against its transcript.
5. **Chapters and data.** Seven passes, one or two design areas each, consolidated 813 candidate principles into the chapters and `work/parts/*.jsonl` to [`tools/SYNTHESIS_SPEC.md`](tools/SYNTHESIS_SPEC.md).
6. **Build.** `tools/build_data.py areas|data` produces the CSVs, and `tools/build_guide.py` generates the checklists, glossary, episode index and skill references. `tools/link_eps.py` expands `{{N}}` episode references into links.

To rebuild after editing data: `python3 tools/build_data.py data && python3 tools/build_guide.py`.

## Rights

All content derives from *Masahiro Sakurai on Creating Games* by Sora Ltd. The transcripts are the official English subtitles, captured for private study. The notes, principles and chapters are paraphrases with short attributed quotes. **Keep this repository private.** Don't publish the transcripts.
