# 046 · Making Your Game Easy to Tune

**Category:** Programming & Tech · [Video](https://www.youtube.com/watch?v=nGaajB8m5Q0) · [Transcript](../transcripts/046-making-your-game-easy-to-tune.md)

## In one sentence
Move every tunable value out of code into designer-editable parameters, with formulas, hidden rarely used fields and one-button conversion to running builds, so tuning iterations are fast.

## Key ideas
- Fine-tuning is a vital process. Sakurai can't share trade secrets or screens from the dev environment, but he outlines the approach.
- Programmers are asked to reference "parameters," the group of values that might need tuning later. For a move with an attack power of 10, the code makes the move happen, but the 10 is a separate parameter designers can adjust. Writing 10 straight into the code would mean diving into the code for every adjustment, which creates real problems.
- Code is the bones and parameters are the muscles: change the muscles and the same bones behave in drastically different ways.
- Parameters live in their own Excel document. A single Smash attack has many parameters, so less-frequently adjusted ones can be hidden, which reduces human error and makes the important values easier to find.
- Excel formulas let parameters refer to each other to keep relative balance, for example making one move always 1/2 as strong as another.
- "Conversion" puts the spreadsheet data into a build where it can be tested. An Excel add-in does it with one button press, updating all active dev kits; he credits Bandai Namco Studios' well-built environment. For the original Smash and Melee, each conversion took ten minutes, even for the smallest tweak, plus a reboot, and he edited text files by hand, so he wrote every parameter in the game himself.
- Since Smash for Wii U/3DS, parameters are kept so more people can adjust them easily, which makes trial and error easy and lets the team tune more values more deeply. Tuning is where you iterate most, so make it as efficient as possible.

## Do this
- Move every value you might tune (damage, speeds, timings and so on) out of code into a parameter file or spreadsheet that designers can edit without touching code.
- Hide rarely adjusted parameters in the editing view so the important ones are easy to find and mistakes are fewer.
- Use formulas to link related parameters (e.g., one move's power = 1/2 of another's) so balance holds when you change a base value.
- Build a one-step conversion that pushes edited parameters to every running test build or dev kit, replacing slow multi-minute conversions and manual reboots.
- Give more team members easy access to adjust parameters so tuning can happen through wider trial and error.

## Avoid
- Hard-coding tunable values directly into code.
- A slow conversion pipeline (ten minutes plus a reboot per tweak) that discourages iteration.
- Making one person the only one who can edit parameters.

## Examples from the episode
- **A move with attack power 10:** the code performs the move; the 10 lives in a separate, adjustable parameter.
- **Super Smash Bros. and Melee:** ten-minute conversions, reboots and hand-edited text files; Sakurai wrote every parameter himself.
- **Super Smash Bros. for Wii U/3DS onward (with Bandai Namco Studios):** an Excel add-in converts and updates all active dev kits with one button press.

## Quote
> You could say the code is the bones, and the parameters are the muscles. (01:14)

## Tags
`numbers-tuning` `iteration` `debug-tools` `balance` `parameters` `tools` `smash-bros`
