# Git Workflow Reference

## Purpose

This reference explains the Git concepts practiced in the **Build an SQL
Reference Object** workshop.

It is intentionally detailed because this workshop introduces several Git
operations that are easy to forget: staging, branching, merging, rebasing,
conflict resolution, stashing, resetting, reverting, and interactive rebasing.

## Working Directory, Staging Area, and Repository

Git work moves through three main areas:

| Area | Meaning | Common Command |
| --- | --- | --- |
| Working directory | Files as they currently exist on disk. | edit file, `touch`, `nano` |
| Staging area | Prepared snapshot for the next commit. | `git add file` |
| Repository history | Permanent committed snapshots. | `git commit -m "message"` |

The most common beginner mistake is thinking that saving a file automatically
adds it to Git history. It does not. Git only records the staged snapshot when a
commit is created.

## `git status`

Use `git status` constantly.

| State | Meaning |
| --- | --- |
| `untracked` | Git sees the file but has never committed it. |
| `modified` | The file was committed before and has new changes. |
| `changes to be committed` | The change is staged. |
| `working tree clean` | No uncommitted tracked changes. |

Example:

```text
On branch main
Changes not staged for commit:
  modified:   sql_reference.json
```

This means the file changed, but the change is not staged yet.

## `git diff`

`git diff` shows unstaged changes.

Example:

```diff
-    "create": "CREATE TABLE table_name;"
+    "create": "CREATE TABLE table_name();"
```

Interpretation:

- `-` means removed line
- `+` means added line

Use `git diff` before `git add` to make sure the file says what you expect.

## `git add`

| Command | Meaning |
| --- | --- |
| `git add README.md` | Stage one file. |
| `git add sql_reference.json` | Stage the JSON file. |
| `git add .` | Stage all visible changed files in the current directory. |

Important: `git add .` is convenient, but it is only safe after checking
`git status`. It can accidentally stage unrelated files if the working tree is
messy.

## `git commit`

Syntax:

```bash
git commit -m "message"
```

Examples:

```bash
git commit -m "Initial commit"
git commit -m "feat: add create database reference"
git commit -m "fix: create table syntax"
```

Commit message pattern:

| Prefix | Meaning |
| --- | --- |
| `feat:` | Adds a new feature or reference. |
| `fix:` | Corrects existing behavior or missing content. |

## `git log`

| Command | Purpose |
| --- | --- |
| `git log` | Detailed commit history. |
| `git log --oneline` | Compact commit history. |
| `git log -1` | Show only the latest commit. |
| `git log -5 --oneline` | Show the latest five commits compactly. |

Compact logs are useful during branch work:

```text
abc1234 feat: add drop table reference
def5678 feat: add create table reference
ghi9012 Initial commit
```

The hash at the beginning identifies the commit.

## Branches

Branches allow work to happen separately from `main`.

| Command | Meaning |
| --- | --- |
| `git branch` | List branches. |
| `git branch branch_name` | Create a branch without switching. |
| `git checkout branch_name` | Switch to an existing branch. |
| `git checkout -b branch_name` | Create and switch to a branch. |
| `git branch -d branch_name` | Delete a merged branch. |

Branch name examples from the workshop:

```text
feat/add-create-table-reference
feat/add-drop-table-reference
feat/add-column-references
feat/add-more-row-references
fix/create-table-syntax
fix/add-missing-rename-references
feat/add-gitignore
```

Good branch names describe the work clearly.

## Merge

Merge brings another branch into the current branch.

Common pattern:

```bash
git checkout main
git merge feat/add-create-table-reference
git branch -d feat/add-create-table-reference
```

Why switch to `main` first:

- Git merges into the branch you are currently on.
- If you want feature work to enter `main`, you must be on `main`.

## Rebase

Rebase replays branch commits on top of another branch.

Common pattern:

```bash
git checkout feat/add-column-references
git rebase main
```

Use rebase when:

- `main` has new commits
- your feature branch is behind
- you want your branch history to look like it started from the latest `main`

Mental model:

```text
Before:
main:   A -- B -- C
branch: A -- B -- D -- E

After git rebase main:
main:   A -- B -- C
branch: A -- B -- C -- D' -- E'
```

The apostrophes mean Git recreated the commits with new hashes.

## Rebase Conflict Resolution

Conflict markers look like:

```text
[conflict start: HEAD]
current branch version
[conflict separator]
commit being replayed version
[conflict end: commit message]
```

In the actual conflicted file, Git writes literal marker lines such as
`<<<<<<< HEAD`, `=======`, and `>>>>>>> commit message`. This reference uses
labels in the code block so the repository does not appear to contain an
unresolved conflict.

Fix process:

1. Open the conflicted file.
2. Remove `<<<<<<<`, `=======`, and `>>>>>>>` marker lines.
3. Keep the correct content from both sides.
4. Make sure the file syntax is valid.
5. Stage the fixed file.
6. Continue the rebase.

Commands:

```bash
git status
git add sql_reference.json
git rebase --continue
```

If the rebase should be cancelled:

```bash
git rebase --abort
```

The workshop uses `--continue`, not `--abort`, because the goal is to finish
the rebase after fixing the JSON.

## Stash

Stash temporarily stores uncommitted work.

| Command | Meaning |
| --- | --- |
| `git stash` | Save current uncommitted changes and clean the working tree. |
| `git stash list` | Show saved stashes. |
| `git stash pop` | Apply latest stash and remove it from stash list. |
| `git stash apply` | Apply latest stash and keep it in stash list. |
| `git stash show` | Show summary of latest stash. |
| `git stash show -p` | Show full patch of latest stash. |
| `git stash drop` | Delete latest stash. |
| `git stash show stash@{1}` | Show a specific stash by index. |

Use stash when:

- work was started on the wrong branch
- you need to switch branches but are not ready to commit
- you want to inspect or move uncommitted changes safely

## Reset

The workshop uses:

```bash
git reset HEAD~1
```

Meaning:

- move `HEAD` back by one commit
- remove the latest commit from branch history
- keep that commit's changes in the working tree
- leave those changes unstaged

Comparison:

| Command | Keeps Changes? | Keeps Staging? | Risk |
| --- | --- | --- | --- |
| `git reset --soft HEAD~1` | yes | yes | lower |
| `git reset HEAD~1` | yes | no | medium |
| `git reset --hard HEAD~1` | no | no | high |

Avoid `--hard` unless you intentionally want to delete local changes.

## Revert

The workshop uses:

```bash
git revert HEAD
```

Meaning:

- keep the original commit in history
- create a new commit that applies the opposite diff

This is safer for shared history than reset because it does not erase an
existing commit.

Revert opens Nano with a default commit message:

```text
Revert "feat: add unique reference"
```

Keeping the default message is acceptable for this workshop.

## `git show`

| Command | Meaning |
| --- | --- |
| `git show` | Show the latest commit and its diff. |
| `git show HEAD~1` | Show the commit before the latest commit. |

In the revert lesson:

- `git show` displays the revert commit
- `git show HEAD~1` displays the commit that was reverted

The two diffs should be opposites.

## Interactive Rebase

Interactive rebase edits local commit history.

Commands from the workshop:

```bash
git rebase --interactive HEAD~2
git rebase --interactive --root
git rebase --interactive HEAD~5
```

The todo list uses commands such as:

| Command | Short | Meaning |
| --- | --- | --- |
| `pick` | `p` | Use the commit as-is. |
| `reword` | `r` | Use the commit but edit its message. |
| `squash` | `s` | Combine this commit into the previous commit. |
| `drop` | `d` | Remove the commit. |

## Drop Commits

Todo example:

```text
d abc1111 feat: add unique reference
d abc2222 Revert "feat: add unique reference"
```

This removes both commits from the local branch history.

## Reword a Commit

Todo example:

```text
r abc1111 feat: add column reference
```

Git opens Nano again for the commit message. The workshop changes:

```text
feat: add column reference
```

to:

```text
feat: add column references
```

## Squash Commits

Todo example:

```text
pick abc1111 feat: add column references
s abc2222 feat: add drop column reference
s abc3333 feat: add rename column reference
s abc4444 feat: add primary key reference
s abc5555 feat: add foreign key reference
```

Result:

- one commit remains
- it contains the combined changes
- commit history is easier to review

## `.gitignore`

`.gitignore` tells Git which untracked files should not appear in `git status`.

Workshop `.gitignore`:

```text
.env
```

That protects:

```text
.env
```

from being committed.

## `sample.env`

`sample.env` is safe to commit because it contains only the variable name:

```text
SECRET=
```

Purpose:

- documents required environment variables
- avoids exposing a real secret
- helps another user create their own `.env`

## Command Summary

| Goal | Command |
| --- | --- |
| Initialize repository | `git init` |
| Show status | `git status` |
| Stage file | `git add file` |
| Stage current directory | `git add .` |
| Commit staged changes | `git commit -m "message"` |
| Show full log | `git log` |
| Show compact log | `git log --oneline` |
| List branches | `git branch` |
| Create branch | `git branch branch_name` |
| Switch branch | `git checkout branch_name` |
| Create and switch branch | `git checkout -b branch_name` |
| Merge branch into current branch | `git merge branch_name` |
| Delete merged branch | `git branch -d branch_name` |
| Rebase current branch on main | `git rebase main` |
| Continue rebase | `git rebase --continue` |
| Stash changes | `git stash` |
| List stashes | `git stash list` |
| Pop latest stash | `git stash pop` |
| Apply latest stash | `git stash apply` |
| Show stash patch | `git stash show -p` |
| Drop stash | `git stash drop` |
| Reset one commit back | `git reset HEAD~1` |
| Revert latest commit | `git revert HEAD` |
| Show latest commit | `git show` |
| Interactive rebase | `git rebase --interactive HEAD~n` |

## Practical Review Checklist

Before committing:

1. Run `git status`.
2. Run `git diff`.
3. Confirm only intended files changed.
4. Stage intentionally with `git add file`.
5. Run `git status` again.
6. Commit with a clear message.

Before merging:

1. Switch to the target branch.
2. Confirm with `git branch`.
3. Merge the source branch.
4. Check `git log --oneline`.
5. Delete the source branch if it is complete.

Before rebasing:

1. Commit or stash work first.
2. Make sure you are on the branch that should be updated.
3. Run `git rebase main`.
4. If conflicts appear, fix the file and continue.
5. Check the log after the rebase.
