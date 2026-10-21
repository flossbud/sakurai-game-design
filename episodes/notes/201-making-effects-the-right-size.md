# 201 · Making Effects the Right Size

**Category:** Effects · [Video](https://www.youtube.com/watch?v=rXwo0qcKJDk) · [Transcript](../transcripts/201-making-effects-the-right-size.md)

## In one sentence
Give effects enough density to match the world's scale: a large flame needs many loops or small, detailed particles, or it will read as a candle.

## Key ideas
- Effects need the right sense of scale, just as characters and stages do.
- Flames are the classic case. A flame as big as a character, or bigger, often looks like it comes from a candle or a torch. Sakurai calls this "extremely common" and an easy trap, because the effect lacks density.
- For Pyra's sword flames he gave the effects team a reference showing the density he wanted, because the fire looked too much like a candle. He wanted the final swing to get even closer to that reference, but texture limits stopped them.
- There are two fixes for flames: increase the number of loops, or use smaller, more detailed particles. Either one makes the flame feel closer to its real size.
- Taking this too far eats into texture memory. Effects are always moving, though, so they don't need to be very detailed. "The key is making them look quick and fierce."
- The same rule applies to every other kind of effect: keep the size of the world in mind and preserve the proper sense of scale.

## Do this
- Place each large fire effect next to a character. If a flame the size of the character reads like a candle or a torch, add density.
- Add density by raising the number of flame loops, or by switching to smaller, more detailed particles.
- When giving effects feedback, attach a visual reference that shows the density you want instead of describing it only in words.
- Spend texture memory on making effects look quick and fierce in motion rather than on fine detail that nobody sees while they move.
- Check every effect, not just fire, against the size of the world it lives in.

## Avoid
- Building big flames from a few large shapes. They lack density and read as candle-sized.
- Chasing detail until effects eat up your texture memory, since motion hides most of it anyway.

## Examples from the episode
- **Super Smash Bros. Ultimate — Pyra's sword flames:** the original fire looked candle-like. Sakurai supplied a density reference, and texture limits capped how far the final swing could go.

## Quote
> As a general rule for creating effects, keep the size of the world in mind and try to preserve the proper sense of scale. (01:39)

## Tags
`effects` `particles` `scale` `readability` `feedback-giving` `hardware`
