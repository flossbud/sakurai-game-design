# 084 · Units of Speed

- **Category:** Design Specifics
- **Video:** https://www.youtube.com/watch?v=_B0cpF8fQ4s
- **Length:** 03:04
- **Source:** official English subtitles burned into the video, read by OCR (tools/ocr_subs.py). Expect rare OCR typos.

---

[00:03](https://youtu.be/_B0cpF8fQ4s?t=3) Speed impacts many aspects of a game. It's very important. Speed equals distance divided by time. If you know any two of these numbers, you can figure out the third.

[00:19](https://youtu.be/_B0cpF8fQ4s?t=19) Back when I was writing specs for sprite-based games like on the NES, we expressed speed with the formula p/f. “Pixels per frame." It measures how many pixels a given object moves each frame.

[00:38](https://youtu.be/_B0cpF8fQ4s?t=38) In Mario Bros., I'd guess Mario runs at a maximum speed of 1 p/f. The NES had a screen width of 256 pixels. So one lap of the screen would be... Let's find out.

[00:58](https://youtu.be/_B0cpF8fQ4s?t=58) That's how long it takes. The Game Boy, NES, and Super NES all utilized different pixel counts. The canvas size for each was different. As such, assigning objects the same speed would yield greatly differing end results.

[01:14](https://youtu.be/_B0cpF8fQ4s?t=74) Then, when 3D games came along, we were able to switch to standard units of speed. km/h, for one. As long as characters and environments were defined in real-life units of measurement, we could use real speeds as-is in the game.

[01:30](https://youtu.be/_B0cpF8fQ4s?t=90) That obviously makes things much easier to understand. That's not to say there are no longer issues to consider, though— depending on the game, there may still be reasons to denote speed as distance per frame. Meters per frame, or centimeters per frame, for example.

[01:49](https://youtu.be/_B0cpF8fQ4s?t=109) Let's take a look at Kirby Air Ride. We expressed speed in the game as km/h. We expressed speed in the game as km/h. * mph in the NA version shown here. These speeds might seem to be rather low, but that's because Kirby is only as big as a 20cm square.

[02:03](https://youtu.be/_B0cpF8fQ4s?t=123) So for him, those “slow" speeds are actually quite fast. This is a land battle from Kid Icarus: Uprising. Pit actually moves extremely fast, even in his normal walk cýcle. He's even faster when running.

[02:17](https://youtu.be/_B0cpF8fQ4s?t=137) If we animated him normally, his legs would never keep up— so we instead gave him more of a bounding motion, and let him slide along the ground. Whether it's in spec sheets or parameters, you won't get far if you can't convey speed. So, it's essential you get your whole team on the same page when it comes to distances by specifying your units of measurement.

[02:42](https://youtu.be/_B0cpF8fQ4s?t=162) Cultivating your sense of speed in games is an important skill. When you're explaining how things should move and writing parameters to match that vision, you'll save yourself a lot of time if your estimates are hitting the mark.
