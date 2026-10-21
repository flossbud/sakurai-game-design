# 030 · Emphasize Objects with Collision

**Category:** Graphics · [Video](https://www.youtube.com/watch?v=FfPN4ZGgBpo) · [Transcript](../transcripts/030-emphasize-objects-with-collision.md)

## In one sentence
Make terrain with collision stand out and tone down non-colliding backdrop so players always know where solid ground is, while keeping the stage attractive and giving gameplay the slight edge.

## Key ideas
- This comes up for every new Smash Bros. stage and is still easy to get wrong.
- In an action game players must always know where solid ground is. With 3D polygons in a perspective view, collision is harder to recognize, so terrain has to be set apart from non-terrain.
- Smash backdrops are elaborate; when artists put too much work into areas without collision and make them stand out, the crucial terrain gets lost. His usual feedback: "your backdrop's outshining your terrain."
- One simple fix is applying aerial perspective to everything that isn't terrain to reduce its presence. Doing only that makes terrain clearer but hurts the overall look.
- Visual appeal matters too: people may say visuals are irrelevant to gameplay, but that won't matter if nobody buys the game. Strike a balance, giving gameplay the slight edge.
- Artists shouldn't just produce artwork; they should understand their art's role in the game and make what's appropriate.

## Do this
- Make a debug view that highlights every surface with collision (Sakurai's example marks them in red) and check during play that each one is instantly distinguishable from the backdrop.
- Give non-colliding background elements less emphasis than terrain; one simple tool is aerial perspective, which pushes them back visually.
- Don't stop at aerial perspective; also check that the stage as a whole still looks appealing.
- In stage art reviews, flag any backdrop that outshines the terrain and shift emphasis back to the colliding geometry.
- Tell artists which elements are walkable terrain and which are decoration before they start, so they know each piece's role.

## Avoid
- A backdrop that outshines the terrain.
- Relying on aerial perspective alone, which hurts the overall look.
- Producing art without considering its role in the game.

## Examples from the episode
- **Super Smash Bros. — stage design:** collision surfaces highlighted in red; elaborate backdrops risk hiding the terrain, which prompts his feedback "your backdrop's outshining your terrain."

## Quote
> Make the objects with collision stand out— and give the backdrop less emphasis. (01:18)

## Tags
`readability` `clarity` `level-design` `collision` `backgrounds` `art-direction` `smash-bros`
