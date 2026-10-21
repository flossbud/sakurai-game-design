# 049 · Making Lead-ins Instant and Impactful

**Category:** Animation · [Video](https://www.youtube.com/watch?v=E8DKndKkHw8) · [Transcript](../transcripts/049-making-lead-ins-instant-and-impactful.md)

## In one sentence
Change the character's pose the instant the attack button is pressed so players know their input registered, and size each windup by weighing responsiveness against impact and online lag.

## Key ideas
- The lead-in (also called anticipation or windup) is the pose between the button press and the actual attack. When charging a Smash Attack in Smash Bros. Ultimate, the character holds the lead-in pose and shakes in place.
- Smash differs from most games here: the moment the button is pressed, the pose changes drastically. Normally you would interpolate from the standby pose so the animation doesn't skip, but in Smash responsiveness comes first.
- Lag from the network or the TV can't be fully removed, but you can show players right away that their input was received. That is the ideal.
- Some attacks have no lead-in at all: Zero Suit Samus's neutral attack comes out one frame after input, and Final Fight's jab is instant and can be thrown out quickly and repeatedly. A game doesn't need lead-ins to work.
- Faster isn't always better. Online, a windup helps cover gaps caused by network lag, and without a big windup an attack can lack visual impact. Whatever you choose, think about input response.

## Do this
- On the first frame after an attack press, jump straight to a clearly different lead-in pose instead of interpolating out of the idle stance.
- For charge attacks, hold the lead-in pose and shake the character in place while the button is held.
- Give quick, spammable moves like jabs no lead-in at all, with the hit coming out the frame after input.
- Give heavy attacks a big, readable windup for visual impact and to absorb network lag online, while keeping its first frame instant.
- When reviewing each attack, count the frames until the player sees their press acknowledged, and treat that number as a design value.

## Avoid
- Smoothly interpolating from the standby pose into the windup, which delays the visible response to the press.
- Making every attack as quick as possible, which loses visual impact and the windup's cover for online lag.

## Examples from the episode
- **Super Smash Bros. Ultimate — charging a Smash Attack:** the fighter snaps to the lead-in pose on the press, then pauses and shakes.
- **Super Smash Bros. Ultimate — Zero Suit Samus's neutral attack:** no lead-in; it comes out one frame after input.
- **Final Fight — jab:** instantaneous and easy to throw out many times.

## Quote
> There's no way to completely eliminate lag from network or TV problems, but we can let players know right away that their input was received. (01:01)

## Tags
`anticipation` `responsiveness` `animation-timing` `feedback` `impact` `combat` `smash-bros`
