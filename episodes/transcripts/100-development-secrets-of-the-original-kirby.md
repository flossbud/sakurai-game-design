# 100 · Development Secrets of the Original Kirby

- **Category:** Grab Bag
- **Video:** https://www.youtube.com/watch?v=ZUY2AtBD6Sk
- **Length:** 17:23
- **Source:** official English subtitles burned into the video, read by OCR (tools/ocr_subs.py). Expect rare OCR typos.

---

[00:12](https://youtu.be/ZUY2AtBD6Sk?t=12) In 2017, an orchestral concert was held to celebrate Kirby's 25th anniversary. For the event, I prepared some secret dev stories from the first Kirby game to present on stage— and it just so happens I still have them. In this video, as a special treat, I'll be sharing that very presentation once again.

[00:36](https://youtu.be/ZUY2AtBD6Sk?t=36) I've already discussed the early Kirby titles in my Game Concepts category of videos, but today I have even more in-depth information to share with you. I'm even throwing in a bonus secret about Meta Knight which I only included in the Osaka performance. This will be a bit longer than usual, but please bear with me.

[00:58](https://youtu.be/ZUY2AtBD6Sk?t=58) Now, let's get right into development secrets of the original Kirby. The material is dense, but I'll try to keep things brisk. Kirby first appeared in Kirby's Dream Land, released in 1992 for the Game Boy. Kirby is a mysterious creature who can inhale and spit out enemies, and fly.

[01:16](https://youtu.be/ZUY2AtBD6Sk?t=76) I didn't think of copy abilities until the next title, Kirby's Adventure, so he didn't have any yet. I came up with the game's concept around May of 1990, when I was just 19. My goal was to show newcomers to games how much fun they can be. It took just under a year to develop.

[01:32](https://youtu.be/ZUY2AtBD6Sk?t=92) The game is quite short, and experienced players can finish it in 20 minutes. But don't write it off just yet. The game has sold over 5 million copies worldwide. At the time, it commanded a lead atop the Game Boy's best-sellers list for several months.

[01:51](https://youtu.be/ZUY2AtBD6Sk?t=111) The hardware used to develop the game was extremely powerful. I don't know anything else like it. And that would be...this. The Twin Famicom.

[02:05](https://youtu.be/ZUY2AtBD6Sk?t=125) We hooked up a trackball we made at Hal Laboratory, loaded up our dev tool from a disk, and used that to develop the game. It was a highly functional setup I’ve never seen elsewhere. I really loved it.

[02:17](https://youtu.be/ZUY2AtBD6Sk?t=137) And it seems it was just blessed by a cat, too. Next, let's look at some actual footage from the dev tool. I had to record it with a composite cable, so it might be a bit rough. First, it let us draw pixel art.

[02:34](https://youtu.be/ZUY2AtBD6Sk?t=154) And combine that art to create characters. And move them around however we wanted. Meta Knight wasn't in the first game, but here he is from Kirby's Adventure. This is how we did things like test out animations.

[02:48](https://youtu.be/ZUY2AtBD6Sk?t=168) Here's the Level 5 boss from Kirby's Adventure—Heavy Mole. We could do all this with just a Famicom. We could even make backgrounds. It was even used to make the title screen, so you can see how multipurpose this dev tool really was.

[03:04](https://youtu.be/ZUY2AtBD6Sk?t=184) so you can see how ultipurpose this dev tool really was. While coming up with the concept for Kirby, I used this tool to visualize how the game might look in motion. Kirby's pixel art stayed roughly the same from this point to the final release.

[03:16](https://youtu.be/ZUY2AtBD6Sk?t=196) If I can change the subject, I’d like to talk a bit now about ROM size. The size we were initially targeting was 512 kilobits. Things changed, and the fina! game ended up being 2 megabits, but it was largely designed for 512 kilobits.

[03:34](https://youtu.be/ZUY2AtBD6Sk?t=214) I can hear you saying, "What's all that supposed to mean?" 512 kilobits is equal to 64 kilobytes. Which equals 0.064 megabytes. Which has even more zeros in gigabytes.

[03:47](https://youtu.be/ZUY2AtBD6Sk?t=227) If you want to compare that size to a certain hard-hitting Nintendo title... It would look like this. Not sure why I'm comparing them, though. Anyway, the game is small.

[04:00](https://youtu.be/ZUY2AtBD6Sk?t=240) Smaller than any of the images used in this presentation, other than some GIFs. Keep that in mind while we move on to this next part. Do you know the names of these characters? They're Waddle Dee and Waddle Doo.

[04:16](https://youtu.be/ZUY2AtBD6Sk?t=256) The “waddle” part refers to the unsteady way ducks and penguins walk. If the names are too similar to keep straight, remember this: The one with the round, eye-shaped letters is the one that has the big eyeball. Sounds like a strategy to study for school.

[04:34](https://youtu.be/ZUY2AtBD6Sk?t=274) Now, why are these two characters so similar? Are they siblings? Cousins? No.

[04:41](https://youtu.be/ZUY2AtBD6Sk?t=281) To be blunt, I wanted to make two characters using the ROM space of only 1.5. This is what I mean. By reusing the back half of the character, I was abīe to cut down on ROM space. This is Gordo.

[04:58](https://youtu.be/ZUY2AtBD6Sk?t=298) This is all the art I needed to make. By flipping the image back and forth vertically and mirroring the entire thing horizontally, it looks like Gordo is moving. Even with Poppy Bros. Sr., who has a lot of art for an enemy, if you look close, you'll see he only has three leg patterns.

[05:15](https://youtu.be/ZUY2AtBD6Sk?t=315) And two head patterns. I used a lot of tricks to make appealing animations with a small footprint. Still, despite not having much space, I wanted the bosses to be big. Kirby was a game made for newcomers, so even attacks that are slightly off-target should still hit.

[05:33](https://youtu.be/ZUY2AtBD6Sk?t=333) What I drew was this. Do you know what it is? Let's mirror it vertically. And put down three of them.

[05:43](https://youtu.be/ZUY2AtBD6Sk?t=343) Stick that image to the background, and you've got Whispy Woods. This design came about because the game's limitations necessitated it. Here's another recurring character, Kracko. The body is made by flipping pieces on both axes, and the eyeball is a single pattern that's also reused for Kracko Jr.

[06:03](https://youtu.be/ZUY2AtBD6Sk?t=363) As you can see, fitting these characters into limited ROM space was a vital process. Let's delve a bit deeper. Here's a sprite set from that dev tool I showed you earlier. Charaçters are made by combining these chopped-up pieces of pixel art.

[06:19](https://youtu.be/ZUY2AtBD6Sk?t=379) If it were divided into 8x8 pieces, as NES game sprites often were, I could have utilized these gaps, too. But the original Kirby used 8x16 pieces, which were a bit more unwieldy. That meant I had to leave those gaps blank.

[06:36](https://youtu.be/ZUY2AtBD6Sk?t=396) Seriously?! We had very limited space, and this spec held the characters back even further. With that in mind, let's look at how Green Greens, also known as Stage 1, is structured. This 256x256 pixel image contains all the characters used in Stage 1.

[06:56](https://youtu.be/ZUY2AtBD6Sk?t=416) Kirby takes up this part. This contains all the actions Kirby can do outside of the level transitions. It's tiny. This section is what you might call "permanent fixtures."

[07:07](https://youtu.be/ZUY2AtBD6Sk?t=427) Elements that stay unchanged throughout the game. The Maxim Tomato got its “M” because it's easy to make with a horizontal flip. That leaves the last section, which are parts specific to the stage. This includes Grizzo, who is the only large-scale enemy in the first Kirby, so the gaps stand out a bit more.

[07:26](https://youtu.be/ZUY2AtBD6Sk?t=446) Here's the pixel art for the background. If you combine it all just right... you end up with this. Not only were we limited to half the usable area of an NES game, we also couldn't mirror the art horizontally.

[07:38](https://youtu.be/ZUY2AtBD6Sk?t=458) We did our best, though, and I'd say it turned out nice in the end— but what do you think? While we're at it, here's King Dedede. No other enemies appear while he's on-screen, so his art is the most lavish.

[07:52](https://youtu.be/ZUY2AtBD6Sk?t=472) By the way, I drew almost all the art that l’ve shown you so far. Kirby, Dedede, Waddle Dee, enemies, backgrounds, items, and effects. There was another designer also involved in the game's other stages. Back in the day, many people drew their art on graph paper first, but I started directly with the pixels.

[08:16](https://youtu.be/ZUY2AtBD6Sk?t=496) Next, I'd like to talk about some secrets of enemy movement. This hermit crab, Coner, might just be the first enemy I drew. It crawls on the ground, falls off the cliff, then slows down in water. Just like you'd expect.

[08:29](https://youtu.be/ZUY2AtBD6Sk?t=509) And Waddle Dees will fall down when they step over a ledge. Also like you'd expect. But in the original Kirby, these “natural” things didn't occur naturally. The truth is...

[08:40](https://youtu.be/ZUY2AtBD6Sk?t=520) The enemies have no terrain collision. To explain what I mean... let's look at the Coner again. It's named for its cone shape.

[08:51](https://youtu.be/ZUY2AtBD6Sk?t=531) This is how it moves, like I described. But it doesn't check for terrain collision. Instead, I made its movement patterns separately, then lined them up with the background. What a wasteful way to do it!

[09:05](https://youtu.be/ZUY2AtBD6Sk?t=545) I used the dev tool from earlier to input the poses and movements. The area in this rectangle is what controls the movements. Let's take a closer look. The part inside this square shows the way Poppy Bros. Sr. steps left and right.

[09:23](https://youtu.be/ZUY2AtBD6Sk?t=563) If we move down a little, you can see how I entered the values. There was only the trackball— no keyboard or anything— so we had to use the cursor to enter the hexadecimal values. This fiddly setup is how I made movements to mimic the terrain, then positioned those movements down to the pixel.

[09:41](https://youtu.be/ZUY2AtBD6Sk?t=581) Nowadays, people would complain about how inefficient it was, but I was just starting out at the time, so I assumed it was par for the course and enjoyed fine-tuning all the details. Not to mention, this method did have its merits.

[09:55](https://youtu.be/ZUY2AtBD6Sk?t=595) Mainly, it was light on processing power. This was an invaluable benefit when working with the Game Boy. One of the series' regulars is a character called Čappy. It gets its name from its cap, of course.

[10:08](https://youtu.be/ZUY2AtBD6Sk?t=608) It also doesn't check for terrain collision. The nice animation certainly helps, but it wouldn't have turned out this bouncy and fun if it had a heavy processing load." Next, I'd like to talk about a surprising overlap with another game you might have heard of.

[10:24](https://youtu.be/ZUY2AtBD6Sk?t=624) This is my design document for the first Kirby. Kirby was already the character you know by this point. But I drew the pixel art first, while these illustrations came later. There's one part of this document that's especially interesting.

[10:38](https://youtu.be/ZUY2AtBD6Sk?t=638) It's a bit hard to read, so let's zoom in. “Normally, the screen scrolls with your character at the center." I used an old word for “character." * In Japanese. “However, if you get hit by an enemy and are sent flying, the screen will stop scrolling."

[10:55](https://youtu.be/ZUY2AtBD6Sk?t=655) "Once you settle, the screen will gently scrolí over and recenter upon you." Hm? This sounds familiar. "If you get sent flying fully off-screen, you'll lose a life." Wait... Can it be?

[11:10](https://youtu.be/ZUY2AtBD6Sk?t=670) Yes—these are the same rules as Super Smash Bros.! I'd already thought up Smash's damage accrual system when I was making the original Kirby game! That's a jaw-dropping fact, I'd say. The concept also states that the distance you're sent flying depends on your health value.

[11:28](https://youtu.be/ZUY2AtBD6Sk?t=688) That's exactly like in Smash. It turns out I thought this up in 1990 while working on the first Kirby— pretty incredible, right? It sounds like I'm making it up, but this design document provès it.

[11:43](https://youtu.be/ZUY2AtBD6Sk?t=703) It also raises a question. Why did I put one of my old ideas in Smash Bros.? The answer is... I had forgotten about it. Totally and completely.

[11:54](https://youtu.be/ZUY2AtBD6Sk?t=714) Last up. We've learned to expect this nowadays since the Kirby series is well-established, but especially when the first game came out, Kirby and the world of Dream Land were full of mystery. For example.

[12:07](https://youtu.be/ZUY2AtBD6Sk?t=727) What's this thing on the screen here? It's just kind of there, but what is it? I'm not sure who came up with it, but they're sometimes called “bourbons." Despite its short run-time, the original Kirby is chock-full of imagery you didn't see in usual games.

[12:22](https://youtu.be/ZUY2AtBD6Sk?t=742) Such as, why does he split into three when you beat a level? Multiple Kirbys are constantly showing up, but you don't see that happen much with Mario or Link. There are plenty of questions about the Warp Star, too. What is it made of? How does it carry you?

[12:36](https://youtu.be/ZUY2AtBD6Sk?t=756) There are game design reasons for it, but it's still a mystery. There's even a stage transition where you're shot out of a whale's blowhole. You end up in the sky, and start shooting mint breath. Here, we're heading to the final battle at Dedede's castle.

[12:49](https://youtu.be/ZUY2AtBD6Sk?t=769) The text in the stage intro scrolls away, which it's never done before that point. Then, touching these Kirby-looking creatures clears the path ahead. It doesn't have to make sense. Don't think!

[13:00](https://youtu.be/ZUY2AtBD6Sk?t=780) Just feel! Embrace the mystery! To top it all off, there's the dynamic ending. Kirby is on a quest to get Dream Land's food back, so he grows giant and carries the entire castle home.

[13:13](https://youtu.be/ZUY2AtBD6Sk?t=793) It's a mysterious world with mysterious creatures that defy all reason— and that's Kirby at its heart. And since we've reached the ending, I think that's a great place to finish up. Did you enjoy the presentation?

[13:26](https://youtu.be/ZUY2AtBD6Sk?t=806) Though, while I have you... Think of this as the encore to the main concert. A little bonus, just for you! Let's talk about Meta Knight.

[13:38](https://youtu.be/ZUY2AtBD6Sk?t=818) I included this section at the end of the presentation I gave at the Osaka performance. Which of the three shapes I've drawn here is correct for the slit in Meta Knight's mask? The answer is: all of them!

[13:55](https://youtu.be/ZUY2AtBD6Sk?t=835) Each one has been used to represent Meta Knight. Let's start with the left one. This is what he looked like in Return to Dream Land and the Kirby anime. It's sort of a V-shaped hole in his mask, as you can see.

[14:08](https://youtu.be/ZUY2AtBD6Sk?t=848) The corners are squared-off. Next, let's look at the one on the right. This is how Meta Knight looks in Smash Bros. We added a concave curve at the edges to give him a more cool, experienced look.

[14:25](https://youtu.be/ZUY2AtBD6Sk?t=865) We wanted him to fit in even when facing realistic opponents, so we adjusted his design for Smash. That's true of plenty of characters, not just Meta Knight. Some elements like the M on his shoulder have also been reflected in more recent Kirby titles. Here are the two side-by-side.

[14:45](https://youtu.be/ZUY2AtBD6Sk?t=885) In newer entries, he's not quite as rotund as the example on the left. That just leaves the one in the middle. What could it be? This is the mask from Meta Knight's first appearance, in Kirby's Adventure— when his design was pixel-based.

[15:03](https://youtu.be/ZUY2AtBD6Sk?t=903) This is what the pixel art itself looks like. Sure enough, the sides kind of taper to points. The slit is in a slightly different position, too. Since the illustration for Kirby's Adventure resembled the pattern on the left, that gradually became how he looked.

[15:19](https://youtu.be/ZUY2AtBD6Sk?t=919) That said, we reexamined this for each game depending on his role, as it was important to find appearances and designs that fit each particular day and age. And that's it for Meta Knight! I’d like to go on one more detour, though.

[15:36](https://youtu.be/ZUY2AtBD6Sk?t=936) It's a question about the screen you see here. This is from the Famicom dev tool I showed you earlier, but what is it? What you're looking at is a prototype character from the SNEŠ title, Kirby Super Star. What you're looking at is a prototype character from the SNEš title, Kirby Super Star.

[15:49](https://youtu.be/ZUY2AtBD6Sk?t=949) While it's true that Kirby Super Star was always conceived to be a Super NES game, there was a waiting period for the SNES dev tools, so I took the art from my design document and sketched out the character at the size l imagined. This is the Beam ability, for example.

[16:05](https://youtu.be/ZUY2AtBD6Sk?t=965) The final game uses the same poses. Though, the effects did change a lot. Here's the Yo-Yo ability. Kirby rides on top of the yo-yo when he uses his Break Spin.

[16:19](https://youtu.be/ZUY2AtBD6Sk?t=979) This is the Fighter ability. This screen covers all the different techniques you can use with the ability. Namely, the Vulcan Jab, Smash Punch, Leg Sweep, Spin Kick, Down Kick, Double Kick, Rising Break, Arm Throw, and Judo Throw.

[16:33](https://youtu.be/ZUY2AtBD6Sk?t=993) The moveset for the final release was mapped out here in early development. Here we have the Cutter ability. This is how it looks in motion. The pose settings at the top and bottom are a little broken, but the Final Cutter combo stayed like this through to the final product.

[16:51](https://youtu.be/ZUY2AtBD6Sk?t=1011) Since the beginning, it's been my style with Kirby to visualize the design as clearly as possible in the early stages of the project. It's easier for the team to move forward confidently with concrete visuals, after all. And there you have it.

[17:07](https://youtu.be/ZUY2AtBD6Sk?t=1027) It's really over this time! I hope you keep playing Kirby games for years to come. Thanks for watching!
