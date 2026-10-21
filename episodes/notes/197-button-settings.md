# 197 · Button Settings

**Category:** UI · [Video](https://www.youtube.com/watch?v=8nfMt4oG6hg) · [Transcript](../transcripts/197-button-settings.md)

## In one sentence
Every game, however simple, should let players reassign buttons, ideally through a graphical controller screen, cursor-based assignment, shared actions and saveable profiles.

## Key ideas
- Sakurai believes every game, no matter how simple, should offer a key config for changing button assignments.
- Button setting screens are design-heavy, and making every developer build their own adds a lot of work. It would be great if consoles let you customize controls game by game, but that hasn't really happened yet.
- Since the Wii, his games have had to support many different controllers, and because Smash Bros. is played together, guest players needed an easy way to set their controls. That led to these decisions:
  - **Controllers are drawn graphically.** Many games use a vertical list, which is easier to make, but it's hard for players to keep track of which button does what.
  - **Pick the button with the cursor, then pick its action.** Some games make you press the button itself to assign it, but the key config screen is a menu and needs an exit button. If pressing that exit button starts reassigning it instead, you have a problem.
  - **Several buttons can share an action.** Smash Bros. has two jump buttons, and you can reassign one of them if you want.
  - **Settings are saved under a profile name.** Choosing your profile before a fight switches to your controls, which helps when there are lots of guest players.
  - **Settings can live on the controller.** When possible, players can store their settings on the actual controller and take them along.
- Confirm and cancel buttons differ by platform. In Japan, PlayStation consoles from the PS5 on use X to confirm and O to cancel, as the rest of the world always has; in Japan it used to be the reverse. The PS4 offered an option to make X confirm, which feels natural because that's where confirm sits on PC and Xbox controllers. That leaves Switch as the only console with the placements reversed.
- Switch lets you change button settings for the whole console, but that affects every application and every game. If that leaves some buttons unmapped, you can't perform the matching actions.
- A button settings screen is a pain for creators to build, but some players need it, so add it whenever possible.

## Do this
- Ship a key config screen in every game, including small and simple ones.
- Show a picture of the controller with each button labeled by its action, instead of a plain vertical list.
- Let players select a button with the cursor and then choose its action from a list, rather than "press the button to assign", so the menu's own exit button never gets captured.
- Allow more than one button to trigger the same action (for example, two jump buttons), and let each one be reassigned on its own.
- Save layouts under player profile names that can be picked right before a match, and store them on the controller itself if the hardware allows.
- Check that no essential action can be left without a button after remapping.

## Avoid
- Vertical-list key configs where players lose track of which button does what.
- "Press the button you want" assignment that conflicts with the menu's exit button.
- Remapping schemes, like a console-wide one, that can leave actions with no button assigned.

## Examples from the episode
- **Smash Bros. — controls setup:** graphical controllers, cursor assignment, two jump buttons, profile names chosen before a fight, and settings saved on the controller, built to support many controllers and guest players since the Wii era.
- **PS5 / PS4 (Japan):** X now confirms and O cancels; the PS4 offered an option to make X confirm.
- **Nintendo Switch:** the only console with reversed placements, and its console-wide remap can leave actions unmapped in games.

## Quote
> However, it's a necessity for some of our players. Whenever possible, I urge you to add support for this feature. (02:57)

## Tags
`button-remapping` `controls` `menus` `accessibility` `multiplayer` `hardware` `smash-bros`
