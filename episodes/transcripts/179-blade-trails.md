# 179 · Blade Trails

- **Category:** Effects
- **Video:** https://www.youtube.com/watch?v=X0GdWg2Q7z8
- **Length:** 03:59
- **Source:** official English subtitles burned into the video, read by OCR (tools/ocr_subs.py). Expect rare OCR typos.

---

[00:03](https://youtu.be/X0GdWg2Q7z8?t=3) The effects left behind after a sword swing are called "blade trails." At least, I've always called them that, but I'm not sure there's a universal term that everyone uses for them. Either way, I'll be calling them blade trails for this video.

[00:20](https://youtu.be/X0GdWg2Q7z8?t=20) This effect you get when swinging a sword was used quite commonly in older 2D games, but pulling it off in a 3D space is a different matter entirely. but pulling it off in a 3D space is à different matter entirely. In Smash Bros., we naturally add blade trails for swords, but also apply a similar effect to punches and kicks to expand upon the blur those create.

[00:42](https://youtu.be/X0GdWg2Q7z8?t=42) But let's put that aside for now. There are two primary ways to depict the blade trail of a sword. One is constructing the path the sword travels out of polygons. This is the much more common method.

[00:55](https://youtu.be/X0GdWg2Q7z8?t=55) It may be easier to understand if you picture a folding fan— the sword is the leading edge of the fan, and polygons are drawn behind it as it moves. Often, we'll make the tail end translucent to make it look like it's fading out. Since the sword moves so fast, simply following its path will tend to result in an angular appearance.

[01:18](https://youtu.be/X0GdWg2Q7z8?t=78) Also, the effect can sometimes be almost imperceptible when viewed from the side. To make the blade trail stand out better, we'll commonly make corrections to the animations. In most cases, a plain horizontal slash won't work too well. Getting back to what I was saying, the other way of depicting blade trails is with 2D meshes.

[01:39](https://youtu.be/X0GdWg2Q7z8?t=99) We rarely employ this method. But we do use it for faster sword animations that finish in a single frame. The sword ends its swing almost instantly, so the blade trail is only shown for a moment. For blade trails like this, we use a 2D mesh—a single flat image.

[01:58](https://youtu.be/X0GdWg2Q7z8?t=118) It may be there for just an instant, but since hit stop occurs if the attack lands, your eyes can still register it. That aside, though. While all sword swings might seem similar, we actually use various different blade trails.

[02:14](https://youtu.be/X0GdWg2Q7z8?t=134) I'll show you a few now. Here is Lucina's. For her, we use a relatively standard blue blade trail." Here is Marth's.

[02:26](https://youtu.be/X0GdWg2Q7z8?t=146) Since the tip of his sword is stronger, we add some emphasis to the trail's edge.

[02:34](https://youtu.be/X0GdWg2Q7z8?t=154) Here is Ike's. He has a heavier sword, so we give it a more frenzied look. Here is Young Link's. His are a little rougher—almost like a strike rather than a slash.

[02:47](https://youtu.be/X0GdWg2Q7z8?t=167) Here is Pit's. His weapon has two colors, so the blade trails match that. Here is Shulk's. It has a sort of “electronic” feel.

[03:01](https://youtu.be/X0GdWg2Q7z8?t=181) As for Bayonetta... You could say she has her own unique flair. Here is Pyra's. We added flames to the blade trail to give the impression the sword is burning.

[03:16](https://youtu.be/X0GdWg2Q7z8?t=196) In the case of Mii Swordfighters, blade trails are tailored to each weapon.

[03:22](https://youtu.be/X0GdWg2Q7z8?t=202) Travis has a beam katana, so the trail doesn't fade out, instead emphasizing that the sword emits light.

[03:32](https://youtu.be/X0GdWg2Q7z8?t=212) Once you've made blade trails yourself, you'll understand just how difficult they can be. With 3D especially, adjusting animations can be time-consuming. Still, blade trails are a vital element. Attacks won't have the same oomph without them, so getting them right can have a tremendous impact.
