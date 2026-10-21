# 172 · How Multiple People Work on One File

- **Category:** Programming & Tech
- **Video:** https://www.youtube.com/watch?v=s5u7VqDl-1I
- **Length:** 02:40
- **Source:** official English subtitles burned into the video, read by OCR (tools/ocr_subs.py). Expect rare OCR typos.

---

[00:04](https://youtu.be/s5u7VqDl-1I?t=4) If you have a large team, you might have hundreds of people working to create the same game. A times, one perșon ight be editing a file when someone else tries to make changes, which might make you wonder: how do they avoid file conflicts?

[00:21](https://youtu.be/s5u7VqDl-1I?t=21) At least, I wondered that myself once. So today, I'll give you an overview of how it works. I'll keep it simple.

[00:33](https://youtu.be/s5u7VqDl-1I?t=33) A game in development is divided into countless files. It might be tens of thousands, hundreds of thousands, or even millions of files— but the larger your game's scope, the more files you'll end up having. There are various ways of handling this, but in most cases, those files are tracked using some kind of management tool.

[00:55](https://youtu.be/s5u7VqDl-1I?t=55) All files get put up on a server. When someone's editing a file, that file gets locked. When they're done, the edited file is then uploaded back to the server and it gets unlocked.

[01:12](https://youtu.be/s5u7VqDl-1I?t=72) And that's basically it, over and over again. However, if you need to edit a particularly large file, only letting one person work on it at once can be a bit inefficient. You may also somehow end up with two conflicting edits, meaning two or more people managed to upload changes at the same time.

[01:31](https://youtu.be/s5u7VqDl-1I?t=91) In such cases, the management tool will attempt to merge the files. In other words, it will compare the edits and stitch them together into one file. Sometimes that's all it takes to resolve the problem, but if the discrepancies don't go away, someone will have to go in and fix them manually.

[01:49](https://youtu.be/s5u7VqDl-1I?t=109) Things will generally proceed like this, so in theory, you would expect everything to continue without a hitch— but then for some reason, the file gets reverted. Reversion is when a person's changes vanish without so much as a trace, and the file returns to how it was before it was edited.

[02:05](https://youtu.be/s5u7VqDl-1I?t=125) For whatever reason, it's a common occurrence.

[02:10](https://youtu.be/s5u7VqDl-1I?t=130) Management tools create a backup every time an edit takes place, so if you're lucky, you might be able to retrieve your changes by going back a version. There shouldn't be any issues, in theory— but in practice, it's a constant source of headaches. Still, plenty of projects rely on these puzzling management tools, even today.

[02:29](https://youtu.be/s5u7VqDl-1I?t=149) And that's it!
