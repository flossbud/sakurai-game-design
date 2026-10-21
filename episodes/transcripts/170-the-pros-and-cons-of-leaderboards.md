# 170 · The Pros and Cons of Leaderboards

- **Category:** Game Essence
- **Video:** https://www.youtube.com/watch?v=g7nC6NtTMIk
- **Length:** 03:15
- **Source:** official English subtitles burned into the video, read by OCR (tools/ocr_subs.py). Expect rare OCR typos.

---

[00:04](https://youtu.be/g7nC6NtTMIk?t=4) Online leaderboards— they have their positives and their negatives, right?

[00:13](https://youtu.be/g7nC6NtTMIk?t=13) One clear positive is that they give players a sense of purpose. Without a leaderboard, you're just fighting—and there's little thrill to that. It's vital that the result of your hard work is linked to an incentive to aim even higher. Another positive: With matchmaking, leaderboards can help connect players of roughly the same skill level.

[00:33](https://youtu.be/g7nC6NtTMIk?t=33) Though, the odds of matching with someone at your skill level who's close enough for stable connection speeds and who's playing at the same time as you are generally very slim. In particular, you need to take areas with low populations into account.

[00:51](https://youtu.be/g7nC6NtTMIk?t=51) If the matching range is too narrow, players will never find a match, but if it's too broad, players will match with people far outside their skill level. This is a really difficult balance to strike. One negative of leaderboards— if I can exaggerate for a second— is that they can be a source of eternal humiliation.

[01:10](https://youtu.be/g7nC6NtTMIk?t=70) If you aren't number one, then you aren't reaching your goal— in other words, you're continually losing. That does come down to attitude, though, since you could also say you're continually winning. Still, leaderboards aren't great at making you feel successful.

[01:27](https://youtu.be/g7nC6NtTMIk?t=87) When you try your hardest and only reach 400th place... or 10,000th place, that can really sap your motivation. To try and mitigate that, we implemented a system called Global Smash Power (GSP) into Smash Bros.

[01:42](https://youtu.be/g7nC6NtTMIk?t=102) It's an inverse ranking syste that uses maximum global player count as the denominator, and quantifies how powerful a given player is within that larger group. In other words, unlike a leaderboard where the lower number is better, this system says that the higher number is better.

[01:59](https://youtu.be/g7nC6NtTMIk?t=119) Frankly, it doesn't always function as well as I had hoped, but I still think it's a good bit better than ordinary leaderboards. Smash Bros. in particular has a lot of people who play it, so the parameter is big too.

[02:13](https://youtu.be/g7nC6NtTMIk?t=133) Nobody would be happy being told they're in x-millionth place, right? This also lets us obscure who the top player in the world is. That's just not helpful information for anyone outside the very elite. Players will just see how far away they are and want to give up.

[02:28](https://youtu.be/g7nC6NtTMIk?t=148) There's also a chance people might use cheats or upload invalid data, and this system lets us naturally exclude that data. In addition to all that, we created a mode called Elite Smash. It gives people the satisfaction of knowing they're a chosen elite, and by pitting these players against each other, it lets us prevent them from matching with lower-ranked players.

[02:54](https://youtu.be/g7nC6NtTMIk?t=174) When it comes to how leaderboards should work, this should provide some useful reference. The obvious choice isn't always the right one, so try to think outside the box and consider methods beyond a standard leaderboard system.
