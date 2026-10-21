# 255 · What Happens When You Shift the Center of Gravity?

- **Category:** Design Specifics
- **Video:** https://www.youtube.com/watch?v=jeA-m-Bzs04
- **Length:** 02:42
- **Source:** official English subtitles burned into the video, read by OCR (tools/ocr_subs.py). Expect rare OCR typos.

---

[00:04](https://youtu.be/jeA-m-Bzs04?t=4) I've included this video in the Design Specifics category, but the same topic also ties into animation and effects, as well.

[00:14](https://youtu.be/jeA-m-Bzs04?t=14) The cannon that shows up in the Kirby games—Shotzo— fires in a way that feels pretty great. The cannonballs shake as they fly forward. During development, we referred to them as “wobbly cannonballs."

[00:28](https://youtu.be/jeA-m-Bzs04?t=28) If we simply sent the cannonballs flying forward in a straight line, it wouldn't be too interesting to look at. So we tried sliding the sprite's position around a bit. It was a six-frame sequence: up, right-up, right-down, down, left-down, and left-up— which then looped.

[00:47](https://youtu.be/jeA-m-Bzs04?t=47) Here it is being shot out. It feels completely different, right? It was also a good fit for the afterimages produced by the Game Boy's screen. When faced with straight, mechanical movements like this, or simple rotations around a center point, I think it's important to try and figure out how to add some personality.

[01:09](https://youtu.be/jeA-m-Bzs04?t=69) Let's look at a bomb throw in Smash Bros. Ultimate as an example. The bomb is spinning. But the axis of rotation is shifted slightly away from the center of the bomb. It makes the movement feel a little erratic.

[01:22](https://youtu.be/jeA-m-Bzs04?t=82) If we had instead set the axis of rotation to the center of the bomb, it would have felt less organic. This is Pyra's side special, Blazing End. And here's the mock-up I made while reviewing it during development. At first, the sword's grip served as the axis of rotation.

[01:45](https://youtu.be/jeA-m-Bzs04?t=105) That's a normal way of approaching the matter, but we then shifted the axis of rotation a bit. I only have footage of the fixed, final version, so I sadly can't put together a proper comparison, but there's a distinct difference in expression. If you're creating from an animation perspective, all of these suggestions may feel like givens.

[02:05](https://youtu.be/jeA-m-Bzs04?t=125) After all, "animation" means putting a soul into something unmoving. But if you're creating from a game design perspective, moving something in a straight line or rotating it in a smooth circle might be what you're used to.

[02:22](https://youtu.be/jeA-m-Bzs04?t=142) In the end, anything works as long as it feels right— but try to find ways to avoid the blandness that can come from simply following your software's tendencies.
