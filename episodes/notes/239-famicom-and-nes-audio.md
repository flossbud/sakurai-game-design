# 239 · Famicom and NES Audio

**Category:** Audio · [Video](https://www.youtube.com/watch?v=eyQSb_tC0Fg) · [Transcript](../transcripts/239-famicom-and-nes-audio.md)

## In one sentence
A Grab Bag-style history of the Famicom's five sound channels and the expansion hardware that changed its music across regions, showing how hard limits shaped game audio.

## Key ideas
- Sakurai can't think of another platform whose audio evolved so much over its lifetime.
- The Famicom's sound chip had two pulse wave channels, one triangle wave channel, one noise channel and one DPCM channel.
- Pulse waves, shaped like a castle's parapets, make a crisp, steady beep and carried most Famicom music. Changing the wave's time ratio (the "duty cycle") changes the texture. The triangle wave sounds mellower or muffled and was commonly used for bass; on the Famicom it was actually a pseudo-triangle. Noise was used less for music and more for effects like hits, explosions, cheers and waves.
- Music and sound effects shared the same five channels, so when an effect played, part of the music often had to cut out.
- DPCM allowed sampling (recording your own sounds), though not as cleanly as today. The best-known example is probably the timpani in Super Mario Bros. 3. It existed from the start but took a lot of cartridge space, so it was rare early in the console's life; later titles with bigger ROMs and better technology felt like a dramatic leap.
- The Famicom Disk System added a "wave memory" channel with a more sustained sound. Many Famicom cartridges also had expansion audio chips built in for higher-quality sound.
- The Disk System never came out outside Japan, and the NES removed the cartridge connector pins used for expansion audio, so overseas cartridges couldn't use those chips and several games sounded different between regions. Later, larger ROMs let developers close the gap with DPCM. He recommends Silver Surfer on the NES, and Naoki Kodaka's Sunsoft work on Journey to Silius and Super Spy Hunter.

## Do this
- When music and sound effects share a limited pool of voices or channels, decide in advance which music part drops out when an effect needs one.
- Assign each sound role a fitting timbre, as Famicom composers did: crisp pulse-style tones for the main music parts, a mellow triangle-style tone for bass, and noise for hits, explosions and similar effects.
- When shipping on several hardware variants or regions, check that every audio feature you rely on exists on each, or provide a fallback, so the music doesn't feel different between versions.
- Study Silver Surfer (NES) and Naoki Kodaka's Sunsoft soundtracks (Journey to Silius, Super Spy Hunter) for what tight limits can still achieve.

## Examples from the episode
- **Super Mario Bros. 3 — timpani:** the most famous DPCM sample.
- **Famicom Disk System:** added a wave memory channel.
- **Japanese vs. overseas versions:** the NES lacked expansion-audio pins, so several games' music felt different abroad.
- **Silver Surfer (NES):** "incredible" music from the era of larger ROMs.
- **Journey to Silius, Super Spy Hunter (Sunsoft, Naoki Kodaka):** fantastic work on the hardware.

## Quote
> Considering the limited capabilities creators of the time had to work with, I can't help but be fascinated with taking a closer look at the technology itself. (05:56)

## Tags
`history` `music` `sound-effects` `hardware` `mixing` `chiptune`
