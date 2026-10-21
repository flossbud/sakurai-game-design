# 005 · Frame Rates

- **Category:** Planning & Game Design
- **Video:** https://www.youtube.com/watch?v=Rjdmi7628GM
- **Length:** 04:00
- **Source:** official English subtitles burned into the video, read by OCR (tools/ocr_subs.py). Expect rare OCR typos.

---

[00:04](https://youtu.be/Rjdmi7628GM?t=4) In the Planning & Game Designcategory, I'll go over what you need to know when coming up with game ideas and mechanics. We'll talk about how to format game design documents elsewhere.

[00:20](https://youtu.be/Rjdmi7628GM?t=20) I suspect most avid gamers already know this, but I'll explain anyway since it's crucial. In the game industry, "frame rate" measures how often the screen is redrawn.

[00:36](https://youtu.be/Rjdmi7628GM?t=36) Think of it like the frames of a film projector. On standard televisions, the screen is redrawn or “refreshed" 60 times each second— that's 60 frames per second (fps).

[00:48](https://youtu.be/Rjdmi7628GM?t=48) In games, these frames are often used as a unit of time. Distance = Time × Speed. In this equation, time has a huge effect on how far and how fast things move. So you can see why frame rate is extremely important.

[01:10](https://youtu.be/Rjdmi7628GM?t=70) 60 fps and 30 fps are quite different both in how they look and how smoothly they control. It might be hard to tell on YouTube, but this is what it looks like.

[01:24](https://youtu.be/Rjdmi7628GM?t=84) 60 fps is an ideal frame rate when possible, but 30 fps is also a common standard. After all, to draw twice as many frames, you'd have to sacrifice half your visual performance. And 30 fps is still more than adequate for playing games.

[01:44](https://youtu.be/Rjdmi7628GM?t=104) In fact, 30 fps is a common standard for many forms of visual media. Frame rates aren't always consistent within games. They can vary based on platform and how a game is programmed. Some games have a variable frame rate, reducing frames when the processor can't keep up.

[02:01](https://youtu.be/Rjdmi7628GM?t=121) That's not to be confused with "slowdown." The game itself isn't slowing down— it's just redrawing the screen less often. Some PC games and high-end machines can surpass 120 or even 200fps, depending on processing power.

[02:18](https://youtu.be/Rjdmi7628GM?t=138) But none of that will matter if your monitor doesn't support it. What you really want is both. Silky smooth graphics are where it's at!

[02:28](https://youtu.be/Rjdmi7628GM?t=148) Now, if I can reminisce a little, let's take a trip back to the days of the NES, SNÉS, and Nintendo 64. Back then, we made games for CRT televisions, which had two standards: NTSC and PAL. Japan and North America used NTSC, which renders images at 30 frames per second.

[02:47](https://youtu.be/Rjdmi7628GM?t=167) Taking advantage of interlacing, you could make a game run at 60 fps. However, Europe and Australia used the PÀL standard. PAL delivered 25 frames per second, meaning our games ran at 50 fps.

[03:04](https://youtu.be/Rjdmi7628GM?t=184) At least for the NES and SNES games I made, we used the number of screen interrupts as our unit of time. In other words, porting games to PAL caused them to run 5/6 as fast.

[03:20](https://youtu.be/Rjdmi7628GM?t=200) Everything moved just a little slower. However, from the Nintendo 64 onward, games used polygon processing. It became easier to draw fewer frames and otherwise run the game as intended, which resulted in less jarring tradeoffs.

[03:40](https://youtu.be/Rjdmi7628GM?t=220) So! Frame rate is about time, the number of images, and resolution, with 60 fps being a general standard. These concepts will come up often, so please try to keep them in mind.
