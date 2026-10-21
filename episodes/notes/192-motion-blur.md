# 192 · Motion Blur

**Category:** Graphics · [Video](https://www.youtube.com/watch?v=xAgkRtpAUFI) · [Transcript](../transcripts/192-motion-blur.md)

## In one sentence
Use blur to show motion and fill the gaps between frames, through drawn blur textures or hardware effects, but keep it subtle and natural (or let players adjust it), because too much blur makes the action hard to read.

## Key ideas
- Sakurai regrets not adding a spinning blur to the star in the middle of the wheel for Kirby Air Ride's Wheel ability. That's done simply by swapping the texture while the object is moving.
- On Super Smash Bros. Ultimate's Spirit Train stage, the train wheels and rails have blur built in from the start, which looks natural as the train moves forward.
- Blur shows the afterimage of a moving object. Between consecutive animation frames, blur fills the gap, making animation more dynamic and less stop-and-start.
- Blade trails are technically a kind of blur, but not exactly the same thing. Blur isn't only for characters; it can also be applied to the background when the player moves the camera.
- There are two ways to show blur: draw it in by hand, like the textures above, or apply it through hardware-based calculations.
- Either way, don't overdo it. Artificial blur can currently make things look worse, and if the visuals are too fuzzy, it's hard to tell what's going on. Teams also struggle to agree on what looks good, so a number of games let players adjust blur strength in the options.
- In the Matrix tech demo, the visuals are at times hard to tell from live-action footage, and blur is an essential part of that effect. The more natural the blur, the more believable it is and the less discomfort players feel.

## Do this
- For spinning or fast-moving parts like wheels, swap in a pre-drawn blurred texture while they're in motion.
- For parts that are always moving, like train wheels and the rails under a moving train, build the blur into the texture from the start.
- Use blur to bridge the gap between fast animation frames and to soften background motion during quick camera moves.
- Check gameplay with blur on and dial it back wherever the image gets fuzzy enough to hide what's happening.
- Add a blur-strength setting to the options menu so players can tune it.

## Avoid
- Overdoing artificial blur until the visuals become fuzzy and hard to read.
- Shipping motion that should feel fast with no blur at all, as with the Wheel's star he regrets.

## Examples from the episode
- **Kirby Air Ride — Wheel ability:** Sakurai wishes the star in the middle of the wheel had a spinning blur.
- **Super Smash Bros. Ultimate — Spirit Train stage:** wheels and rails have blur applied from the start.
- **The Matrix tech demo:** natural blur helps the visuals pass for live-action footage.

## Quote
> The more natural a blur effect, the more believable it'll be, and the less discomfort players will feel. (02:11)

## Tags
`motion-blur` `effects` `readability` `animation-timing` `camera` `accessibility` `kirby` `smash-bros`
