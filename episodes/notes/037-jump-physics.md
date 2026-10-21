# 037 · Jump Physics

**Category:** Design Specifics · [Video](https://www.youtube.com/watch?v=noKsDZ-UPq8) · [Transcript](../transcripts/037-jump-physics.md)

## In one sentence
Build jumps from an initial upward velocity plus per-frame downward acceleration, then shape the rise, fall, air control and windup to fit what your game needs.

## Key ideas
- A typical jump: apply upward velocity (say 5 units), then add 1 unit of downward acceleration each frame while airborne, so velocity goes 4, 3, 2... After reaching 0 the acceleration continues, so the fall speeds up (1, 2, 3, 4). On flat ground the character lands when downward velocity equals the initial upward velocity. Horizontal (X) movement usually stays constant or decelerates slightly; maximum velocity and inertia also come into it.
- The right jump depends on the game's goal. In Super Mario Bros. the rise is gentle: downward acceleration starts very low and rises suddenly at the peak, so Mario falls much faster than he rose, and holding the button longer jumps higher, which suits that design.
- In Metroid, Samus rises even slower and also falls slowly, almost floating, perhaps because the height you shoot from matters so much.
- In Ghosts 'n Goblins the jump is low and you can't change direction at all once airborne, so you know where you'll land. It's restrictive, but having to plan every jump is solid game essence, and it lets players attack while jumping backwards.
- From Street Fighter II Turbo on, Zangief's Spinning Pile Driver falls faster than it rises, giving the slam more impact. Even with the same trajectory, changing speed changes the feel drastically.
- Smash jumps have a short windup, now the same for every fighter; removing it would make players jump before they could input an Up Smash. Each new Smash, he asks whether a jump is even needed; the answer is always yes, but the physics change every time.
- Smash Bros. Ultimate (the first since Kirby Super Star to do this) applies very strong upward velocity at the start of each jump, then greatly increases downward acceleration for a few frames; once the jump snaps to a halt, gravity returns to normal. This lets players escape a jam even if they react a little late. It adds parameters and bug risk, but the benefits are worth it.

## Do this
- Implement jumps as an initial upward velocity plus a downward acceleration added every frame (with a maximum fall speed), and keep horizontal speed constant or slightly decelerating in the air.
- Use separate gravity values for rising and falling: low gravity on the way up and a sharp increase at the peak gives a gentle rise and a fast fall, which pairs well with jump height that depends on how long the button is held.
- Choose air control to fit the game: allow steering for forgiving platforming, or lock direction after takeoff if you want every jump to be a planned commitment.
- For slams and throws, make the descent faster than the ascent to add impact without changing the trajectory.
- If jump and up-attacks share the same stick direction, keep a short pre-jump windup, the same length for every character, so the attack input registers before the jump starts.
- For a snappy jump that rescues late reactions, apply a very strong initial upward velocity, greatly increase downward acceleration for a few frames until the jump halts, then return gravity to normal.

## Avoid
- Using one default jump for every game regardless of its goal.
- Removing the pre-jump windup when up-attacks and jumps share an input.

## Examples from the episode
- **Super Mario Bros.:** gentle rise, sudden increase in downward acceleration at the peak, much faster fall; button hold changes height.
- **Metroid:** Samus rises and falls slowly, almost floating, which may help with aiming at different heights.
- **Ghosts 'n Goblins:** low jump with no mid-air direction change; you must plan each jump and can attack while jumping backwards.
- **Street Fighter II Turbo — Zangief's Spinning Pile Driver:** falls faster than it rises, giving the slam more impact.
- **Super Smash Bros. — jump windup:** unified short windup so Up Smash can still be input.
- **Super Smash Bros. Ultimate (and Kirby Super Star):** strong initial burst, then a few frames of heavy downward acceleration before normal gravity.

## Quote
> Even with the same trajectory, adjusting a move's speed can drastically change how it feels. (02:44)

## Tags
`jump-physics` `controls` `numbers-tuning` `responsiveness` `impact` `platforming` `smash-bros`
