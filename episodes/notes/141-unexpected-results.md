# 141 · Unexpected Results

**Category:** Design Specifics · [Video](https://www.youtube.com/watch?v=6P8zwwQ9OhU) · [Transcript](../transcripts/141-unexpected-results.md)

## In one sentence
Late optimization or differences between dev hardware and retail units can silently change the difficulty you tuned, so re-check on the final build and the real production unit, and when a launch problem is too risky to fix at its core, patch it with narrow, contained changes.

## Key ideas
- Even in Sakurai's own games, unexpected and undesirable things end up in the release version. He swallows his pride and shows three cases.
- **Meteos (DS):** He programmed every planet's parameters himself and confirmed everything on actual hardware, on a tight schedule. Near the end, the game's processing was optimized, and because game speed was directly tied to processing speed, the game got faster. The difficulty curve shifted and play became harder than intended: some sequences are tough to finish in the time allotted. He calls it "a disappointing memory." He was only involved in the first Meteos.
- **Sodatete! Kouchuu Ouja Mushiking:** He tuned the game on a custom development board just under one square meter in size and never played the actual portable unit. On the finalized production unit, the Mushi got hungry faster than he expected, probably because the dev board and production unit ran at different processing speeds. The game is still playable.
- **Smash Bros. Ultimate:** At initial release, CPU fighters felt too difficult. Several team members all raised the same concern, so he doesn't think he imagined it. He still doesn't know the cause; his only, unproven theory is a processing speed increase.
- **The fix was deliberately narrow:** Adjusting the core CPU functions or each mode's difficulty would have meant bug-testing many game elements again, so that was off the table. Instead the team lowered the difficulty of Challenger fights and added a Very Easy difficulty to World of Light through a downloadable patch. "In the old days," there would have been no way to fix it at all.
- "When you're working with computers, sometimes there's no telling what you might get." There's no checklist that covers every possible problem, and successes "may all be balancing precariously on the edge of failure."

## Do this
- Find out whether any gameplay timing (enemy or block speed, time limits, hunger or decay rates) depends on processing speed. If it does, replay the difficulty-critical content after every optimization pass, and schedule a final difficulty check after late optimization lands.
- Before sign-off, play the finished game on the actual retail/production hardware, not only on the dev board or dev kit you tuned with.
- Treat it as a real problem when several team members independently report the same feel issue (e.g., that CPU opponents feel too difficult), even if you can't find the cause.
- For a post-launch difficulty problem, prefer contained fixes, such as lowering specific encounters or adding an easier difficulty option, over changing core AI or global difficulty code, which would force wide re-testing.

## Avoid
- Tuning only on a dev board and never playing the production unit.
- Assuming smoother performance is purely a win when game speed is tied to processing speed.
- Touching core systems (e.g., CPU AI functions) in a late patch when a narrow change can address the symptom.

## Examples from the episode
- **Meteos:** late processing optimization sped up the game and made planets harder than intended.
- **Sodatete! Kouchuu Ouja Mushiking:** tuned on a dev board just under one square meter. On the production unit, the Mushi got hungry faster.
- **Smash Bros. Ultimate:** CPU fighters were too hard at launch. A patch lowered Challenger fight difficulty and added Very Easy to World of Light.

## Quote
> But when you're working with computers, sometimes there's no telling what you might get. (03:13)

## Tags
`difficulty` `numbers-tuning` `hardware` `optimization` `game-speed` `updates` `meteos` `smash-bros`
