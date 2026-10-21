# 033 · Text Size

**Category:** UI · [Video](https://www.youtube.com/watch?v=W1ubngQNJpw) · [Transcript](../transcripts/033-text-size.md)

## In one sentence
Size and lay out text for each language (kanji need bigger characters, alphabetic text needs more length) and check it on the real target screen so it is never too small.

## Key ideas
- Japanese players often wonder why text in overseas games is so small. The appropriate text size varies from language to language.
- Kanji pack a lot of meaning into each character, so the characters need to be larger, but fewer are needed. English letters are visually simpler and legible at smaller sizes, but more of them are needed, and French sentences tend to run even longer. Each language needs its own way of fitting information into the space.
- If you design a layout with only English in mind and no flexibility for other languages, the translated text may end up too small.
- This is less common than it used to be: developers are more aware, resolutions are higher, and fonts are easier to scale. Some games let players choose the font size, which is extremely accommodating and easier to add to games with a clean interface and more screen space for text.
- Handheld games (such as on Nintendo Switch) usually use larger fonts, probably because developers check them on the actual handheld and quickly spot text that's too small. Text that's too big may not look stylish, though.
- On low-resolution consoles like the NES, developers crammed kanji into 8x8 sprites, and players' brains filled in the missing detail.

## Do this
- Design text boxes and UI layouts with room for every target language: larger glyphs for Japanese or Chinese, longer strings for English and especially French, instead of sizing everything to English.
- Check each localized build's text size on the actual target display (for handheld games, on the handheld itself) throughout development.
- Offer a player-selectable font size where your interface has the space for it.
- Keep the interface clean so there's spare screen space for text to grow.
- Balance readability and style: make text large enough to read, but not so large it stops looking stylish.

## Avoid
- Laying out UI with only English in mind.
- Text so large it no longer looks stylish.

## Examples from the episode
- **Japanese vs. English vs. French text:** kanji are large but few; English is small but needs more letters; French runs longer still.
- **Nintendo Switch handheld games:** usually larger fonts, because developers check them on the actual handheld.
- **NES — kanji in 8x8 sprites:** developers squeezed kanji into tiny sprites and players' brains filled in the detail.

## Quote
> This is something I'd like to impress on developers both in Japan and abroad: the appropriate text size will vary from language to language. (00:04)

## Tags
`localization` `readability` `accessibility` `hud` `menus` `fonts` `hardware`
