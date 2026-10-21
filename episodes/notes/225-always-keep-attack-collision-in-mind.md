# 225 · Always Keep Attack Collision in Mind

**Category:** Animation · [Video](https://www.youtube.com/watch?v=rwwF_4blK-o) · [Transcript](../transcripts/225-always-keep-attack-collision-in-mind.md)

## In one sentence
Animators must always know when and where an attack's collision is active, so the animation lines up with the hitbox and the strongest pose lands on the hit frame.

## Key ideas
- Smash Bros. is seen from the side, so fighters' silhouettes must look good from the side. This creates problems in development.
- Attack collision isn't mapped tightly to the sword or fist; it covers a wider area. Movement in Smash is fast and coordinate-based, so tight hitboxes would make attacks miss and stress players.
- Attacks whose range doesn't cross the median line (the line where fighters stand) are hard to land, and Sakurai has them fixed.
- A game designer can make any animation connect by placing the collision, but a big gap between the animation and its collision feels wrong. Some mismatch is fine if it makes the game more fun. If the animation itself is in the wrong position, it feels even more broken.
- Timing matters too: when collision starts, and the pose the fighter is in at a likely clean hit. That is when hitstop happens and players see the pose clearly; on a finishing blow the screen stops completely. A weak pose there is no good, so on sword swings collision starts only partway through the swing.
- Some animators think gameplay is the designers' job, but animation has a huge effect on how a game feels, so everyone must keep gameplay in mind.

## Do this
- In fast games, make attack hitboxes wider than the visible weapon or fist so attacks don't whiff and frustrate players.
- Check that every attack's motion and hitbox cross the line or plane where opponents stand; fix any that don't.
- Put the first active collision frame where the pose looks strongest (e.g., partway into a sword swing), because that's the frame hitstop freezes.
- Give animators a hitbox overlay (active frames plus placement) and review attacks with collision visible.
- Allow some mismatch between visuals and collision for fun, but keep the animation positioned where the hitbox actually is.

## Avoid
- Hitboxes mapped exactly to the weapon in a fast game, which makes attacks miss.
- Fixing a misplaced animation by stretching the hitbox to meet it.
- A weak pose on the frame where hitstop freezes the screen.
- Animators treating gameplay as only the designers' responsibility.

## Examples from the episode
- **Smash Bros. — attack collision:** wider than the sword or fist because of fast coordinate-based movement.
- **Smash Bros. — sword swings:** collision starts partway through the swing so the hitstop frame shows a strong pose; finishing blows stop the screen completely.

## Quote
> When crafting attack animations, it's important that the animators are always aware of when and where collision occurs. (01:52)

## Tags
`hitboxes` `animation-timing` `hitstop` `combat` `silhouette` `impact` `communication` `smash-bros`
