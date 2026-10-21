# 044 · Distinguishing Between Major and Minor Elements

**Category:** Graphics · [Video](https://www.youtube.com/watch?v=NBXt-Uq7dHg) · [Transcript](../transcripts/044-distinguishing-between-major-and-minor-elements.md)

## In one sentence
Spend limited performance and labor on what players actually look at (screen center, playable surfaces, assets shown up close) and cut detail nobody will ever see.

## Key ideas
- Console hardware isn't as powerful as most people think, so if you don't economize on performance you may not reach your goals. Decide which elements are major and which are minor, meaning which have more or less impact.
- Smash stages often use a skysphere-like backdrop, but players mostly look at the center of the screen, so focus the skysphere's detail on the area in front of the camera. On foreground terrain, the stage surface matters more than the foundations, which are often off-screen.
- Fighters might seem more important than stages, but they're often shown fairly small, so don't get carried away; consider how much of the screen each element takes up. However, fighter models are also shown up close in all kinds of assets, not just gameplay, so prioritize them accordingly.
- LOD (swapping in lower-polygon assets as objects get farther from the camera) is labor-intensive, so the performance benefit has to be worth it.
- The stage team worked in some very particular details. Sakurai didn't request them, but as long as artists met deadlines and performance didn't suffer, he didn't object, because a bit of playfulness makes the game better. When they made the car tires in the backdrop of Inkling's stage actually turn, something truly nobody would see, he asked them to tone it down.
- Distinguishing major from minor elements and allocating resources is an essential skill, and not only for graphics.

## Do this
- Rank each asset by how much it's actually seen: screen center and the area in front of the camera first, peripheral and off-screen parts last; spend polygons and texture detail in that order.
- On terrain, put detail into the playable surface and simplify foundations that are usually off-screen.
- Set each model's budget by how much screen space it occupies in play, but raise it if the model is also shown up close in other assets.
- Before building LOD versions, estimate whether the performance gain is worth the extra labor.
- Allow small playful details only when they meet deadlines and don't cost performance, and cut details no player will ever see.

## Avoid
- Spending effort on details truly nobody will see, such as turning car tires deep in a backdrop.
- Over-investing in elements that appear small on screen.
- Building LOD where the benefit isn't worth the labor.

## Examples from the episode
- **Super Smash Bros. — skyspheres and terrain:** detail goes in front of the camera and on the stage surface, not on off-screen foundations.
- **Super Smash Bros. — fighters vs. stages:** fighters are small during play, but their models are shown up close in other assets.
- **Super Smash Bros. — Inkling's stage:** backdrop car tires that actually turned were toned down because nobody would see them.

## Quote
> Distinguish between major and minor elements, and allocate your resources effectively. (02:24)

## Tags
`hardware` `optimization` `prioritization` `level-design` `scope` `lod` `smash-bros`
