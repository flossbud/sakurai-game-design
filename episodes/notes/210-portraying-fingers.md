# 210 · Portraying Fingers

**Category:** Animation · [Video](https://www.youtube.com/watch?v=nCvdmQKrjf8) · [Transcript](../transcripts/210-portraying-fingers.md)

## In one sentence
Angle the fingers in a diagonal grip on anything swung with the forearm so it looks natural, and spend finger bones and processing only where they matter.

## Key ideas
- A hand holding something is an easy place to make a mistake. When you simply grip an object it naturally sits perpendicular to your fingers, but when you swing it along with your forearm you use a diagonal grip.
- His bad example "looks too much like an action figure." Older games with fewer polygons and simpler skeletons had little choice, but you should still angle the fingers to get a natural grip.
- Fingers are very complex for their size, so when processing load is a problem they tend to be "the first things to go." They aren't removed entirely. Instead they are locked in place while still looking as if they could move.
- Artists sometimes make several finger patterns and swap them in when appropriate.
- The number of movable fingers can hint at what the hardware can do, but only when comparing the same game against the same standards. To players with high-spec machines the whole issue may seem like "ancient history."
- Always consider processing cost. On a screen with many characters, giving every finger its own structure and calculating its movement continuously is very expensive. Depending on the hardware and your goals, cut where you can and divert processing to the parts that matter.

## Do this
- For weapons and tools swung with the forearm (swords, bats, hammers), pose the grip diagonally across the fingers instead of at a right angle to them.
- Review every held-item pose for the stiff "action figure" look, and fix it by angling the fingers.
- When processing is tight, lock finger joints and swap between a few pre-made finger patterns instead of animating every joint.
- Estimate the processing cost of finger articulation on your busiest screens, and move that budget to whatever matters most for your game.

## Avoid
- A rigid perpendicular grip on a swung weapon, which makes the character look like an action figure.
- Fully articulating and simulating every finger on screens crowded with characters.

## Examples from the episode
- **On-screen comparison (game not named):** a character gripping a weapon at a right angle looks like an action figure, while the corrected version uses a diagonal grip.
- **Crowded game screen (shown, not named):** giving structure to every finger there and calculating its movement would be very expensive.

## Quote
> if you're going to swing it along with your forearm, you use a diagonal grip. (00:12)

## Tags
`animation` `poses` `hands` `hardware` `optimization` `character-design`
