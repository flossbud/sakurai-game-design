# 225 · Always Keep Attack Collision in Mind

- **Category:** Animation
- **Video:** https://www.youtube.com/watch?v=rwwF_4blK-o
- **Length:** 02:42
- **Source:** official English subtitles burned into the video, read by OCR (tools/ocr_subs.py). Expect rare OCR typos.

---

[00:03](https://youtu.be/rwwF_4blK-o?t=3) Smash Bros. is a game that's viewed from the side. Hence, it's important that the fighters' silhouettes look good from a side perspective, but this does lead to issues in development...

[00:17](https://youtu.be/rwwF_4blK-o?t=17) To start with, I’d like to discuss the collision assigned to the game's various attack animations. Attack collision isn't directly mapped to the fighter's sword or fist, as seen here, but is instead made to cover a wider range. Because of the fast coordinate-based movement in Smash Bros., the game needs to have wide attack collision.

[00:41](https://youtu.be/rwwF_4blK-o?t=41) Otherwise, attacks will tend to miss, and players will get more and more stressed. Next, I'd like to talk about how this all works with the animation team. When an attack's range doesn't pass through the median line, it's hard for that attack to land. Of course, I ask for such cases to be fixed.

[01:03](https://youtu.be/rwwF_4blK-o?t=63) Technically, the attack animation can go wherever it wants, and as long as a game designer sets up the collision, the attack will still connect. However, this will result in a large gap between the animation and its collision. To an extent, it's okay if the visuals and collision don't line up, assuming it makes the game more fun, but if even the animation's positioning is off, things will start to feel even more broken.

[01:31](https://youtu.be/rwwF_4blK-o?t=91) The timing of when the collision starts is also important, as is the pose the fighter is in when they're likely to land a clean hit. This is the point where hit stop will occur. Players will get a clear view—and if it's a finishing blow, the screen will stop completely.

[01:52](https://youtu.be/rwwF_4blK-o?t=112) Weak attack poses are no good in these situations. That's why with sword swings, for example, collision doesn't start until the sword is already partway through the swing. When crafting attack animations, it's important that the animators are always aware of when and where collision occurs.

[02:14](https://youtu.be/rwwF_4blK-o?t=134) Strictly speaking, game designers are the ones making gameplay adjustments, so some animators may think this isn't their responsibility. But given how massive an impact animation can have on how a game feels, it's vital that everyone keeps the gameplay in mind as they work.
