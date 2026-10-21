# 254 · HUDs

**Category:** UI · [Video](https://www.youtube.com/watch?v=a_HB81ujHHE) · [Transcript](../transcripts/254-huds.md)

## In one sentence
Design your HUD to be both easy and fun to use, keeping useful information on screen while finding tricks so it doesn't crowd the play area.

## Key ideas
- A HUD ("heads-up display") is the information overlaid on the play area. Real HUDs in fighter planes, and lately in cars, use a half-mirror so you don't have to look away and the display appears at a distance, which makes it a safer way to get information.
- In a game, the HUD is everything placed at the forefront of the screen. Elements that track characters arguably feel more "HUD-like" than static elements around the edges.
- Sakurai's impression: Japanese games often show a lot of information, while games from abroad tend to be more restrained, possibly to emphasize immersion and avoid clutter. Many games let you hide the HUD, though as a player he values function and keeps everything displayed.
- A HUD is useful, but it can crowd the screen. Every game tries to solve that in its own way.
- Smash Bros. (from Brawl onward): fighters' faces are in the HUD because the fighters are sometimes quite small on screen, which boosts character appeal, as does the way the faces look toward the audience. The backgrounds behind them have patterns that move upward with UV scrolling, so it looks like they're fighting with burning spirit, unlike a flat, static image. If a fighter overlaps the HUD, the HUD turns semi-transparent. Player cursors above fighters' heads would be an eyesore if always visible, so they hide automatically based on distance and situation.
- Kirby Air Ride: a different meter appears depending on your copy ability, and if your machine is destroyed, the meter breaks. Opponents you've attacked or defeated appear as on-screen icons, because in 3D it's hard to tell how many opponents you've damaged.
- Meteos (outside the game screen proper): the alien's head spins, and spins faster when you activate the Speeder, which makes the feature fun to use and to look at.

## Do this
- Go through every HUD element and decide whether it can hide itself depending on distance or situation, the way Smash's player cursors do.
- Make HUD panels turn semi-transparent when a character moves behind them.
- If characters appear small on screen, add their portraits to the HUD, posed facing the player, to carry character appeal.
- Animate HUD backgrounds subtly (for example, a pattern scrolling upward with UV scrolling) instead of using a flat, static image.
- Make meters react to game state: change the meter to suit the current ability or mode, visibly break it when the vehicle or character is destroyed, and show icons for information that's hard to track in 3D, such as which opponents you've hit.

## Avoid
- Markers that are always visible and become an eyesore.
- HUD elements that cover the characters they overlap.

## Examples from the episode
- **Super Smash Bros. Brawl onward — HUD faces:** portraits with UV-scrolling backgrounds, semi-transparency on overlap, and auto-hiding player cursors.
- **Kirby Air Ride — meters and icons:** ability-specific meters that break with your machine, and icons for opponents you've attacked or defeated.
- **Meteos — spinning alien head:** spins faster when the Speeder is active.

## Quote
> Remember that your game should be both easy and fun to play, so design your HUD with those goals in mind. (02:59)

## Tags
`hud` `clarity` `readability` `feedback` `character-design` `smash-bros` `kirby` `meteos`
