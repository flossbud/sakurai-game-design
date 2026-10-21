# Episode notes spec

How each episode of *Masahiro Sakurai on Creating Games* is turned into study notes. These notes feed the study guide (`study-guide/`) and the skill's data (`skills/sakurai-game-design/data/`).

## Inputs

- `episodes/index.csv` lists each episode's number, video id, title, category, length and transcript path.
- `episodes/transcripts/NNN-slug.md` holds the official English subtitles, read from the video by OCR. Rare OCR typos are possible, so fix obvious ones silently when quoting.

## Output 1: `episodes/notes/NNN-slug.md`

Use the same file name as the transcript. Template:

```markdown
# NNN · Title

**Category:** X · [Video](https://www.youtube.com/watch?v=ID) · [Transcript](../transcripts/NNN-slug.md)

## In one sentence
The single lesson of the episode, stated as advice to a game developer.

## Key ideas
- 3–7 bullets. Paraphrase in plain words, and keep Sakurai's *reasoning* (the "because"), not just the rule.
- Keep any concrete numbers he gives (frame counts, seconds, percentages, team sizes).

## Do this
- 2–6 concrete, imperative actions a developer could take this week, e.g. "Add 4–8 frames of hitstop to heavy hits, scaled by damage."
- Write them so they make sense without having seen the video.

## Avoid
- 0–4 anti-patterns he warns about. Omit the section if there are none.

## Examples from the episode
- **Game — scene or mechanic:** what it shows. Only include examples he actually uses.

## Quote
> One short verbatim line (at most 30 words) that captures the episode. (MM:SS)

## Tags
`tag-one` `tag-two` …  (4–10 kebab-case tags; reuse the vocabulary below where it fits)
```

For non-lesson episodes (channel intro, Grab Bag history, Finale), keep the template. Put history and anecdotes in "Key ideas" and pull out whatever lessons are there. If an episode has really no actionable advice, write "Do this: —".

## Output 2: one JSON line per episode in the batch's JSONL file

```json
{"ep": 12, "summary": "<In one sentence>", "takeaways": ["<=12 words each, 2-5 items"], "games": ["Kirby Super Star", "..."], "tags": ["..."],
 "principles": [
   {"principle": "<imperative rule, <=14 words>", "domain": "<domain>", "why": "<1-2 sentences, Sakurai's reasoning>",
    "how": "<1-2 sentences, concrete application>", "anti_pattern": "<what not to do, or empty>",
    "example": "<game/scene he cites, or empty>", "quote": "<verbatim <=30 words, or empty>", "tags": ["..."]}
 ]}
```

Give 1–4 principles per episode. A principle must be advice someone could act on, not a fact about history.

### `domain` (pick exactly one)

| domain | covers |
|---|---|
| `essence` | Game essence: risk and reward, what makes play fun, core loops, push and pull, rewarding skill |
| `balance` | Difficulty, balancing, beginners and experts, handicaps, fairness, assist features |
| `planning` | Concepts, specs, planning documents, scope, structure, pacing, tutorials, cutscenes, content volume |
| `feel` | Game feel and design specifics: hitstop, responsiveness, controls, input, cancels, camera, screen transitions, frame rate |
| `animation` | Character animation, poses, timing, anticipation and follow-through, collision vs. animation |
| `visuals` | Graphics, art direction, character design, readability, color, effects, particles, screen flashes |
| `audio` | Sound effects, music, voice, mixing, audio references |
| `ui` | Menus, HUD, help text, icons, wordless clarity, accessibility of information |
| `team` | Directing, producers, supervising, specs for teammates, giving feedback, playtesting with others |
| `craft` | Work ethic, creativity, health, productivity, career, handling criticism |
| `marketing` | Targeting, trailers, reveals, online updates, community |
| `tech` | Programming, tools, debug features, builds, hardware limits |
| `case-study` | Lessons stated through the design history of one of his games |

### Tag vocabulary (prefer these; add new ones when needed)

risk-reward, core-fun, player-agency, rewarding-skill, push-pull, hitstop, screen-shake, impact, feedback, responsiveness, input-buffer, cancels, controls, camera, frame-rate, transitions, loading, readability, clarity, silhouette, color, character-design, effects, particles, flashing, lighting, animation-timing, anticipation, hitboxes, difficulty, beginners, experts, handicap, assist, player-time, pacing, climax, tutorial, onboarding, cutscenes, story, boss-design, enemy-design, level-design, combat, multiplayer, party-game, competitive, single-player, rewards, collectibles, replayability, randomness, balance, numbers-tuning, scope, specs, prototyping, playtesting, iteration, direction, delegation, communication, feedback-giving, motivation, health, ideas, criticism, marketing, trailers, updates, dlc, menus, hud, help-text, icons, sound-effects, music, voice, mixing, localization, accessibility, debug-tools, hardware, history, smash-bros, kirby, kid-icarus, meteos
