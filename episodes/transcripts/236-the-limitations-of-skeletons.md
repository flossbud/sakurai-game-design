# 236 · The Limitations of Skeletons

- **Category:** Animation
- **Video:** https://www.youtube.com/watch?v=q77TZaISg1Y
- **Length:** 03:12
- **Source:** official English subtitles burned into the video, read by OCR (tools/ocr_subs.py). Expect rare OCR typos.

---

[00:03](https://youtu.be/q77TZaISg1Y?t=3) When animating a character in CG, you can rig it with a “skeleton" to make the process smoother.

[00:12](https://youtu.be/q77TZaISg1Y?t=12) For real-life moving objects, the motion of an extremity is fundamentally determined by how its base moves. A wrist, for example, has its position set by moving the shoulder first, then the elbow, then the wrist itself. In the CG world, this is called “FK," or “forward kinematics."

[00:35](https://youtu.be/q77TZaISg1Y?t=35) The opposite—where you move the hand wherever you want, thereby deciding the shoulder and elbow angles— is called “IK," or “inverse kinematics." This can be very helpful when editing, and makes it easier to align limbs with the ground. Both processes have been around since I started studying CG, so they have quite a history by now.

[00:58](https://youtu.be/q77TZaISg1Y?t=58) I'd say they're fundamental. By the way, the structural units themselves are referred to as “bones” and “joints."

[01:13](https://youtu.be/q77TZaISg1Y?t=73) Now, I'd like to share some of my thoughts about these skeletons. For many, this may already be a solved problem, but I'll go over it in case I can help provide some insight. A joint's range of motion is naturally limited to 180 degrees. But I wish there was a way to bend them back further...

[01:35](https://youtu.be/q77TZaISg1Y?t=95) Here's what I mean by that. The left is our current limit, and the right is where I want it to be. For more oomph in the animation, I want to push beyond the straight arm. Yet skeletons built with joints that bend backwards would be generally harder to use, I'd say.

[01:55](https://youtu.be/q77TZaISg1Y?t=115) IK-based joints might start bending the opposite way you'd expect, for example.

[02:01](https://youtu.be/q77TZaISg1Y?t=121) Yet in CG, sometimes you'll want to exaggerate beyond realistic limitations. There are ways to deal with this, like adding more joints or building out the skeleton, but due to processing load and the need for animators with cartoon-focused sensibilities, we haven't been able to go that far on projects like Smash Bros.

[02:21](https://youtu.be/q77TZaISg1Y?t=141) I did suggest we try, at the start of development, but this is one problem we've yet to solve. In any case, I'd say that pushing beyond common sense is what gives animation its greatness. Give me something that breaks free from convention.

[02:40](https://youtu.be/q77TZaISg1Y?t=160) While skeletons were the example for this video, the same can be said about many things. If you're too tied down to convenient systems, you'll end up struggling to step away from their convenience. You'll form boundaries in your mind about what is and isn't possible. But creation is all about freedom—so try to push your ideas beyond those perceived íimits.

[03:00](https://youtu.be/q77TZaISg1Y?t=180) But creation is all about freedom—so try to push your ideas beyond those perceived limits.
