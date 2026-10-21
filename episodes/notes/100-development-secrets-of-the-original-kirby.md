# 100 · Development Secrets of the Original Kirby

**Category:** Grab Bag · [Video](https://www.youtube.com/watch?v=ZUY2AtBD6Sk) · [Transcript](../transcripts/100-development-secrets-of-the-original-kirby.md)

## In one sentence
Treat hard limits as design fuel: reuse and mirror art to fit tiny memory, fake expensive systems with hand-placed patterns when processing is scarce, and visualize the design concretely early so the team can move forward with confidence.

## Key ideas
- **The project:** Kirby's Dream Land (Game Boy, 1992). Sakurai came up with the concept around May 1990, at 19, to show newcomers how fun games can be. It took just under a year to make, experienced players can finish it in 20 minutes, and it sold over 5 million copies and led the Game Boy charts for several months. Copy abilities didn't arrive until Kirby's Adventure.
- **Visualize early:** the team developed on a Twin Famicom with a HAL-made trackball and a dev tool loaded from disk. The tool could draw pixel art, assemble it into characters, move them, test animations, and build backgrounds and even the title screen. Sakurai used it while forming the concept to see the game in motion, and Kirby's pixel art stayed roughly the same from then to release. Later, while waiting for SNES dev tools, he sketched Kirby Super Star's abilities at their intended size in the same Famicom tool. Beam's poses, Fighter's whole moveset (Vulcan Jab, Smash Punch, Leg Sweep, Spin Kick, Down Kick, Double Kick, Rising Break, Arm Throw, Judo Throw) and the Final Cutter combo all survived to the final game. It's always been his style to visualize the design as clearly as possible early, because concrete visuals help the team move forward confidently.
- **ROM tricks:** the game was designed mostly for 512 kilobits (64 KB), though it shipped at 2 megabits.
  - Waddle Dee and Waddle Doo share a back half: "two characters using the ROM space of only 1.5."
  - Gordo is one image flipped vertically and mirrored horizontally.
  - Poppy Bros. Sr. has only three leg patterns and two head patterns.
  - Kracko's body is flipped on both axes, and its eyeball is reused for Kracko Jr.
  - The Maxim Tomato has an "M" because it's easy to make with a horizontal flip.
  - Because the game was for newcomers, Sakurai wanted big bosses so that slightly off-target attacks would still hit. With so little space, Whispy Woods became one drawn piece, mirrored vertically, placed three times and stuck to the background.
- **Sprite budget:** sprites were built from 8x16 pieces rather than the 8x8 common on NES, so leftover gaps couldn't be used. All of Stage 1's characters fit in one 256x256 image: a tiny section with all of Kirby's actions, "permanent fixtures" that appear throughout the game, and stage-specific parts. Background art had half the usable area of an NES game and couldn't be mirrored horizontally. King Dedede gets the most lavish art because no other enemies appear while he's on screen. Sakurai drew almost all the art himself, working directly in pixels instead of sketching on graph paper first.
- **No terrain collision for enemies:** Coner crawling, falling off a cliff and slowing in water, or a Waddle Dee falling off a ledge, look natural but involve no collision checks. Sakurai authored movement patterns separately, typing hexadecimal values with the trackball cursor (there was no keyboard), and lined them up with the background to the pixel. Wasteful, but light on processing, which was invaluable on Game Boy, and part of why Cappy turned out so bouncy and fun.
- **Smash rules in 1990:** the first Kirby design document already describes them. The screen scrolls with the character, stops when you get knocked flying, then gently recenters once you settle. Getting knocked fully off-screen loses a life, and knockback distance depends on your health value. He had completely forgotten this by the time he made Smash.
- **Mystery and redesign:** Kirby's world runs on mystery: "bourbons," Kirby splitting into three after a level, the Warp Star, being shot out of a whale's blowhole, intro text that scrolls away, Kirby growing giant and carrying the castle home. "It doesn't have to make sense." Meta Knight's mask slit has three valid shapes: tapered pixel art in Kirby's Adventure, a V with squared corners in Return to Dream Land and the anime, and concave curves in Smash for a cooler, more experienced look beside realistic opponents. Each game reexamined his design to fit its role and era.

## Do this
- Stretch art memory by sharing and flipping parts: build look-alike variants from one shared half (Waddle Dee/Doo), animate simple objects by flipping one frame on both axes (Gordo), cap limb frames (three leg and two head patterns), and reuse parts like eyes across related characters (Kracko and Kracko Jr.).
- Give the richest art budget to scenes where only one major character is on screen, as with Dedede's fight.
- In beginner-focused games, make bosses big enough that slightly off-target attacks still connect.
- When CPU is scarce, hand-author enemy movement paths that match the terrain instead of running per-frame collision checks. It's cheap and leaves headroom for lively, bouncy animation.
- Before full production (or before the final tools arrive), mock up key characters at their intended on-screen size and lay out complete movesets, so the team has concrete visuals to build from.
- Revisit a returning character's design for each new game's role and setting, the way Meta Knight's mask was reshaped to fit beside realistic Smash fighters.

## Examples from the episode
- **Kirby's Dream Land — Waddle Dee & Waddle Doo:** share the same back half to save ROM.
- **Kirby's Dream Land — Gordo:** one image flipped vertically and horizontally reads as motion.
- **Kirby's Dream Land — Whispy Woods:** one mirrored piece placed three times on the background, a big target for beginners.
- **Kirby's Dream Land — Coner and Cappy:** no terrain collision. Movement patterns were lined up with the background by hand, which was cheap on processing.
- **Kirby's Dream Land — design document:** Smash-style knockback, camera and off-screen-KO rules written in 1990.
- **Kirby's Dream Land — ending:** Kirby grows giant and carries Dedede's castle home. The mystery is the point.
- **Meta Knight — mask slit:** three different shapes across Kirby's Adventure, Return to Dream Land/the anime and Smash Bros.
- **Kirby Super Star — prototypes:** Fighter's moveset and the Final Cutter combo were mapped out early in the Famicom tool and survived to release.

## Quote
> Since the beginning, it's been my style with Kirby to visualize the design as clearly as possible in the early stages of the project. (16:51)

## Tags
`kirby` `history` `hardware` `rom-size` `character-design` `enemy-design` `boss-design` `prototyping` `beginners` `smash-bros`
