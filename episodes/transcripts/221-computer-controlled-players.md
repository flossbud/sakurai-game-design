# 221 · Computer-Controlled Players

- **Category:** Planning & Game Design
- **Video:** https://www.youtube.com/watch?v=uleauI0IwZM
- **Length:** 05:06
- **Source:** official English subtitles burned into the video, read by OCR (tools/ocr_subs.py). Expect rare OCR typos.

---

[00:03](https://youtu.be/uleauI0IwZM?t=3) Let's look at the "attract modes" for some older games— by which I mean the gameplay demos that play when you don't start the game. This should be fun!

[00:33](https://youtu.be/uleauI0IwZM?t=33) Hmm... I'd guess the computer is just moving the character around at random, and it's not going great. When the computer is in control of a playable character, we often label it CP or CPU.

[00:44](https://youtu.be/uleauI0IwZM?t=44) As it turns out, humans and computers are quite different. The more freedom a game offers, the harder it is to make CPU players that can play it, and on top of that, if they react faster than a human can, it can feel extremely unfair to players.

[01:23](https://youtu.be/uleauI0IwZM?t=83) In board games or card games, if the computer manages to get a good roll on a dice throw, people will tend to think it's cheating.

[01:34](https://youtu.be/uleauI0IwZM?t=94) Though, there's not much you can do about that. The computer's controlling both, after all. Even when it does things a human can do, people still often think it's unfair. This will depend greatly on your game's content and genre, but for a game like Smash Bros., making computer player Al is extremely difficult.

[01:57](https://youtu.be/uleauI0IwZM?t=117) Still, it's a hassle you just have to deal with for players who want to play competitive games solo. On my projects, I tend to be more hands-off with this task, comparatively speaking. Though I do supervise, of course. Now, let's talk about how to make a CPU player for an action game.

[02:20](https://youtu.be/uleauI0IwZM?t=140) The computer doesn't have eyes, so it uses information from various categories. It decides what to do based on its opponent's positioning and status. The character's regular and special attack ranges— as well as its movement range—are converted to data, or pulled from the original data, then stored in the form of reach and attack-timing details.

[02:41](https://youtu.be/uleauI0IwZM?t=161) Similarly, the computer needs to reference the attack data of the opposing character. With all this data, it then decides what to do.

[02:54](https://youtu.be/uleauI0IwZM?t=174) Depending on a game's flow, the computer may change to a different type of logic or behavior partway through. It may get angry at lower HP, for example. It may be set to maintain the character's optimu distance, or to take into account speed and jump height.

[03:10](https://youtu.be/uleauI0IwZM?t=190) Some games might even make the CPU player go easy on you if they're winning too much. As such, when contradictions arise in the differing logic types, the computer player may not act properly. Like when two potential choices contradict each other. This grows more common as you add more complex mechanics and more criteria to track.

[03:31](https://youtu.be/uleauI0IwZM?t=211) When it comes to Smash Bros. Ultimate, we gave CPU players a sort of "reflex," meaning they can't react instantaneously. And if their directional controls are reversed, they will even get somewhat confused. Though, just like with real players, it's rare that they won't adjust to the change.

[03:52](https://youtu.be/uleauI0IwZM?t=232) They won't just keep going in the wrong direction and fail off, for example. Compared to past titles, we adjusted the CPU players in Smash Bros. Uitimate to take a more aggressive approach. In other words, they're not great at defense or evasion, or against players who sit back and wait.

[04:14](https://youtu.be/uleauI0IwZM?t=254) Players who choose a high CPU level want to fight against powerful opponents. If those CPU players just waited around or displayed machine-like reflexes, that wouldn't be very fun— so we prioritized offense and tried to give the ĊPUs the ability to fight and win.

[04:38](https://youtu.be/uleauI0IwZM?t=278) As an extreme example, if the CPUs always used perfect shields or dodged every attack, we could make them essentially invincible.

[04:47](https://youtu.be/uleauI0IwZM?t=287) But that wouldn't be any fun at all, now would it? In the end, it's important to remember that our goal is to make things as fun as possible.
