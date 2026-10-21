# 046 · Making Your Game Easy to Tune

- **Category:** Programming & Tech
- **Video:** https://www.youtube.com/watch?v=nGaajB8m5Q0
- **Length:** 04:00
- **Source:** official English subtitles burned into the video, read by OCR (tools/ocr_subs.py). Expect rare OCR typos.

---

[00:03](https://youtu.be/nGaajB8m5Q0?t=3) Fine-tuning your game is a vital process. Though, if you're not accustomed to game development, it might be hard to visualize how exactly to go about balancing a game. I can't dig in too much since this involves some trade secrets, but I'd like to at least share some info to the extent that I'm able.

[00:22](https://youtu.be/nGaajB8m5Q0?t=22) I won't be able to show you any actual screens from our dev environment, so I apologize in advance if this feels a bit abstract.

[00:32](https://youtu.be/nGaajB8m5Q0?t=32) First, when the team is coding a game, I ask the programmers to reference a group of numerical values called “parameters." These represent all the values in the game we might want to fine-tune later on. Say we have a move with an attack power of 10.

[00:50](https://youtu.be/nGaajB8m5Q0?t=50) The code itself is what makes the move actually happen, but the value—10— is separated as a parameter, letting the designers easily adjust it later on. Of course, you could write the value 10 directly into the code and reach the same result, but you'd have to dive into the code every time you want to adjust that value— which can create some real problems.

[01:14](https://youtu.be/nGaajB8m5Q0?t=74) You could say the code is the bones, and the parameters are the muscles. Adjust the muscles to be bigger or move faster, and you can make the same bones behave in drastically different ways. Naturally, you want things to feel just right in the end.

[01:31](https://youtu.be/nGaajB8m5Q0?t=91) Parameters are maintained in their own separate Excel document, where you can fine-tune the game just by adjusting values. In Smash Bros., there are quite a few parameters to set just for a single attack, so we made it possible to hide parameters that are adjusted less frequently.

[01:51](https://youtu.be/nGaajB8m5Q0?t=111) This helps reduce human error and makes it easier to find the important values, so hiding the parameters you don't use often is an effective approach. Another advantage of using Excel is that the software makes it easy to integrate formulas. This way, parameters can refer to each other and keep things in relative balance.

[02:11](https://youtu.be/nGaajB8m5Q0?t=131) ...Which isn't too clear, is it? Well, this can let you do things like make one move always be 1/2 as strong as another, for example. By the way, if you want to reflect these parameters in the actual game, you need to perform a process known as "conversion."

[02:28](https://youtu.be/nGaajB8m5Q0?t=148) Though, other people may have different names for it. In short, just changing the Excel data doesn't actually do anything— you have to insert it into the build where it can be tested. We have an Excel add-in that handles this process, and just one button press will reflect the new parameters on all active dev kits.

[02:48](https://youtu.be/nGaajB8m5Q0?t=168) This is extremely useful! Having such a well-constructed development environment was one of the especially great parts of working with Bandai Namco Studios. For the original Smash Bros. and Smash Bros. Melee, just one of these conversions would take ten minutes to finish.

[03:06](https://youtu.be/nGaajB8m5Q0?t=186) Even the smallest tweak—ten minutes. You also had to reboot the game, and we weren't using Excel, so I had to tap away at text files to make each edit. In those days, it's fair to say I wrote every single parameter in the game myself.

[03:22](https://youtu.be/nGaajB8m5Q0?t=202) That was the only way to get it done. Nowadays—ever since Smash Bros. for Wii U/3DS— our parameters are maintained in a way that lets more people adjust them easily, so it's easy to experiment through trial and error and fine-tune more values to a deeper level.

[03:41](https://youtu.be/nGaajB8m5Q0?t=221) This is the area where you'll likely need to iterate the most, so make sure your team can do so as efficiently as possible.
