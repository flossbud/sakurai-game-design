# 150 · The Perils of Interpolation

- **Category:** Animation
- **Video:** https://www.youtube.com/watch?v=oFwamE6Hy04
- **Length:** 04:20
- **Source:** official English subtitles burned into the video, read by OCR (tools/ocr_subs.py). Expect rare OCR typos.

---

[00:04](https://youtu.be/oFwamE6Hy04?t=4) Imagine translating what was once a 2D game into a 3D game. Even with the same poses, animations that were snappy in 2D tend to not work so well.

[00:17](https://youtu.be/oFwamE6Hy04?t=17) Animation tools are designed to be extremely convenient, and once you've set enough poses, will interpolate the movements between them. This can cause issues such as a model clipping into itself, but those details are quite easy to clean up.

[00:32](https://youtu.be/oFwamE6Hy04?t=32) But convenience doesn't mean quality. Even if you use the same poses and animation times as the 2D game, the interpolated frames tend to overpower that and make the animation feel slow. For example, look at this lead-in pose in its original game.

[00:49](https://youtu.be/oFwamE6Hy04?t=49) And this attack pose.

[00:55](https://youtu.be/oFwamE6Hy04?t=55) Recreating that animation with a 3D model gives us something like this. Though, we did place the middle kick a little lower than the original. I won't say this animation is bad, per se... Actually, I will.

[01:12](https://youtu.be/oFwamE6Hy04?t=72) The kick comes out in only 8 frames, but it still feels too slow. That's not very good. Now, here's how it looked in the release version of Smash Bros. Ultimate. It's still an 8-frame kick, but it feels very different.

[01:30](https://youtu.be/oFwamE6Hy04?t=90) The release version looks much snappier. The crucial poses in an animation are called “key frames," and we ġenerally want to reach them quite quickly. We don't need much time on the in-between frames, instead saving it for the lead-in and the attack. If possible, try to give the poses even more energy than the original key frames.

[02:02](https://youtu.be/oFwamE6Hy04?t=122) Here is Ryu's crouching heavy punch from his original game—an uppercut. The pixel art is extremely well made, I'd say. It's stunningly dynamic. The original had just three poses.

[02:16](https://youtu.be/oFwamE6Hy04?t=136) They play forward, then back to make the animation. However, if you translate it as-is into 3D, simply interpolating between those poses will kill the animation's momentum. Here's how we did it in Smash Bros. Ultimate.

[02:35](https://youtu.be/oFwamE6Hy04?t=155) It might not look all that different from how it looked in the original, but... Let's start at the top. In the original, his right forearm starts the animation in front of his body. We decided to pull it back a little bit.

[02:50](https://youtu.be/oFwamE6Hy04?t=170) We hold that anticipation for a relatively long time. The three key poses from the original game are here, but they're only on-screen for one frame each. But if the attack hits, those poses will leave an impression.

[03:05](https://youtu.be/oFwamE6Hy04?t=185) Make sure your animations really come out swinging! The first frame of the original is especially different in Smash, but that's because Ryu starts in a crouch in his game, and we wanted to express more momentum. For the follow-through after the attack, we made sure it took a different trajectory.

[03:24](https://youtu.be/oFwamE6Hy04?t=204) In other words, we ended up with different poses than the original's backwards movement by necessity, but we kept it as close as possible. You don't want your follow-through to be the same as your standby pose. Different games aim for different things, so it's not always necessary to speed through your animations, but I'd say you should always consider if your animations match your game, or if they're exaggerated enough.

[03:59](https://youtu.be/oFwamE6Hy04?t=239) Interpolation means filling in the gaps between key poses. You should use it well when you can, but take care not to make your animations lose their impact in the process.
