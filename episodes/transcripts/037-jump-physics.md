# 037 · Jump Physics

- **Category:** Design Specifics
- **Video:** https://www.youtube.com/watch?v=noKsDZ-UPq8
- **Length:** 04:53
- **Source:** official English subtitles burned into the video, read by OCR (tools/ocr_subs.py). Expect rare OCR typos.

---

[00:04](https://youtu.be/noKsDZ-UPq8?t=4) Think about a character's jump. It's an extremely simple action, but there's a lot here you have to consider.

[00:17](https://youtu.be/noKsDZ-UPq8?t=17) First of all, if you're talking about how jumps are programmed in games... Generally speaking, a set fall speed is continuously applied to a character while they're airborne. First, we apply upward velocity. Let's say our velocity is 5— in any unit of measurement.

[00:39](https://youtu.be/noKsDZ-UPq8?t=39) Then, while the character is airbone, we add 1 unit of downward acceleration per frame. That means in the next frame, the character's upward velocity will be reduced to 4. In the next frame, it's 3. Then 2.

[00:55](https://youtu.be/noKsDZ-UPq8?t=55) The velocity decreases bit by bit. Even after we hit 0, we keep adding downward acceleration. That will make the character fall faster with each frame. Starting with 1, then 2, 3, 4.

[01:11](https://youtu.be/noKsDZ-UPq8?t=71) If the terrain is flat, the character will land when downward velocity equals the initial upward velocity. These values apply to the Y axis— the character's vertical movement— but horizontal movement on the X axis generally stays consistent, or maybe decelerates slightly.

[01:31](https://youtu.be/noKsDZ-UPq8?t=91) There are other concepts involved, too, like maximum velocity and inertia, but I wanted to keep things basic. Remember, though: your jump might change depending on the goal of your game. Take, for example, the jump in Super Mario Bros.

[01:48](https://youtu.be/noKsDZ-UPq8?t=108) It's relatively gentle on the way up. That means downward acceleration starts out very low, but increases suddenly at the peak of the jump, and Mario falls much faster than he rose. How long you hold the button also changes the height of the jump, which works well with this design.

[02:08](https://youtu.be/noKsDZ-UPq8?t=128) In Metroid, Samus rises even slower than that. She also falls pretty slowly, making it feel a bit like she's floating. This is a game where the height you shoot at is vital, so this jump may have been meant to help with that.

[02:24](https://youtu.be/noKsDZ-UPq8?t=144) In Ghosts 'n Goblins, the jump height is relatively low, and you can't change direction even a little once you've jumped. The moment you jump, you know where you'll land. The controls are more restrictive, but there's solid “game essence" in having to carefully plan each jump, and this way players can attack while jumping backwards.

[02:44](https://youtu.be/noKsDZ-UPq8?t=164) This is Zangief's Spinning Pile Driver from Street Fighter II. From Street Fighter II Turbo onward, Zangief falls more quickly than he rises. This gives the move more impact as he slams his opponent into the ground. Even with the same trajectory, adjusting a move's speed can drastically change how it feels.

[03:08](https://youtu.be/noKsDZ-UPq8?t=188) For jumps in Smash Bros., there's a windup right before you jump. There used to be a wide variety of these among the various fighters, but nowadays they're all unified to the same short windup. If we removed it entirely, players would end up jumping before they could input an Up Smash— so we have to keep it in some form.

[03:29](https://youtu.be/noKsDZ-UPq8?t=209) By the way, every time we start working on a new Smash Bros., I ask myself whether we even need a jump. The answer has always been yes, but the physics do change with each game. Smash Bros. Ultimate is the first title since Kirby Super Star to feature a certain fairly innovative jump design.

[03:51](https://youtu.be/noKsDZ-UPq8?t=231) Pop quiz: What is it?

[04:00](https://youtu.be/noKsDZ-UPq8?t=240) Let me explain. We start by applying a very strong upward velocity at the beginning of each jump. Then for a few frames, we greatly increase downward acceleration. Once the jump sņaps to a halt, downward acceleration is returned to normal.

[04:14](https://youtu.be/noKsDZ-UPq8?t=254) This way, players can still get out of a jam even if they react a little late. This introduces even more parameters and complicates the physics, and it increases the risk of bugs, but it's a nice jump with some great benefits.

[04:29](https://youtu.be/noKsDZ-UPq8?t=269) Bet you didn't notice this while playing, right? Just one of the many secret ingredients to the game.

[04:37](https://youtu.be/noKsDZ-UPq8?t=277) There's a lot that goes into even a single jump! Tinker a bit, and you never know what you might come up with.
