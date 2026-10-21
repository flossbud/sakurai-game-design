# 141 · Unexpected Results

- **Category:** Design Specifics
- **Video:** https://www.youtube.com/watch?v=6P8zwwQ9OhU
- **Length:** 04:04
- **Source:** official English subtitles burned into the video, read by OCR (tools/ocr_subs.py). Expect rare OCR typos.

---

[00:04](https://youtu.be/6P8zwwQ9OhU?t=4) I've worked on my fair share of games, and it's not uncommon to find something unexpected and undesirable in the final release version of a game. Today, I'm going to swallow my pride and show you a few examples.

[00:20](https://youtu.be/6P8zwwQ9OhU?t=20) Back when we made Meteos, I programmed all the parameters for each planet myself. Meteos was made for the Nintendo DS, and I of course confirmed everything on actual hardware while tuning the game.

[00:32](https://youtu.be/6P8zwwQ9OhU?t=32) The schedule was quite a tight one, so by the end I was really pushing to make every minute count. There were lots of planets, after all. However, as we approached the end and the game's processing was optimized, the game speed ended up faster than before.

[00:48](https://youtu.be/6P8zwwQ9OhU?t=48) Smoother performance would usually be a welcome change, but as game speed was directly tied to processing speed, any increase to the latter meant an increase to both. This ended up altering the game's difficulty curve. In other words, it made the gameplay more difficult than I had intended for it to be.

[01:09](https://youtu.be/6P8zwwQ9OhU?t=69) If you play Meteos, you'll run into sequences that are tough to finish in the time alloted. But that's not how I intended for it to work. It's a disappointing memory for me. There were several other Meteos titles developed after the original was released, but I was only involved in the first game, so I can't speak to any of those.

[01:35](https://youtu.be/6P8zwwQ9OhU?t=95) Along the same lines, I worked on a game called Sodatete! Kouchuu Ouja Mushiking, which I developed using a custom development board just under one square meter in size. I used that for all my tuning, so I never tried the actual game for myself, despite its portable nature.

[01:53](https://youtu.be/6P8zwwQ9OhU?t=113) Then, once I played the finalized production unit, I noticed the Mushi got hungry faster than I expected. I'd guess there was some kind of discrepancy between the dev board and production unit's processing speeds, making this another unfortunate outcome.

[02:12](https://youtu.be/6P8zwwQ9OhU?t=132) Not to say that the game is unplayable. Last, we have Smash Bros. Ultimate. In the initial release version of the game, for some reason, CPU fighters felt too difficult. I have even less of a grasp of why this happened than the previous two examples, but several team members all raised the same concerns, so I don't think I imagined it.

[02:33](https://youtu.be/6P8zwwQ9OhU?t=153) I still don't know the cause. My only theory is that it resulted from some kind of processing speed increase, but I don't have any proof. If we had tried to adjust the core CPU functions or the difficulty settings for each mode, we would have had to bug test a lot of game elements over again, so that was off the table.

[02:54](https://youtu.be/6P8zwwQ9OhU?t=174) However, we did manage to address the issue to some extent. We lowered the difficulty of Challenger fights, and added a Very Easy difficulty to World of Light. Unlike the first two examples, we were able to fine-tune these issues through a downloadable patch, but in the old days, we would have been flat out of luck.

[03:13](https://youtu.be/6P8zwwQ9OhU?t=193) Granted, it's always unfortunate to have unexpected problems pop up, no matter the era. Some of you watching this might wonder, "How could stuff like that happen?!" But when you're working with computers, sometimes there's no telling what you might get. The fact that most other development went smoothly is perhaps a bit of good luck on my part.

[03:38](https://youtu.be/6P8zwwQ9OhU?t=218) Those successes may all be balancing precariously on the edge of failure. And it's not like there's a checklist of problems you can cross off one by one. But that's why I put together this video: to show that sometimes these things just happen.
