# 084 · Units of Speed

**Category:** Design Specifics · [Video](https://www.youtube.com/watch?v=_B0cpF8fQ4s) · [Transcript](../transcripts/084-units-of-speed.md)

## In one sentence
State every speed in an explicit unit the whole team shares (pixels per frame for sprites, real-world or distance-per-frame units for 3D), and train your sense of speed so your parameters land close the first time.

## Key ideas
- Speed affects many parts of a game. Speed = distance ÷ time, so if you know any two you can work out the third.
- For sprite games like those on the NES, his specs used p/f, "pixels per frame," the number of pixels an object moves each frame. He guesses Mario's top speed in Mario Bros. is about 1 p/f, and the NES screen is 256 pixels wide (he shows how long one lap of the screen takes).
- The Game Boy, NES and Super NES each had different pixel counts. Because the canvas sizes differed, the same speed value gave very different results on each.
- With 3D came standard units like km/h. If characters and environments are built in real-world units, real speeds can be used as-is, which is much easier to understand. Some games still have reasons to use distance per frame, such as meters or centimeters per frame.
- Kirby Air Ride expressed speed in km/h (mph in North America). The numbers look low because Kirby is only about a 20 cm square, so for him those speeds are actually fast.
- In Kid Icarus: Uprising, Pit moves extremely fast even when walking, and faster when running. A normal walk cycle couldn't keep up, so they gave him a bounding motion and let him slide along the ground.
- Specs and parameters don't work if you can't convey speed, so get the whole team on the same page by stating units of measurement. A good sense of speed saves a lot of time when you estimate parameters.

## Do this
- Pick one speed unit for the project (px/frame for 2D sprites, km/h or m/frame for real-scale 3D), document it, and include it in every spec and parameter name.
- Build characters and environments at real-world scale if you want to use real speeds directly.
- Judge speeds relative to the character's size: a small character covers its own body length fast even at a low km/h value.
- When a character moves faster than a natural walk or run cycle can support, switch to stylized locomotion (bounding, sliding) instead of speeding up a normal leg cycle.
- Practice estimating a movement's speed by eye before checking the real number, to calibrate your sense of speed.

## Avoid
- Reusing raw speed values across platforms or resolutions with different pixel counts.
- Specs and parameters that give speeds without units.

## Examples from the episode
- **Mario Bros.:** Mario's top speed is roughly 1 pixel per frame on a 256-pixel-wide NES screen.
- **Kirby Air Ride:** speeds in km/h (mph in NA) that look low because Kirby is only about 20 cm across.
- **Kid Icarus: Uprising:** Pit's very fast walk and run use a bounding, sliding motion because normal legs couldn't keep up.

## Quote
> So, it's essential you get your whole team on the same page when it comes to distances by specifying your units of measurement. (02:17)

## Tags
`numbers-tuning` `specs` `communication` `frame-rate` `animation-timing` `kirby` `kid-icarus`
