# 121 · Squashing and Scaling

**Category:** Animation · [Video](https://www.youtube.com/watch?v=Sm0LAm4sJKc) · [Transcript](../transcripts/121-squashing-and-scaling.md)

## In one sentence
Don't overlook scaling in animation: squash and stretch while keeping the object's volume about the same gives things texture, life and a physical presence.

## Key ideas
- Computer animation has three basic transformations: scaling (resizing), rotation (turning) and translation (moving). Rotation and translation are used everywhere, but scaling often isn't, and you shouldn't underestimate it. Depending on what you animate, it can really punch things up.
- A bouncing ball looks fine without scaling, but with scaling it feels totally different, "almost as if you can reach out and touch it."
- Squash and stretch gives objects texture and life. The key rule is to keep the object's mass roughly the same: if you squash vertically, stretch horizontally to match.
- Kirby has squashed when crouching and landing since the Game Boy era. When Kirby became a 3D model, squashing alone made him lose physical presence, so in a Daily Report Sakurai asked the team to follow the pixel art and add volume on the sides, like an oval track: "If you just squash vertically, your oval will end up dull."
- The team discussed using blend shapes to interpolate between two models; he doesn't remember the final method, but they did more than scale Kirby down vertically. Scaling shows up even in the smallest animation details.
- Mario's fist growing when he punches is exaggeration, which is a different technique from squash and stretch.

## Do this
- Add squash to landings and crouches, then compare the animation side by side with and without scaling.
- When you squash on one axis, scale the other axes up so the overall volume stays about constant.
- For 3D characters, don't just scale the Y axis. Shape the squashed pose so the sides bulge out (an oval-track profile), with a sculpted pose or blend shape if needed.
- Check small actions (landings, crouches, impacts) for spots where a touch of scaling would add punch.

## Avoid
- Squashing only vertically without widening, which loses volume and physical presence ("your oval will end up dull").
- Treating rotation and translation as the whole toolkit and ignoring scale.

## Examples from the episode
- **Bouncing ball GIF:** the same bounce with and without scaling; with it, the ball feels touchable.
- **Kirby — crouch and landing squash:** used since the Game Boy; the 3D model needed extra side volume, per Sakurai's Daily Report image.
- **Mario — punching fist:** the fist grows, which is exaggeration rather than squash and stretch.

## Quote
> A key rule to follow with this technique is to always keep the object's mass roughly the same. (01:09)

## Tags
`squash-and-stretch` `animation` `impact` `character-design` `kirby` `3d-models`
