# 068 · Put Parameters in Brackets

**Category:** Programming & Tech · [Video](https://www.youtube.com/watch?v=v6ozfbqNa54) · [Transcript](../transcripts/068-put-parameters-in-brackets.md)

## In one sentence
In spec sheets, write each character-specific tunable value as a plain-language phrase in brackets with a placeholder for the number, so programmers know exactly what to expose and anyone can tune it later without misreading it.

## Key ideas
- Code and parameters are separate. The commands and formulas behind movement are the code, an instruction manual for the game's commands; numbers like movement speed and attack power are the parameters that flesh those commands out. The previous video covered parameters shared by all characters; this one covers character-specific movements and special actions from each character's spec sheet.
- **Workflow:** a planner turns the director's or game designer's ideas into spec sheets (blueprints); a programmer implements code from them so the character works in the build; then the planner fine-tunes the parameters. Barring bugs the programmer's job ends there, but parameters keep being tweaked for balance to the very end.
- You could write values like walking speed or special-move speed straight into the code and the game would work, but then every adjustment would need a programmer. Instead, parameters live in a reference table separate from the code that the planner can adjust at any time.
- Spec sheets must state clearly which parts should be separated out as parameters and communicate that to the programming team. Each parameter's meaning must be crystal clear to anyone, because several people usually tune them later.
- **Sakurai's three methods:** (1) write parameter info in plain language, (2) enclose parameters in brackets, (3) mark the value with "O". Example: "Initiate movement at [Special startup X-velocity is O]." "At the same time, decelerate by [Special X-deceleration is O/frame]." His rule is that anything inside brackets becomes a parameter. A separate file lists every bracketed phrase with its value next to it, so tuning means editing those values.
- Most people (Sakurai included, once) just write "X-velocity" or "X-deceleration" and rely on the names. Plain-language brackets make it clear what you want to fine-tune and leave no room for misinterpretation. The notation works best for unique specs, less well for global values like general attack power. You won't get far with tuning if you can't explain things clearly.

## Do this
- Keep tunable numbers (speeds, decelerations, timings) out of the code, in an external table that designers can edit without a programmer.
- In spec sheets, wrap every value you want exposed in brackets as a plain-language phrase, e.g. "[Special startup X-velocity is O]", and adopt the team rule that anything in brackets becomes a parameter.
- Mark the value itself with a placeholder ("O") and include units where they matter, such as "O/frame".
- Maintain a separate parameter list that pairs each bracketed phrase with its current value, and do all tuning there.
- Use this notation for character- or move-specific specs, and handle global values like general attack power separately.

## Avoid
- Hard-coding parameters so that every tweak has to go through a programmer.
- Labeling parameters only with terse names like "X-velocity" that others may misread.

## Examples from the episode
- **Sakurai's spec sheet notation:** "Initiate movement at [Special startup X-velocity is O]." / "At the same time, decelerate by [Special X-deceleration is O/frame]." This describes a horizontal dash that decelerates as it goes.

## Quote
> I established a rule that anything inside brackets is turned into a parameter. (03:22)

## Tags
`specs` `numbers-tuning` `communication` `balance` `iteration` `parameters` `tech`
