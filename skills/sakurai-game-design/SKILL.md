---
name: sakurai-game-design
description: "Game design intelligence distilled from all 261 episodes of Masahiro Sakurai's 'Masahiro Sakurai on Creating Games' (Kirby, Super Smash Bros., Kid Icarus: Uprising). Use when designing, tuning, reviewing or planning a game or game feature: core loop and risk/reward, combat and hit feel (hitstop, screen shake, attack animation, cancels), jumps and controls, difficulty and balance, enemies and bosses, rewards and progression, pacing, tutorials and onboarding, cutscenes, UI/HUD/menus, readability of effects/visuals/audio, playtesting, scoping a game or game jam, directing a team, or trailers and reveals. Searchable local data: 302 principles, 291 techniques, 114 review lenses, 130 quotes, 230 glossary terms, plus notes and transcripts for all 261 episodes."
---

# Sakurai Game Design

Masahiro Sakurai's design knowledge as a searchable knowledge base: 302 principles (each with why, how to apply, anti-pattern, example and source episodes), 291 implementable techniques, 114 review lenses, 130 verbatim quotes and 230 glossary terms. All of it is drawn from the official English subtitles of his 261-episode YouTube series, with per-episode notes and full transcripts for checking the source.

## When to apply

Use this skill when the task involves **how a game plays, feels, reads or gets made**: designing a mechanic, enemy, boss, level, reward or mode; tuning combat feel, jumps, difficulty or balance; reviewing a build or design doc; planning scope, a prototype or a game jam; writing specs for teammates; designing menus, HUD, tutorials or cutscenes; judging effects, animation or audio; or answering "what would Sakurai do?"

Skip it for engine plumbing, build systems, networking code or anything that doesn't change what the player experiences, unless it affects responsiveness, frame rate or the tuning pipeline (those are covered under `tech`).

## Design priorities

*Work top-down: a game that fails priority 1 can't be saved by priority 7. Query an area with `--area <area>`. `references/quick-reference.md` lists every principle by area.*

| # | Category | Impact | Area | Key checks (must have) | Anti-patterns (avoid) |
|---|---|---|---|---|---|
| 1 | Game essence | CRITICAL | `essence` | Risk and reward side by side (ESS-01); every action has an opposing downside (ESS-02); riskiest play pays most (ESS-03); stress then release into growth (ESS-04) | Copying a mechanic without knowing why it's fun (ESS-05); strong options with no counterweight |
| 2 | Audience and kindness | CRITICAL | `balance` | Target player chosen first (BAL-01); beginners protected early (BAL-02); no permanent stuck points (BAL-03); tuned with a handicap, then easier (BAL-04) | Tuning difficulty to the dev team; "average" options with no peaks or valleys (BAL-06) |
| 3 | Player's time | CRITICAL | `planning`, `ui` | Core fun within the first minutes (PLAN-03); control time maximized (PLAN-04); skip and pause anything non-interactive (UI-01); back in control within seconds of failing (BAL-05, FEEL-06) | Long intros, slow fades, unskippable cutscenes, waits that aren't play |
| 4 | Feel and response | CRITICAL | `feel`, `animation` | Press frame visibly registers (FEEL-01, ANIM-01); stops on big moments (FEEL-02); hits connect where they look like they do (FEEL-04, ANIM-02); lag hunted down (FEEL-03) | Dead button presses; impact with no stop, shake or sound; testing on laggy TVs |
| 5 | Clarity | HIGH | `visuals`, `ui` | Gameplay elements stand out from decoration (VIS-01); characters visible inside effects (VIS-02); color never the only signal (VIS-03); silhouettes read in solid black (VIS-04); playable without reading (UI-05) | Additive-only effects; heavy blur or depth of field; style beating legibility |
| 6 | Rewards and structure | HIGH | `essence`, `planning` | Rewards designed early and fit the concept; next reward visible; difficulty shaped like a mountain trail, not a ramp | Rewards with nothing to spend them on; enemies scaled in lockstep with the player |
| 7 | Specs and tuning pipeline | HIGH | `tech`, `planning` | Tunables outside code (TECH-01); speed independent of frame rate (TECH-04); frame-rate target held (TECH-05); timings in frames, speeds in units | Magic numbers in code; specs a teammate can't implement without asking |
| 8 | Exaggeration and polish | MEDIUM | `animation`, `visuals`, `audio` | "Too much is just right" poses; impact sounds that hit instantly with a short tail (AUD-02); mixing by relevance (AUD-01) | Interpolation softening key poses; realistic-but-weak motion; long reverb tails |
| 9 | Direction and team | MEDIUM | `team`, `craft` | One director decides (TEAM-01); concept steady, small corrections (TEAM-02); problems raised early with a fix (TEAM-03); decisions on the spot (TEAM-04) | Majority votes on creative calls; reviews left overnight; feedback relayed through one person |
| 10 | Marketing and shipping | LOW | `marketing` | Honest images (MKT-02); trailers reach gameplay fast (MKT-03); ship as if no patch is coming (MKT-04, TECH-17) | Trailers that open on logos and story; planning to fix it in a patch |

Some advice pulls in two directions (depth vs. reach, a steady concept vs. course correction, exaggeration vs. faithfulness to a source). Read the "Tensions to hold" table in `study-guide/01-how-sakurai-thinks.md` before applying a principle outside its context.

---

## Running the search tool

The tool and data live in this skill's directory. Use the full path; don't assume a working directory:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/skills/sakurai-game-design/scripts/search.py" "<query>" [--domain <dataset>] [--area <area>] [-n N]
```

If `CLAUDE_PLUGIN_ROOT` isn't set (for example when working inside this repo), use the skill's base directory shown when the skill loads: `<base>/scripts/search.py`. It needs Python 3 and has no dependencies.

| Command | Use it for |
|---|---|
| `search.py "<2-5 words>"` | Best matches across principles, techniques and lenses |
| `search.py "<query>" --domain principles\|techniques\|lenses\|episodes\|quotes\|glossary` | One dataset |
| `search.py "<query>" --area feel` | Restrict to a design area: `essence balance planning feel animation visuals audio ui team craft marketing tech case-study` |
| `search.py --review "<feature or design, in a sentence>"` | A design-review brief: lenses, prioritized principles, techniques, anti-patterns, episodes to read |
| `search.py --episode 47` / `--transcript 47` | An episode's notes, or its full transcript |
| `search.py --areas` | Areas and their principle counts |

### Query contract

- Build each query around **one intent in 2–5 plain words**, such as `"hitstop sword"`, `"beginner difficulty"`, `"menu help text"` or `"boss strategy reward"`.
- Check that the top result's area fits the question. **Retry once** with narrower words or an explicit `--area` if results are off-topic.
- If nothing matches, say so and fall back to the priority table above, labeled as general guidance. **Never present a 0-result search as Sakurai's view**, and never invent Sakurai quotes, numbers or examples.
- The series has gaps. Sakurai gives no hitstop frame counts, no shake amplitudes and nothing on input buffering or coyote time. When you need a number he didn't give, say so and label your value as a starting point to tune.

## Workflows

### A. Designing something new (game, mechanic, enemy, boss, mode, menu)

1. **Audience and essence first.** Run `search.py "<the thing> risk reward" --area essence`, plus `--area balance` for who it's for. Write down the target player, the risk, the reward and how close together they are.
2. **Area detail.** Query the relevant areas: `feel`/`animation` for actions, `visuals`/`audio` for presentation, `ui` for menus and HUD, `planning` for structure, pacing, tutorials and rewards.
3. **Techniques.** Run `search.py "<concern>" --domain techniques` for concrete recipes, such as hit-stop poses, screen-shake presets, the explosion phases or the jump model.
4. **Spec it.** Timings go in frames, speeds in explicit units, and every tunable number in a parameter (TECH-01, PLAN specs).
5. **Present the design** with principle IDs and episode numbers next to each decision, so a teammate can read the reasoning in the episode notes.

### B. Reviewing a design or build

1. Run `search.py --review "<one-sentence description of the feature>"`.
2. For **every lens** returned, state what the design does now, what the principle says, and the concrete change.
3. Also run the pre-ship questions in `study-guide/checklists.md` (all CRITICAL principles as yes/no questions).
4. Report findings ranked by player impact (CRITICAL, then HIGH, then MEDIUM). For each one, give the issue, the principle ID and episodes, the fix, and how to verify the fix.
5. Keep **Sakurai's stated position** (cite it) separate from **your extrapolation** (label it).

### C. Tuning game feel

Search techniques by symptom: `"hits feel weak"`, `"jump floaty"`, `"attack unresponsive"`, `"screen hard to read"`. Apply one change at a time and compare builds with and without it, which is Sakurai's own method in several episodes.

### D. Planning and scoping (prototype, proposal, game jam)

Query `--area planning` and `--area team`. The core moves are: fix one concept and steer by it; prove the core fun in a bare prototype; write proposals hot, fast and brief; commit to one plan with no Plan B; cut anything that doesn't serve the concept; put the climax first. Chapter 04 of the study guide is the long form.

### E. "What does Sakurai say about X?"

Search principles and quotes (`--domain quotes`), then open the cited episode notes (`--episode N`). Read the transcript (`--transcript N`) when wording or nuance matters. Quote only lines that appear in `quotes.csv` or a transcript, and keep them short.

## References

| File (relative to the plugin root) | Contents |
|---|---|
| `study-guide/01-how-sakurai-thinks.md` | The 12 habits of mind, tensions, the Sakurai loop. **Read first for any open-ended design task.** |
| `study-guide/02`–`14-*.md` | Chapters by area: principles, techniques and numbers, common mistakes, review questions, exercises, watch list |
| `study-guide/checklists.md` | Pre-ship CRITICAL questions plus review questions per area |
| `study-guide/glossary.md` | Sakurai's terms (game essence, push and pull, hit stop, lead-in, follow-through, …) |
| `skills/sakurai-game-design/references/quick-reference.md` | Every principle, one line each, by area |
| `skills/sakurai-game-design/references/techniques.md` | Every technique in full |
| `episodes/notes/NNN-*.md`, `episodes/transcripts/NNN-*.md` | Per-episode study notes and full subtitles |

## Pre-delivery checklist (any game feature)

Before calling a feature done, answer these 10 questions. They are the Sakurai loop from chapter 01.

- [ ] **Audience:** who is it for, and is its risk level right for them? (BAL-01)
- [ ] **Essence:** is the reward right next to the risk? (ESS-01)
- [ ] **Rewards:** can the player see what they're working toward, and does it fit the concept?
- [ ] **Feel:** does the press frame react, and does the impact frame stop, shake, flash and sound? (FEEL-01, FEEL-02)
- [ ] **Clarity:** in a frozen screenshot of the busiest moment, can a newcomer tell what's happening? (VIS-01, VIS-02)
- [ ] **Time:** is any part waiting rather than playing, and can it be cut or skipped? (PLAN-04, UI-01)
- [ ] **Distinctness:** does each option have a two-word identity with strengths *and* weaknesses? (BAL-06)
- [ ] **Spec:** are timings in frames, speeds in units and tunables outside code? (TECH-01)
- [ ] **Test:** was it played with a handicap and by fresh players watched in silence, then made easier? (BAL-04)
- [ ] **Trim:** does anything here not serve the concept? (PLAN-01)

## Source and rights

All content derives from *Masahiro Sakurai on Creating Games* (Sora Ltd.). Notes and principles are paraphrased. Transcripts are the official English subtitles, read from the videos by OCR for private study. Don't paste long transcript passages into public output; quote briefly and link the episode.
