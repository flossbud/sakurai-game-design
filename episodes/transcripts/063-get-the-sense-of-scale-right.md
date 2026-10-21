# 063 · Get the Sense of Scale Right

- **Category:** Graphics
- **Video:** https://www.youtube.com/watch?v=A6Rbb5sK4nI
- **Length:** 03:52
- **Source:** official English subtitles burned into the video, read by OCR (tools/ocr_subs.py). Expect rare OCR typos.

---

[00:04](https://youtu.be/A6Rbb5sK4nI?t=4) When overseeing a game's graphics, one adjustment I very frequently ask for is to "get the sense of scale right."

[00:14](https://youtu.be/A6Rbb5sK4nI?t=14) For example, a large object in a stage may end up looking like something small. If you think about it, a huge object and a plastic model of that object generally share the same shape and color. This tells us that even objects with the same shape can give us very different senses of scale.

[00:33](https://youtu.be/A6Rbb5sK4nI?t=33) In most cases, this will manifest as big things looking smaller than they're supposed to. You don't see small things looking too big very often. This issue also tends to be heavily dependent on the final visuals in a game. Aerial perspective, ambient light, and ray tracing have a clear impact, as does a toy camera effect, or miniature faking in the rendering.

[00:59](https://youtu.be/A6Rbb5sK4nI?t=59) But let's put that aside. Instead, we should think about how a single model can have different senses of scale. Its textures, for example. Does the art applied to the model make it look real, or fake?

[01:13](https://youtu.be/A6Rbb5sK4nI?t=73) When creating textures like these, a common mistake is not making a big enough loop, or painting the material too small. For this example, take note of the off-color spots on each tile, and minor hue variations in the grass.

[01:29](https://youtu.be/A6Rbb5sK4nI?t=89) You need to increase the scale and look at it from farther away. Oh, and if your texture is too saturated, it'll be less affected by ambient light— which will make it look more fake. If you're going for realism, don't overdo it on the saturation.

[01:49](https://youtu.be/A6Rbb5sK4nI?t=109) Of course, these adjustments should come after you establish the game's atmosphere. I find that “specularity," or a glossy look, is particularly difficult to get right. I find that “specularity,” or a glossy look, is particularly difficult to get right. Too much gloss will make things look like toys.

[02:03](https://youtu.be/A6Rbb5sK4nI?t=123) Some larger objects do need that gloss, but limiting the surface area and specular strength will produce drastically different results. On that note, let's discuss “normal maps." Normal mapping lets us add additional information to the texture to determine where light will reflect.

[02:22](https://youtu.be/A6Rbb5sK4nI?t=142) It's similar to bump mapping, even though it's flat. If this doesn't match the scale of your asset, the end result will feel pretty off. With large, mechanical objects, you'll also need details like dirt.

[02:36](https://youtu.be/A6Rbb5sK4nI?t=156) And even if an object is meant to be grayscale or another kind of monotone, it's still good to mix different hues into the plating for variety. And so on. I've given a lot of examples, but you'll notice I never mentioned the shape of the model.

[02:53](https://youtu.be/A6Rbb5sK4nI?t=173) There certainly are things to watch out for with shape, but I'd consider those lower priority than the other points I've raised. And like I showed you, the plastic model is the same shape as the real thing. Let's compare the two again.

[03:08](https://youtu.be/A6Rbb5sK4nI?t=188) The scale model appears more saturated, with stronger, wider specularity. It isn't affected much by ambient light. Similar materials look flatter and more monotone. Normally, objects made in CG will look more like a scale model, so you have to find ways to make up that difference.

[03:31](https://youtu.be/A6Rbb5sK4nI?t=211) As always, it's important to choose a style that fits your game's needs. Don't think of it as just making a model, and do your best to consider the big picture!
