# 244 · The Limitations of Particle Effects

**Category:** Effects · [Video](https://www.youtube.com/watch?v=jAQv4PTQvQE) · [Transcript](../transcripts/244-the-limitations-of-particle-effects.md)

## In one sentence
Particles always cost processing, so get the most out of each one: keep them short and fast, pack several into one billboard, stagger their timing and positions, and draw them large.

## Key ideas
- "Particles" are effects that scatter in large numbers, including billboard particles. They need to appear in the largest possible quantity at the lowest possible processing cost, which takes a range of techniques.
- Sakurai has used particle-like effects since the first Kirby game, when just getting anything on screen was hard. Each jump in hardware power eased the limits, but particles always have some cost, so his teams set rules for using them.
- Keep them short. Lingering after-effects would be nice, but new particles have to appear quickly. The shorter lifespan is made up for with higher speed.
- Combine several particles into one, and make them somewhat large. The bubbles from a Steel Diver projectile look like many particles but are a few panels, each holding several bubbles. An abundance of tiny particles would be great but isn't affordable, so each billboard is drawn large to make the most of it.
- Stagger the timing: instead of spawning particles for several objects at once, offset them to reduce how many are on screen at the same time. Stagger the positions too, because there's no point in making lots of particles if they all land on top of each other.
- He envies the lavish effects in games like Tekken 7, but Smash differs in hardware power, camera distance and the number of hit effects. They reproduced such effects as best they could but couldn't for fast repeated hits. You can only work within your game's limits.
- In Kirby's Dream Land, the stars from defeating an enemy and the bomb explosions are hand-placed in each animation frame; there's no particle-movement code, only coordinates. They were built bit by bit with a Famicom-based dev tool and used a lot of ROM but little processing. The inhale effect plays randomly from a set of movement patterns. Mixing white and black pixels made it visible on any background color, though using a whole 8x16 piece for a 2x4 image felt wasteful. That hardware trained you to be economical.

## Do this
- Give particles short lifetimes and higher velocity, so bursts still read without lingering on screen.
- Pack several particles (e.g., a cluster of bubbles) into one billboard texture instead of spawning each one separately.
- When several objects emit at once, offset their spawn timing so fewer particles are on screen at the same time.
- Offset spawn positions so particles don't overlap and waste drawing.
- Use fewer, larger billboards rather than many tiny ones.
- When processing is tight, use hand-authored frame animations or random picks from a few preset motion patterns instead of simulating particles, and mix light and dark pixels so effects show on any background.

## Avoid
- Long-lived particles that crowd the screen when new ones keep spawning.
- Piles of particles stacked on top of each other.
- Copying effects from a game with different hardware, camera distance or hit frequency without adapting them.

## Examples from the episode
- **Steel Diver — projectile bubbles:** a few panels, each holding several bubbles.
- **Tekken 7 vs. Smash Bros.:** Smash reproduced lavish effects as best it could, but not for fast repeated hits.
- **Kirby's Dream Land — enemy-defeat stars and bomb explosions:** hand-placed per frame, with no particle code.
- **Kirby's Dream Land — inhale effect:** plays randomly from set movement patterns, and mixes white and black pixels to show on any background.

## Quote
> All you can do is work within your game's limits and try to aim for the best effect possible. (02:58)

## Tags
`particles` `effects` `hardware` `optimization` `readability` `kirby` `smash-bros`
