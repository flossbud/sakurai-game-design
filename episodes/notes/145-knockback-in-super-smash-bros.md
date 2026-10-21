# 145 · Knockback in Super Smash Bros.

**Category:** Programming & Tech · [Video](https://www.youtube.com/watch?v=HVktK4a9Yfo) · [Transcript](../transcripts/145-knockback-in-super-smash-bros.md)

## In one sentence
When knockback is your core mechanic, give each attack its own set of knockback parameters (direction, a multiplier, a guaranteed minimum with scaling, and an optional fixed value) so every hit can be tuned to land and feel right at any damage level.

## Key ideas
- In Smash, attacks don't simply deplete health according to their strength. Knockback "is at the heart of its game essence," so it needs unique considerations.
- **Core rule:** The more damage an attack deals, and the higher the target's accumulated damage percentage, the greater the knockback.
- **Direction:** Other fighting games have more limited knockback directions, but in Smash knockback can be set to any direction. A special modifier can make the knockback respond to the direction the attacker is traveling, which helps more hits of an aerial combo land.
- **The target matters:** Even with all other conditions equal, the knockback arc changes with the target fighter's fall velocity and weight.
- **Multiplier:** Adjusts the knockback an attack inflicts when it lands, so a strong attack can cause only slight knockback, or a weak one can launch far. This allows "some real fine-tuning."
- **Guaranteed minimum:** A minimum amount of knockback the attack always inflicts. A launcher shouldn't do nothing to a barely damaged opponent, and "there should at least be some reaction." Adding this value on its own would make knockback too big, so knockback scaling keeps it in check.
- **Fixed knockback:** An exact knockback regardless of other conditions, so the target always reacts the same way at any damage. On Mario's Super Jump Punch, the early successive hits use fixed knockback and only the final hit uses standard knockback, because it would be a problem if later hits missed when the opponent's damage was too low or too high.
- This parameter structure has existed since the original Smash Bros. Its rules are unorthodox compared with the average game, so it takes this kind of detail to make it fun. There are many more attack parameters beyond these.

## Do this
- If launching opponents is your core mechanic, calculate knockback from both the attack's damage and the target's accumulated damage, so hits grow more dangerous as damage builds.
- Give every attack a freely settable launch angle, plus an optional flag that bends the launch toward the attacker's direction of travel, so aerial combo hits keep connecting.
- Factor target weight and fall speed into the launch arc, so fighters respond differently to the same hit.
- Add a per-attack knockback multiplier, so a high-damage move can launch only slightly or a low-damage move can launch far.
- Give attacks a guaranteed minimum knockback so even barely damaged targets visibly react, and pair it with a scaling term so the minimum doesn't inflate already-large launches.
- On multi-hit moves, use fixed (damage-independent) knockback for every hit except the last and normal knockback for the finisher, so the whole sequence connects at any damage percentage.

## Avoid
- Damage-dependent knockback on the early hits of a multi-hit move. Later hits miss when the target's damage is too low or too high.
- Adding a minimum knockback without scaling, which makes knockback too big.

## Examples from the episode
- **Smash Bros. — knockback direction:** settable in any direction, with a modifier that follows the attacker's travel direction to help aerial combos.
- **Smash Bros. — launching attacks on low-damage opponents:** the minimum value guarantees a visible reaction.
- **Mario's Super Jump Punch:** fixed knockback on the initial successive hits, standard knockback on the final hit.

## Quote
> "Knockback" is at the heart of its game essence, so we have to make a few unique considerations. (00:03)

## Tags
`knockback` `combat` `numbers-tuning` `combos` `core-fun` `smash-bros`
