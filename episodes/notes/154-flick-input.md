# 154 · Flick Input

**Category:** Design Specifics · [Video](https://www.youtube.com/watch?v=ChNceKFm2kI) · [Transcript](../transcripts/154-flick-input.md)

## In one sentence
When new hardware offers a new input, find a control that uses what only it can do (like reading how fast the analog stick reaches its edge to trigger a dash), but don't shoehorn in every possible use.

## Key ideas
- The Nintendo 64's analog stick differed from the D-pad in two ways: you could move in any direction, and you could tilt it by varying amounts. Both suited 3D exploration (in Japan it was even called the "3D stick").
- Sakurai also paid attention to the time a stick input takes to reach the edge of its range. He named the resulting control "flick input" (localized as "Tap" in the N64 Super Smash Bros.). It's a defining feature of Smash that gives the controls real physicality.
- Before this, dashing or running usually meant tapping the same direction twice, or combining movement with a button (the old "B-button dash"). Both took two steps or two buttons, which made things complicated. Scaling walking speed to how far the stick is tilted lets players both feel the controls and understand them more easily.
- **Downside:** accidental dashes. Smash Ultimate lets players adjust flick sensitivity.
- **Kid Icarus: Uprising** uses flick input for both dashing and dodging. Drawing in enemy attacks before dodging ties into the game's risk and reward, and the controls stay relatively simple, so it fits well in several ways.
- On hardware with new peripherals, think for a moment about what they make possible. But don't shoehorn in functionality: in Brawl, Sakurai didn't try to use every possible function of the Wii's Nunchuk or pointer.
- He's glad he got in early and designed a unique control method for such a widely used device, and wonders how much less remarkable Smash might have been without it.

## Do this
- Map movement speed to analog tilt (partial tilt walks) and trigger a dash when the stick travels from neutral to its edge quickly: one motion instead of a double-tap or a held button.
- Expose a sensitivity setting for the flick threshold, since accidental dashes are a known downside.
- Reuse the same flick gesture for evasive actions (e.g., a dodge) where drawing enemy attacks in close and then evading creates risk and reward, keeping the control scheme simple.
- When designing for hardware with a new input device, list what it can do that older inputs can't, then adopt only the uses that genuinely fit your game.

## Avoid
- Shoehorning every possible use of a new peripheral into your game.
- Making a basic action like dashing take two steps or two buttons when a single analog gesture would do.

## Examples from the episode
- **Super Smash Bros. (N64):** flick input ("Tap") triggers dashes, and tilt amount sets walking speed.
- **Super Smash Bros. Ultimate:** adjustable flick sensitivity to reduce accidental dashes.
- **Kid Icarus: Uprising:** flick to dash and to dodge, tied to risk and reward.
- **Super Smash Bros. Brawl:** deliberately didn't use every Nunchuk or pointer function.

## Quote
> When designing games for hardware that features new peripherals, you should think for a moment about what's possible with those peripherals. (01:32)

## Tags
`controls` `input` `analog-stick` `responsiveness` `hardware` `risk-reward` `smash-bros` `kid-icarus`
