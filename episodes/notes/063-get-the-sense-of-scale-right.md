# 063 · Get the Sense of Scale Right

**Category:** Graphics · [Video](https://www.youtube.com/watch?v=A6Rbb5sK4nI) · [Transcript](../transcripts/063-get-the-sense-of-scale-right.md)

## In one sentence
Make big objects feel big through texture scale, restrained saturation and gloss, matching normal maps and surface detail rather than through shape, because CG objects naturally look like scale models.

## Key ideas
- One adjustment Sakurai asks for very often when supervising graphics is to "get the sense of scale right." A huge object and a plastic model of it share the same shape and color, so the same shape can give very different senses of scale.
- Big things looking too small is the usual problem; small things looking too big is rare. Final rendering affects it a lot (aerial perspective, ambient light, ray tracing, toy-camera effects and miniature faking), but the episode focuses on how one model can read at different scales.
- **Textures:** a common mistake is a texture loop that isn't big enough or material painted too small, as with the off-color spots on tiles and the hue variation in grass. Increase the scale and look at it from farther away.
- **Saturation and gloss:** an oversaturated texture is less affected by ambient light and looks more fake, so don't overdo saturation when going for realism. Specularity (gloss) is especially hard to get right; too much makes things look like toys. Some large objects do need gloss, but limiting its area and strength changes the result drastically. These adjustments come after the game's atmosphere is established.
- **Normal maps and detail:** normal maps (similar to bump maps, though flat) must match the asset's scale or the result feels off. Large mechanical objects need details like dirt, and even grayscale or monotone plating benefits from mixed hues.
- **Shape is lower priority**, since the plastic model has the same shape as the real thing. Compared with the real object, the scale model is more saturated, has stronger and wider specularity, is less affected by ambient light, and its similar materials look flatter and more uniform. CG objects normally look like a scale model, so you have to make up that difference. Choose a style that fits the game and consider the big picture, not just the model.

## Do this
- Review large objects in-scene from a distance and ask whether they read as huge or as a toy; fix materials before touching the shape.
- Enlarge texture repeat loops and the scale of painted details (tile spots, grass hue variation) until the pattern no longer betrays a small object.
- Lower texture saturation on realistic assets so ambient light can affect them.
- Shrink the glossy area and lower specular strength on large objects.
- Check that normal-map detail matches the asset's real-world size, add dirt to big mechanical objects, and mix subtle hues into gray or single-color surfaces.
- Make these scale adjustments after the game's overall atmosphere and lighting are set.

## Avoid
- Texture loops that are too small, or material detail painted too small.
- Oversaturated textures on assets meant to look real.
- Heavy, wide gloss that makes large objects look like toys.
- Normal maps whose detail doesn't match the asset's scale.

## Examples from the episode
- **A real object vs. its plastic scale model:** same shape and color, but the model is more saturated and glossier, barely affected by ambient light, and flatter in material.
- **Tile and grass textures:** off-color tile spots and grass hue variation that need a larger loop to read at the right scale.

## Quote
> Normally, objects made in CG will look more like a scale model, so you have to find ways to make up that difference. (03:08)

## Tags
`scale` `textures` `materials` `lighting` `color` `art-direction`
