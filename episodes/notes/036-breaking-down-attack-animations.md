# 036 · Breaking Down Attack Animations

**Category:** Animation · [Video](https://www.youtube.com/watch?v=LewXWM7HDd8) · [Transcript](../transcripts/036-breaking-down-attack-animations.md)

## In one sentence
Structure every attack as standby, lead-in, attack and follow-through: snap instantly into a big lead-in pose, freeze the hit with hitstop, hold a distinct follow-through, and add cancel frames.

## Key ideas
- Attack animations in Sakurai's games have four parts: standby, lead-in, attack and follow-through.
- Standby is the pose every other pose starts from. Almost all animations are built from the ground or aerial standby poses, so nail them down first and don't change them.
- The lead-in (anticipation or windup) often starts with a big, unexpected movement on the very first frame; the game "jumps" to the pose. A smoother transition from standby would take too long. Jumping straight to a big pose tells the player their input was recognized and encourages the opponent to dodge the moment they see it.
- The attack is the key pose: when the attack can hit, plus a little movement before or after. Hitstop freezes the animation when the attack lands, making that moment a firm, readable pose; everything hinges on it.
- The follow-through is the opening after the attack. The player can't control the character, so the pose is kept very distinct from standby and held as long as possible. Cancel frames let the player move, jump or attack again before fully returning to standby, a bit of elbow room. Smash didn't use them until after Melee, which made earlier games feel a little heavy or rigid.
- For every new animation he specifies four things: the standby pose, the attack pose, the attack start frame, and the total frames (the time until the attack can be canceled). The lead-in fills the gap between standby and attack, and the follow-through between attack and total frames, so this is often enough for animators to start, though he adds specific directions too.

## Do this
- Finalize the ground and aerial standby poses first, and don't change them once other animations are built on them.
- Make the first frame of each attack jump straight to a big windup pose instead of easing out of standby, so the input feels acknowledged instantly.
- Apply hitstop on contact so the attack freezes on a clear, readable key pose.
- Make the follow-through pose clearly different from standby and hold it, so everyone can read the window when the attacker can't act.
- Add cancel frames late in the follow-through so the player can move, jump or attack before the animation returns to standby.
- In each attack request to animators, specify four values: standby pose, attack pose, the frame the attack starts, and total frames until it can be canceled.

## Avoid
- Smooth, slow transitions from standby into the windup that delay the response.
- Follow-through poses that look like standby.
- Returning control only after the character is fully back in standby, which feels heavy or rigid.

## Examples from the episode
- **Super Smash Bros. Melee and earlier — no cancel frames:** control came back only at the standby pose, which made things feel a little heavy or rigid.
- **Sakurai's animation specs:** standby pose, attack pose, attack start frame and total frames give animators their starting point.

## Quote
> By instantly jumping to a big pose, the player can immediately know their input was recognized. (00:56)

## Tags
`animation-timing` `anticipation` `hitstop` `cancels` `responsiveness` `specs` `combat` `readability`
