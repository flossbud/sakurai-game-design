# 036 · Breaking Down Attack Animations

- **Category:** Animation
- **Video:** https://www.youtube.com/watch?v=LewXWM7HDd8
- **Length:** 03:35
- **Source:** official English subtitles burned into the video, read by OCR (tools/ocr_subs.py). Expect rare OCR typos.

---

[00:04](https://youtu.be/LewXWM7HDd8?t=4) A great many games feature attack animations. In the games I've made, they can be broken down as follows.

[00:14](https://youtu.be/LewXWM7HDd8?t=14) Standby. Lead-in. Attack. And follow-through.

[00:22](https://youtu.be/LewXWM7HDd8?t=22) Let's take a look at these one by one. First, the standby. This is the pose from which all the others originate. Almost all of our animations are built from ground or aerial standby poses, so it's vital we nail these down first and don't change them.

[00:42](https://youtu.be/LewXWM7HDd8?t=42) The lead-in. This could also be called the “anticipation” or “windup." It's the pose that starts an attack— like raising your weapon to strike. In my games, these animations often start with a big, unexpected movement on the very first frame.

[00:56](https://youtu.be/LewXWM7HDd8?t=56) The game “jumps” to the pose. A smoother transition between standby and lead-in would take too much time. By instantly jumping to a big pose, the player can immediately know their input was recognized.

[01:10](https://youtu.be/LewXWM7HDd8?t=70) This also ençourages their opponent to dodge the moment they see it. The attack. Naturally, this is the key pose of an attack. This is when the attack can register as a hit, plus a bit of movement before or after.

[01:27](https://youtu.be/LewXWM7HDd8?t=87) We often use something called “hit stop" to stop the animation when an attack lands, making the crux of the attack— when you can actually hit your opponent— a firm, readable pose. You could say everything hinges on this moment.

[01:44](https://youtu.be/LewXWM7HDd8?t=104) Then, the follow-through. This is, in other words, the opening after an attack. The hit has finished registering, and the pose hangs for a moment before returning to standby. The player can't control the character here, so we keep this pose very distinct from the standby pose, and hold it as long as possible.

[02:06](https://youtu.be/LewXWM7HDd8?t=126) Additionally, we also assign “cancel frames” to follow-throughs. This lets players regain control without fully returning to the standby pose. The animation doesn't have to finish before the player can move, jump, or attack again. It's a little bit of elbow room, basically.

[02:26](https://youtu.be/LewXWM7HDd8?t=146) We didn't employ this concept until after Smash Bros. Melee, meaning you didn't regain control until your character returned to the standby pose. This made things feel a little heavy or rigid, I'd say. Now, as I've touched on before, whenever we make new animations, I always specify the following four things.

[02:48](https://youtu.be/LewXWM7HDd8?t=168) The standby pose. The attack pose. The attack start frame. and the total frames— or the time until the attack can be canceled.

[03:00](https://youtu.be/LewXWM7HDd8?t=180) As the lead-in fits between the standby and the attack, and the follow-through between the attack and the last total frame, these four pieces of information are often enough to give animators a good starting point. Of course, in practice, I'll often jump in with plenty of specific directions as well.

[03:17](https://youtu.be/LewXWM7HDd8?t=197) Now, as for the lead-in, the attack, and the follow-through... I might talk about them more later if the mood strikes.
