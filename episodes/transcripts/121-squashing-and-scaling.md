# 121 · Squashing and Scaling

- **Category:** Animation
- **Video:** https://www.youtube.com/watch?v=Sm0LAm4sJKc
- **Length:** 02:50
- **Source:** official English subtitles burned into the video, read by OCR (tools/ocr_subs.py). Expect rare OCR typos.

---

[00:04](https://youtu.be/Sm0LAm4sJKc?t=4) Increasing or decreasing the size of a model is known as "scaling." It's one of the most basic principles of animation.

[00:14](https://youtu.be/Sm0LAm4sJKc?t=14) For polygons and animations in computer graphics, there are three fundamental transformations: resizing an object—scaling— turning an object—rotation— and moving an object around— also known as translation.

[00:30](https://youtu.be/Sm0LAm4sJKc?t=30) Both rotating and translating objects are commonplace techniques in practice, but the same may not be true of scaling. Still, you shouldn't underestimate it. Depending on what you're animating, it can really punch things up.

[00:45](https://youtu.be/Sm0LAm4sJKc?t=45) Let's say we're animating a bouncing ball. Something like this. This is just a GIF animation I threw together. It's not too bad as-is...

[00:57](https://youtu.be/Sm0LAm4sJKc?t=57) but if we use scaling as well, this is what we get. The ball itself feels totally different. It's almost as if you can reach out and touch it.

[01:09](https://youtu.be/Sm0LAm4sJKc?t=69) Flattening objects with scaling like this is often called “squash and stretch," and it's an effective way to give an object texture and life. A key rule to follow with this technique is to always keep the object's mass roughly the same. If you're squashing vertically, I'd suggest you stretch horizontally to match.

[01:31](https://youtu.be/Sm0LAm4sJKc?t=91) We've been squashing Kirby when he crouches and lands ever since the Game Boy era. We continued doing so even after we started using 3D models for him, but I found that only squashing him makes him lose some physical presence. Here's an image I posted in one of my Daily Reports at the time.

[01:49](https://youtu.be/Sm0LAm4sJKc?t=109) I asked them to not just scale him, but to follow the pixel art on the right— giving him some more volume, similar to an oval track. If you just squash vertically, your oval will end up dull." I wanted some more volume on the sides.

[02:06](https://youtu.be/Sm0LAm4sJKc?t=126) We had discussed using “blend shape” to interpolate between two models, but I don't quite remember how that turned out. Either way, you can see we did more than just scale him down vertically. Scaling techniques like this can be found in even the smallest animation details.

[02:27](https://youtu.be/Sm0LAm4sJKc?t=147) While Mario's fist does get bigger when he punches, that's more about exaggeration— which is a bit different from what I’ve discussed here. If your animations need some oomph, try introducing these techniques.
