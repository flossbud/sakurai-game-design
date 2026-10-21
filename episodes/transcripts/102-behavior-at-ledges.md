# 102 · Behavior at Ledges

- **Category:** Design Specifics
- **Video:** https://www.youtube.com/watch?v=rcuihq0j7VM
- **Length:** 02:30
- **Source:** official English subtitles burned into the video, read by OCR (tools/ocr_subs.py). Expect rare OCR typos.

---

[00:04](https://youtu.be/rcuihq0j7VM?t=4) In many games where you control a character, it's possible for that character to fall off a ledge. There are a variety of ways to handle this, but of course, some are better than others.

[00:16](https://youtu.be/rcuihq0j7VM?t=16) First, characters could simply fall regardless of any other conditions. Many games were like this in the old days— often to their own detriment— so it's good to reflect on whether or not it's really worth using. Next, let's consider a character falling during movement, but not during actions.

[00:36](https://youtu.be/rcuihq0j7VM?t=36) If you let a player fall off a ledge the moment they're nudged forward by an action, it may make them feel like their input was canceled—which isn't great. Instead, for example, you might make it so attacks that step forward don't let them fall. Next, let's consider games where some actions make the character fall, while others don't.

[00:59](https://youtu.be/rcuihq0j7VM?t=59) This is the way to do it, I'd say. For example, you might make it so forward dodges don't fall, while attacks that rush forward do. If you don't account for momentum, too, it may be too easy to go flying off the stage. Let's look at Smash Bros.

[01:15](https://youtu.be/rcuihq0j7VM?t=75) Moves like Fox Illusion will stop when you hit the ledge. A Falcon Kick, however, will send you straight over. Though, not if you hit the ledge toward the end of the move. Drill Rush is another risky choice to use near the ledge.

[01:31](https://youtu.be/rcuihq0j7VM?t=91) But it, too, stops at the ledge toward the end of the move. With moves like Egg Roll, we set parameters to determine what speed causes Yoshi to fly off the ledge. Back to the more general topic, though.

[01:46](https://youtu.be/rcuihq0j7VM?t=106) Some games make you “push" against ledges to fall off them. Another effective technique is to adjust the player's movement direction if the ledge is more or less parallel to the direction of their movement.

[02:01](https://youtu.be/rcuihq0j7VM?t=121) Falling off ledges isn't as straightforward as it seems. As you can see, there are plenty of aspects you need to consider. Some games even make the player jump automatically when they reach a ledge. For creators, don't overlook how things feel during playtesting, and try to find the mechanics that best suit your game.
