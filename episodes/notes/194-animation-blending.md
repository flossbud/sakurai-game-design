# 194 · Animation Blending

**Category:** Animation · [Video](https://www.youtube.com/watch?v=HYHajZ0wBfU) · [Transcript](../transcripts/194-animation-blending.md)

## In one sentence
Blend between animations so transitions such as cancels look natural from any starting pose, but keep blends short and snappy, because long automatic blends kill rhythm and impact and can distort the motion.

## Key ideas
- Animation blending combines two or more animations.
- Cancel frames are one use. After an attack you're briefly vulnerable, then you enter cancel frames where you can input another action. That input doesn't snap the character into the next animation; it blends the canceled action into the new one.
- Idle-to-walk and attack-to-walk both look natural. The walk that follows is the same, but the starting poses are very different, and blending is what makes both work.
- You can set both the strength and the duration of a blend. But as with interpolation, making animation too smooth reduces its rhythm and impact, and because blending is automatic, the result can come out distorted. So don't let blends last too long: keep them quick and snappy.
- Shifting your shield is another kind of blending: movement around a circle combined with the fixed stance at the center.
- Blending doesn't play a big role in a fast game like Smash Bros. It shines in fully 3D games, where upper and lower bodies move separately, legs settle naturally on terrain, slopes affect turning animations and characters change states often. It gets so complex you can't tell where blending starts and ends.
- Animation is about more than making things look lively, and existing technology can't fill every gap. Research continues, and in a way game animation isn't so different from robotics.

## Do this
- When an action is canceled into another (for example attack into walk), blend from the current pose into the new animation instead of snapping.
- Keep blend durations short so transitions stay quick and snappy and attacks keep their rhythm and impact.
- Review automatic blends frame by frame for distortion, and fix or shorten any that break the pose.
- For directional moves like tilting a shield, blend a fixed center stance with poses placed around a circle according to stick direction.
- In fully 3D games, consider layered blending: upper and lower body animated separately, feet placed on the terrain, and turning animations that react to slopes.

## Avoid
- Long, overly smooth blends that sap rhythm and impact.
- Trusting automatic blending without checking it for distorted poses.

## Examples from the episode
- **Smash Bros. — cancel frames:** canceling an attack into walking blends the two animations.
- **Idle-to-walk vs. attack-to-walk:** the same walk animation starting from very different poses, both looking natural.
- **Smash Bros. — shield shifting:** circular movement blended with the fixed center stance.
- **Fully 3D games:** separate upper and lower body motion, terrain-aware legs and slope-affected turns.

## Quote
> As a result, you don't want a blend to last too long. Make it quick and snappy. (01:49)

## Tags
`animation` `animation-blending` `cancels` `animation-timing` `impact` `responsiveness` `smash-bros`
