# 189 · Randomness Spices Games Up

- **Category:** Design Specifics
- **Video:** https://www.youtube.com/watch?v=e9v_FwUGOwY
- **Length:** 03:54
- **Source:** official English subtitles burned into the video, read by OCR (tools/ocr_subs.py). Expect rare OCR typos.

---

[00:04](https://youtu.be/e9v_FwUGOwY?t=4) "Randomness," or the arbitrary determination of certain elements, can spice up a game if you use it effectively.

[00:13](https://youtu.be/e9v_FwUGOwY?t=13) Let's start by talking about the upside. Games are all about repeating the same content over and over again, and randomness makes it harder for players to get bored. It can be a challenge for a game with static rules to deliver play variety.

[00:28](https://youtu.be/e9v_FwUGOwY?t=28) But add a bit of randomness, and things will play out differently each time— keeping the experience fresh and boosting the fun. Rather than offering fixed results, changing up probabilities can add some flavor to player strategy.

[00:44](https://youtu.be/e9v_FwUGOwY?t=44) At first glance, randomly-decided elements might feel like they detract from strategy, but it's actually the opposite, since you're giving players the challenge of handling a range of situations. Having said that, I'm sure there are plenty of times when randomness doesn't feel great. That brings us to the downside.

[01:03](https://youtu.be/e9v_FwUGOwY?t=63) To start, you could say it's not really fair. When you're not fighting on equal footing— and luck ultimately determines the outcome— it's naturally possible that all of your hard work will come to nothing. If a player only loses because they were unlucky, they might have trouble accepting the outcome.

[01:22](https://youtu.be/e9v_FwUGOwY?t=82) In a game, players need to feel to some extent like they're responsible for their own failure. Some games like RPGs treat “luck" as a stat you can increase to boost your characters' strength. There's a lengthy history to this, but it goes at least as far back as 1981 and its implementation in Wizardry.

[01:41](https://youtu.be/e9v_FwUGOwY?t=101) This can make randomness a little easier to accept, but players often forget about it, since it's not a top priority as far as stats go. Or maybe they're reluctant to put precious resources into a vague luck stat. Randomness is also not a great fit for things like sports or strict competitions.

[02:04](https://youtu.be/e9v_FwUGOwY?t=124) If you want a contest to be decided by the skill of the competitors alone, you'll be more inclined to keep random elements out of your game. In recent years, we've started phasing randomness out of Smash Bros. fighters in no small amount. While Peach's Smash Attack used to give you a random result, you çan now change it by pressing either up or down.

[02:25](https://youtu.be/e9v_FwUGOwY?t=145) However, the Hero's command list is randomized each time you open it. This, we decided, was okay to include. Even if the commands you get are random to an extent, you still need to have the skill to properly use each command.

[02:41](https://youtu.be/e9v_FwUGOwY?t=161) Additionally, items still include a marked degree of randomness, even now. This shakes up the playing field and gives anyone a chance to come back, no matter their skill level. Of course, advanced players do make better use of items than beginners, but that's still preferable to deciding matches purely by skill.

[03:03](https://youtu.be/e9v_FwUGOwY?t=183) At its core, the series is less about winning and more about having fun and moving on to the next match, so I think this direction is the right fit.

[03:15](https://youtu.be/e9v_FwUGOwY?t=195) By the way, I have one word of caution regarding randomness. Computers can only do things in a predetermined way, so they're not strictly capable of producing true randomness. In some cases, players can reset the game or perform certain actions to always get the results they want.

[03:35](https://youtu.be/e9v_FwUGOwY?t=215) To prevent such issues, it's a good idea to reference an indefinite value such as the system's internal clock, and factor that in when generating random values.
