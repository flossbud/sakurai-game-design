# 068 · Put Parameters in Brackets

- **Category:** Programming & Tech
- **Video:** https://www.youtube.com/watch?v=v6ozfbqNa54
- **Length:** 05:03
- **Source:** official English subtitles burned into the video, read by OCR (tools/ocr_subs.py). Expect rare OCR typos.

---

[00:03](https://youtu.be/v6ozfbqNa54?t=3) I'd like to start today by reiterating a point from the previous video in this category. A game's code and its parameters are two separate things.

[00:13](https://youtu.be/v6ozfbqNa54?t=13) If the commands and formulas that enable character movement are the code, then numeriçal values like movement speed and attack power are the parameters. The code is an instruction manual for the various commands in a game. The parameters are the numbers used to flesh out those commands.

[00:30](https://youtu.be/v6ozfbqNa54?t=30) Last time, I discussed parameters that are shared by all characters—stats such as general attack power. In this video, I'd like to focus more on topics like character-specific movements and special actions— parameters that are based on what's unique to each character's spec sheet. I should start by explaining the workflow we use when creating games as a team.

[00:56](https://youtu.be/v6ozfbqNa54?t=56) First, the director or game designer's ideas are turned into spec sheets by a planner. Think of these like blueprints. A programer then implements code according to those spec sheets, Aacongthoseshts which allows the character to function in the build.*are els aed simatitels.

[01:12](https://youtu.be/v6ozfbqNa54?t=72) The baton is then passed back to the planner, who fine-tunes the parameters. Assuming there are no bugs, the programmer's job ends here— but the parameters will continue to be tweaked to the very end for game balance purposes. Now, then.

[01:28](https://youtu.be/v6ozfbqNa54?t=88) We certainly could write all those parameters directly into the game code. Values like walking speed or movement speed, for example, or the movement speed of special moves. All those could be written into the code, and the game would still work just fine.

[01:45](https://youtu.be/v6ozfbqNa54?t=105) However, that would mean every adjustment we make would have to be handled by the programmer— so instead, we generally make it so that parameters like those various speeds can be tweaked externally. In other words, we create a reference table separate from the code, which the planner can adjust at any point.

[02:02](https://youtu.be/v6ozfbqNa54?t=122) But we already covered that last time. Now, let's discuss spec sheets. To make sure they're implemented correctly, it's vital that we state which parts should be separated as parameters, and communicate that very clearly to the programming team.

[02:17](https://youtu.be/v6ozfbqNa54?t=137) Additionally, the meaning of each parameter should be crystal clear, no matter who's looking at it. Usually, multiple people will be tuning them later on, after all. There are various ways to handle this depending on your project, but there are three methods I’ve arrived at myself over the years.

[02:34](https://youtu.be/v6ozfbqNa54?t=154) but there are three methods I've arrived at myself over the years. Number one: write parameter info on your spec sheet in plain language. Number two: enclose parameters in brackets. Number three: Denote numerical values with a O.

[02:53](https://youtu.be/v6ozfbqNa54?t=173) Here's an example of how I'd write one of these in a spec sheet. “Initiate movement at [Special startup X-velocity is O]." “At the same time, decelerate by [Special X-deceleration is O/frame]." That's a general example, but were you able to visualize how the character dashes horizontally, and decelerates at the same time?

[03:22](https://youtu.be/v6ozfbqNa54?t=202) That bracketed notation is exactly how it shows up in my spec sheets. I established a rule that anything inside brackets is turned into a parameter. And the values adjusted by those parameters are denoted with O. Separate from the spec sheets, we also make a file that's just a list of all these parameters— the text written inside the brackets with the value shown next to it.

[03:48](https://youtu.be/v6ozfbqNa54?t=228) Fine-tuning the game is as simple as adjusting these values. If you've never worked with parameters, you may be wondering what the point of all this is. I suspect most people will just write "X-velocity" or “X-deceleration" and express their parameters through those names alone.

[04:07](https://youtu.be/v6ozfbqNa54?t=247) I used to do the same thing myself. However, by using plain language to write out your parameters and making it clear what values you'd like to fine-tune, it's possible to make the process a bit simpler and easier to understand.

[04:22](https://youtu.be/v6ozfbqNa54?t=262) I should mention, this notation is most effective when you need to write unique specs. It doesn't work as well for the kinds of parameters I discussed last time— ones like general attack power, which are used across the entire game.

[04:35](https://youtu.be/v6ozfbqNa54?t=275) I wasn't sure how teams on other projects handled this, but I thought of this method to let us tune parameters with no room for misinterpretation— because just as with spec sheets, you won't get far with your tuning if you can't explain things clearly. And who knows, there may be even better ways out there for tackling this sort of thing.
