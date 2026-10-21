# 183 · Long Ago, Numbers Were Used to Draw Pixel Art

**Category:** Grab Bag · [Video](https://www.youtube.com/watch?v=5pJC1YLMbhk) · [Transcript](../transcripts/183-long-ago-numbers-were-used-to-draw-pixel-art.md)

## In one sentence
Early-1980s pixel art was typed in as hexadecimal numbers, one bit per pixel, with stacked bit layers for color and simple compression, and knowing those roots shows how much complexity modern graphics have added.

## Key ideas
- In the early 1980s, making a game on a "microcomputer" PC usually meant having no graphics tools, so everyone entered the value of each pixel as data, in numbers.
- Base 16 (hexadecimal) counts 0 to 9, then A to F (A is 10, B is 11), and only carries to "10" after F. One hex digit draws a 4×1 strip of pixels: 0 is empty, 1 fills the rightmost pixel, 2 fills the second from the right, 3 (1 + 2) fills both, 4 and 8 carry to the next pixels, and F fills all four.
- Two hex digits give 8 pixels in a row (for example 4E), and eight rows make an 8×8 monochrome image. His example picture is 18, 7E, 5E, FF, FF, 7E, 7E, 18.
- People commonly drew on graph paper first and counted out the values afterward. Sakurai used a cross as his guide and estimated values from position. He borrowed a school friend's pocket computer and tapped away on it during class to keep improving his game content and pixel art (he admits he should have been paying attention).
- Color: for three colors as on the NES, you stack two same-sized pixel layers. Each pixel is then empty in both, filled in the first, filled in the second or filled in both, giving four combinations: three colors plus transparency.
- Data compression shortened things further, for example writing 0x8 instead of 00000000.
- Input is far easier today, but that's outweighed by how complex modern graphics have become, so there's really no comparison. It's still interesting to see how it all started.

## Do this
- When working with tight memory or retro-style formats, store sprites as 1-bit layers and stack two layers to get three colors plus transparency.
- Compress repeated runs of the same value (write "0x8" instead of eight zeros) rather than storing every pixel.
- Plan pixel art on a grid, or graph paper, first, and only then convert it into data.

## Examples from the episode
- **Early-1980s microcomputers:** no graphics tools, so pixel art was entered as hex values.
- **8×8 example image:** encoded as 18, 7E, 5E, FF, FF, 7E, 7E, 18.
- **NES:** three colors plus transparency from two stacked pixel layers.
- **Sakurai's school days:** coding pixel art on a borrowed pocket computer during class.

## Quote
> Everyone used data—numbers, that is— to enter the value of each pixel. (00:26)

## Tags
`history` `pixel-art` `hexadecimal` `data-compression` `hardware` `tech`
