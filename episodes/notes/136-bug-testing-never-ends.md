# 136 · Bug Testing Never Ends

**Category:** Team Management · [Video](https://www.youtube.com/watch?v=yIXB0vGJBuw) · [Transcript](../transcripts/136-bug-testing-never-ends.md)

## In one sentence
Full bug coverage is combinatorially impossible, so point your testing at the systems most likely to break (one character controlling another, scene changes, extreme terrain, growth and parameter systems), and re-test widely after every fix, because fixes create new bugs.

## Key ideas
- Buggy games don't mean the developers were fine with patching later. "Everyone would rather have their game be perfect from the very beginning." The problem is that modern games are often too big and complex to clean up through regular bug testing.
- **The combinations explode:** Smash Ultimate's 89 fighters alone give about 8,000 one-on-one pairings. Multiply in both fighters' movesets, bugs that only appear at certain times, items, a third player and their attacks, four or more players, terrain, stages, stage hazards and spirits, and the total is "truly astronomical." Fully testing means checking all of it, which is impossible. Meanwhile, once players find a bug and learn to reproduce it, it spreads across the internet.
- **Strategy:** Don't brute-force it. Target likely problem areas first, while accepting that this approach has limits too.
- **Where bugs cluster in Smash Ultimate:**
  - Grabs and throws, because actions that forcibly control another fighter easily cause processing contradictions (e.g., grabbing a fighter in the middle of a special move).
  - Final Smashes with scene changes, which must restrain and release fighters and keep anything from one scene out of the other.
  - Extreme Stage Builder terrain, where some collision issues have to be accepted. V-shaped terrain is especially tough.
  - The Spirits system, which adds many mechanics beyond normal play. Any game with parameters, character growth or unlockable skills is "grueling to test."
- **Scale:** A game that takes dozens of hours to finish might need thousands to tens of thousands of hours to test fully.
- **Patches can't ship instantly:** Fixing one bug can introduce others ("enbugging"), so every fix means redoing plenty of other checks.
- **Context:** Demanding that games be completely bug-free would make releasing games practically impossible. That standard belongs to banks, airports and communication infrastructure, where major bugs must not slip through.

## Do this
- Estimate your test matrix early: multiply characters × opponents × moves × items × player counts × stages/hazards × progression modifiers. That shows where full coverage is impossible and where you must prioritize.
- Put the first and heaviest test passes on interactions where one entity takes control of another (grabs, throws, restraints), especially when triggered while the target is in a special state such as a special move.
- For cutscene-style moves that change scenes, test that every captured character is restrained and released correctly and that nothing from one scene leaks into the other.
- If players can build levels, decide which terrain shapes you support, stress-test V-shaped geometry for collision bugs, and accept a few issues at the extremes.
- Budget extra test time for every parameter, growth or unlockable-skill system you add, since each one multiplies the states to check.
- After each bug fix, run regression checks across related systems before releasing the patch, instead of shipping the fix right away.

## Avoid
- Brute-forcing every combination instead of targeting likely problem areas.
- Rushing a hotfix out without re-checking. A fix can introduce new bugs.
- Holding a game to a "completely bug-free" standard. It would make release practically impossible.

## Examples from the episode
- **Smash Bros. Ultimate — fighter pairings:** 89 fighters ≈ 8,000 combinations, before moves, items, extra players, stages, hazards and spirits.
- **Smash Bros. Ultimate — grabs and throws:** grabbing a fighter mid special move causes processing contradictions.
- **Smash Bros. Ultimate — Final Smashes with scene changes:** fighters must be restrained and released, and the two scenes kept separate.
- **Stage Builder:** extreme terrain, especially V-shaped terrain, produces collision issues.
- **Spirits:** a wide array of extra mechanics, a "gargantuan task" to test.

## Quote
> If people get the idea that a game has to be completely bug-free, it will end up practically impossible to release games. (03:37)

## Tags
`bug-testing` `regression-testing` `scope` `updates` `collision` `smash-bros`
