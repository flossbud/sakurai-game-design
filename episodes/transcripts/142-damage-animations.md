# 142 · Damage Animations

- **Category:** Animation
- **Video:** https://www.youtube.com/watch?v=0xHE3ypX96U
- **Length:** 04:11
- **Source:** official English subtitles burned into the video, read by OCR (tools/ocr_subs.py). Expect rare OCR typos.

---

[00:03](https://youtu.be/0xHE3ypX96U?t=3) Today, I'd like to talk about the animations that occur when characters take damage.

[00:12](https://youtu.be/0xHE3ypX96U?t=12) In the case of Super Smash Bros., the moment a character takes damage, they quickly change to a pained-looking pose. This first frame of the damage animation has hit stop applied to it, so it's easy to see. As such, it's vital that this pose really expresses the pain.

[00:33](https://youtu.be/0xHE3ypX96U?t=33) The damage pose and standby pose can be quite similar in some games, but we like to go for something more extreme that's nothing like the standby pose. This way, you can clearly tell the character got hit, even from far away.

[00:49](https://youtu.be/0xHE3ypX96U?t=49) However, we don't jump to the damage animation instantly. Using interpolation, we transition from the pose at the time of impact to the first frame of the damage animation. Just a quick segue.

[01:05](https://youtu.be/0xHE3ypX96U?t=65) I touch on this a little bit in my Design Specifics video on hit stop.

[01:13](https://youtu.be/0xHE3ypX96U?t=73) Characters always enter damage poses when hit, no matter the situation, so if your opponent's hitbox is lengthened, they might enter that damage pose at quite a distance. While there are merits to applying hit stop on the extended hitbox frame, we instead opt to emphasize the sense of impact.

[01:34](https://youtu.be/0xHE3ypX96U?t=94) But we encountered a problem with this. When hitting a fighter with a neutral attack... Depending o their stance, they might move backwards, causing the rest of your combo to miss. In this case, it was an issue with the top node position of the attacked fighter— a problem that can arise whenever you change a character's stance.

[02:02](https://youtu.be/0xHE3ypX96U?t=122) Damage reactions in Smash Bros, can be divided into high, middle, and low, and are chosen based on which is closest to the point of impact. Additionally, reactions on the ground can have three strengths: small, medium, and large. Multiply it all out and you end up with nine possible reaction types.

[02:27](https://youtu.be/0xHE3ypX96U?t=147) Getting knocked back comes with its own separate set of variations.

[02:40](https://youtu.be/0xHE3ypX96U?t=160) Compared to other fighting games which feature mostly humanoid characters, Smash Bros. has a wide array of uniquely-shaped fighters. Even the humanoid characters can be sword wielders, shield wielders, or other weapon wielders— so there's lots of variation.

[02:56](https://youtu.be/0xHE3ypX96U?t=176) If everyone had standard human proportions, we could have repurposed animations across fighters, but we don't have that luxury. Adding even one fighter ends up being quite a lot of work.

[03:12](https://youtu.be/0xHE3ypX96U?t=192) For all our damage animations, we emphasize breaking a character's symmetry and making their silhouette clearly legible. Take knockback for example. By twisting a character's body, we can make the silhouette of their arms and legs read clearly— something that wouldn't be possible if we just sent them flying sideways.

[03:30](https://youtu.be/0xHE3ypX96U?t=210) We carefully craft every detail of these animations to make sure both players feel the impact of the attack.

[03:40](https://youtu.be/0xHE3ypX96U?t=220) As a small aside. This is how I drew Kirby's damage pose in the design document for Kirby Super Star. This is actually a recreation based on how I remember doing it, but it shows how moments of extremity can work great in situations like these.

[03:58](https://youtu.be/0xHE3ypX96U?t=238) The more punch, the better.
