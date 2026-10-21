# 102 · Behavior at Ledges

**Category:** Design Specifics · [Video](https://www.youtube.com/watch?v=rcuihq0j7VM) · [Transcript](../transcripts/102-behavior-at-ledges.md)

## In one sentence
Decide action by action whether a character can fall off a ledge, letting momentum-heavy rushes go over while short steps and dodges stop at the edge, so players never feel their input was canceled or that they slid off by accident.

## Key ideas
- Characters that always fall off ledges regardless of conditions were common in old games, "often to their own detriment," so think hard before choosing that.
- Falling while moving but never during actions is one option. Its reasoning: if a small forward nudge from an action drops the player off the ledge, it feels like their input was canceled. Attacks that step forward, for example, shouldn't make you fall.
- Sakurai recommends letting some actions fall and others not: forward dodges stop at the edge, for example, while attacks that rush forward carry over. Account for momentum too, or going flying off the stage becomes too easy.
- In Smash Bros., Fox Illusion stops at the ledge. Falcon Kick sends you over unless you reach the ledge toward the end of the move. Drill Rush is risky near the ledge but also stops there late in the move. Egg Roll has parameters that set what speed sends Yoshi off the ledge.
- Other techniques: make players "push" against the edge to fall off, adjust the movement direction when the ledge runs roughly parallel to it, or even jump automatically at the ledge.
- Ledge behavior is less straightforward than it looks. Pay attention to how it feels in playtesting and pick the mechanics that suit your game.

## Do this
- Build a per-move table of ledge behavior ("stops at edge" or "carries over") instead of one global rule.
- Keep short forward-stepping attacks and forward dodges on the platform. Let fast rushing attacks carry over the edge as a deliberate risk.
- For long rushing moves, make the late part of the move stop at the ledge so a nearly finished move doesn't fling the player off.
- For rolling or momentum moves, set a speed threshold above which the character flies off the ledge and below which they stop.
- For plain walking, consider requiring the player to keep pushing toward the edge before they fall, or bend their movement along ledges that run nearly parallel to their direction.
- Put ledge behavior on your playtest checklist and judge it by feel.

## Avoid
- Letting characters fall off every ledge unconditionally.
- Letting a small forward nudge from an action drop players off, which feels like a canceled input.
- Ignoring momentum, which makes it too easy to fly off the stage.

## Examples from the episode
- **Super Smash Bros. — Fox Illusion:** stops when it reaches the ledge.
- **Super Smash Bros. — Falcon Kick:** goes straight over, unless the ledge is reached toward the end of the move.
- **Super Smash Bros. — Drill Rush:** risky near ledges, but stops at the ledge late in the move.
- **Super Smash Bros. — Egg Roll:** a speed parameter decides when Yoshi flies off the ledge.

## Quote
> If you let a player fall off a ledge the moment they're nudged forward by an action, it may make them feel like their input was canceled—which isn't great. (00:36)

## Tags
`ledges` `controls` `movement` `responsiveness` `playtesting` `numbers-tuning` `smash-bros`
