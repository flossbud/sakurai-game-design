# 255 · What Happens When You Shift the Center of Gravity?

**Category:** Design Specifics · [Video](https://www.youtube.com/watch?v=jeA-m-Bzs04) · [Transcript](../transcripts/255-what-happens-when-you-shift-the-center-of-gravity.md)

## In one sentence
Don't settle for perfectly straight motion or rotation around an exact center: add a wobble to trajectories and move pivots off-center so objects move with personality instead of following your software's bland defaults.

## Key ideas
- The topic is filed under Design Specifics, but it ties into animation and effects too.
- Shotzo, the cannon in the Kirby games, fires in a way that feels great because its cannonballs shake as they fly. The team called them "wobbly cannonballs." A ball flying in a straight line wasn't interesting to look at, so they slid the sprite's position around in a six-frame loop: up, right-up, right-down, down, left-down, left-up. It feels completely different, and it also suited the afterimages of the Game Boy's screen.
- When faced with straight, mechanical movement or simple rotation around a center point, it's important to figure out how to add personality.
- In Smash Bros. Ultimate, a thrown bomb spins around an axis shifted slightly away from its center, which makes the motion feel a little erratic. Rotating around the exact center would have felt less organic.
- Pyra's side special, Blazing End, first used the sword's grip as the axis of rotation, a normal choice. Sakurai made a mock-up during review and the axis was shifted a bit, which gave a distinct difference in expression.
- To animators this may all be obvious, since "animation" means putting a soul into something unmoving. Designers working from a game design perspective, though, may be used to moving things in straight lines or smooth circles.
- Anything works as long as it feels right, but look for ways to avoid the blandness that comes from just following your software's tendencies.

## Do this
- Give straight-flying projectiles a small looping positional offset on top of their path, such as a six-frame cycle of up, right-up, right-down, down, left-down, left-up.
- For thrown or spinning objects and swung weapons, move the pivot slightly off the geometric center (or off the grip) and compare it with the centered version.
- Review motion that comes straight from engine or tool defaults (linear movement, rotation around the center) and ask how each one could show more personality.
- During reviews, make a quick mock-up of the alternative motion so the team can see the difference.

## Avoid
- Straight-line movement and smooth center-point rotation left exactly as your software produces them.

## Examples from the episode
- **Kirby series — Shotzo's "wobbly cannonballs":** a six-frame sprite-offset loop makes the shots feel far better than a straight line.
- **Super Smash Bros. Ultimate — bomb throw:** the spin axis is offset from the bomb's center, so the motion feels slightly erratic and more organic.
- **Super Smash Bros. Ultimate — Pyra's Blazing End:** the rotation axis was moved off the sword's grip after Sakurai's mock-up.

## Quote
> Try to find ways to avoid the blandness that can come from simply following your software's tendencies. (02:22)

## Tags
`animation-timing` `rotation` `organic-motion` `projectiles` `effects` `kirby` `smash-bros`
