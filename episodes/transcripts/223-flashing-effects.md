# 223 · Flashing Effects

- **Category:** Effects
- **Video:** https://www.youtube.com/watch?v=Mmw39T_dBLI
- **Length:** 04:12
- **Source:** official English subtitles burned into the video, read by OCR (tools/ocr_subs.py). Expect rare OCR typos.

---

[00:07](https://youtu.be/Mmw39T_dBLI?t=7) “Flashing” refers to the effect used to make things like the screen or certain characters shine. That's what I call it, at least, but that's likely not the only term used for the effect.

[00:20](https://youtu.be/Mmw39T_dBLI?t=20) Due to stricter regulations nowadays, modern ports of classic games tend to keep the effect mild— but it was truly dazzling back in the day, especially on CRT screens! When using flashing to cover the entire game screen, it's similar to screen shake in that the large area provides more impact.

[00:41](https://youtu.be/Mmw39T_dBLI?t=41) Making a character flash lets you better emphasize changes to that character's status. Both are crucial. When making a character flash, it's common practice these days to use either additive blending or specific lighting.

[00:59](https://youtu.be/Mmw39T_dBLI?t=59) Additive blending refers to the process of adding a particular hue to a character. By rapidly alternating between normal colors and a version with white added, you can create a flash effect. However, when applying a color uniformly across an object, you'll unfortunately reduce its contrast. Equal amounts of the color end up getting added to both the dark areas and the light areas, making things average out and look too similar.

[01:26](https://youtu.be/Mmw39T_dBLI?t=86) Also, when making an object flash white, there's a chance you'll make the object less noticeable on a light background.

[01:37](https://youtu.be/Mmw39T_dBLI?t=97) When faced with this problem on my past projects, I made sure to combine both light and dark elements in the flashes. The dark parts would still stand out on a light background, making the image much more reādable. However, I tried something different on Smash Bros. Ultimate.

[01:55](https://youtu.be/Mmw39T_dBLI?t=115) If you simply brighten a character when they get hit, they'll vanish into the background like this. Instead, we chose to add shadows to the flashing effects to give them internal contrast. This image is the mockup I created to show the development team what I was proposing.

[02:16](https://youtu.be/Mmw39T_dBLI?t=136) And here's how it looks in the actual game. ..Can't see it? Actually, the effect is more pronounced if you zoom out. Pull the camera back, and look at what happens.

[02:28](https://youtu.be/Mmw39T_dBLI?t=148) I wish the effect could be stronger up close as well, but that would mean more of the screen flashing when the camera's zoomed in—and that's no good.

[02:39](https://youtu.be/Mmw39T_dBLI?t=159) Regular flashing effects also change in strength depending on camera distance. Here, the camera is close up.

[02:48](https://youtu.be/Mmw39T_dBLI?t=168) Here, the camera is far away.

[02:53](https://youtu.be/Mmw39T_dBLI?t=173) By the way, these white flashes show that the character is invulnerable.

[03:02](https://youtu.be/Mmw39T_dBLI?t=182) Characters are invulnerable when getting up, as you can see here.

[03:11](https://youtu.be/Mmw39T_dBLI?t=191) Note that a character will flash yellow when they get grabbed and thrown. This shows the period after they're thrown in which they can't be grabbed again.

[03:23](https://youtu.be/Mmw39T_dBLI?t=203) Lastly, let's discuss what can be expressed through lighting. In Smash Bros. Ultimate, we commonly use something known as rim lighting." It looks like there's light shining on characters from behind, thus emphasizing their outlines. In addition to certain damage types, we often use it to show status changes such as invulnerability.

[03:46](https://youtu.be/Mmw39T_dBLI?t=226) In almost all cases, flashing effects only last for a single, brief moment. Depending on an LCD screen's response time, they can end up looking different, making them difficult to get right— but considering the impact they add, they're worth taking the time to perfect.
