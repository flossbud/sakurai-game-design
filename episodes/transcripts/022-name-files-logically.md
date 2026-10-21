# 022 · Name Files Logically

- **Category:** Programming & Tech
- **Video:** https://www.youtube.com/watch?v=XMzR5mJHPDg
- **Length:** 04:52
- **Source:** official English subtitles burned into the video, read by OCR (tools/ocr_subs.py). Expect rare OCR typos.

---

[00:04](https://youtu.be/XMzR5mJHPDg?t=4) In the Programming & Tech category of videos, I'll be covering technical subjects that involve direct interfacing with computers. Though, there's only so much I'll be able to talk about. On the whole, I don't think this category will have too many videos.

[00:21](https://youtu.be/XMzR5mJHPDg?t=21) It's easy to stray into confidential territory, and depending on your dev environment, team size, and target hardware, the details of what you're doing could be drastically different. So while there are plenty of tricks of the trade, I'll be sticking to broad overviews that won't cause any problems.

[00:41](https://youtu.be/XMzR5mJHPDg?t=41) Let's get started.

[00:46](https://youtu.be/XMzR5mJHPDg?t=46) In Smash Bros., this is known as an “Up Special." But you might hear me accidentally flipping it and saying “Special Up” instead. Now why is that? Well, the name we use internally is "Special Move (Up)," believe it or not.

[01:02](https://youtu.be/XMzR5mJHPDg?t=62) That's true across the whole development team. There's a logical reason for that, so allow me to explain. First, every action in the game has a corresponding class of file name. Youcould also call these "labels."

[01:17](https://youtu.be/XMzR5mJHPDg?t=77) We decided the naming scheme when making the first Smash Bros., and still use it today. Let's start with A Button standard attacks, which we refer to as “Attack” in file names. These are your regular punches and kicks.

[01:33](https://youtu.be/XMzR5mJHPDg?t=93) Conversely, special moves that use the B Button are labeled “Special." Things like the Fireball or the Super Jump Punch. So for example, a neutral attack is named "Attack1." A smash attack is named “Attack4."

[01:49](https://youtu.be/XMzR5mJHPDg?t=109) That's how we distinguish them. With a neutral attack combo, we use increasing numerals to note order, like "Attack11," "Attack12," "Attack13”. For tilt attacks, smash attacks, and special moves, directional input matters.

[02:07](https://youtu.be/XMzR5mJHPDg?t=127) A centered stick is “N,” or neutral. Up is "Hi," side is "S" and down is “Lw.” Following these rules, a side smash attack would be labeled “AttackS4."

[02:22](https://youtu.be/XMzR5mJHPDg?t=142) On that note, we add “Air" to designate aerial moves. A forward aerial attack would be “AttackAirF." One big advantage of this is that anyone can look at a file name and know what move it's for, but another huge point in its favor is that everything stays niċe and neat when sorted.

[02:42](https://youtu.be/XMzR5mJHPDg?t=162) "Attack” moves stay together, and they're ordered by strength from neutral to tilt to smash attacks. Since special moves start with “Special," they become their own category that's easy to distinguish from the rest.

[02:56](https://youtu.be/XMzR5mJHPDg?t=176) If we called them “SAttack” or “HiAttack," with the direction coming first... It would just make a huge mess when you sorted them all. Using anything but numbers for strength is a problem for the same reason. The “SpecialHi” label, put back into English, could be viewed as "Special Move (Up)."

[03:16](https://youtu.be/XMzR5mJHPDg?t=196) And that's how it is. That might raise a question, though: why do we call it an “Up Special" in-game? That might raise a question, though: why do we call it an "Up Special" in-game? That's because from the player's perspective, the directional input comes first.

[03:31](https://youtu.be/XMzR5mJHPDg?t=211) You tilt the stick up, then press the special-move button to do an Up Special. The name matches how you perform the move. And thus, even though it's a bit confusing, the names differ internally versus in-game. I might accidentally use the wrong name sometimes, but I hope you'll forgive me for that.

[03:54](https://youtu.be/XMzR5mJHPDg?t=234) Keep your development file names and labels concise and easy to understand! Someone looking at them for the first time should know at a glance just what they're for. If they're too short, they'll be easy to type but hard to understand— so I suggest finding an appropriate balance.

[04:12](https://youtu.be/XMzR5mJHPDg?t=252) There's one last thing I’d like to mention! For Japanese developers, try to avoid using romanized Japanese in your file names. Especially on bigger projects, you'll end up making it harder for people who don't speak the language.

[04:29](https://youtu.be/XMzR5mJHPDg?t=269) Overseas teams that join the project later might not be able to make sense of it. I warn my team of this often, but it still happens a fair amount. Remember: it's not just you who needs to understand your game.
