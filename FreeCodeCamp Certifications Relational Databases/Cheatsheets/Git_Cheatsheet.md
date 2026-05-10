# Git Cheatsheet

This cheatsheet is a quick lookup reference for Git syntax learned in the
freeCodeCamp Relational Databases Certification track.

Use it when checking repository state, staging work, committing, branching,
merging, rebasing, resolving conflicts, stashing changes, and protecting local
environment files.

## Repository Setup

| Goal | Command | Example | Notes |
| --- | --- | --- | --- |
| Create repository | `git init` | `git init` | Creates the hidden `.git` folder. |
| Show hidden files | `ls -a` | `ls -a` | Confirms `.git` exists in Linux shell. |
| Check status | `git status` | `git status` | Most important habit in the workshop. |
| Create and switch branch | `git checkout -b branch` | `git checkout -b main` | Used to create `main` after `git init`. |

## Staging and Committing

| Goal | Command | Example | Notes |
| --- | --- | --- | --- |
| Stage one file | `git add file` | `git add README.md` | Prepares one file for commit. |
| Stage all visible changes | `git add .` | `git add .` | Use only after checking `git status`. |
| Commit staged changes | `git commit -m "message"` | `git commit -m "feat: add create database reference"` | Records staged snapshot. |
| Show unstaged diff | `git diff` | `git diff` | Review changes before staging. |
| Show latest commit diff | `git show` | `git show` | Useful after revert or commit review. |
| Show previous commit diff | `git show HEAD~1` | `git show HEAD~1` | `HEAD~1` means one commit before HEAD. |

## Logs

| Goal | Command | Example |
| --- | --- | --- |
| Full history | `git log` | `git log` |
| Compact history | `git log --oneline` | `git log --oneline` |
| Latest commit only | `git log -1` | `git log -1` |
| Last five commits | `git log -5 --oneline` | `git log -5 --oneline` |

## Branches and Merges

| Goal | Command | Example | Notes |
| --- | --- | --- | --- |
| List branches | `git branch` | `git branch` | `*` marks current branch. |
| Create branch | `git branch branch_name` | `git branch feat/add-create-table-reference` | Creates branch without switching. |
| Switch branch | `git checkout branch_name` | `git checkout main` | Moves working tree to branch state. |
| Create and switch | `git checkout -b branch_name` | `git checkout -b fix/create-table-syntax` | Common feature/fix workflow. |
| Merge into current branch | `git merge branch_name` | `git merge feat/add-drop-table-reference` | Run from the target branch. |
| Delete merged branch | `git branch -d branch_name` | `git branch -d feat/add-drop-table-reference` | Safe delete after merge. |

## Rebase

| Goal | Command | Example | Notes |
| --- | --- | --- | --- |
| Rebase current branch | `git rebase branch` | `git rebase main` | Replays current branch commits on top of `main`. |
| Continue after conflict | `git rebase --continue` | `git rebase --continue` | Use after fixing and staging conflict files. |
| Cancel rebase | `git rebase --abort` | `git rebase --abort` | Returns to pre-rebase state. |
| Interactive rebase | `git rebase --interactive HEAD~n` | `git rebase --interactive HEAD~5` | Edit recent commit history. |
| Interactive from root | `git rebase --interactive --root` | `git rebase --interactive --root` | Rewrites from first commit; use carefully. |

## Interactive Rebase Commands

| Todo Command | Short | Meaning |
| --- | --- | --- |
| `pick` | `p` | Keep commit as-is. |
| `reword` | `r` | Keep commit but edit message. |
| `squash` | `s` | Combine commit into previous commit. |
| `drop` | `d` | Remove commit from history. |

Example squash:

```text
pick abc1111 feat: add column references
s abc2222 feat: add drop column reference
s abc3333 feat: add rename column reference
```

## Conflict Resolution

| Step | Command or Action |
| --- | --- |
| Check conflict state | `git status` |
| Open conflicted file | use editor |
| Remove markers | delete `<<<<<<<`, `=======`, `>>>>>>>` |
| Keep correct combined content | make file valid again |
| Stage resolved file | `git add file` |
| Continue rebase | `git rebase --continue` |

Conflict marker shape:

```text
[conflict start: HEAD]
current branch content
[conflict separator]
incoming commit content
[conflict end: commit message]
```

Real Git conflict files use literal marker lines such as `<<<<<<< HEAD`,
`=======`, and `>>>>>>> commit message`. The cheatsheet labels them in the code
block so the repository does not look like it contains an unresolved conflict.

## Stash

| Goal | Command | Notes |
| --- | --- | --- |
| Save uncommitted work | `git stash` | Cleans working tree. |
| List stashes | `git stash list` | Shows `stash@{0}`, `stash@{1}`, etc. |
| Apply and remove latest stash | `git stash pop` | Most common restore command. |
| Apply and keep latest stash | `git stash apply` | Useful when reusing a stash. |
| Show summary | `git stash show` | File-level summary. |
| Show full patch | `git stash show -p` | Detailed diff. |
| Show specific stash | `git stash show stash@{1}` | Reads older stash. |
| Drop latest stash | `git stash drop` | Deletes a stash entry. |

## Undoing Commits

| Goal | Command | What Happens |
| --- | --- | --- |
| Remove latest commit, keep changes unstaged | `git reset HEAD~1` | Commit disappears; changes return to working tree. |
| Remove latest commit, keep changes staged | `git reset --soft HEAD~1` | Commit disappears; changes stay staged. |
| Remove latest commit and changes | `git reset --hard HEAD~1` | Destructive. |
| Undo latest commit with a new commit | `git revert HEAD` | Safer for shared history. |

## `.gitignore` and Environment Files

| Goal | File or Command | Example |
| --- | --- | --- |
| Ignore local env file | `.gitignore` | `.env` |
| Keep secret local | `.env` | `SECRET=MY_SECRET` |
| Provide safe template | `sample.env` | `SECRET=` |
| Check ignored file | `git status --ignored` | `git status --ignored` |

Rule:

```text
Commit sample.env.
Do not commit .env.
```
