# 118 · Family BASIC

**Category:** Programming & Tech · [Video](https://www.youtube.com/watch?v=89_FhHQ5n-g) · [Transcript](../transcripts/118-family-basic.md)

## In one sentence
Start making games with whatever tool you can get, and tinker with simple movement code such as inertia, because that hands-on experimenting is how you learn what shapes game feel.

## Key ideas
- Family BASIC (June 1984, about a year after the Famicom launched in Japan) turned a Famicom into a home computer. Sakurai calls it the biggest reason he got into the game industry. A full computer set cost about 400,000 yen, too much for a middle-schooler, so he saved six months of allowance to buy it.
- The cartridge had only 2 KB of program RAM, roughly 2,000 typed characters. Its Hu-BASIC (Hudson was involved) was customized for the Famicom and stood out for its sprite management features.
- A six-line program using the MOVE command makes a character walk around. DEF MOVE sets the character, direction (8 directions), speed, distance, priority (in front of or behind the background) and palette. The built-in character presets (Mario, Pauline, Luigi's palette) were crucial: drawing your own pixel art in code would have used up the tiny program space. Mario gets three animation patterns: climbing for up, jumping for diagonal, walking for sideways.
- MOVE is easy to use but hard to use well: it is limited to eight directions and his program struggled to respond to player input. The SPRITE command was more practical. He shows a controller-driven sprite with a little inertia, which moved smoothly where typical home-computer code of the time gave stilted movement.
- Experimenting this way taught him concepts like inertia and let him see how different changes affect the feel of a game. He drew on that knowledge when developing Kirby's Dream Land.
- A separate background tool offered Mario Bros. and Donkey Kong Jr. assets. It also showed the Famicom's "attribute" limit: palettes are shared across 16x16 areas, so placing an object (an inkwell) recolors the ground under it. To keep both correct you may have to shift the object, for example up a space. The cartridge also took two AA batteries for battery-backed saves of your programs. The batteries drained fast and he remembers it as unreliable; cassette tapes via the Data Recorder were more common. Per his research, the first actual game with battery backup was Dragon Slayer for the Super Cassette Vision (February 1986), well after this.
- Without Family BASIC he wouldn't have realized he could make games, and Kirby and Smash Bros. wouldn't exist. His advice: the most important thing is to sit down and try to make a game.

## Do this
- Build a tiny prototype of one controllable character and tweak its inertia and acceleration values one at a time, noting how each change alters the feel.
- When memory or time is tight, use built-in or placeholder assets so your budget goes into behavior instead of art.
- If you target hardware with tile-attribute color limits (16x16 palette areas on the Famicom), align objects to that grid or shift them so neighbors don't take on the wrong palette.
- Pick whatever tool is accessible now and make a small, complete game rather than waiting for better equipment.

## Avoid
- Relying on a convenient high-level movement command when responsive control matters; MOVE was limited to eight directions and lagged on player input.

## Examples from the episode
- **Family BASIC — MOVE command:** a six-line program moves Mario (or Pauline, or Luigi's palette) using built-in presets with three animation patterns.
- **Family BASIC — SPRITE command:** a controller-driven sprite with inertia that moves smoothly in any direction.
- **Family BASIC background tool — attributes:** placing an inkwell recolors the Mario Bros. floor under it because 16x16 areas share palettes.
- **Kirby's Dream Land:** development drew on what he learned experimenting in Family BASIC.
- **Dragon Slayer (Super Cassette Vision):** by his research, the first game to use battery backup (February 1986).

## Quote
> But the most important thing to do is to first sit down and try to make a game. (11:39)

## Tags
`history` `prototyping` `programming` `responsiveness` `controls` `hardware` `kirby` `motivation`
