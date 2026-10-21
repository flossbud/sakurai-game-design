# 118 · Family BASIC

- **Category:** Programming & Tech
- **Video:** https://www.youtube.com/watch?v=89_FhHQ5n-g
- **Length:** 12:10
- **Source:** official English subtitles burned into the video, read by OCR (tools/ocr_subs.py). Expect rare OCR typos.

---

[00:03](https://youtu.be/89_FhHQ5n-g?t=3) The biggest driving factor behind my getting into the game industry was getting my hands on Family BASIC. I actually have it right here. This is Family BASIC.

[00:15](https://youtu.be/89_FhHQ5n-g?t=15) Looking at it now, the keyboard seems really small, doesn't it?

[00:21](https://youtu.be/89_FhHQ5n-g?t=21) It released in June of 1984. About a year after the Famicom released in Japan. Incredibly, by attaching this devicę to your Famicom, you could turn it into your own home computer. I repainted this white part of the unit myself.

[00:40](https://youtu.be/89_FhHQ5n-g?t=40) Gorgeous, right? Just like the actual Famicom console, the white part here tended to yellow over time. But I solved that problem. And here's the Family BASIC cartridge.

[00:51](https://youtu.be/89_FhHQ5n-g?t=51) It had its own onboard RAM, but only 2 kilobytes to store your program. That's about 0.002 megabytes. Type in just 2,000 characters, and you'll have filled up the whole thing. Even for the time, it was very small.

[01:07](https://youtu.be/89_FhHQ5n-g?t=67) But it had some really great capabilities that took advantage of the Famicom's strengths. I think I'll boot it up for the first time in a while. You want to see, right? I hope it works.

[01:21](https://youtu.be/89_FhHQ5n-g?t=81) Okay, I'm turning it on! Yes, it works! It's working! I'll start by pressing a button on the keyboard.

[01:32](https://youtu.be/89_FhHQ5n-g?t=92) “I am the Family Computer." Not “Family BASIC," huh. Right, it always starts out by asking you things like your name. But the keyboard!

[01:45](https://youtu.be/89_FhHQ5n-g?t=105) It really is small!

[01:52](https://youtu.be/89_FhHQ5n-g?t=112) My fingers are having trouble finding the right keys on this thing. “You are Masahiro Sakurai." Yep, that's me! I'm ready to begin!

[02:04](https://youtu.be/89_FhHQ5n-g?t=124) "Do you want to use GAME BASIC?" Hmm, there's a “Hello” button down here. What does that do, again? Only one way to find out.

[02:12](https://youtu.be/89_FhHQ5n-g?t=132) "Ah!" “Hello!" I'm great, thank you. It seems you're doing well, too, even after 30 years.

[02:23](https://youtu.be/89_FhHQ5n-g?t=143) You must have gotten a lot of sleep. “I am now following your instructions." I suppose so. Though, all I did was say hello.

[02:33](https://youtu.be/89_FhHQ5n-g?t=153) "Shall I tell your fortune?" Well.. It might take a while, so I'll pass. I want to hurry up and show everyone what BÀSIC can do.

[02:42](https://youtu.be/89_FhHQ5n-g?t=162) “No fortunes today." “Um.…. Um..." Um? Did you forget what we were doing?

[02:49](https://youtu.be/89_FhHQ5n-g?t=169) It's an ancient 6502, so I wouldn't be too surprised if it's getting forgetful. Oh, it remembered. That's not very computer-like, is it? I hope it doesn't go forgettinġ our program on us.

[03:01](https://youtu.be/89_FhHQ5n-g?t=181) I hope it doesn't go forgetting our program on us. Let's use GAME BASIC. Yes. "Understood!"

[03:10](https://youtu.be/89_FhHQ5n-g?t=190) "Commencing GAME BASIC..." How do I use this, again? Let's try "1." Ohhh, right. It's all coming back.

[03:19](https://youtu.be/89_FhHQ5n-g?t=199) I think “Hu-BASIC” is a version of BASIC that Hudson was involved with— and it has some pretty impressive capabilities. This is a custom version designed specifically for the Famicom, and it's especially notable for all of its sprite manağement features.

[03:36](https://youtu.be/89_FhHQ5n-g?t=216) Let's give it a try. Man, this keyboard is rough.

[03:49](https://youtu.be/89_FhHQ5n-g?t=229) And...done. The program is only six lines, but when we run it... this is what happens. I'd say this is an extremely simple program for Family BĀSIC, but the MOVE command is what's really impressive, with how easily it lets you move the character around.

[04:13](https://youtu.be/89_FhHQ5n-g?t=253) Let me explain what's happening. First, lines 10 and 20 turn on sprites and pick graphics— basic operations that will almost always show up in your code. Then we have FOR.

[04:27](https://youtu.be/89_FhHQ5n-g?t=267) This increments the N value from 0 to 7 as it loops until NEXT. This DEF MOVE command is where we define which character will be used for the MOVE command. Let's have it run again. This N says to move while the value is between 0 and 7.

[04:47](https://youtu.be/89_FhHQ5n-g?t=287) The 0 next to the SPRITE here means the sprite will be Mario. If we change it to a 1... the sprite changes to Pauline. Though, her colors aren't right.

[04:58](https://youtu.be/89_FhHQ5n-g?t=298) The N+1 here is what gives it a direction. In other words, in our loop from 0 to 7, we'll get directional vectors for 1, 2, 3, 4, 5, 6, 7, and 8. This number is the speed.

[05:11](https://youtu.be/89_FhHQ5n-g?t=311) This is the travel distance. What was this, again? Priority, maybe. Whether the background is in front of or behind the sprite.

[05:18](https://youtu.be/89_FhHQ5n-g?t=318) And I think this number sets the palette. If I change it to a 2... Oh, it gave Pauline the right colors. One highlight of Family BASIC is its wide array of easy-to-use character presets.

[05:35](https://youtu.be/89_FhHQ5n-g?t=335) It's really a great feature. To put it more clearly, if you had to code in all your own pixel art, just creating these characters would put you over the little program space available. But let's change it back to Mario and take a look.

[05:57](https://youtu.be/89_FhHQ5n-g?t=357) And make the palette 0. Oh, but palette 1 is Luigi's colors.

[06:05](https://youtu.be/89_FhHQ5n-g?t=365) There he is. These are his colors from the original Mario Bros. game. His face is yellow. The upward movement uses his animátion for climbing a ladder, diagonal is his jump, and sideways is his walk, giving us three different patterns.

[06:24](https://youtu.be/89_FhHQ5n-g?t=384) This level of freedom... Well, you can't say it's too high. It's actually pretty limited. But controlling the characters themselves like this is quite easy in fact, and that's where the greatness of Family BASIC really shines through.

[06:39](https://youtu.be/89_FhHQ5n-g?t=399) That said, the MOVE command may be simple to use, but it's a true challenge to use well. You're limited to these eight directions, for example. And i made your progra struggle a bit when responding to player input.

[06:58](https://youtu.be/89_FhHQ5n-g?t=418) On that note, I’ve put together a bit of code showing off something more practical than the MOVE command: the SPRITE command. I forgot soe of the commands, and I had to try really hard to remember them all, but I did the best I could— so apologies if it's a bit rough.

[07:17](https://youtu.be/89_FhHQ5n-g?t=437) This is what happens when I run it. You can actually control this sprite using a Famicom controller. It even has a little inertia. It's really incredible to have smooth-moving Famicom sprites that you can easily move around using just a regular Famicom controller.

[07:38](https://youtu.be/89_FhHQ5n-g?t=458) If you'd written code like this on a typical home computer at the time, you would have ended up with some very stilted movements. But here, the sprite could zoom around in any direction you wanted. It was really great.

[07:52](https://youtu.be/89_FhHQ5n-g?t=472) Thanks to this, I was able to teach myself about plenty of concepts like the inertia I'm showing off now, and it let me toy around and see how different changes might impact the feel of a game. I was able to draw on that knowledge and more during development on Kirby's Dream Land, so I really owe a lot to Family BASIC.

[08:19](https://youtu.be/89_FhHQ5n-g?t=499) You can draw backgrounds using a separate tool. Though, this is on the Famicom, so it's not the fanciest. This is the floor from Mario Bros. For all these things, you can change the palette...

[08:36](https://youtu.be/89_FhHQ5n-g?t=516) and put them where you want, just like that. This section seems to be all Mario Bros. assets. Like this. There's a wide variety, including objects like mountains.

[08:49](https://youtu.be/89_FhHQ5n-g?t=529) These white things may be hard to identify as they are now, but if I change the palette... It's reminiscent of Donkey Kong Jr. The platforms, specifically.

[09:01](https://youtu.be/89_FhHQ5n-g?t=541) Something like this?

[09:06](https://youtu.be/89_FhHQ5n-g?t=546) There. Incidentally, the Famicom had issues with something called “attributes." Like... Let's see. Is this an inkwell here? I’m not sure what it's from.

[09:18](https://youtu.be/89_FhHQ5n-g?t=558) If you place it down... As you can see, the ground underneath changes color, almost like it's frozen. Since the paļettes here are divided into 16x16 areas that have to share the same colors, the color of the ground changed to match that of the inkwell.

[09:40](https://youtu.be/89_FhHQ5n-g?t=580) If you wanted to place both objects using their correct colors, you may have to do something like shift them up a space.

[09:51](https://youtu.be/89_FhHQ5n-g?t=591) Wasn't that fascinating? By the way, there's another great thing about Family BASIC. It's here. On the back of the cartridge, there's a place to insert two AA batteries.

[10:05](https://youtu.be/89_FhHQ5n-g?t=605) In other words, battery backup. ...Sorry. I'm taking this footage by myself, so I can't zoom in closer. But I'll show you a close-up photo.

[10:20](https://youtu.be/89_FhHQ5n-g?t=620) Thanks to this, you çan actually save programs you've written. Though, the batteries drain quickly, and I don't remember it being all that reliable. But it is what it is. This part here is a sliding switch, which lets you toggle whether or not the batteries are supplying power.

[10:39](https://youtu.be/89_FhHQ5n-g?t=639) The more common way to save creations was to cassette tapes with the Data Recorder. I did some research, and apparently the first actual game to use battery backup was Dragon Slayer for the Super Cassette Vision, which released in February of 1986— so this was a fair bit before that.

[11:05](https://youtu.be/89_FhHQ5n-g?t=665) Back in the 1980s, I think a lot of people bought computers in hopes of breaking into the game industry. But that was far too expensive for a middle-schooler like me. A whole set sold for about 400,000 yen. But!

[11:21](https://youtu.be/89_FhHQ5n-g?t=681) Then Family BASIC came along offering to turn my Famicom into a computer, so I saved up six months of allowance so that I could buy it. If I'd never gotten my hands on Family BASIC, I never would have realized I could actually make games, and I wouldn't have ended up in the industry.

[11:39](https://youtu.be/89_FhHQ5n-g?t=699) That means Kirby and Super Smash Bros. wouldn't exist today. You never know what might come along and change your life. But the most important thing to do is to first sit down and try to make a game. I hope this channel can be just the impetus future game creators need to get started.
