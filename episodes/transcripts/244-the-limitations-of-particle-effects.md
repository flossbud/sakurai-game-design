# 244 · The Limitations of Particle Effects

- **Category:** Effects
- **Video:** https://www.youtube.com/watch?v=jAQv4PTQvQE
- **Length:** 04:40
- **Source:** official English subtitles burned into the video, read by OCR (tools/ocr_subs.py). Expect rare OCR typos.

---

[00:03](https://youtu.be/jAQv4PTQvQE?t=3) Effects that scatter out in large quantities are generally known as "particles." Effects that scatter out in large quantities are generally known as “particles." Like what you see here.

[00:13](https://youtu.be/jAQv4PTQvQE?t=13) which I’ve discussed previously Including the billboard variety which I’ve discussed previously, particles need to appear in as large a quantity as possible while having as low a processing load as possible— which is achieved through a variety of techniques.

[00:27](https://youtu.be/jAQv4PTQvQE?t=27) When it comes to games l’ve created, I’ve been using particle-like effects since the very first Kirby game. At the time, getting anything to display was challenging enough.

[00:40](https://youtu.be/jAQv4PTQvQE?t=40) Though of course, these restrictions eased with each increase in hardware power. Particles became less intensive to process. Though, they'll always have some cost. As great as it would be to use tons of different particle effects, that isn't possible—so we've had to set some rules around their use.

[00:57](https://youtu.be/jAQv4PTQvQE?t=57) Generally speaking, we keep them short. It would be nice to leave lots of after-effects on-screen, but given how quickly the next particles need to appear, we don't have that luxury. We compensate for this shorter lifespan with increased speed.

[01:21](https://youtu.be/jAQv4PTQvQE?t=81) Next: we combine multiple particles into one. It might look like there are lots of bubbles coming from this Steel Diver projectile, but it's actually just several panels containing multiple bubbles each.

[01:40](https://youtu.be/jAQv4PTQvQE?t=100) Stagger the effect timing. Instead of creating particles for several objects at once, we stagger the timing, thus reducing how many particles are displayed at the same time.

[01:56](https://youtu.be/jAQv4PTQvQE?t=116) We stagger their positions, too, to keep them from overlapping. After all, there's no point in creating lots of particle effects if they all end up on top of each other. Make them somewhat large. It would be great if we could show an abundance of tiny particle effects, but we just can't do that.

[02:18](https://youtu.be/jAQv4PTQvQE?t=138) Instead, we draw each billboard large to use them as effectively as possible.

[02:26](https://youtu.be/jAQv4PTQvQE?t=146) While I’m envious of the opulent effects seen in games like Tekken 7.. Smash Bros. differs not only in hardware power, but things like camera distance and number of impact effects as well.

[02:41](https://youtu.be/jAQv4PTQvQE?t=161) Still, we did our best to reproduce them! We couldn't do the same things with fast repeated hits, though.

[02:58](https://youtu.be/jAQv4PTQvQE?t=178) All you can do is work within your game's limits and try to aim for the best effect possible. Now, let's take another look at the first Kirby game. The effect when you defeat an enemy sort of looks like particles, right?

[03:15](https://youtu.be/jAQv4PTQvQE?t=195) There are several variations.

[03:21](https://youtu.be/jAQv4PTQvQE?t=201) But actually, the stars are positioned manually in each frame of animation, then displayed in order by the game. There's no code or data for calculating particle movement. Only the coordinates for playing the animation.

[03:34](https://youtu.be/jAQv4PTQvQE?t=214) The same goes for explosions from bombs and the like. They're composed entirely of animation frames.

[03:44](https://youtu.be/jAQv4PTQvQE?t=224) For Kirby's Dream Land, we made a lot of these things a little bit at a time using a Famicom-based dev tool. While it took up a lot of ROM space, the actual effect was light on processing. You could say the inhalation effect is particles, too. It randomly plays from a number of set movement patterns.

[04:02](https://youtu.be/jAQv4PTQvQE?t=242) By combining white and black pixels, we were able to make sure it would show up against any color background.

[04:11](https://youtu.be/jAQv4PTQvQE?t=251) Though at the time, using an entire 8x16 piece for a single 2x4 image felt extremely wasteful.

[04:24](https://youtu.be/jAQv4PTQvQE?t=264) Working with the hardware back then was all about saving space, so it trained you to be economical.
