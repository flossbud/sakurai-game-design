# 061 · Don't Anchor Your Center Point

- **Category:** Design Specifics
- **Video:** https://www.youtube.com/watch?v=kLmd2F8LaLk
- **Length:** 02:51
- **Source:** official English subtitles burned into the video, read by OCR (tools/ocr_subs.py). Expect rare OCR typos.

---

[00:03](https://youtu.be/kLmd2F8LaLk?t=3) Cameras used in 3D games have a "center point" that they focus on. This center point usually isn't visible, but any game with a camera will have one.

[00:18](https://youtu.be/kLmd2F8LaLk?t=18) The reason a game's camera can rotate so tightly around your character is because the center point is often set to the character's position. In other words, the center point is anchored to the character. But believe me when I say: don't anchor your center point to the character!

[00:36](https://youtu.be/kLmd2F8LaLk?t=36) You're probably thinking I've lost it right about now. Let's take a look at Super Mario 64. Keep an eye on Mario's position in the game screen. Even when he's walking around, he stays at the center.

[00:49](https://youtu.be/kLmd2F8LaLk?t=49) That makes sense, right? But now, let's have him jump. His relative position moves up, away from the center of the screen. It's obvious when you look closely, but not so obvious in practice.

[01:03](https://youtu.be/kLmd2F8LaLk?t=63) Here is Smash Bros. Ultimate, with the camera set to track the fighter. This is what you end up with when you anchor the center point to a character. It's really tough to tell how high Mario is jumping, right? So, the center point shouldn't track on the Y axis— or should at least track less— to let players feel the height of their jumps.

[01:27](https://youtu.be/kLmd2F8LaLk?t=87) If you anchor the center point, it might be hard to discern how the character is moving. Of course, doing so may still be the right decision for some titles, but framing your camera correctly can really improve presentation, so don't let it go to waste. This is Armored Core.

[01:43](https://youtu.be/kLmd2F8LaLk?t=103) Move up, down, left, or right, and your AC moves away from the center of the screen. This makes it easier to see the bullets and missiles you’ve dodged, so it's much more impactful. Anchoring the center point may work great for third-person racing games with realistic precision.

[02:03](https://youtu.be/kLmd2F8LaLk?t=123) But in Kirby Air Ride... when you go into a drift, the Air Ride machine moves slightly away from the center point. I did this so that players would really feel the input, and to boost the sensation of careening past walls as you drift.

[02:20](https://youtu.be/kLmd2F8LaLk?t=140) For games like side-scrollers that want to give you a wider field of vision, the camera will move to show more of the screen ahead of you.

[02:30](https://youtu.be/kLmd2F8LaLk?t=150) Don't assume the camera should always be following your character, but instead make sure it fits your gameplay and presentation. This is a very important point, so be sure to keep it in mind.
