# 047 · Eight Hit Stop Techniques

- **Category:** Design Specifics
- **Video:** https://www.youtube.com/watch?v=tycbMSjDDLg
- **Length:** 05:32
- **Source:** official English subtitles burned into the video, read by OCR (tools/ocr_subs.py). Expect rare OCR typos.

---

[00:03](https://youtu.be/tycbMSjDDLg?t=3) "Hit stop" is an effect added when an attack hits its target. Both you and your opponent stop for a brief moment. There's a long history behind it, but one game's striking use of hit stop left a deep, lasting impression— by which I mean Final Fight.

[00:18](https://youtu.be/tycbMSjDDLg?t=18) The game would have been drastically different without it. Hit stop is a vital part of Smash Bros. as well, Hit stop is a vital part of Smash Bros, as well, but its implementation uses several techniques that are rarely or even never seen in other games.

[00:31](https://youtu.be/tycbMSjDDLg?t=31) Today, I'd like to talk about these hit stop techniques as seen in Smash Bros. Ultimate. Look at me, spilling trade secrets!

[00:44](https://youtu.be/tycbMSjDDLg?t=44) As a general rule, hit stop in Smash Bros. is never just a stop— there's always a bit of “shake," too. It does still work as a hit stop if all you do is stop movement, but I like to be a little more particular about it.

[00:58](https://youtu.be/tycbMSjDDLg?t=58) Technique one: make the receiving character shake more. Hit stop halts the movement of both characters, but I make the one receiving damage shake more, while the one inflicting damage shakes less.

[01:12](https://youtu.be/tycbMSjDDLg?t=72) In other games, sometimes the attacker doesn't shake at all, or sometimes neither the attacker nor the receiver shake. Technique two: don't move the hit box. If you just shake a fighter when they get hit, you'l end up shaking their hit box, too— making attacks that should connect miss instead.

[01:33](https://youtu.be/tycbMSjDDLg?t=93) In Smash Bros., only the character model moves, while the hit box itself stays in place. Technique three: shake horizontally on the ground, shake in all directions in the air. In Smash Bros., fighters on the ground affected by hit stop shake only from side to side, while fighters in the air affected by hit stop shake up and down as well.

[01:56](https://youtu.be/tycbMSjDDLg?t=116) Considering how the fighters face each other, it would be better if they always shook vertically, but doing so while they're on the ground would cause their legs to clip through the surface. This was less of a concern in 2D games. Technique four: gradually resolve the shake.

[02:15](https://youtu.be/tycbMSjDDLg?t=135) The amount of shake isn't a fixed value— it starts off big, and ends up smaller. By calculating the time the hit stop will last, you can make it resolve appropriately. Technique five: control the amount of hit stop.

[02:30](https://youtu.be/tycbMSjDDLg?t=150) In Smash Bros., the stronger an attack, the more hit stop it inflicts, but I also apply a multiplier to that. Take Marth's Smash Attack, for example. The base of his sword does less damage, so there's not as much feedback.

[02:45](https://youtu.be/tycbMSjDDLg?t=165) But the tip of his sword deals high damage, and bam—you really feel it. This isn't just a difference in attack values, but also the multiplier taking effect— making each hit feel even stronger than the damage dealt. Even on moves that deal the same damage, Ryu's hit stops appear bigger, while Kazuya's hit stops appear smaller.

[03:08](https://youtu.be/tycbMSjDDLg?t=188) This is done to more closely match their original games. Technique six: interpolate into the damage pose. In many games, the receiving character freezes in place during hit stop. In many games, the receiving character freezes in place during hitstop.

[03:21](https://youtu.be/tycbMSjDDLg?t=201) They snap to one pose. In Smash Bros., though, several interpolated frames transition the character to the damage pose when they take a hit. They don't freeze where they are.

[03:32](https://youtu.be/tycbMSjDDLg?t=212) And they don't snap straight to the damage pose. Instead, the motion is smoothly blended across four or so frames, giving a fluid, satisfying result. Technique seven: keep the attacker moving very slightly during the hit stop.

[03:49](https://youtu.be/tycbMSjDDLg?t=229) This is the pinnacle of these hit stop techniques. Say a fighter with a sword takes a strong swing at their opponent. If you look closely during the hit stop, you'll see that the tip of the sword is still inching upward. During the hit stop, the attacker's animation keeps moving at a pace so slow, it doesn't even move every frame.

[04:11](https://youtu.be/tycbMSjDDLg?t=251) Once the hit stop ends, the animation resumes as if nothing ever happened. We can toggle this effect on or off, so you won't see it in every attack. This was included to make swords look like they're actually cutting, This was included to makeswords look like they're actually cutting, so some attacks are better off without it.

[04:30](https://youtu.be/tycbMSjDDLg?t=270) Some other things we do include lengthening the hit stop for lightning, or reducing hit stop in multiplayer battles, but I won't get into that here. By the way, the amount of shake varies based on camera distance. When the camera is pulled back, characters will shake comparatively more than usual.

[04:53](https://youtu.be/tycbMSjDDLg?t=293) This way, the impact will look and feel the same regardless of whether the viewer is near or far, but. Well, I think you get the idea, right?

[05:06](https://youtu.be/tycbMSjDDLg?t=306) Talking about this comes naturally because I came up with many of these techniques myself. I understand why they're needed— and also the results they can bring. Each one might be hard to catchon its own, but when they're all working together, they can really make a game that much better.
