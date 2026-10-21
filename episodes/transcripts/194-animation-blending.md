# 194 · Animation Blending

- **Category:** Animation
- **Video:** https://www.youtube.com/watch?v=HYHajZ0wBfU
- **Length:** 03:04
- **Source:** official English subtitles burned into the video, read by OCR (tools/ocr_subs.py). Expect rare OCR typos.

---

[00:04](https://youtu.be/HYHajZ0wBfU?t=4) Animation blending is a technique that lets you combine two or more animations.

[00:12](https://youtu.be/HYHajZ0wBfU?t=12) To give an example, in my video about the specifics of attack animations, I talked about a concept known as “cancel frames." After an attack, you'll be briefly vulnerable, then transition into cancel frames where you can input another action.

[00:25](https://youtu.be/HYHajZ0wBfU?t=25) Inputting an action here won't just snap the character to the next animation, though— it'll blend the animations between the canceled action and the one you input. Here's a transition from idle to walking. It looks natural, right?

[00:45](https://youtu.be/HYHajZ0wBfU?t=45) Here's a transition from attacking to walking. This looks natural too, right? Here's the moment it changes from idle to walking. Here's the moment it changes from attacking to walking.

[01:06](https://youtu.be/HYHajZ0wBfU?t=66) The ensuing walk animation is the same, but the starting pose is drastically different. This is the result of animation blending.

[01:33](https://youtu.be/HYHajZ0wBfU?t=93) With animation blending, you can set both the strength and duration of a blend. But as I noted in my prior video on interpolation, making the animation too smooth can decrease its rhythm and impact. And since it's an automated process, the animation can end up distorted.

[01:49](https://youtu.be/HYHajZ0wBfU?t=109) As a result, you don't want a blend to last too long. Make it quick and snappy. The movements seen when shifting your shield are another kind of animation blending. It's a combination of movement in a circle with the fixed stance at the center.

[02:08](https://youtu.be/HYHajZ0wBfU?t=128) However, animation blending doesn't play too great a role in a fast-paced game like Smash Bros. If anything, the technology shines brighter in fully 3D games. Upper and lower bodies move separately, while legs position themselves naturally on terrain. Inclines affect turn animations, and characters change states often.

[02:28](https://youtu.be/HYHajZ0wBfU?t=148) It's so complex that you can't tell where the blending begins and ends.

[02:36](https://youtu.be/HYHajZ0wBfU?t=156) There's more to animationthan simply making things that look lively— and you can't rely on existing technology to fill in all the gaps, either. I imagine somewhere out there, research continues tirelessly even today. In a way, what we're doing in games might not be too different from robotics.
