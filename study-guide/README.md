# Designing Like Sakurai: a Study Guide

A study guide to all 261 episodes of [*Masahiro Sakurai on Creating Games*](https://www.youtube.com/@sora_sakurai_en) (2022–2024), the YouTube series in which the director of Kirby and Super Smash Bros. explains how he designs games.

Every claim here traces back to an episode. Chapters link to [per-episode notes](../episodes/notes/), and each note links to the full transcript and the video. The same knowledge is packaged for AI agents as the [`sakurai-game-design` skill](../skills/sakurai-game-design/SKILL.md).

## Start here

1. Read **[01 · How Sakurai Thinks](01-how-sakurai-thinks.md)**: the 12 habits of mind behind everything else, the tensions in his advice, and a 10-step loop for designing or reviewing any feature. (About 20 minutes.)
2. Pick a track below, or jump to the chapter for whatever you're working on.
3. Run the **[pre-ship checklist](checklists.md)** against your own game.

## Chapters

| # | Chapter | Covers | Principles · techniques |
|---|---|---|---|
| 01 | [How Sakurai Thinks](01-how-sakurai-thinks.md) | The habits of mind, tensions, the Sakurai loop, a top-10 watch list | n/a |
| 02 | [Game Essence: Risk, Reward and Push-and-Pull](02-game-essence.md) | What makes play fun, stress and release, rewards, borrowing fun without copying | 24 · 21 |
| 03 | [Balance and Difficulty](03-balance-and-difficulty.md) | Target players, beginners vs. experts, handicapped tuning, distinct characters, randomness | 22 · 21 |
| 04 | [Planning, Structure and Pacing](04-planning-and-structure.md) | Concepts, proposals, specs, prototypes, openings, tutorials, cutscenes, the player's time, a small-team plan | 26 · 24 |
| 05 | [Game Feel: Impact, Response and Control](05-game-feel.md) | Hitstop, screen shake, responsiveness, lag, jumps, knockback, camera, transitions | 24 · 33 |
| 06 | [Animation](06-animation.md) | Lead-ins, attack poses, follow-through, damage poses, exaggeration, collision, blending | 21 · 24 |
| 07 | [Visuals, Characters and Effects](07-visuals-and-effects.md) | Readability, silhouettes, color, hit marks, flashes, explosions, scale, art direction | 26 · 31 |
| 08 | [Audio: Sound Effects, Music and Mixing](08-audio.md) | Mixing by relevance, impact sounds, themes, ambience, feedback to composers | 19 · 20 |
| 09 | [UI and Clarity](09-ui-and-clarity.md) | Menus, HUD, help text, skipping, remapping, text speed, wordless clarity | 23 · 23 |
| 10 | [Directing, Supervising and Working With a Team](10-directing-and-teams.md) | Decisions, feedback by retouch, daily reports, raising problems, playtesting | 27 · 22 |
| 11 | [Work Ethic, Creativity and a Career in Games](11-work-ethic-and-creativity.md) | Getting ideas, starting now, speed over polish, input and output, health, never fighting | 26 · 15 |
| 12 | [Marketing, Reveals and Online Updates](12-marketing-and-updates.md) | Honest images, trailers, demos, reveal videos, the Dojo, patches and DLC | 22 · 16 |
| 13 | [Tech, Tools and Production Pipelines](13-tech-and-tools.md) | Tunable parameters, frame rate, debug modes, testing, bug tickets, hardware | 25 · 25 |
| 14 | [Case Studies: How Sakurai's Games Were Designed](14-case-studies.md) | Kirby, Smash 64 to Ultimate, Air Ride, Meteos, Kid Icarus: Uprising, Mushiking, the channel itself | 17 · 16 |
| | [Checklists](checklists.md) | Pre-ship CRITICAL questions plus review lenses per area | |
| | [Glossary](glossary.md) | Sakurai's terms: game essence, push and pull, hit stop, lead-in, … | |
| | [Episode index](episode-index.md) | All 261 episodes, by category and in release order, with each one's lesson | |

Every chapter has the same shape: **the big ideas**, then **principles** (each with why, what to do, what to watch out for, his example and the source episodes), **techniques and numbers**, **common mistakes**, **review questions**, **exercises** and a **watch list**. Principle IDs (`FEEL-02`, `BAL-04`, …) are shared with the skill's data, so people and agents can cite the same rule.

## Tracks

| Track | For | Read |
|---|---|---|
| **One evening** | Everyone | 01 → [checklists](checklists.md) (pre-ship section) → the CRITICAL principles of whichever chapter matches your current task |
| **Game designer** | Systems, levels, combat | 01 → 02 → 03 → 04 → 05 → 14 |
| **Artist / animator** | Art, animation, VFX | 01 → 06 → 07 → 05 (impact sections) → 09 |
| **Audio** | Sound and music | 01 → 08 → 05 (impact sections) |
| **Programmer** | Gameplay and tools | 01 → 05 → 13 → 04 (specs) |
| **Lead / director / producer** | Running the project | 01 → 04 → 10 → 11 → 12 → 13 |
| **Game jam crash course** | A team with 48 hours | 01 (habits 1, 3, 4, 6) → 04 ("A small-team plan") → 05 principles FEEL-01 to FEEL-06 → 02 principles ESS-01 to ESS-05 → [pre-ship checklist](checklists.md) |

## How to study it

- **Play while you read.** After each chapter, do one of its exercises on your own game, or on a game you admire. Sakurai's own method is to compare a build with and without a single change.
- **Watch the source.** Each chapter ends with a ranked watch list. Most episodes run 2–5 minutes. Visual topics (effects, animation, posing) are much clearer on video than in the transcripts.
- **Count frames.** Several chapters assume you can feel durations in frames. Episode [76](../episodes/notes/076-learn-to-count-frames.md) teaches the "1-and-2-and" method. Practice it.
- **Review in pairs.** Have a teammate run [checklists.md](checklists.md) against your feature without your explanation. That's the "fresh tester" Sakurai insists on.
- **Mind the tensions.** Sakurai's advice is situational. When two principles conflict, the "Tensions" sections (chapter 01 and most chapters) explain which side applies when.

## What the series doesn't cover

The chapter authors flagged these gaps. Fill them from other sources, and don't attribute them to Sakurai.

- **Feel numbers:** he gives no hitstop frame counts, no screen-shake amplitudes, no cancel-window or blend lengths, and no fade durations. His one in-stop figure is "about four frames" to blend a victim into the damage pose. His jump numbers are teaching values.
- **Input:** nothing on input buffering or coyote time.
- **Scheduling:** no milestone or estimating method; the only time targets are "core fun within the first three minutes" and "a failure effect of about a second".
- **Small teams:** almost no direct advice for indies or jams. The small-team material in chapters 04 and 10 applies his principles but isn't his own words.
- **Economy and monetization:** little on economy math, pricing or monetization.
- **Online features:** nothing on telemetry, CI or crash reporting, and online play only as regional matchmaking.
- **Level layout:** sparse beyond errands, peaks and flats, and terrain that guides the eye.
- **Accessibility details:** no photosensitivity guidelines, font sizes or safe-area margins.

## Source and rights

All content derives from *Masahiro Sakurai on Creating Games* by Sora Ltd. The notes, principles and chapters are paraphrases for study. Quotes are short and verbatim from the official English subtitles (read from the videos by OCR, so expect rare typos). This repository is private study material, so keep it that way.
