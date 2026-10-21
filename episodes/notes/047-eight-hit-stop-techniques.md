# 047 · Eight Hit Stop Techniques

**Category:** Design Specifics · [Video](https://www.youtube.com/watch?v=tycbMSjDDLg) · [Transcript](../transcripts/047-eight-hit-stop-techniques.md)

## In one sentence
Treat hit stop as more than a freeze: shake the victim (not the hitbox) more than the attacker, scale the stop by strength and a per-move multiplier, and blend poses during it, because these small touches stack into hits that feel strong.

## Key ideas
- Hit stop briefly stops both attacker and target when a hit lands. Final Fight's striking use of it left a lasting impression on Sakurai, and the game "would have been drastically different without it." In Smash Bros., hit stop is never just a stop: there is always some shake too.
- **Shake (techniques 1–2):** the character receiving damage shakes more and the attacker shakes less. Only the character model shakes; the hitbox stays in place, because shaking the hitbox makes attacks that should connect miss.
- **Direction and decay (techniques 3–4):** on the ground, fighters shake only side to side; in the air they shake in all directions. Vertical shake would suit facing opponents better, but on the ground it makes legs clip through the floor (less of a problem in 2D). The shake starts big and shrinks; because the hit stop duration is calculated up front, the shake can be made to resolve over exactly that time.
- **Amount (technique 5):** stronger attacks cause more hit stop, and a multiplier on top lets a hit feel stronger than its damage. Marth's sword tip hits much harder than its base. Ryu's hit stops look bigger and Kazuya's smaller on moves with the same damage, to match their original games.
- **Poses (techniques 6–7):** instead of freezing or snapping into one damage pose, the victim blends into it over about four frames. The attacker's animation keeps creeping forward so slowly that it doesn't move every frame (a sword tip still inching upward), then resumes as if nothing happened. That creep is toggled per attack, since it exists to make swords look like they cut and some attacks look better without it.
- **Other adjustments:** lightning attacks get longer hit stop, multiplayer battles get less, and characters shake more when the camera is pulled back so the impact looks the same near or far (the video numbers seven techniques and mentions the camera adjustment as an aside).
- Each technique is hard to notice on its own, but together they make the game much better.

## Do this
- On hit, freeze both characters and add a positional shake to the rendered model only: larger amplitude on the victim, smaller on the attacker, with hitboxes and hurtboxes left where they are.
- Shake grounded characters only horizontally and airborne characters in all directions; start with a large amplitude and decay it to zero over the hit stop duration you already calculated.
- Compute hit stop length from attack strength, then apply a per-move (or per-character) multiplier so sweet spots like a sword tip feel heavier than their raw damage.
- Blend the victim into the damage pose over about four frames during hit stop instead of snapping to it.
- For sword swings, keep the attacker's animation advancing at a tiny fraction of normal speed during hit stop, behind a per-attack toggle.
- Increase shake amplitude when the camera is zoomed out so hits read the same at any distance.

## Avoid
- Shaking the collision hitbox with the model, which makes attacks that should connect miss.
- Vertical shake on grounded 3D characters, which makes their legs clip through the floor.
- A fixed shake amount, or a pure freeze where the victim snaps to a single pose.

## Examples from the episode
- **Final Fight — hit stop:** an early, striking use of hit stop that defined how the game felt.
- **Super Smash Bros. Ultimate — Marth's Smash Attack:** the base of the sword gives little feedback; the high-damage tip, plus a multiplier, makes hits feel stronger than the damage.
- **Super Smash Bros. Ultimate — Ryu vs. Kazuya:** on moves with the same damage, Ryu's hit stops appear bigger and Kazuya's smaller, matching their source games.
- **Super Smash Bros. Ultimate — strong sword swing:** during hit stop the tip of the sword keeps inching upward.

## Quote
> Each one might be hard to catch on its own, but when they're all working together, they can really make a game that much better. (05:06)

## Tags
`hitstop` `impact` `feedback` `hitboxes` `animation-timing` `camera` `combat` `smash-bros`
