# 208 · Bug Testing Systems

**Category:** Team Management · [Video](https://www.youtube.com/watch?v=mQJEWMmZutA) · [Transcript](../transcripts/208-bug-testing-systems.md)

## In one sentence
Run bug testing as a dedicated, ticket-driven system (latest daily build, systematic coverage, severity classes, routing to whoever can fix it, tickets kept as resolved), because every fix can create a new bug.

## Key ideas
- Every game needs a system for finding and fixing bugs. A release version usually has only a handful of bugs, but countless ones were fixed to get there. Having programmers and other people who fix bugs do the playtesting wastes a lot of time, so almost every project has a dedicated bug-testing team, and some companies specialize in it.
- The basic rule is that everyone uses the latest daily build. Bugs found on the wrong version aren't helpful and can cause problems.
- Testers don't play aimlessly. They work through design documents to test combinations, split into subteams that each check one part of the game, and make checklists.
- Once someone finds a bug and can reproduce it, they report it as a ticket, a task written and tracked online. Managing and assigning tickets makes it less likely that anything gets overlooked.
- A manager assigns a class by severity. **Class S** covers hangs and bugs that might corrupt save data. **Class A** covers bugs that stop players from progressing. Lower-class bugs are sometimes waived on purpose.
- The manager also assigns each bug to a subteam or person, and programmers aren't always the right choice: artists fix character problems and animators fix broken animations. After a fix, the ticket goes back to the tester, who confirms it in a variety of configurations. The ticket is then set to "resolved" rather than discarded, in case the bug comes back.
- Related tickets get cross-referenced or merged, and people help teammates who have too many tickets. "Visualizing tasks is vital."
- Testing is hardest in games with near-limitless combinations, like Smash Bros., and open-world games are tough too. Smash sometimes ran CPU battles all night to find bugs. Near the end of a project, testers in Japan, North America and Europe pass save data back and forth for worldwide testing.
- Every fix can introduce new bugs, so being careful can't prevent them all. The goal is to find and fix them quickly.

## Do this
- Require every tester to be on the latest daily build before filing a report.
- Have testers work from the design documents and checklists, split into subteams by game area, and test feature combinations systematically instead of free-playing.
- Turn a bug into a ticket in an online tracker only once it has reproduction steps.
- Give every ticket a severity class (S for hangs or save corruption, A for progression blockers, lower classes that may be waived) and assign it to the discipline that owns the problem, such as art, animation or code.
- After a fix, send the ticket back to the tester to verify in several configurations, then mark it resolved rather than deleting it. Cross-link related tickets.
- For games with huge numbers of combinations, run automated CPU-vs-CPU sessions overnight to catch bugs.

## Avoid
- Using programmers as your main playtesters, which wastes their time.
- Accepting bug reports from outdated builds.
- Deleting closed tickets, which loses the history you need if the bug comes back.
- Believing that being careful will stop fixes from introducing new bugs.

## Examples from the episode
- **Smash Bros.:** near-limitless combinations make it one of the hardest games to test, so CPU battles ran all night to find bugs.
- **Global playtests:** testers in Japan, North America and Europe pass save data back and forth near the end of a project.
- **Open-world games:** hard to test because the player can go almost anywhere.

## Quote
> However, the trickiest thing about bugs is that whenever you resolve one, you run the risk of introducing new bugs. (03:46)

## Tags
`bug-testing` `qa` `playtesting` `debug-tools` `builds` `delegation` `communication` `smash-bros`
