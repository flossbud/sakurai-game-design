# 103 · Screen Shake

- **Category:** Effects
- **Video:** https://www.youtube.com/watch?v=2JXR7IASSog
- **Length:** 03:40
- **Source:** official English subtitles burned into the video, read by OCR (tools/ocr_subs.py). Expect rare OCR typos.

---

[00:04](https://youtu.be/2JXR7IASSog?t=4) Making the screen shake can be just the ticket for conveying a big impact, so I'd say go for it whenever appropriate. I’ve been using it often since Kirby's Adventure, and consider it to be very important. It may make the screen difficult to see, though, so you don't want to shake things too much.

[00:27](https://youtu.be/2JXR7IASSog?t=27) Let's start with the two main ways you can shake the screen. You can move the camera itself, or you can move the whole image after it's rendered. The former involves moving a camera in 3D space.

[00:39](https://youtu.be/2JXR7IASSog?t=39) That means objects in the distance may not be as affected by the shake. With the latter, the whole screen clearly shakes. That includes the Ul as well, and it might reveal some empty space at the edges of the screen, so take that into account.

[00:59](https://youtu.be/2JXR7IASSog?t=59) The former is likely more common, but since you may end up with almost no shake the farther from the camera you go, you'll need to think about how you move your center point. The “center point” is the point the camera is looking at.

[01:14](https://youtu.be/2JXR7IASSog?t=74) You may sync its shake with your camera, or you may consider making it shake even more than the camera itself. If you move a far-off center point too subtly, it won't look like there's much movement happening at all.

[01:27](https://youtu.be/2JXR7IASSog?t=87) We use a number of screen shake patterns and techniques for Super Smash Bros. For a while now, we've used large, medium, small, and extra-small patterns of screen shake. Large, medium, and small aren't just scaled versions of the same shake, but actually use different patterns entirely.

[01:45](https://youtu.be/2JXR7IASSog?t=105) Let's take a look. This is “small." It only shakes up and down. This is “medium."

[01:53](https://youtu.be/2JXR7IASSog?t=113) There's some horizontal shake here, too. And this is “large." It might be hard to tell the difference from medium, but there's even more shake. Here's a sustained shake.

[02:06](https://youtu.be/2JXR7IASSog?t=126) Vertical shake helps convey the movement of the terrain. For shakes like this, it's best to not move too much on either axis. And now, some implementation techniques. We change the size of the screen shake based on the distance of the camera.

[02:20](https://youtu.be/2JXR7IASSog?t=140) This keeps things from feeling off. That distance affects the field of view as well, so we have to adjust the shake to look good everywhere. Take stages like Flat Zone, for example.

[02:34](https://youtu.be/2JXR7IASSog?t=154) The tighter field of view here makes our usual shake feel really big, so we tweaked it to match. The shaking starts strong, then gradually subsides. It's not a clean whirlpool pattern, but something with a little more randomness to make it feel nicer.

[02:56](https://youtu.be/2JXR7IASSog?t=176) And so on. In the old days, I'd sometimes jostle my mouse to shake the camera, then design the screen movements based around that.

[03:07](https://youtu.be/2JXR7IASSog?t=187) A game without screen shake might feel pretty bland. Even a tiny amount of shake can give attacks a drastically different impact. Screen shake is a very common technique, and it's an effective one, too. In 3D scenes, it can be tough to find just the right amount of shake, but it'll make your game feel better, so I'd say it's a crucial element worth putting effort into.
