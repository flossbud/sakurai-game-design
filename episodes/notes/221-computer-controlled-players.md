# 221 · Computer-Controlled Players

**Category:** Planning & Game Design · [Video](https://www.youtube.com/watch?v=uleauI0IwZM) · [Transcript](../transcripts/221-computer-controlled-players.md)

## In one sentence
Build CPU opponents from data on reach, timing and the opponent's state, give them human-like reaction limits, and tune them to be fun (aggressive and beatable) rather than flawless.

## Key ideas
- In old games' attract modes (demos that play when nobody starts the game), the computer often seems to move the character at random, "and it's not going great." A computer-controlled playable character is usually called a CP or CPU.
- Humans and computers are very different. The more freedom a game offers, the harder it is to build CPU players for it, and CPUs that react faster than a human can feel "extremely unfair."
- In board and card games, people tend to suspect cheating when the computer gets a good dice roll. The computer controls both sides, so even moves a human could make look unfair.
- CPU AI for a game like Smash Bros. is extremely difficult, but players who want to play competitive games alone need it. Sakurai is comparatively hands-off with this task, though he supervises it.
- An action-game CPU has no eyes, so it decides from categories of data: the opponent's position and status, its own regular and special attack ranges and movement range (converted to data or pulled from the original data and stored as reach and attack-timing details), and the opposing character's attack data.
- Logic can switch partway through a match. A CPU might get "angry" at low HP, keep its character's optimum distance, factor in speed and jump height, or go easy on you if it is winning too much. When logic types contradict each other, the CPU may behave wrongly, and this becomes more common as mechanics and tracked criteria grow more complex.
- In Smash Bros. Ultimate, CPUs have a kind of "reflex," so they can't react instantly. Reversed controls confuse them a little, but like real players they rarely fail to adjust and won't just keep walking off the stage.
- Ultimate's CPUs were tuned more aggressively than in past games, so they are weaker at defense, at evasion and against players who wait. Players who pick a high CPU level want strong opponents, and a CPU that waits around or shows machine-like reflexes isn't fun, so the team prioritized offense and the ability to fight and win.
- CPUs that always perfect-shielded or dodged every attack could be made essentially invincible, "But that wouldn't be any fun at all." The goal is to make things as fun as possible.

## Do this
- Precompute each character's attack reach, attack timing and movement range as data the AI can query, and give the AI the opponent's attack data, position and status.
- Add an artificial reaction delay so CPUs can't respond faster than a human.
- Organize AI behavior into modes that switch with the match state (for example: aggressive at low HP, holding optimal distance, easing off when winning too much), and test specifically for cases where two modes give conflicting orders.
- Tune high difficulty levels toward aggressive offense rather than waiting or perfect defense.
- Cap how often CPUs can perfect-shield or dodge, so they stay beatable.
- Make CPUs briefly confused by effects like reversed controls, then have them adapt rather than walk off the stage.

## Avoid
- Superhuman reaction speed, which feels extremely unfair.
- High-level CPUs that turtle, wait around or defend perfectly.
- Piling on behavior criteria without checking for contradictions between them.

## Examples from the episode
- **Old attract modes:** the computer seems to move the character at random, and it doesn't go well.
- **Board and card games:** the computer's lucky dice rolls get read as cheating.
- **Super Smash Bros. Ultimate:** CPUs have a "reflex" delay, are briefly confused by reversed controls, and were tuned for offense over defense.

## Quote
> In the end, it's important to remember that our goal is to make things as fun as possible. (04:47)

## Tags
`ai` `cpu-players` `enemy-design` `difficulty` `fairness` `combat` `single-player` `smash-bros`
