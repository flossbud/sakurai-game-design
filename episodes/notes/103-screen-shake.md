# 103 · Screen Shake

**Category:** Effects · [Video](https://www.youtube.com/watch?v=2JXR7IASSog) · [Transcript](../transcripts/103-screen-shake.md)

## In one sentence
Use screen shake to sell big impacts—with a distinct pattern per impact size, scaled to camera distance and field of view, decaying with some randomness—but never so much that the screen becomes hard to read.

## Key ideas
- Screen shake is "just the ticket" for conveying a big impact, and Sakurai has used it often since Kirby's Adventure, considering it very important. Too much makes the screen hard to see, though.
- There are two main methods. **Move the camera in 3D:** distant objects may barely shake. **Move the whole rendered image:** everything clearly shakes, including the UI, and empty space may show at the screen edges.
- Camera shake is probably more common. Because far-away things barely move, think about the camera's center point (the point it's looking at). Sync its shake with the camera or shake it even more. If a distant center point moves too subtly, it won't look like much is happening.
- Smash Bros. has long used large, medium, small and extra-small shakes. These are different patterns, not scaled copies: small shakes only up and down, medium adds some horizontal shake, and large shakes even more. Sustained shakes use vertical motion to convey moving terrain and shouldn't move too much on either axis.
- Smash scales shake by camera distance, which also affects field of view, so it looks right everywhere. Flat Zone's tighter field of view made the usual shake feel really big, so it was retuned. Shakes start strong and gradually die down, not in a clean whirlpool but with a little randomness, which feels nicer.
- Early on, Sakurai would sometimes jostle his mouse to shake the camera and design screen movements around that.
- A game without screen shake can feel bland. Even a tiny shake changes how hard attacks feel. Getting the amount right in 3D is tough but worth the effort.

## Do this
- Create 3–4 shake presets (e.g., large, medium, small, extra-small) as distinct patterns: small = vertical only, medium = adds horizontal, large = more amplitude on both axes. Map them to impact strength.
- When shaking a 3D camera, shake its look-at point too, as much as the camera or more, so distant scenery visibly moves.
- Scale shake amplitude by camera distance and field of view, and retune scenes with an unusually narrow FOV where the default shake looks oversized.
- Make shakes start strong and decay over time, adding a little randomness to the path instead of a clean circular or spiral motion.
- For long rumbles (like quaking terrain), use mostly vertical motion with small amplitude on both axes.
- If you shake the rendered image instead, plan for the HUD shaking along with it and for blank edges showing at the screen border.

## Avoid
- Shaking so hard the screen becomes difficult to see.
- Moving a distant camera target so subtly that the shake barely shows.
- Shipping impacts with no shake at all, which can make the game feel bland.

## Examples from the episode
- **Super Smash Bros. — shake presets:** large/medium/small/extra-small, each a different pattern (small = vertical only; medium adds horizontal).
- **Super Smash Bros. — Flat Zone:** the tighter field of view made normal shake feel too big, so it was retuned for that stage.
- **Kirby's Adventure:** Sakurai has used screen shake often ever since this game.

## Quote
> Even a tiny amount of shake can give attacks a drastically different impact. (03:07)

## Tags
`screen-shake` `impact` `camera` `feedback` `effects` `readability` `smash-bros`
