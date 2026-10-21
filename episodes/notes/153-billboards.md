# 153 · Billboards

**Category:** Effects · [Video](https://www.youtube.com/watch?v=_o29OOOarPY) · [Transcript](../transcripts/153-billboards.md)

## In one sentence
Use billboards (flat images that always face the camera) for particles, light flashes and cheap objects because they render cheaply, but know their weaknesses: they look odd when the camera circles them, and misused Y-axis billboards look too skinny.

## Key ideas
- A billboard is a flat object that always faces the camera directly, usually a two-polygon mesh.
- In Super Mario 64, the iron balls rolling down the slope are billboards: each is a single image with no animation. King Bob-omb mixes the two techniques: his eyes, crown and more are 3D models, while his main body is a billboard.
- Particles and similar effects are generally displayed with billboards. Pause an explosion and rotate the camera and you see that it's just flat images, though extra touches like sparks are still needed.
- 2D objects have a relatively low rendering cost, and billboards are "just perfect for intangible effects such as flashes of light."
- Smash Bros. food items have traditionally been billboards, which is why they look a little strange when you rotate the camera around them.
- A "Y-axis billboard" faces the camera by rotating only around the Y-axis. Misused for effects, it can leave images that feel "a bit too skinny."
- Today's games are so detailed that billboards are nearly impossible to spot, so awareness of them has faded.

## Do this
- Build explosions, flashes and other intangible effects from camera-facing billboard particles, then layer extra elements such as sparks on top.
- Use billboards to save rendering cost on simple objects (e.g., a rolling ball, pickup items), and consider a hybrid: a billboard body with 3D-modeled parts attached.
- Orbit the camera around every billboarded object during review. If it looks wrong from some angles and players can see it that way, switch it to a model.
- Use Y-axis billboards only where an upright orientation makes sense, and check effects built with them so they don't read as too skinny.

## Avoid
- Misusing Y-axis billboards for effects, which makes images feel too skinny.
- Billboarding objects that players will look at from many camera angles. They look strange as the camera rotates.

## Examples from the episode
- **Super Mario 64 — iron balls:** single unanimated billboard images.
- **Super Mario 64 — King Bob-omb:** billboard body with 3D-modeled eyes and crown.
- **Smash Bros. — explosion:** flat images when paused and viewed from a rotated camera.
- **Smash Bros. — food items:** billboards that look odd when the camera rotates around them.

## Quote
> 2D objects have a relatively low rendering cost. And billboards are just perfect for intangible effects such as flashes of light. (01:06)

## Tags
`effects` `particles` `billboards` `rendering` `performance` `camera` `smash-bros`
