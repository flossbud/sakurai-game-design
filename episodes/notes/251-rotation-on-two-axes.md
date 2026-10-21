# 251 · Rotation on Two Axes

**Category:** Animation · [Video](https://www.youtube.com/watch?v=Mh7nTn9_r40) · [Transcript](../transcripts/251-rotation-on-two-axes.md)

## In one sentence
When you animate anything that isn't a machine, never rotate on a single axis: pair the main turn with a second axis, move the connected joints, and hand-tune the timing so the motion looks believable and has personality.

## Key ideas
- A head turned purely around the vertical (Y) axis looks mechanical. That kind of single-axis rotation is generally not a good approach.
- Even when the turn you want is a Y-axis turn, rotate on two axes for human movement. Look down and then turn (X + Y), or tilt the head to the side as it turns (Z + Y).
- For anything non-mechanical, use this twisting two-axis rotation. A wrist turned on one axis looks underwhelming, "almost like a drill," while tilting it a little before turning looks more believable.
- Connected parts move too. The shoulder and collarbone work in tandem with the wrist, so in a twisting motion like revving a motorcycle, the shoulder and collarbone positions should shift along with the wrist.
- For rotation speed, the function curves your 3D software generates might look believable, but it's better to take control yourself, for example by slightly offsetting the rotation of the two axes or adding an occasional counter-motion.
- Rotations that end in the same pose can show very different personalities depending on the path. Turning the head to the side while dipping down, rising up or staying level all look different.
- Keep eye movement in mind when animating the head. Animators often turn the whole head fully before facial animation exists, but once the eye line is added, that big a head turn may be more movement than you want.

## Do this
- For every turn (head, wrist, torso), add a second rotation axis: a dip (X) or a tilt (Z) layered on the Y turn.
- When a hand or wrist twists, keyframe the shoulder and collarbone so they move with it.
- Don't accept the software's default curves. Offset the timing of the two axes slightly, and try a small counter-motion.
- Choose the path of a turn (downward, upward or level) on purpose to express the character's personality, not just the end pose.
- Plan head turns together with the eye line, and reduce the head rotation once the eyes carry part of the look.

## Avoid
- Single-axis rotation on organic characters, such as a robotic head turn or a drill-like wrist twist.
- Leaving rotation timing to the curves your 3D software generates.
- Turning the head fully before the eyes are animated, then ending up with an oversized movement.

## Examples from the episode
- **Sakurai's own head turn:** he turns his head on one axis to show how mechanical it feels, then compares head turns that go downward, upward or directly sideways.
- **Revving a motorcycle:** a twisting wrist motion where the shoulder and collarbone must move with the wrist.

## Quote
> When creating human movement, make it a point to rotate on two axes. (00:38)

## Tags
`animation-timing` `rotation` `organic-motion` `posing` `function-curves` `eye-line`
