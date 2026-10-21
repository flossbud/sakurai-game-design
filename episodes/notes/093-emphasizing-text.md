# 093 · Emphasizing Text

**Category:** UI · [Video](https://www.youtube.com/watch?v=bZSNYX5CVpw) · [Transcript](../transcripts/093-emphasizing-text.md)

## In one sentence
In text-heavy games, use text effects (size, color, animation, font) to convey emotion, and build them as editable script so translators can restyle the emphasis for each language.

## Key ideas
- Works built around reading often use effects that change how text appears: font size, color, animation, a different font, and so on. Screen shake and flashes can do similar jobs, but this episode is about the text itself.
- Text effects may not suit more serious titles. Still, changing how certain letters or words appear helps convey a character's emotions and adds flavor to a plain presentation, which makes such effects almost essential.
- Design the system so that translators can directly adjust the scripting (the bits of code that trigger the effects) when the game is localized. It's better left to the translation team than to developers, because different languages emphasize things in different ways.
- Japan's long comics culture is full of techniques like kakimoji (sound effects written into the background) and manpu (symbols like a bead of sweat or a vein mark, which don't happen in real life but have a clear meaning, often an emotion). Changing fonts or speech-bubble styles packs a lot of expression into a small space.
- Given that history, using only one text size feels almost wasteful, and it's worth pushing for more. But not every language benefits from text effects the same way, so native speakers should decide what reads naturally.
- Text display is about as basic as features get, but in a game with lots of reading, going the extra mile in how it's expressed can pay off.

## Do this
- Add inline markup to your dialogue system for size, color, animation and font changes, applied to individual words or letters.
- Store these tags in the localizable script itself, so translators can add, remove or move emphasis per language without a programmer.
- Ask native-speaker translators to decide how emphasis should look in their language instead of copying the source-language styling.
- Use different speech-bubble styles and simple emotion symbols to pack more expression into limited screen space.

## Avoid
- Hardcoding text effects in code where translators can't adjust them.
- One flat text style throughout an expressive, text-heavy game. He calls that almost wasteful.

## Examples from the episode
- **Japanese comics — kakimoji and manpu:** written-in sound effects and symbols (sweat beads, vein marks) that express emotion clearly in little space.

## Quote
> It's best to let native speakers from each country consider natural presentation, which is exactly why you want to make it so that translators can edit the scripting themselves. (01:50)

## Tags
`localization` `text-effects` `readability` `story` `clarity` `help-text`
