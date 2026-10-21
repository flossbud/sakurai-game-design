# 183 · Long Ago, Numbers Were Used to Draw Pixel Art

- **Category:** Grab Bag
- **Video:** https://www.youtube.com/watch?v=5pJC1YLMbhk
- **Length:** 04:10
- **Source:** official English subtitles burned into the video, read by OCR (tools/ocr_subs.py). Expect rare OCR typos.

---

[00:10](https://youtu.be/5pJC1YLMbhk?t=10) Grab Bag! Long ago, if you were making a game on a PC called a "microcomputer," you needed a way to draw pixel art for the characters. I'm talking about the early 1980s.

[00:26](https://youtu.be/5pJC1YLMbhk?t=26) But in most cases, there weren't any graphics tools available. Everyone used data—numbers, that is— to enter the value of each pixel. I'm sure you're wondering, "how do you draw like that?!"

[00:40](https://youtu.be/5pJC1YLMbhk?t=40) For posterity's sake, today I'll be teaching you how we used to draw pixel art back in the microcomputer days. To start, there's something called a base-16 numeral system. In this system, unlike with normal base-10, numbers carry to the next place value at 16.

[00:58](https://youtu.be/5pJC1YLMbhk?t=58) In base-10, you count from 0 to 9 before getting to 10. In base-16, numbers above 9 are written as A, B, C, D, E, and F— then after F is when you get to 10. The place value carries up.

[01:13](https://youtu.be/5pJC1YLMbhk?t=73) You can think of A as 10 and B as 11. With a single base-16 value, we can draw a 4x1 piece of art. This is 0. Changing it to 1 fills in the rightmost pixel.

[01:32](https://youtu.be/5pJC1YLMbhk?t=92) This is 2. The second pixel from the right is filled in, while the rightmost pixel resets. This is 3. 1 plus 2 makes 3.

[01:42](https://youtu.be/5pJC1YLMbhk?t=102) Here's 4. Once again, it carried up. Then 5, 6, 7—and it carries up again at 8. This is 9.

[01:53](https://youtu.be/5pJC1YLMbhk?t=113) 8 plus 1 makes 9. This is A—in other words, 10. Then B, C, D, E, and F. At F, all the pixels are filled.

[02:05](https://youtu.be/5pJC1YLMbhk?t=125) With these, you can make a 4-pixel wide piece of art. That means with two base-16 values, you can show 8 pixels in a row. For example, 4E would look like this. With eight rows, you can create an 8x8 piece of monochrome pixel art.

[02:25](https://youtu.be/5pJC1YLMbhk?t=145) In other words, this picture would be... 18, 7E, 5E, FF, FF, 7E, 7E, 18— if you were writing it in base-16. I hope I got that right.

[02:41](https://youtu.be/5pJC1YLMbhk?t=161) It was common to draw on graph paper first, then count out the values afterward. In my case, I used a cross as my guide, then estimated values based on the position. I borrowed a pocket computer from a school friend and would tap tap tap on the keys during class so I could keep improving on my game content and pixel art.

[03:01](https://youtu.be/5pJC1YLMbhk?t=181) But I really should have been paying attention in class! ...Right? Now, let's say you want color. If you have three colors like on the NES, all you need is two pieces of same-sized pixel data.

[03:15](https://youtu.be/5pJC1YLMbhk?t=195) If you stack them and look at each pixel, either both are empty, the first is filled, the second is filled, or both are filled— giving you four combinations that let you depict three colors plus transparency. In practice, you can also use something called data compression.

[03:31](https://youtu.be/5pJC1YLMbhk?t=211) In other words, instead of writing out 00000000 for a series, it's shorter to just write 0x8.

[03:43](https://youtu.be/5pJC1YLMbhk?t=223) Compared to entering pixels as data, things are much easier nowadays, but that ease of input is outweighed by the complexity of modern graphical demands. So really there's no comparison. Still, it's interesting to see how it all started, right?
