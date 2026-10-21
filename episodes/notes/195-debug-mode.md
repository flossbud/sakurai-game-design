# 195 · Debug Mode

**Category:** Programming & Tech · [Video](https://www.youtube.com/watch?v=AdBcCQtuATc) · [Transcript](../transcripts/195-debug-mode.md)

## In one sentence
Give your team a well-organized debug mode, built into the normal controller through button combinations, because it's used every day and has a huge effect on productivity even though it's stripped from the final game.

## Key ideas
- During development, games have a "debug mode" or "developer mode" with a wide range of features. It's hard to sum up in a word, but it's used to test and analyze the game while it's being made.
- In Smash Bros. it's now easy to set every fighter to a given damage percentage. Before that feature existed, the team got the same result in other ways, such as setting Fox's forward tilt to deal 100% damage. Without the right debug features, you spend time inventing workarounds.
- The trajectory guide in Training Mode started as a debug feature Sakurai asked for. He worried it might reveal too much about how the game works, but included it because it's easy to understand.
- He also used debug mode to capture the Screenshot of the Day: pausing the action, turning fighters, adjusting camera zoom and changing the view angle. It had limits, though: fighters couldn't be moved closer to or farther from the screen, and objects could vanish from fighters' hands.
- Debug mode is often put on a separate controller, but he recommends combining debug and gameplay on a single controller, using button combinations, because hunting down that second controller every time is a real pain.
- Today it's standard to ship with debug modes fully stripped out. But teams use them every day, so they matter hugely for productivity. They also bloat easily, so keep them organized and pruned so development runs smoothly.

## Do this
- Build debug commands for the setups you test most often (for example, setting every character to a chosen damage percentage) instead of improvising workarounds like temporarily changing a move's damage.
- Put debug functions on button combinations of the normal gameplay controller rather than on a separate debug controller.
- Include a capture toolset for screenshots: pause, rotate characters, zoom and change the camera angle.
- Look for debug visualizations that are easy to understand, like a knockback trajectory guide, and consider shipping them in a training mode.
- Regularly organize and prune the debug menu so it doesn't bloat, and strip it from the release build.

## Avoid
- Missing debug features that force the team to spend time on workarounds.
- A separate debug controller that has to be hunted down every time.
- Letting the debug menu bloat into a disorganized mess.

## Examples from the episode
- **Smash Bros. — damage percentage:** now set directly; earlier faked by making Fox's forward tilt deal 100% damage.
- **Smash Bros. — Training Mode trajectory guide:** began as a debug feature Sakurai requested.
- **Smash Bros. — Screenshot of the Day:** captured with debug-mode pause, rotation, zoom and angle controls.

## Quote
> the convenience a debug mode provides will have a huge impact on a team's productivity. (02:09)

## Tags
`debug-tools` `tools` `productivity` `controls` `training-mode` `screenshots` `smash-bros`
