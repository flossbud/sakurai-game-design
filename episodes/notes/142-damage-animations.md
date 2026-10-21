# 142 · Damage Animations

**Category:** Animation · [Video](https://www.youtube.com/watch?v=0xHE3ypX96U) · [Transcript](../transcripts/142-damage-animations.md)

## In one sentence
Make the first frame of every damage reaction an extreme, asymmetric pain pose that looks nothing like standby. Hitstop holds that frame on screen, so a hit should read instantly, even from far away.

## Key ideas
- In Smash, a character snaps into a pained pose the moment they take damage. Hitstop is applied to that first frame of the damage animation, so it's easy to see, which is why it's vital that the pose "really expresses the pain."
- In some games the damage pose is close to the standby pose. Smash deliberately goes "more extreme" and makes it nothing like standby, so "you can clearly tell the character got hit, even from far away."
- The switch isn't instant: the game interpolates from the pose at impact to the first damage frame as "just a quick segue." (He refers to his hitstop video for more.)
- Characters always enter a damage pose when hit, so if an attacker's hitbox is lengthened, the target can react from quite a distance. Sakurai notes there are merits to applying hitstop on the extended-hitbox frame, but Smash opts to emphasize the sense of impact.
- **A pitfall:** When a neutral attack hits, the target's change of stance could, depending on the stance, move them backwards and make the rest of the combo miss. The cause was the attacked fighter's top node position, a problem that "can arise whenever you change a character's stance."
- **Reaction set:** Damage reactions are high, middle or low, chosen by which is closest to the point of impact. On the ground they also come in three strengths (small, medium, large), giving nine reaction types. Knockback has its own separate set of variations. Smash's oddly shaped fighters and its sword, shield and other weapon wielders mean animations can't be reused across characters as they could with standard human proportions, so each new fighter is a lot of work.
- **Silhouette:** All damage animations break the character's symmetry and keep the silhouette legible. In knockback, the body is twisted so the arms and legs read clearly, which wouldn't happen if the character just flew sideways. The goal is for both players to feel the impact. Sakurai's (recreated) drawing of Kirby's damage pose from the Kirby Super Star design document shows how well moments of extremity work: "The more punch, the better."

## Do this
- Author the first frame of every damage animation as an extreme pain pose that's clearly different from idle/standby, and make sure that is the frame held during hitstop.
- Blend over a few frames from the pose at the moment of impact into that first damage frame instead of snapping to it.
- Build a reaction matrix: choose high, middle or low by which body region is closest to the impact point, and small, medium or large by hit strength (9 grounded variants), with a separate set for knockback.
- Whenever a damage pose changes a character's stance, check that the root/top node doesn't shift the character backward. Run multi-hit strings (e.g., a neutral-attack combo) against each stance and confirm that every hit still connects.
- In damage and knockback poses, twist the torso and break symmetry so the arms and legs read as clear silhouettes. Avoid a stiff body flying sideways.

## Avoid
- Damage poses that look like the standby pose. The hit becomes hard to read from a distance.
- Stance changes on hit that move the target's top node backward and make follow-up hits miss.
- Symmetric, side-on knockback poses that hide limb silhouettes.

## Examples from the episode
- **Smash Bros. — first damage frame:** an extreme pose held by hitstop, interpolated from the pose at impact.
- **Smash Bros. — neutral attack combo:** follow-up hits missed because the target's stance change moved them back (a top node position issue).
- **Smash Bros. — reaction set:** high/middle/low × small/medium/large = nine ground reactions, plus separate knockback variations.
- **Smash Bros. — knockback:** twisted bodies so arm and leg silhouettes read clearly.
- **Kirby Super Star:** Kirby's extreme damage pose as drawn in the design document (shown as a recreation).

## Quote
> The damage pose and standby pose can be quite similar in some games, but we like to go for something more extreme that's nothing like the standby pose. (00:33)

## Tags
`animation-timing` `hitstop` `silhouette` `readability` `impact` `feedback` `hitboxes` `combat` `smash-bros` `kirby`
