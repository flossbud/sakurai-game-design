# 197 · Button Settings

- **Category:** UI
- **Video:** https://www.youtube.com/watch?v=8nfMt4oG6hg
- **Length:** 03:20
- **Source:** official English subtitles burned into the video, read by OCR (tools/ocr_subs.py). Expect rare OCR typos.

---

[00:03](https://youtu.be/8nfMt4oG6hg?t=3) I believe that every game, no matter how simple, should let you change button assignments through a key config.

[00:13](https://youtu.be/8nfMt4oG6hg?t=13) Button setting screens are a rather design-heavy feature. Asking every developer to create their own leads to a lot more work during development. Thus, it would be great if the consoles themselves let you customize controls on a game-by-game basis, but that hasn't really happened yet.

[00:31](https://youtu.be/8nfMt4oG6hg?t=31) For games I've made, we've had to support lots of different controllers since the Wii came around. And Smash Bros. is meant to be played together, so we needed a way for guest players to easily set their controls. With all that in mind, here are some considerations we had to make during development. Controllers are all depicted graphically.

[00:56](https://youtu.be/8nfMt4oG6hg?t=56) Many games set up their key configs as a verticaí list, which is certainly easier to make— but it can be difficult for players to keep track of which button does what. Next, we made it so you use the cursor to choose a button, then pick an action to assign to that button. Some games make you press the button itself to assign it to an action, but we opted not to do that.

[01:25](https://youtu.be/8nfMt4oG6hg?t=85) The key config screen is a menu in itself, so players need a button to let them exit it. If pressing that exit button instead starts the process of changing the button's assignment, you'll end up with a bit of a problem. We also let multiple buttons share the same action.

[01:40](https://youtu.be/8nfMt4oG6hg?t=100) For example, there are two jump buttons in Smash Bros. You can assign one to a different action if you want. Additionally, button settings can be saved to a profile name. By selecting that profile name before a fight, you'll switch to those preset controls, which can help if you have lots of guest players.

[02:04](https://youtu.be/8nfMt4oG6hg?t=124) When possible, we've even let players store button settings on the actual controller to take with them. In Japan, PlayStation systems starting with the PS5 use X to confirm and O to cancel. It's always been that way in the rest of the world, but for us, it used to be the other way around.

[02:23](https://youtu.be/8nfMt4oG6hg?t=143) On the PS4, you had the option to change X to the confirm button, which feels natural enough, since that's where the confirm button is on a PC or Xbox controller, leaving Switch as the only console with the placements reversed. On Switch, you're able to change button settings for the entire console.

[02:41](https://youtu.be/8nfMt4oG6hg?t=161) However, that changes the for all applications, including how they work in every game. If, as a result, you end up with some unmapped buttons, you won't be able to perform any of the corresponding actions.

[02:57](https://youtu.be/8nfMt4oG6hg?t=177) For game creators, making a button settings screen can be a real pain in the neck. However, it's a necessity for some of our players. Whenever possible, I urge you to add support for this feature.
