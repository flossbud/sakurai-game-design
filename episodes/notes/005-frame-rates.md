# 005 · Frame Rates

**Category:** Planning & Game Design · [Video](https://www.youtube.com/watch?v=Rjdmi7628GM) · [Transcript](../transcripts/005-frame-rates.md)

## In one sentence
Treat frames as your game's unit of time (distance = time × speed), and choose your frame rate on purpose: 60 fps is ideal, 30 fps is an acceptable standard.

## Key ideas
- Frame rate is how often the screen is redrawn. Standard TVs refresh 60 times a second, or 60 frames per second (fps).
- Games often use frames as their unit of time. Since "Distance = Time × Speed," time has a huge effect on how far and how fast things move, which makes frame rate "extremely important."
- 60 fps and 30 fps differ both in how they look and in how smoothly they control. 60 is ideal when possible. 30 is a common standard because drawing twice as many frames means sacrificing half your visual performance, and 30 is still "more than adequate."
- A variable frame rate (dropping frames when the processor can't keep up) is not "slowdown." The game isn't running slower; it's just redrawing the screen less often.
- PCs and high-end machines can go past 120 or even 200 fps, but that only matters if the monitor supports it. "What you really want is both."
- History: in the CRT era, NTSC (Japan and North America) rendered 30 frames per second, and interlacing let games run at 60 fps. PAL (Europe and Australia) delivered 25, so games ran at 50 fps. His NES and SNES games used screen interrupts as the unit of time, so PAL versions ran at 5/6 speed.
- From the Nintendo 64 onward, polygon processing made it easier to draw fewer frames while running the game as intended, so the tradeoffs were less jarring.

## Do this
- Pick a target frame rate early: 60 fps if your visual budget allows, or 30 fps if you need the rendering headroom (60 costs about half of it).
- Specify timings like attack length, invincibility and jump arcs in frames at your target rate, and remember that speed × time sets how far things move.
- Keep game speed independent of how many frames get drawn, so a dropped frame doesn't slow the game. Avoid the 5/6-speed problem of PAL-era ports.
- When diagnosing performance, decide whether you're seeing frame drops (less redrawing) or true slowdown (the game itself running slower).
- Check high-refresh support against real displays, since 120+ fps does nothing on a monitor that can't show it.

## Avoid
- Confusing a variable frame rate with slowdown.
- Tying game logic to a refresh rate that varies by region or platform without accounting for it.

## Examples from the episode
- **His NES/SNES games — PAL versions:** time was counted in screen interrupts, so the 50 fps PAL versions ran 5/6 as fast and everything moved a little slower.
- **Nintendo 64 onward — polygon processing:** dropping frames without changing game speed became easier.
- **Side-by-side footage:** the same scene at 60 fps and 30 fps.

## Quote
> In games, these frames are often used as a unit of time. Distance = Time × Speed. (00:48)

## Tags
`frame-rate` `responsiveness` `controls` `numbers-tuning` `hardware` `history`
