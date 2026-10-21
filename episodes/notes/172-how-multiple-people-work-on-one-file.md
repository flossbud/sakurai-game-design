# 172 · How Multiple People Work on One File

**Category:** Programming & Tech · [Video](https://www.youtube.com/watch?v=s5u7VqDl-1I) · [Transcript](../transcripts/172-how-multiple-people-work-on-one-file.md)

## In one sentence
Keep every project file on a server under a management tool that locks, merges and backs up edits, and still expect lost changes, because big teams collide on shared files all the time.

## Key ideas
- A large team can have hundreds of people working on one game, and a game in development is split into tens of thousands, hundreds of thousands or even millions of files. The bigger the scope, the more files, so most projects track them with some kind of management tool.
- The basic loop: all files live on a server. When someone edits a file, it gets locked; when they finish, the edited file is uploaded back to the server and unlocked. That repeats over and over.
- Locking alone has limits: only letting one person work on a particularly large file at a time is inefficient, and two people can still manage to upload conflicting edits at the same time.
- For conflicts, the tool tries to merge, comparing the edits and stitching them into one file. Sometimes that's enough; if the discrepancies remain, someone has to fix them by hand.
- Reversion is when a person's changes vanish without a trace and the file goes back to how it was before the edit. Sakurai says that, for whatever reason, it happens often.
- The tools back up every edit, so going back a version may recover lost work. It should work in theory, but in practice it is "a constant source of headaches", and many projects still rely on these tools.

## Do this
- Put every game file on a shared server under a management tool instead of passing copies around by hand.
- Lock a file before you edit it, then upload it and release the lock when you're done, so nobody edits the same file at the same time.
- For large files that several people need at once, allow simultaneous edits, let the tool auto-merge, and name someone to resolve by hand any conflicts the merge leaves behind.
- When an edit goes missing, look in the version history first. The tool keeps a backup of every edit, so rolling back a version can often bring the change back.

## Avoid
- Assuming the tool makes conflicts impossible. It works in theory, but reverts and bad merges still happen regularly.
- Letting a single person hold a particularly large file locked while others wait on it.

## Examples from the episode
- None. The episode is a general overview of how teams manage shared files, without game-specific examples.

## Quote
> There shouldn't be any issues, in theory— but in practice, it's a constant source of headaches. (02:10)

## Tags
`version-control` `file-locking` `merging` `tools` `scope` `team-workflow`
