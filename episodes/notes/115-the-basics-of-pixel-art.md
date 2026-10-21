# 115 · The Basics of Pixel Art

**Category:** Graphics · [Video](https://www.youtube.com/watch?v=NDno0U5UxSI) · [Transcript](../transcripts/115-the-basics-of-pixel-art.md)

## In one sentence
On a tiny canvas with few colors, draw symmetric shapes at odd-numbered sizes so they have a true center, and give each extra color a specific job (highlight, edge softening, reflection).

## Key ideas
- Sakurai drew Kirby's pixel art for the original Game Boy Kirby himself, plus a good few enemies and backgrounds, some reused in the next Kirby game on the NES. These techniques come from hardware with very few colors.
- NES and Game Boy art was often built from 16x16-pixel sprites, which let art move smoothly on screen. Kirby himself is 16x16.
- At this size a 15x15 circle looks more like a true circle than a 16x16 one, even though it is smaller, because an odd size has clear median (center) lines. The same applies when building with broad units in a crafting game: odd-numbered sides are easier.
- With only black and white you can still show a lot. An outline plus a highlight reads as a bubble; a mesh (dither) pattern makes the shape look flat rather than round, and flipping the mesh changes the feel; solid black plus a highlight reads as a cannonball.
- One more color lets you soften the edges, which he calls essential for precise details. On a reflective material, a third color can show the floor's reflection. How well the smoothed edges work depends on the background color.
- Aside: in Kirby's Adventure, Kirby looks a little plumper and his color changes a bit when he has a copy ability.

## Do this
- Draw round or symmetric sprites at odd dimensions (e.g., a 15x15 circle inside a 16x16 sprite) so there is a single center row and column.
- In voxel or crafting builds with chunky units, give symmetric structures odd-numbered widths.
- Before adding colors, see how far a silhouette or outline plus one highlight can carry the material (bubble vs. cannonball). Spend a third color on anti-aliased edges or a reflection, not on decoration.
- Pick edge-softening colors against the actual background the sprite will sit on, and check them in place.

## Avoid
- Drawing small circles at even sizes; with no center line they look less round.
- Shading an object with a mesh pattern when you want it to read as round; the mesh flattens it.

## Examples from the episode
- **Kirby (Game Boy) — Kirby's sprite:** a 16x16 sprite Sakurai drew himself; some art was reused for the NES sequel.
- **Kirby's Adventure — copy abilities:** Kirby is drawn slightly plumper and his color shifts a little when he holds a copy ability.

## Quote
> If you compare them, you'll see the 15x15 one is more of a true circle. That's because it has clear median lines. (01:03)

## Tags
`pixel-art` `readability` `color` `character-design` `kirby` `history`
