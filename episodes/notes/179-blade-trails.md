# 179 · Blade Trails

**Category:** Effects · [Video](https://www.youtube.com/watch?v=X0GdWg2Q7z8) · [Transcript](../transcripts/179-blade-trails.md)

## In one sentence
Give every swing a blade trail that suits the weapon, built as a fading polygon ribbon (or a one-frame flat image for instant swings), and adjust the animation until the trail reads clearly, because attacks lose their oomph without one.

## Key ideas
- "Blade trails" is Sakurai's name for the effect left behind by a sword swing; there may be no universal term. They were common in older 2D games, but doing them in 3D is a different matter entirely. Smash Bros. uses them for swords and also adds a similar effect to punches and kicks to extend their blur.
- **Method 1, polygons (the much more common one):** build the path the sword travels out of polygons. Picture a folding fan: the sword is the leading edge and polygons are drawn behind it as it moves. The tail end is often made translucent so it looks like it's fading out.
- Problems with method 1: the sword moves so fast that simply following its path tends to look angular, and the trail can be almost invisible from the side. To make trails stand out, the team commonly corrects the animations, and in most cases a plain horizontal slash doesn't work well.
- **Method 2, a 2D mesh (rarely used):** a single flat image, used for very fast swings that finish in one frame. The trail only shows for an instant, but because hitstop kicks in if the attack lands, your eyes can still register it.
- Sword swings look similar, but each fighter gets a different trail that fits the weapon and character (see the examples below).
- Blade trails are hard to make, and in 3D adjusting the animations takes a lot of time. They're still vital: without them attacks lack oomph, so getting them right has a tremendous impact.

## Do this
- Build sword trails as a ribbon of polygons swept behind the blade's path, with the tail fading out through translucency.
- Check every swing from the gameplay camera. If the trail looks angular or almost disappears from that angle, change the swing animation; don't rely on plain horizontal slashes.
- For swings that finish in a single frame, show one flat 2D trail image for that instant, and count on hitstop to hold it on screen long enough to read on hit.
- Give each weapon its own trail: an emphasized edge for a sword whose tip is strongest, a rough frenzied trail for a heavy blade, colors that match a two-tone weapon, flames for a burning sword, and no fade-out for a weapon that emits light.
- Add a similar trail or extended blur to punches and kicks, not only to weapons.

## Avoid
- Plain horizontal slashes whose trails vanish when seen from the side.
- Trails that simply trace the raw blade path and come out looking angular.
- One generic trail shared by every sword, when the trail could express each weapon's character.

## Examples from the episode
- **Smash Bros. — Lucina:** a relatively standard blue trail.
- **Smash Bros. — Marth:** extra emphasis on the trail's edge, because the tip of his sword is stronger.
- **Smash Bros. — Ike:** a heavier sword, so a more frenzied-looking trail.
- **Smash Bros. — Young Link:** rougher trails, closer to a strike than a slash.
- **Smash Bros. — Pit:** his weapon has two colors, and the trails match them.
- **Smash Bros. — Shulk:** a trail with an "electronic" feel.
- **Smash Bros. — Bayonetta:** her own unique flair.
- **Smash Bros. — Pyra:** flames added to suggest the sword is burning.
- **Smash Bros. — Mii Swordfighters:** trails tailored to each weapon.
- **Smash Bros. — Travis:** a beam katana, so the trail doesn't fade out, emphasizing that the sword emits light.

## Quote
> Attacks won't have the same oomph without them, so getting them right can have a tremendous impact. (03:32)

## Tags
`effects` `blade-trails` `impact` `hitstop` `animation-timing` `readability` `character-design` `smash-bros`
