# 022 · Name Files Logically

**Category:** Programming & Tech · [Video](https://www.youtube.com/watch?v=XMzR5mJHPDg) · [Transcript](../transcripts/022-name-files-logically.md)

## In one sentence
Name development files and labels with a consistent, concise scheme that stays tidy when sorted (category first, then direction, then numbers for strength), so anyone can tell what a file is at a glance.

## Key ideas
- In Smash Bros., the move players know as "Up Special" is internally "Special Move (Up)," or "SpecialHi." That's why he sometimes says "Special Up." The whole team uses these labels.
- Every action in the game has a file-name class, or "label." The scheme was set when making the first Smash Bros. and is still used.
  - A Button standard attacks are "Attack," and B Button special moves are "Special."
  - Numbers mark strength: a neutral attack is "Attack1," a smash attack "Attack4." Combo steps count up: "Attack11," "Attack12," "Attack13."
  - Directions: "N" (neutral), "Hi" (up), "S" (side), "Lw" (down). A side smash is "AttackS4."
  - "Air" marks aerials. A forward aerial is "AttackAirF."
- Benefits: anyone can read a file name and know which move it is, and "everything stays nice and neat when sorted." Attack moves stay together, ordered by strength from neutral to tilt to smash, and Special moves form their own easy-to-spot category.
- Putting the direction first ("SAttack," "HiAttack") "would just make a huge mess when you sorted them all." Using anything but numbers for strength causes the same problem.
- In the game, the move is still called "Up Special," because from the player's side the directional input comes first. "The name matches how you perform the move." Internal and in-game names can differ.
- Keep names concise and easy to understand, so someone seeing them for the first time knows at a glance what they're for. Names that are too short are easy to type but hard to understand, so find a balance.
- Japanese developers should avoid romanized Japanese in file names. On bigger projects it makes things harder for people who don't speak the language, and overseas teams joining later may not understand it. "It's not just you who needs to understand your game."

## Do this
- Define a naming scheme at project start and keep it: broad category first (e.g., Attack / Special), then modifiers (direction N/Hi/S/Lw, "Air" for aerials), then numbers for strength or sequence (1, 4; 11/12/13 for combo steps).
- Sort an asset folder by name and check that related files group together in a sensible order. If they don't, reorder the parts of the name.
- Use numbers rather than words for strength levels so they sort correctly.
- Name player-facing moves in the order the player inputs them (direction, then button), even if internal labels differ.
- Choose names a newcomer can decode at a glance, not so abbreviated they're cryptic.
- Use English rather than romanized native-language words in file names whenever other or overseas teams might join.

## Avoid
- Putting direction or other modifiers before the category ("SAttack," "HiAttack").
- Words instead of numbers for strength or order.
- Overly abbreviated names that are fast to type but hard to read.
- Romanized Japanese file names on large or international projects.

## Examples from the episode
- **Super Smash Bros. — action labels:** Attack1, Attack11–13, Attack4, AttackS4, AttackAirF, SpecialHi.
- **Super Smash Bros. — "Up Special" vs. "Special Move (Up)":** the in-game name follows the player's input order; the internal label follows the sorting scheme.

## Quote
> Remember: it's not just you who needs to understand your game. (04:29)

## Tags
`naming` `file-organization` `communication` `localization` `smash-bros`
