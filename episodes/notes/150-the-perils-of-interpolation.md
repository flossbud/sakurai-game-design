# 150 · The Perils of Interpolation

**Category:** Animation · [Video](https://www.youtube.com/watch?v=oFwamE6Hy04) · [Transcript](../transcripts/150-the-perils-of-interpolation.md)

## In one sentence
Don't let your animation tool's interpolation water down the key poses. Reach the key frames fast, spend the time on the anticipation and the strike, and push the poses further than the source, so 3D moves stay as snappy as their 2D originals.

## Key ideas
- Take a 2D game into 3D with the same poses, and animations that were snappy in 2D "tend to not work so well."
- Animation tools interpolate the motion between the poses you set. That causes small problems like a model clipping into itself, which are easy to clean up. But "convenience doesn't mean quality": even with the same poses and timings as the 2D original, the interpolated frames overpower them and make the animation feel slow.
- **The kick example:** A lead-in pose and attack pose from an original game, recreated on a 3D model (with the middle kick placed a little lower), comes out in only 8 frames but still feels too slow. In the release version of Smash Ultimate it is still an 8-frame kick, but it looks much snappier.
- **Key frames:** The crucial poses are "key frames," and you generally want to reach them quickly. Spend little time on the in-between frames and save it for the lead-in and the attack. If possible, give the poses even more energy than the original key frames.
- **Ryu's crouching heavy punch (an uppercut):** The original pixel art has just three poses, played forward and then back. Translated as-is to 3D, simple interpolation between them kills the momentum. In Smash Ultimate, his right forearm, which starts in front of his body in the original, is pulled back a little. The anticipation is held for a relatively long time. The three original key poses are all there but on screen for only one frame each, and if the attack hits, they still leave an impression. The first frame differs most because Ryu starts from a crouch in his own game and Smash wanted more momentum.
- **Follow-through:** Instead of the original's backwards playback, the follow-through takes a different trajectory. That was necessary, but it was kept as close to the original as possible. "You don't want your follow-through to be the same as your standby pose."
- Not every game needs to rush its animations, but always ask whether your animations match your game and are exaggerated enough. Use interpolation well, but don't let it rob the animation of impact.

## Do this
- When converting 2D animation (or any reference pose set) to 3D, don't accept default interpolation between the original poses. Scrub the result and cut in-between time so the key poses arrive quickly.
- Spend the frame budget on the anticipation (lead-in) and the strike, not the transitions: hold the anticipation pose relatively long, then snap through the key poses, even at one frame each.
- Push each key pose further than the reference, e.g., pull the attacking arm back more in the wind-up for more momentum.
- Give the follow-through its own trajectory instead of reversing the attack, and make sure it doesn't simply return to the standby pose.
- Judge speed by eye in-game, not by frame count alone. An 8-frame attack can still feel slow if its in-betweens are mushy.

## Avoid
- Trusting the tool's convenience, so that interpolated frames overpower the key poses and the animation feels slow.
- Playing a 2D pose sequence forward and then backward in 3D as the follow-through.
- A follow-through that's identical to the standby pose.

## Examples from the episode
- **Smash Bros. Ultimate — a kick:** recreated with straight interpolation, the 8-frame kick felt too slow. The release version is still 8 frames but much snappier.
- **Ryu — crouching heavy punch:** three pixel-art poses played forward and back in his original game. In Smash Ultimate: forearm pulled back, long-held anticipation, key poses on screen one frame each, and a follow-through on a different trajectory.

## Quote
> You should use it well when you can, but take care not to make your animations lose their impact in the process. (03:59)

## Tags
`animation-timing` `anticipation` `interpolation` `key-frames` `impact` `responsiveness` `combat` `smash-bros`
