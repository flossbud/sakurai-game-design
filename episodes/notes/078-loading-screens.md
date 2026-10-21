# 078 · Loading Screens

**Category:** UI · [Video](https://www.youtube.com/watch?v=JKV-30FD6NY) · [Transcript](../transcripts/078-loading-screens.md)

## In one sentence
If you can't hide load times in immersive presentation, clearly show a simple, elegant loading indicator that fits your game's world, and don't build presentation around development-build load times that will change.

## Key ideas
- Loading is unavoidable, and nobody likes watching "Loading" linger on screen.
- The first Resident Evil shows a door opening between rooms, which is really the game loading in the background. He calls it a great example of immersive presentation matched to load times. A loading icon there would ruin the illusion, so when hiding is done that well, no indicator is better. (As an aside, the length of the animation could hint at which rooms had zombies.)
- That was decades ago. Modern hardware loads very fast and today's players have little interest in waiting, so games need to feel faster. At minimum, a wait is easier to accept when you show that the game is loading.
- Some games still weave loading cleverly into presentation, but if you can't, it's better to just state clearly that the game is loading.
- Load times usually get optimized and changed between development and release, and they're typically shorter in the final game. So you may not want loading screens to depend on presentation.
- Loading indicators should be simple and elegant, and ready to show whenever needed. Few games still show text like "Now Loading...". If you use an indicator, make it evoke the atmosphere of your world.

## Do this
- Build one reusable loading indicator that can appear anywhere, for any length of time, styled to match your game's world instead of plain "Now Loading..." text.
- Only use presentation that hides loading (door-opening transitions and the like) if it still works when final load times are shorter or vary. Don't set its length from today's development build.
- When a load can't be disguised, show the indicator right away so the player knows the game hasn't stalled.

## Avoid
- Presentation tied to development-era load times that will change before release.
- Putting a loading icon on top of a transition that is already hiding the load, which breaks the illusion.

## Examples from the episode
- **Resident Evil (first game) — door transitions:** a door-opening animation hides loading so well that an indicator would only hurt it.

## Quote
> If you're going to use indicators, try to make them evoke the atmosphere of your game's world! (02:04)

## Tags
`loading` `transitions` `player-time` `icons` `clarity`
