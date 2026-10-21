# 076 · Learn to Count Frames!

**Category:** Planning & Game Design · [Video](https://www.youtube.com/watch?v=JZ1Jd0u3b6U) · [Transcript](../transcripts/076-learn-to-count-frames.md)

## In one sentence
Train yourself to feel frame durations (at 60 fps) by counting "1-and-2-and," so you can specify timing, speed and distance in frames and catch mistakes when the build doesn't match.

## Key ideas
- Frames are the unit games use to measure time. If you can measure time, you can gauge speed and distance too, so frames are the basis for all movement. Having a feel for them is "an absolute must."
- No stopwatch counts frames, but you can learn to ballpark them. He assumes 60 frames per second: one second is 60 frames.
- Counting "1, 2, 3" isn't precise, so add an in-between beat: "1-and-2-and-3-and." That puts about 30 frames between beats, and halving a beat gives 15 frames. "1-and" splits into two 15-frame intervals.
- Reference points for 15 frames: roughly the time from inputting a Smash Attack in Smash Bros. to its release, and the startup of a standard kick in Tekken. Startup on a heavy punch in Street Fighter II is a bit less than half that. These vary by character and move.
- Estimate other values from those anchors. 20 frames, for example, is a little past the midpoint between 0 and 30. In racing games you can work out precise goal times by measuring the intervals between frames.
- Directors who brief the team with a poseable figure and precise frame assignments (from an earlier episode) need this skill to prepare that data.
- Even when you specify the right frame counts, code or data errors still happen. A trained sense of timing helps you notice them.

## Do this
- Practice clapping seconds while saying "1-and-2-and-3-and." Each beat is about 30 frames at 60 fps and half a beat about 15. Check yourself against your engine's frame counter until you're close.
- Memorize a few reference moves from games you know (for example, Smash Attack input-to-release ≈ 15 frames) and estimate new timings relative to the 0/15/30-frame anchors.
- Write timing in animation and move specs as exact frame numbers instead of words like "quick" or "slow."
- After implementation, play each move and check it by feel against the spec. If it feels off, inspect the code and data for errors.

## Avoid
- Assigning frame counts in specs that you can't actually feel or verify.

## Examples from the episode
- **Super Smash Bros. — Smash Attacks:** about 15 frames between input and release.
- **Tekken — standard kick:** startup of about 15 frames.
- **Street Fighter II — heavy punch:** startup a bit less than half of 15 frames.
- **Racing games:** precise goal times can be found by measuring frame intervals.

## Quote
> Frames are the basis for all movement in games. That's why it's so important to learn how long they are. (00:47)

## Tags
`frame-rate` `animation-timing` `numbers-tuning` `specs` `direction`
