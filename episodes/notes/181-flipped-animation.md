# 181 · Flipped Animation

**Category:** Animation · [Video](https://www.youtube.com/watch?v=TJDMDxnWU5g) · [Transcript](../transcripts/181-flipped-animation.md)

## In one sentence
In side-view games, mirror characters' animations when they turn around so they always face the camera and show their faces, and plan ahead for the extra work and handedness problems this brings.

## Key ideas
- Two Links facing each other: one is turned toward the viewer and the other away. Two Marios facing each other: both are turned toward the viewer. That second case is "flipped animation", the team's internal name for mirroring certain poses and movements. There's no official name, and it's an oddity you really only find in games.
- Street Fighter II used pixel-art sprites, so it simply used mirrored images to face left and right. Street Fighter IV uses polygon characters but keeps the SFII mirroring.
- It's a lot of work. You don't have to recreate every animation, but it causes plenty of other problems: a right-handed straight punch becomes a left-handed one, and you have to quickly switch the hand a character holds an item in.
- It's hard to apply to characters who aren't horizontally symmetrical, so it doesn't suit sword-based fighters.
- They do it because it looks better. Smash Bros. didn't start mirroring until after Brawl. Without it, the character on the right faces away, so you can't see his expression and get little information, even though such an expressive character really should be facing you.
- Because Smash Bros. is viewed from the side, this creates many strange quirks. Kirby's run, seen straight on, shows him running diagonally toward the camera; from the normal side view, that lets you see his face and get all the visual information. Older titles had no flipped animation, so the run had to be shown directly from the side. That isn't much fun to look at, and for half of his movement you can't even see his face.
- Aside: Dee Jay in Super Street Fighter II wears pants that say "MAXIMUM" because every letter still looks right when mirrored. Kirby's Maxim Tomato was also designed as two mirror images joined together, which is why it has an "M".

## Do this
- In a side-view game, mirror a character's animation set when they change facing instead of rotating the model 180°, so expressive characters face the camera from either side of the screen.
- Turn side-view poses slightly toward the camera (for example, a run angled diagonally toward the viewer) so the face and key visual information stay visible.
- Plan for mirroring side effects: a right-handed punch becomes left-handed, and held items must quickly switch hands when the character flips.
- Leave out mirroring for characters who aren't horizontally symmetrical, such as sword fighters.
- Design logos, lettering and emblems that will be mirrored so they still read correctly when flipped (like "MAXIMUM" or the Maxim Tomato's "M").

## Avoid
- Letting an expressive character show the back of their head whenever they stand on one side of the screen.
- Animating runs and other moves in pure profile, so the face is hidden for half the movement.

## Examples from the episode
- **Link vs. Mario (opening footage):** two Links facing each other show one front and one back; two mirrored Marios both face the viewer.
- **Street Fighter II / Street Fighter IV:** SFII mirrored its sprites, and SFIV kept that mirroring even with polygon characters.
- **Smash Bros. — after Brawl:** the release version mirrors the right-hand character so his expression is visible.
- **Smash Bros. — Kirby's run:** he actually runs diagonally toward the camera so his face is visible from the side view; older titles showed him in pure profile.
- **Super Street Fighter II — Dee Jay:** his "MAXIMUM" pants use letters that survive horizontal mirroring.
- **Kirby — Maxim Tomato:** designed as two mirror images stuck together, hence the "M".

## Quote
> We can't see his expression, and receive little information. For someone this expressive, he should really be facing us, right? (01:28)

## Tags
`animation` `mirroring` `readability` `character-design` `camera` `fighting-games` `smash-bros` `kirby`
