# 129 · Motion Sickness in 3D Games

**Category:** Planning & Game Design · [Video](https://www.youtube.com/watch?v=OS4CZkBBbW4) · [Transcript](../transcripts/129-motion-sickness-in-3d-games.md)

## In one sentence
3D motion sickness comes from on-screen motion that your inner ear doesn't feel, so offer options to tone down camera embellishments like footstep shake and inertial sway, and test with people who actually get sick.

## Key ideas
- Motion sickness can hit some players hard in 3D games. Sakurai rarely gets it and can play for hours, but he sympathizes with those who do.
- The cause is car sickness in reverse: the eyes (scenery) disagree with the inner ear (speed changes and shaking). A driver's body motion matches the curves and inclines they see, so they rarely get sick; a passenger looking inside the car or at a phone does, which is why carsick people are told to look into the distance.
- In a game there are no real speed changes, so the inner ear reports nothing, while the on-screen image can create an extreme sense of inertia. That mismatch makes people sick. Some people are worse in vehicles, others worse in games.
- Player-side tips: widen your field of vision so you stay aware that the TV is static and nothing else is moving (hard when absorbed); motion-sickness medicine may help with games too; stress and fatigue have a big impact, so avoid playing too long.
- Design-side: tone down presentation. The common FPS option to turn off vertical shake from footsteps can be very effective. If you show a vehicle's frame, lock it in place with no inertial movement.
- There's a trade-off: the more presentation you remove, the less entertaining the game looks, because a camera built to avoid motion sickness has little embellishment. Adding a cue that tells players the screen isn't really moving doesn't help much at the edge of the screen and is intrusive in the middle. Even so, there's no harm in offering options against motion sickness.
- If nobody on your team gets 3D motion sickness, you may struggle to test for it, since it varies so much from person to person.

## Do this
- Add an option to turn off vertical camera shake from footsteps (head bob).
- If the view includes a vehicle frame or cockpit, offer a mode that locks it to the screen with no inertial movement.
- List every inertia-heavy camera effect in your game and expose toggles for them instead of stripping them for everyone, since they add entertainment for players who aren't affected.
- Recruit playtesters who are prone to 3D motion sickness, and don't sign off on camera comfort based on a team that never feels sick.

## Avoid
- Assuming your camera is comfortable because nobody on the team gets sick.
- Relying on a "the screen isn't moving" reference element: at the edge it barely helps, and in the middle it's intrusive.

## Examples from the episode
- **FPS games — footstep shake toggle:** turning off vertical shake from footsteps can be very effective.
- **Vehicle frames on screen:** locking them in place, with no inertia, reduces sickness.
- **Car sickness — driver vs. passenger:** drivers rarely get sick because what they see matches what they feel.

## Quote
> Look at your game's presentation, and you'll find there's no harm in including options to counteract motion sickness. (02:40)

## Tags
`accessibility` `camera` `motion-sickness` `screen-shake` `options` `playtesting`
