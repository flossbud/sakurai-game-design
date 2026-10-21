# 044 · Distinguishing Between Major and Minor Elements

- **Category:** Graphics
- **Video:** https://www.youtube.com/watch?v=NBXt-Uq7dHg
- **Length:** 02:46
- **Source:** official English subtitles burned into the video, read by OCR (tools/ocr_subs.py). Expect rare OCR typos.

---

[00:03](https://youtu.be/NBXt-Uq7dHg?t=3) When developing for game consoles, you have to constantly think about performance. Generally speaking, hardware isn't as powerful as the average person might think. If you don't economize performance, you might not realize your goals. At times like this, it's important to consider whether an element is a major or a minor one.

[00:22](https://youtu.be/NBXt-Uq7dHg?t=22) In other words, you need to discern what parts of your game will have more—or less—impact.

[00:30](https://youtu.be/NBXt-Uq7dHg?t=30) Let's take a look at the Smash Bros. screen layout. In many stages, the backdrop is similar to a skysphere, and you can take in the scenery to some degree. But the place players are most likely to be looking is the center of the screen.

[00:46](https://youtu.be/NBXt-Uq7dHg?t=46) So even when it comes to skyspheres, the area in front of the camera is going to be getting the most attention, meaning that's what you should focus on. With foreground terrain, the foundation parts that are often off-screen matter less than the stage's surface.

[01:01](https://youtu.be/NBXt-Uq7dHg?t=61) Comparing fighters and stages, it might seem like the fighters should be given higher priority— but since they're often displayed at a relatively smaller size, you don't need to get carried away.

[01:12](https://youtu.be/NBXt-Uq7dHg?t=72) It's important to consider how much of the screen each element takes up. That said, the fighters are shown up close for all kinds of assets, so you have to remember these models aren't just for gameplay, and prioritize accordingly. A technique called LOD* lets you swap in lower-polygon assets the further an object is from the camèra.

[01:34](https://youtu.be/NBXt-Uq7dHg?t=94) But implementing this is labor-intensive, so the perfomance benefit needs to be worth it. By the way, you may occasionally glimpse some very particular details the stage team worked into Smash Bros. I've shown a few of them in my daily screens, too.

[01:54](https://youtu.be/NBXt-Uq7dHg?t=114) Of course, I didn't personally request these to be included, but as long as the artists met deadlines and the game's performance didn't suffer, I didn't object, either. The game is better off with a bit of playfulness.

[02:07](https://youtu.be/NBXt-Uq7dHg?t=127) But when I realized they made the car tires in the backdrop of Inkling's stage actually turn, that's when I asked them to tone it down. It was something truly nobody would see.

[02:24](https://youtu.be/NBXt-Uq7dHg?t=144) Distinguish between major and minor elements, and allocate your resources effectively. Economizing your game in this way is an essential skill—and not only for graphics.
