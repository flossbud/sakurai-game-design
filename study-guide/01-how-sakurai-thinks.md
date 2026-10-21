# 01 · How Sakurai Thinks

> Masahiro Sakurai (Kirby, Super Smash Bros., Kid Icarus: Uprising, Meteos) spent 261 episodes explaining how he designs games. Most of the episodes are small and specific: hitstop frames, help text, how fingers should grip a sword. Underneath them sit a dozen habits of mind that he applies to everything. This chapter names those habits so that the rest of the guide reads as one way of thinking rather than 800 separate rules. If you remember only one chapter, remember this one.

He states his purpose plainly: "help make games around the world a little more fun" ([1](../episodes/notes/001-about-this-channel.md)). He calls his advice a *boost* on top of your own experience, not a replacement for it ([1](../episodes/notes/001-about-this-channel.md), [261](../episodes/notes/261-masahiro-sakurai-on-creating-games-finale-special.md)). The same goes for this guide. Read it, then go make something and check it against what you learned.

---

## The habits

### 1. Find the game essence: risk and reward, close together

Sakurai's central idea is **game essence**: a game's *push and pull*, the fun of taking a risk to earn a reward. In Space Invaders you can only hit an invader by moving under it, which is also where it can hit you. In Super Mario Bros. the jump that dodges a Koopa Troopa is the same jump that stomps it. His rule: **risk and reward must be in close proximity, and in the right amounts** ([6](../episodes/notes/006-risk-and-reward.md)).

Everything else follows from that rule. Stress followed by relief, growth and then progress is the basic loop of play, so if you remove enemies you must still keep the stress ([9](../episodes/notes/009-squeeze-and-release.md), [71](../episodes/notes/071-do-we-really-need-enemies.md)). Every action verb should pair a danger with an opportunity ([193](../episodes/notes/193-game-essence-in-action-games.md)). Flight only feels good when falling is possible ([65](../episodes/notes/065-falling-sells-the-feeling-of-flight.md)). Stronger moves need longer recovery so that missing them can be punished ([82](../episodes/notes/082-do-competitive-games-have-to-be-complex.md)). When a genre fun is worth borrowing, *deconstruct, analyze and rebuild* it: find out why it's fun (usually its risk and reward) and rebuild that, rather than copying the surface ([57](../episodes/notes/057-deconstruct-analyze-and-rebuild.md), [86](../episodes/notes/086-game-essence-in-falling-block-puzzle-games.md), [134](../episodes/notes/134-game-essence-in-shooting-games.md)).

He is equally clear that essence is not everything. There is fun beyond push and pull ([26](../episodes/notes/026-fun-beyond-game-essence.md)): collection, simulation of work ([203](../episodes/notes/203-making-work-games-fun.md)), customization ([182](../episodes/notes/182-customization-lets-your-imagination-play.md)), spectacle. And **more game essence means less broad appeal** ([148](../episodes/notes/148-more-game-essence-means-less-broad-appeal.md)). See habit 7.

> "You can't be a chef if you can't discern taste." ([6](../episodes/notes/006-risk-and-reward.md), ≈07:01)

**Ask:** Where exactly is the risk in this mechanic, and is the reward sitting right next to it?

### 2. Take the player's side, every time

Players don't see your schedule, your tools or your team's struggles, and they "aren't going to cut you slack just because development was hard" ([21](../episodes/notes/021-try-telling-that-to-the-player.md)). When a compromise is convenient for developers but worse for players, look for another way. Game development is a job in service of the player, not a hobby that indulges your own taste ([7](../episodes/notes/007-game-development-isnt-a-game.md)). You'll forget the hardship, but the game will last, and every player multiplies the effect of your effort ([67](../episodes/notes/067-youll-forget-the-hardship-but-the-game-will-endure.md)).

This is why he praises players openly ([95](../episodes/notes/095-praise-the-player.md)), never leaves an input without a response ([104](../episodes/notes/104-dont-be-unresponsive.md)), never lets a cutscene take away a win the player earned ([113](../episodes/notes/113-game-writing-is-unique.md)), and treats the hard-won balance of a shipped game as something to protect with careful, narrow patches ([141](../episodes/notes/141-unexpected-results.md), [231](../episodes/notes/231-online-updates.md)).

**Ask:** Am I deciding this for the player's experience or for my own convenience?

### 3. The player's time is a cost you're charging them

> "The time players spend in a game is a cost, so it's best to be mindful of the time they're choosing to give you." ([250](../episodes/notes/250-be-mindful-of-the-time-players-are-giving-you.md), ≈02:31)

Slowness is the "one big trap to avoid", the thing "that might make it so nobody loves your game" ([73](../episodes/notes/073-say-no-to-slow.md)). So he cuts waits, loading fades and bloated cutscenes ([73](../episodes/notes/073-say-no-to-slow.md), [246](../episodes/notes/246-speedy-screen-transitions.md), [78](../episodes/notes/078-loading-screens.md)). He makes everything skippable and pausable ([180](../episodes/notes/180-let-them-skip-let-them-pause.md), [233](../episodes/notes/233-in-game-cutscenes.md)) and lets text advance as fast as the player can read ([211](../episodes/notes/211-advancing-text.md)). After a failure, play a punchy effect of about a second and hand control straight back, because fast retries make players tolerate far more difficulty ([117](../episodes/notes/117-make-retries-quick.md)). Players should reach real gameplay and understand why the game is fun within the first three minutes ([17](../episodes/notes/017-just-let-them-play.md)), ideally by opening on a playable climax ([235](../episodes/notes/235-start-with-the-climax.md)). Tutorials go inside real play ([85](../episodes/notes/085-making-tutorials-feel-natural.md), [173](../episodes/notes/173-teaching-players-how-to-play.md)). Long play time is not a selling point; it should be the *result* of fun ([250](../episodes/notes/250-be-mindful-of-the-time-players-are-giving-you.md)).

Behind all this is his view of competition: every new game competes with *every* game ever made, plus everything else people could do with their hours ([72](../episodes/notes/072-competing-with-the-past.md), [198](../episodes/notes/198-competition-and-abundance.md)).

**Ask:** How many seconds of this is the player not actually playing, and can I cut them?

### 4. Every input answered, every big moment felt

Sakurai treats game feel as engineering, not magic. The character's pose changes on the very frame the button is pressed ([36](../episodes/notes/036-breaking-down-attack-animations.md), [49](../episodes/notes/049-making-lead-ins-instant-and-impactful.md)). Big moments stop the action briefly, with hitstop, so the player feels the impact of success or defeat ([3](../episodes/notes/003-stop-for-big-moments.md)). His "Eight Hit Stop Techniques" episode stacks small touches on top of the freeze: shake the victim more than the attacker, shake the model but not the hitbox, scale the stop by strength with a per-move multiplier, and blend poses during it ([47](../episodes/notes/047-eight-hit-stop-techniques.md)). Screen shake gets a pattern per impact size, scaled by camera distance and decaying with some randomness ([103](../episodes/notes/103-screen-shake.md)). Impact sounds hit hard instantly with a short reverb tail ([167](../episodes/notes/167-strong-attack-light-reverb.md)). Every press gets some reaction, even during cutscenes ([104](../episodes/notes/104-dont-be-unresponsive.md)). Hand control back the moment players expect it, through well-placed cancel frames ([77](../episodes/notes/077-follow-throughs-make-the-impact.md)).

None of it works if the display adds lag, so test on screens set to Game Mode ([8](../episodes/notes/008-down-with-lag.md)).

**Ask:** On the frame the player presses, what changes on screen and in the speakers? On the frame of impact, what stops, shakes, flashes and sounds?

### 5. Too much is just right

> "When it comes to animation, too much is just right!" ([28](../episodes/notes/028-too-much-is-just-right.md), ≈02:14)

Games lose information compared with real life: characters are small, faces are simplified, there's no touch or smell. So performance has to be exaggerated to get across at all ([91](../episodes/notes/091-exaggerate-to-make-up-for-information-loss.md)). He pushes attack poses past "OK" ([28](../episodes/notes/028-too-much-is-just-right.md), [62](../episodes/notes/062-attack-poses.md)), damage poses until they look nothing like standby ([142](../episodes/notes/142-damage-animations.md)), and faces past finished ([166](../episodes/notes/166-facial-animations.md)). Key poses must be reached fast, without letting interpolation soften them ([150](../episodes/notes/150-the-perils-of-interpolation.md)). Real skeletons and software defaults are not limits: bend past realism, rotate on two axes, shift pivots off-center ([236](../episodes/notes/236-the-limitations-of-skeletons.md), [251](../episodes/notes/251-rotation-on-two-axes.md), [255](../episodes/notes/255-what-happens-when-you-shift-the-center-of-gravity.md)), and borrow manga conventions when they read better than realism ([232](../episodes/notes/232-manga-like-visuals.md)).

Exaggeration is a tool, not a reflex. Sound can go either way: exaggerated for fighters, realistic when it carries information ([89](../episodes/notes/089-audio-as-fiction-and-non-fiction.md)). Licensed games and arrangements of beloved music answer to the original first ([146](../episodes/notes/146-the-original-piece-is-always-right.md), [188](../episodes/notes/188-faithfulness-comes-first-in-licensed-games.md)).

**Ask:** If I doubled this pose, sound or effect, would it read better from the player's distance?

### 6. Clarity before decoration

The player must always be able to read the game state. Terrain with collision should stand out from backdrop ([30](../episodes/notes/030-emphasize-objects-with-collision.md)). Characters must stay visible inside their own effects ([35](../episodes/notes/035-let-your-characters-shine.md)). Effects need dark elements as well as bright ones so they pop on any background ([16](../episodes/notes/016-make-it-pop.md), [223](../episodes/notes/223-flashing-effects.md), [131](../episodes/notes/131-hit-marks.md)). Check gameplay colors through a color-blindness filter and in black and white ([214](../episodes/notes/214-a-world-with-less-color.md)). Keep motion blur and depth of field restrained ([192](../episodes/notes/192-motion-blur.md), [174](../episodes/notes/174-making-things-look-miniature.md)). Put navigation information in the main view, not only the mini-map ([119](../episodes/notes/119-maps-are-game-screens-too.md)). A game should be playable without reading a word ([240](../episodes/notes/240-making-things-clear-even-without-words.md)). Spend detail where players actually look ([44](../episodes/notes/044-distinguishing-between-major-and-minor-elements.md)).

In UI, clarity and style are a trade-off to settle on purpose for each game ([18](../episodes/notes/018-clarity-vs-style.md), [111](../episodes/notes/111-menus-define-your-world.md)). Don't let style quietly win.

**Ask:** Freeze any frame of a busy moment. Can a newcomer tell who is where, what just hit, and what's dangerous?

### 7. Decide who it's for, then be kind to them

Every design starts with a target player ([4](../episodes/notes/004-kirbys-dream-land.md), [112](../episodes/notes/112-branching-tastes.md), [148](../episodes/notes/148-more-game-essence-means-less-broad-appeal.md)). Kirby's Dream Land deliberately cut risk (inhale enemies, fly over pits) to welcome newcomers ([4](../episodes/notes/004-kirbys-dream-land.md)). Kirby's Adventure layered optional depth (copy abilities) on that simple core, so novices could finish and experts could dig deeper ([11](../episodes/notes/011-kirbys-adventure.md)). That layering pattern recurs throughout his work.

Developers are terrible difficulty testers because they know the game too well. Tune while handicapping yourself (one hand, less health), then make it easier than you think it should be ([256](../episodes/notes/256-give-yourself-a-handicap-when-balancing-your-game.md)). Watch children play without asking them questions ([248](../episodes/notes/248-elementary-school-play-testers.md)). Lower the barrier from the first moment until players are hooked, without lecturing them ([242](../episodes/notes/242-being-kind-to-beginners.md)). Always give a stuck player a way forward, because a player who quits gets nothing from your challenge ([213](../episodes/notes/213-better-than-not-being-able-to-beat-the-game.md)).

**Ask:** Who exactly is this for, and what happens to a first-time player in their first five minutes?

### 8. Distinct beats average

> "Average and mediocre are the same thing!" ([218](../episodes/notes/218-average-and-mediocre-are-the-same-thing.md), ≈02:05)

When balancing, don't sand strengths down. Amplify weaknesses to offset them, so every character keeps peaks and valleys ([218](../episodes/notes/218-average-and-mediocre-are-the-same-thing.md), [247](../episodes/notes/247-amplify-both-strengths-and-weaknesses.md)). Start from a neutral baseline, then push parameters until each character's identity fits in a word or two ([206](../episodes/notes/206-using-parameters-to-establish-characters.md)). Characters need exaggerated, readable silhouettes and a core that everyone on the team understands ([243](../episodes/notes/243-establishing-characters-through-their-design.md)). Imitation is a fine start, but by release your game needs many kinds of appeal the original lacks ([196](../episodes/notes/196-crafting-similar-games.md)). Present your game as its own thing, not by comparison ([161](../episodes/notes/161-avoiding-comparison.md)). A director must have a personal eye for details others miss ([70](../episodes/notes/070-directors-need-to-be-unique.md)).

**Ask:** Could someone describe each option, character or level in two words, and would those words all be different?

### 9. Question the givens

> "It's best to always approach your 'givens' as if they aren't givens at all." ([82](../episodes/notes/082-do-competitive-games-have-to-be-complex.md), ≈03:36)

At the start of every project he re-examines the genre's inherited rules. That's why every Smash has slightly different jump physics ([82](../episodes/notes/082-do-competitive-games-have-to-be-complex.md)). He questions menus and input devices ([169](../episodes/notes/169-i-want-to-choose-fast.md)), the score itself ([200](../episodes/notes/200-presenting-scores.md)), tool defaults ([236](../episodes/notes/236-the-limitations-of-skeletons.md), [255](../episodes/notes/255-what-happens-when-you-shift-the-center-of-gravity.md)), and what a new piece of hardware uniquely allows ([125](../episodes/notes/125-kid-icarus-uprising.md), [154](../episodes/notes/154-flick-input.md)). Smash itself began by naming a real problem in an existing genre and designing rules that solved it ([27](../episodes/notes/027-super-smash-bros.md)).

The counterweight: where a de facto standard saves the player from learning something, use it, and let them remap ([175](../episodes/notes/175-its-easier-if-they-already-know.md), [197](../episodes/notes/197-button-settings.md)).

**Ask:** Which rule in this design did I inherit without deciding it?

### 10. Specify precisely: frames, units, parameters

Sakurai doesn't direct by vibes. Frames are the unit of time ([5](../episodes/notes/005-frame-rates.md)), and he trains himself to *count* them ([76](../episodes/notes/076-learn-to-count-frames.md)). Speeds get explicit units the whole team shares ([84](../episodes/notes/084-units-of-speed.md)). Jumps are built from an initial velocity plus per-frame gravity ([37](../episodes/notes/037-jump-physics.md)). Knockback has named parameters per attack ([145](../episodes/notes/145-knockback-in-super-smash-bros.md)). Tunable values live outside code, editable by designers and pushed to builds with one button ([46](../episodes/notes/046-making-your-game-easy-to-tune.md)), and specs mark every tunable number in plain-language brackets ([68](../episodes/notes/068-put-parameters-in-brackets.md)). Animators get a list with every move's length and hit timing before they start ([14](../episodes/notes/014-assigning-animations.md)), and they must always know where the hitbox is ([225](../episodes/notes/225-always-keep-attack-collision-in-mind.md)). Late changes to processing speed can silently change difficulty, so re-check on final hardware ([141](../episodes/notes/141-unexpected-results.md)).

**Ask:** Could a teammate implement this from my spec without asking me a single question?

### 11. Decide fast, share everything, steer by the concept

A concept is "like a beam of light from a lighthouse" ([187](../episodes/notes/187-staying-true-to-your-concept.md)): fix it before production and steer by it. Within that, make decisions on the spot ([191](../episodes/notes/191-dont-put-decisions-off.md)) and clear every review the same day ([177](../episodes/notes/177-finish-everything-within-the-day.md), [261](../episodes/notes/261-masahiro-sakurai-on-creating-games-finale-special.md)). Raise problems the moment you see them, with a proposed fix ([60](../episodes/notes/060-dont-wait-to-speak-your-mind.md)). Commit to one plan instead of offering a Plan B ([109](../episodes/notes/109-dont-rely-on-a-plan-b.md)). Explain to everyone at once rather than relaying ([114](../episodes/notes/114-explain-ideas-to-everyone-at-once.md)). Keep the whole team seeing the whole game through daily reports and screenshots ([43](../episodes/notes/043-sharing-info-within-a-team.md), [123](../episodes/notes/123-daily-report-suggestions.md)). Give art feedback by drawing over it ([90](../episodes/notes/090-supervising-art-through-retouches.md), [165](../episodes/notes/165-odds-and-ends-of-supervising.md)). Creative calls belong to the person holding the big picture, not to a majority vote ([158](../episodes/notes/158-the-majority-shouldnt-always-rule.md)). And a director's job includes trimming ([258](../episodes/notes/258-a-directors-job-is-to-trim.md)).

**Ask:** Is anyone on the team blocked waiting for me right now?

### 12. Speed and output over polish, and respect the people

"Short and snappy! Speed above all else!" ([261](../episodes/notes/261-masahiro-sakurai-on-creating-games-finale-special.md), ≈10:57). Write proposals hot and fast ([52](../episodes/notes/052-prep-your-proposals-hot-and-fast.md)), present them as quick slides ([12](../episodes/notes/012-presentations-are-all-about-speed.md), [38](../episodes/notes/038-writing-game-proposals.md)), and start now instead of waiting for motivation ([83](../episodes/notes/083-just-do-it-already.md)). Take in a lot (many games, played thoughtfully) and put out a lot, steadily ([126](../episodes/notes/126-broad-input-broad-output.md)). He planned and scripted all 260 episodes before recording one, proved the idea with a three-episode pilot, and accepted small imperfections to keep going ([261](../episodes/notes/261-masahiro-sakurai-on-creating-games-finale-special.md)).

Through it all, never fight with coworkers. The industry is small ([249](../episodes/notes/249-never-get-into-fights.md)). A director's instructions are really requests to the people doing the work ([260](../episodes/notes/260-up-is-down-and-down-is-up.md)). He holds up Satoru Iwata as the model: trust, calm logic and one-on-one talk ([259](../episodes/notes/259-mr-iwata.md)).

**Ask:** What's the smallest version I can ship to a real person today?

---

## Tensions to hold

Sakurai's advice isn't a list of absolutes, and several lessons pull against each other. Knowing *when* each one applies is the actual skill.

| Tension | One side | Other side | How he reconciles it |
|---|---|---|---|
| Depth vs. reach | Push and pull is the core of fun ([6](../episodes/notes/006-risk-and-reward.md), [82](../episodes/notes/082-do-competitive-games-have-to-be-complex.md)) | More essence means less broad appeal ([148](../episodes/notes/148-more-game-essence-means-less-broad-appeal.md), [4](../episodes/notes/004-kirbys-dream-land.md)) | Pick the audience first, then set the risk. Layer optional depth on a simple core ([11](../episodes/notes/011-kirbys-adventure.md)). |
| Steady vs. adaptive | Never change direction midway ([187](../episodes/notes/187-staying-true-to-your-concept.md)) | Correct calls quickly once they're wrong ([191](../episodes/notes/191-dont-put-decisions-off.md)) | Keep the concept fixed and steer the details constantly. |
| Standard vs. original | Use de facto standard controls ([175](../episodes/notes/175-its-easier-if-they-already-know.md)) | Question every given ([82](../episodes/notes/082-do-competitive-games-have-to-be-complex.md), [169](../episodes/notes/169-i-want-to-choose-fast.md)) | Standardize what players already know; innovate where the fun is. |
| Exaggerated vs. faithful | Too much is just right ([28](../episodes/notes/028-too-much-is-just-right.md), [91](../episodes/notes/091-exaggerate-to-make-up-for-information-loss.md)) | The original is always right ([146](../episodes/notes/146-the-original-piece-is-always-right.md)); in licensed games, faithfulness comes first ([188](../episodes/notes/188-faithfulness-comes-first-in-licensed-games.md)) | Exaggerate your own work; honor what players already love. |
| Vision vs. data | Market research describes paths others already took ([226](../episodes/notes/226-targeting-and-market-research.md)); beware echo chambers ([228](../episodes/notes/228-echo-chambers.md)) | Choose targets from a top-down view of the market ([112](../episodes/notes/112-branching-tastes.md)) | Use the market to choose *who*, and your own vision to decide *what*. |
| Speed vs. polish | Speed above all ([261](../episodes/notes/261-masahiro-sakurai-on-creating-games-finale-special.md)); patches are a bonus ([231](../episodes/notes/231-online-updates.md)) | Relentless polish passes ([253](../episodes/notes/253-odds-and-ends-of-supervising-sora-edition.md)); the game outlives the hardship ([67](../episodes/notes/067-youll-forget-the-hardship-but-the-game-will-endure.md)) | Move fast on process and drafts, and polish what players actually touch. |
| Fair vs. lucky | Randomness keeps play fresh ([189](../episodes/notes/189-randomness-spices-games-up.md)) | Luck must never decide a loss on its own ([189](../episodes/notes/189-randomness-spices-games-up.md)); skill games level the field only through chaos and options ([202](../episodes/notes/202-handicap-systems.md)) | Decide on purpose how much skill your audience wants reflected. |

---

## The Sakurai loop: a working method for any feature

Use this when designing or reviewing anything, from a boss to a menu:

1. **Audience.** Who is this for, and how much risk do they want? ([148](../episodes/notes/148-more-game-essence-means-less-broad-appeal.md), [112](../episodes/notes/112-branching-tastes.md))
2. **Essence.** What's the risk, what's the reward, and are they close together? ([6](../episodes/notes/006-risk-and-reward.md), [193](../episodes/notes/193-game-essence-in-action-games.md))
3. **Rewards.** What does the player get, can they see the next one, and does it fit the concept? ([75](../episodes/notes/075-consider-rewards-first.md), [23](../episodes/notes/023-keeping-rewards-in-sight.md), [151](../episodes/notes/151-planning-your-games-rewards.md))
4. **Feel.** What happens on the press frame and on the impact frame? ([49](../episodes/notes/049-making-lead-ins-instant-and-impactful.md), [3](../episodes/notes/003-stop-for-big-moments.md), [47](../episodes/notes/047-eight-hit-stop-techniques.md))
5. **Clarity.** Can a newcomer read it in a frozen screenshot? ([30](../episodes/notes/030-emphasize-objects-with-collision.md), [35](../episodes/notes/035-let-your-characters-shine.md), [214](../episodes/notes/214-a-world-with-less-color.md))
6. **Time.** How much of it is waiting, and can it be cut or skipped? ([73](../episodes/notes/073-say-no-to-slow.md), [180](../episodes/notes/180-let-them-skip-let-them-pause.md))
7. **Distinctness.** Does it have a two-word identity, with strengths *and* weaknesses? ([206](../episodes/notes/206-using-parameters-to-establish-characters.md), [218](../episodes/notes/218-average-and-mediocre-are-the-same-thing.md))
8. **Spec.** Are timings in frames, speeds in units and tunables in parameters? ([5](../episodes/notes/005-frame-rates.md), [84](../episodes/notes/084-units-of-speed.md), [46](../episodes/notes/046-making-your-game-easy-to-tune.md))
9. **Test.** Play it handicapped, watch fresh players silently, then make it easier. ([256](../episodes/notes/256-give-yourself-a-handicap-when-balancing-your-game.md), [248](../episodes/notes/248-elementary-school-play-testers.md))
10. **Trim.** Cut what doesn't serve the concept. ([258](../episodes/notes/258-a-directors-job-is-to-trim.md), [187](../episodes/notes/187-staying-true-to-your-concept.md))

The [checklists](checklists.md) turn this loop into review questions per area. The `--review` mode of the skill's search tool runs it against a specific feature.

---

## If you only watch ten episodes

1. [6 · Risk and Reward](../episodes/notes/006-risk-and-reward.md): the definition of game essence.
2. [57 · Deconstruct, Analyze, and Rebuild](../episodes/notes/057-deconstruct-analyze-and-rebuild.md): how to borrow fun without copying.
3. [250 · Be Mindful of the Time Players are Giving You](../episodes/notes/250-be-mindful-of-the-time-players-are-giving-you.md): the player's time as a cost.
4. [3 · Stop for Big Moments!](../episodes/notes/003-stop-for-big-moments.md): hitstop and impact.
5. [36 · Breaking Down Attack Animations](../episodes/notes/036-breaking-down-attack-animations.md): the anatomy of an attack.
6. [28 · Too Much is Just Right](../episodes/notes/028-too-much-is-just-right.md): exaggeration.
7. [148 · More Game Essence Means Less Broad Appeal](../episodes/notes/148-more-game-essence-means-less-broad-appeal.md): choosing your audience.
8. [218 · Average and Mediocre Are the Same Thing](../episodes/notes/218-average-and-mediocre-are-the-same-thing.md): balance without blandness.
9. [187 · Staying True to Your Concept](../episodes/notes/187-staying-true-to-your-concept.md): steering by a concept.
10. [261 · Masahiro Sakurai on Creating Games: Finale Special](../episodes/notes/261-masahiro-sakurai-on-creating-games-finale-special.md): how he planned and shipped 260 episodes.
