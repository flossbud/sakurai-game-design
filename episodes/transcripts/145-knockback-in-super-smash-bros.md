# 145 · Knockback in Super Smash Bros.

- **Category:** Programming & Tech
- **Video:** https://www.youtube.com/watch?v=HVktK4a9Yfo
- **Length:** 03:19
- **Source:** official English subtitles burned into the video, read by OCR (tools/ocr_subs.py). Expect rare OCR typos.

---

[00:03](https://youtu.be/HVktK4a9Yfo?t=3) In Smash Bros., attacks don't simply deal damage to an opponent or deplete their health based on the strength of the attack inflicted. "Knockback" is at the heart of its game essence, so we have to make a few unique considerations.

[00:20](https://youtu.be/HVktK4a9Yfo?t=20) In this video, I’d like to discuss the attack parameters used in Super Smash Bros, which relate to knockback. In this video, I'd like to discuss the attack parameters used in Super Smash Bros, which relate to knockback. In Smash Bros., the more damage an attack deals, and the higher the damage percentage accumulated by the target, the greater the knockback will be.

[00:48](https://youtu.be/HVktK4a9Yfo?t=48) These determine the direction of the knockback. This exists with more limited directionality in some other fighting games, but in Smash Bros., we can set knockback to occur in any direction. And by applying a special modifier, we can make the knockback react to the direction the attacker is traveling.

[01:08](https://youtu.be/HVktK4a9Yfo?t=68) With aerial combos, for example, this helps more of the attacker's hits land. Furthermore, the arc of the knockback, even with all other conditions equal, will change based on values like the target fighter's fall velocity and weight.

[01:27](https://youtu.be/HVktK4a9Yfo?t=87) A multiplier allows us to adjust the knockback inflicted when an attack lands. We can make strong attacks cause only slight knockback, or weak attacks knock fighters back quite far— as you can see, it allows for some real fine-tuning.

[01:47](https://youtu.be/HVktK4a9Yfo?t=107) This is the minimum amount of knockback an attack inflicts, no matter what. For example, an opponent that hasn't taken much damage won't get knocked back much at all by attacks meant to launch them upward, but there should at least be some reaction, and this parameter lets us guarantee a set minimum amount of knockback.

[02:05](https://youtu.be/HVktK4a9Yfo?t=125) However, simply tacking this value on would make the knockbacks too big, so we use knockback scaling to keep everything in check.

[02:18](https://youtu.be/HVktK4a9Yfo?t=138) This value lets us set an exact knockback regardless of other conditions. No matter how much damage a fighter has taken, they'll always react exactly the same way. Take Mario's Super Jump Punch. The initial successive hits use a fixed knockback value, while only the final hit uses the standard knockback.

[02:41](https://youtu.be/HVktK4a9Yfo?t=161) It would be quite the problem if later hits didn't land because the opponent's damage was too low or too high.

[02:50](https://youtu.be/HVktK4a9Yfo?t=170) The structure behind these parameters has existed since the original Smash Bros. It has some pretty unorthodox rules compared to the average game, so it takes this sort of special detail to make it feel fun. There's plenty more that goes into attack parameters beyond what I just showed you, but for this video, I tried to keep the topic focused.
