# Build an SQL Reference Object

## Context

This document summarizes the **Build an SQL Reference Object** workshop from
the freeCodeCamp Relational Databases Certification track.

The workshop was completed in **GitHub Codespaces** through the CodeRoad
extension. The original lesson is interactive and step-based, so this repository
keeps a cleaned learning record instead of raw copied prompts from the CodeRoad
interface.

The main learning target is Git. The SQL reference object is the practice file
used to make Git concepts visible through real file changes, commits, branches,
merges, rebases, conflicts, stashes, resets, reverts, interactive rebases,
squashes, and ignored environment files.

## Workshop Goal

Build a small Git repository named `sql_reference` that contains:

- `README.md`
- `sql_reference.json`
- `.gitignore`
- `sample.env`

The final JSON stores common SQL syntax patterns for database, table, row, and
column operations. The more important outcome is understanding how Git records
each step of that work.

## Why This Workshop Matters

This workshop is much more than a simple JSON exercise. It teaches the everyday
Git workflow that appears in real projects:

1. Create a repository.
2. Add files.
3. Stage changes.
4. Commit small units of work.
5. Create feature and fix branches.
6. Merge completed branches.
7. Rebase long-running branches so their history stays current.
8. Resolve conflicts when two branches edit the same area.
9. Temporarily save work with `git stash`.
10. Undo commits with `git reset` and `git revert`.
11. Rewrite local branch history with interactive rebase.
12. Squash several small commits into one cleaner commit.
13. Ignore sensitive local files with `.gitignore`.
14. Provide a safe `sample.env` template for other users.

## Important Safety Rule

The workshop creates a real `.env` file containing a secret-like value. That
file must never be committed.

The final project keeps:

- `.gitignore`
- `sample.env`

The final project does not commit:

- `.env`

In this repository, `.env` is also ignored by the root `.gitignore`, so the
local `.env` file remains protected.

## Final Project Files

| File | Purpose |
| --- | --- |
| `sql_reference/README.md` | Minimal project title for the practice repository. |
| `sql_reference/sql_reference.json` | Final SQL command reference object. |
| `sql_reference/.gitignore` | Ignores `.env`. |
| `sql_reference/sample.env` | Documents the required environment variable without exposing a secret. |

## Final SQL Reference Object

The final `sql_reference.json` file contains:

```json
{
  "database": {
    "create": "CREATE DATABASE database_name;",
    "drop": "DROP DATABASE database_name;",
    "rename": "ALTER DATABASE database_name RENAME TO new_name;"
  },
  "table": {
    "create": "CREATE TABLE table_name();",
    "drop": "DROP TABLE table_name;",
    "rename": "ALTER TABLE table_name RENAME TO new_name;"
  },
  "row": {
    "insert": "INSERT INTO table_name(columns) VALUES(values);",
    "update": "UPDATE table_name SET column_name = new_value WHERE condition;",
    "delete": "DELETE FROM table_name WHERE condition;"
  },
  "column": {
    "add": "ALTER TABLE table_name ADD COLUMN column_name;",
    "drop": "ALTER TABLE table_name DROP COLUMN column_name;",
    "rename": "ALTER TABLE table_name RENAME COLUMN column_name TO new_name;",
    "primary_key": "ALTER TABLE table_name ADD PRIMARY KEY(column_name);",
    "foreign_key": "ALTER TABLE table_name ADD FOREIGN KEY(column_name) REFERENCES table_name(column_name);"
  }
}
```

Important note: the workshop temporarily adds a `unique` column reference, then
uses that change to demonstrate `git reset`, `git revert`, and interactive
rebase. The final JSON does not keep the `unique` reference because the exercise
uses it mainly as Git history practice.

## Phase 1: Create the Repository

### Command Sequence

```bash
echo hello git
mkdir sql_reference
cd sql_reference
git init
ls -a
git status
git checkout -b main
git status
```

### What Each Command Does

| Command | Meaning |
| --- | --- |
| `echo hello git` | Confirms that the terminal is running commands correctly. |
| `mkdir sql_reference` | Creates a new folder for the practice repository. |
| `cd sql_reference` | Moves into that folder. |
| `git init` | Creates a new Git repository by adding a hidden `.git` directory. |
| `ls -a` | Lists hidden files and folders, including `.git`. |
| `git status` | Shows branch, staging, and working tree state. |
| `git checkout -b main` | Creates and switches to a branch named `main`. |

### Expected Repository State

After `git init`, the folder contains a hidden `.git` directory:

```text
.
..
.git
```

Example `git status` shape before the first commit:

```text
On branch main

No commits yet

nothing to commit (create/copy files and use "git add" to track)
```

### Why the `.git` Folder Matters

The `.git` folder stores Git's internal database:

- commit objects
- branch references
- index/staging information
- configuration
- history metadata

The project files are visible in the working directory. Git's memory of those
files lives inside `.git`.

## Phase 2: Create the First Commit

### Command Sequence

```bash
touch README.md
nano README.md
git status
git add README.md
git status
touch sql_reference.json
git status
git add sql_reference.json
git status
git commit -m "Initial commit"
git status
git log
```

### README Content

`README.md` starts with:

```text
SQL Reference
```

### What Happens Before Staging

After creating `README.md`, Git sees it as untracked:

```text
Untracked files:
  README.md
```

Untracked means Git can see the file, but it is not part of Git history yet.

### What Happens After `git add README.md`

The file moves into the staging area:

```text
Changes to be committed:
  new file:   README.md
```

The staging area is a preparation area. A commit records what is staged, not
every file that exists in the folder.

### Why `sql_reference.json` Is Added Before the First Commit

The first commit should represent the initial repository structure. The workshop
adds both files to the same first commit:

- `README.md`
- `sql_reference.json`

### Commit Output Shape

The exact hash is different on every machine, but the output shape looks like:

```text
[main abc1234] Initial commit
 2 files changed, 1 insertion(+)
 create mode 100644 README.md
 create mode 100644 sql_reference.json
```

### First `git log` Shape

```text
commit abc1234...
Author: Your Name <you@example.com>
Date:   ...

    Initial commit
```

The long value after `commit` is the commit hash. Git uses it as the unique ID
for that snapshot.

## Phase 3: Add Database References on `main`

### Add CREATE DATABASE

`sql_reference.json` becomes:

```json
{
  "database": {
    "create": "CREATE DATABASE database_name;"
  }
}
```

Command sequence:

```bash
git status
git diff
git add sql_reference.json
git status
git commit -m "feat: add create database reference"
git log
```

### Why `git diff` Is Used Before Staging

`git diff` shows unstaged changes:

```diff
+{
+  "database": {
+    "create": "CREATE DATABASE database_name;"
+  }
+}
```

Lines starting with `+` are additions. This is a safety check before staging.

### Add DROP DATABASE

The database object becomes:

```json
"database": {
  "create": "CREATE DATABASE database_name;",
  "drop": "DROP DATABASE database_name;"
}
```

Command sequence:

```bash
git status
git diff
git add sql_reference.json
git commit -m "feat: add drop database reference"
git log
```

### Why These Commits Start With `feat:`

`feat:` means the commit adds a feature or new behavior. In this workshop, each
new SQL command reference is treated as a small feature.

At this point, `main` has three commits:

```text
abc3333 feat: add drop database reference
abc2222 feat: add create database reference
abc1111 Initial commit
```

## Phase 4: Create and Merge the First Feature Branch

### Create a Branch Without Switching

```bash
git branch
git branch feat/add-create-table-reference
git branch
```

The branch exists, but the `*` still points to `main`:

```text
  feat/add-create-table-reference
* main
```

### Switch to the Feature Branch

```bash
git checkout feat/add-create-table-reference
git branch
```

Now the `*` moves:

```text
* feat/add-create-table-reference
  main
```

### Add CREATE TABLE

The first table reference is added next to the `database` object:

```json
"table": {
  "create": "CREATE TABLE table_name;"
}
```

Command sequence:

```bash
git status
git diff
git add sql_reference.json
git commit -m "feat: add create table reference"
git log
git log --oneline
```

### Why `git log --oneline` Is Useful

Normal `git log` is detailed. `git log --oneline` is easier when the history
gets longer:

```text
abc4444 feat: add create table reference
abc3333 feat: add drop database reference
abc2222 feat: add create database reference
abc1111 Initial commit
```

### Merge the Feature Branch into `main`

```bash
git checkout main
git log --oneline
git branch
git merge feat/add-create-table-reference
git log --oneline
git branch -d feat/add-create-table-reference
git branch
```

The important idea:

- the commit was created on the feature branch
- `main` did not have it until the merge
- after the merge, the feature branch can be deleted

Example branch deletion output:

```text
Deleted branch feat/add-create-table-reference (was abc4444).
```

## Phase 5: Create and Merge a Branch in One Command

### Command Sequence

```bash
git checkout -b feat/add-drop-table-reference
git status
git diff
git add sql_reference.json
git commit -m "feat: add drop table reference"
git checkout main
git branch
git merge feat/add-drop-table-reference
git branch -d feat/add-drop-table-reference
```

### What `git checkout -b` Means

`git checkout -b branch_name` does two things:

1. creates the branch
2. switches to it immediately

### DROP TABLE Reference

The table object becomes:

```json
"table": {
  "create": "CREATE TABLE table_name;",
  "drop": "DROP TABLE table_name;"
}
```

## Phase 6: Start a Long-Running Column Branch

### Create the Branch

```bash
git checkout -b feat/add-column-references
```

### Add ADD COLUMN

The column object begins as:

```json
"column": {
  "add": "ALTER TABLE table_name ADD COLUMN column_name;"
}
```

Command sequence:

```bash
git diff
git add .
git commit -m "feat: add column reference"
git log --oneline
```

### Why This Branch Is Long-Running

This branch will eventually contain several related column references:

- add column
- drop column
- rename column
- primary key
- foreign key

The workshop keeps it open while other branches are created and merged into
`main`. That creates opportunities to practice rebasing and conflict resolution.

## Phase 7: Fix a Bug on a Separate Branch

### Why the Fix Is Separate

The workshop notices that the CREATE TABLE syntax should be:

```sql
CREATE TABLE table_name();
```

not:

```sql
CREATE TABLE table_name;
```

The fix is unrelated to the active column feature, so it belongs on a separate
fix branch.

### Command Sequence

```bash
git checkout main
git checkout -b fix/create-table-syntax
git status
git diff
git add sql_reference.json
git commit -m "fix: create table syntax"
git checkout main
git branch
git merge fix/create-table-syntax
git log --oneline
git branch -d fix/create-table-syntax
```

### What the Diff Means

The diff is conceptually:

```diff
-    "create": "CREATE TABLE table_name;"
+    "create": "CREATE TABLE table_name();"
```

This is a bug fix because it corrects an existing reference.

## Phase 8: Rebase the Column Branch onto `main`

### Why Rebase Is Needed

The column branch was created before the table syntax fix. That means its
history is behind `main`.

Rebasing updates the branch by replaying its unique commits on top of the
latest `main`.

### Command Sequence

```bash
git checkout feat/add-column-references
git log --oneline
git rebase main
git log --oneline
```

### Mental Model

Before rebase:

```text
main:   A -- B -- C -- D -- fix/create-table-syntax
branch: A -- B -- C -- D -- feat/add-column-reference
```

After rebase:

```text
main:   A -- B -- C -- D -- fix/create-table-syntax
branch: A -- B -- C -- D -- fix/create-table-syntax -- feat/add-column-reference
```

The feature commit is moved to the top of the updated main history.

## Phase 9: Add DROP COLUMN

### JSON Change

The column object becomes:

```json
"column": {
  "add": "ALTER TABLE table_name ADD COLUMN column_name;",
  "drop": "ALTER TABLE table_name DROP COLUMN column_name;"
}
```

### Command Sequence

```bash
git status
git diff
git add sql_reference.json
git commit -m "feat: add drop column reference"
git log --oneline
```

## Phase 10: Simulate Parallel Work on Row References

### Create Insert Row Branch

```bash
git checkout main
git checkout -b feat/add-insert-row-reference
```

### Add INSERT Row Reference

```json
"row": {
  "insert": "INSERT INTO table_name(columns) VALUES(values);"
}
```

### Commit and Merge

```bash
git add sql_reference.json
git commit -m "feat: add insert row reference"
git checkout main
git branch
git merge feat/add-insert-row-reference
```

This simulates another developer adding row-related work while the column branch
is still active.

## Phase 11: Rebase with a Conflict

### Why the Conflict Happens

The row branch and column branch both edit nearby parts of the same JSON file.
When Git tries to replay the column commits on top of the updated main branch,
it cannot automatically decide how to combine the objects.

### Command Sequence

```bash
git checkout feat/add-column-references
git rebase main
```

Expected conflict status shape:

```text
CONFLICT (content): Merge conflict in sql_reference.json
error: could not apply ...
```

### Conflict Marker Shape

The file may contain sections like:

```json
[conflict start: HEAD]
  "row": {
    "insert": "INSERT INTO table_name(columns) VALUES(values);"
  }
[conflict separator]
  "column": {
    "add": "ALTER TABLE table_name ADD COLUMN column_name;"
  }
[conflict end: feat: add column reference]
```

In the real file, Git uses literal marker lines: `<<<<<<< HEAD`, `=======`,
and `>>>>>>> commit message`. They are written with labels here so this
repository does not look like it still contains an unresolved conflict.

### How to Fix It

The correct fix is not to keep either side blindly. The correct fix is to
restore valid JSON with both objects:

```json
  "row": {
    "insert": "INSERT INTO table_name(columns) VALUES(values);"
  },
  "column": {
    "add": "ALTER TABLE table_name ADD COLUMN column_name;"
  }
```

Then continue:

```bash
git status
git add sql_reference.json
git status
git rebase --continue
git log --oneline
```

### Why `git rebase --continue` Is Needed

During a rebase conflict, Git pauses. After the file is fixed and staged, Git
needs an explicit instruction to continue replaying the remaining commits.

## Phase 12: Add RENAME COLUMN

### JSON Change

```json
"rename": "ALTER TABLE table_name RENAME COLUMN column_name TO new_name;"
```

### Command Sequence

```bash
git status
git diff
git add sql_reference.json
git commit -m "feat: add rename column reference"
```

Now the column branch has several unique commits that will later be squashed.

## Phase 13: Learn `git stash`

### The Mistake

The workshop switches to the insert-row branch and adds an update-row reference
there. That is the wrong branch for the change.

### Add UPDATE Row Reference

```json
"update": "UPDATE table_name SET column_name = new_value WHERE condition;"
```

### Stash the Work

```bash
git status
git stash
git status
git stash list
```

### What `git stash` Does

`git stash` temporarily saves uncommitted changes and returns the working tree
to a clean state.

Example output shape:

```text
Saved working directory and index state WIP on feat/add-insert-row-reference: abc1234 feat: add insert row reference
```

### Pop the Stash

```bash
git stash pop
git stash list
```

`pop` applies the latest stash and removes it from the stash list.

### Apply the Stash Without Removing It

```bash
git stash
git stash list
git stash show
git stash show -p
git stash apply
git stash list
```

`apply` brings the changes back but keeps the stash entry.

### Drop a Stash

```bash
git stash
git stash list
git stash show stash@{1}
git stash show -p stash@{1}
git stash drop
git stash list
```

Useful naming rule:

- `stash@{0}` is the newest stash
- `stash@{1}` is the next older stash

## Phase 14: Move Stashed Work to the Correct Branch

### Command Sequence

```bash
git checkout main
git branch -d feat/add-insert-row-reference
git checkout -b feat/add-more-row-references
git stash list
git stash pop
git stash list
git diff
git add sql_reference.json
git commit -m "feat: add update row reference"
git checkout main
git merge feat/add-more-row-references
```

### Why This Is Better

The update-row reference is now committed on a branch whose name matches the
work:

```text
feat/add-more-row-references
```

Good branch names make history easier to review.

## Phase 15: Rebase Column Branch Again and Resolve Another Conflict

### Command Sequence

```bash
git checkout feat/add-column-references
git rebase main
git status
git add sql_reference.json
git status
git rebase --continue
git log --oneline
```

### Why This Conflict Is Harder

By this point, `main` has row references, and the column branch has column
references. The JSON file must be reconstructed so every object is in the right
place:

- database commands under `database`
- table commands under `table`
- row commands under `row`
- column commands under `column`

The correct mindset during conflict resolution is:

1. remove conflict markers
2. preserve all valid work
3. restore valid JSON syntax
4. stage the resolved file
5. continue the rebase

## Phase 16: Add Primary Key and Foreign Key References

### Add Primary Key

```json
"primary_key": "ALTER TABLE table_name ADD PRIMARY KEY(column_name);"
```

Command sequence:

```bash
git diff
git add sql_reference.json
git commit -m "feat: add primary key reference"
```

### Add Foreign Key

```json
"foreign_key": "ALTER TABLE table_name ADD FOREIGN KEY(column_name) REFERENCES table_name(column_name);"
```

Command sequence:

```bash
git diff
git add sql_reference.json
git commit -m "feat: add foreign key reference"
```

## Phase 17: Add DELETE Row Reference

### Command Sequence

```bash
git checkout feat/add-more-row-references
git diff
git add sql_reference.json
git commit -m "feat: add delete row reference"
git checkout main
git merge feat/add-more-row-references
git branch -d feat/add-more-row-references
```

### JSON Change

```json
"delete": "DELETE FROM table_name WHERE condition;"
```

### Why `WHERE` Matters

The `WHERE` condition limits which rows are deleted. Without it, a SQL
`DELETE` command can remove every row in the table.

## Phase 18: Add Missing Rename References on a Fix Branch

### Create the Fix Branch

```bash
git checkout -b fix/add-missing-rename-references
```

### Add Database Rename

```json
"rename": "ALTER DATABASE database_name RENAME TO new_name;"
```

Command sequence:

```bash
git diff
git add sql_reference.json
git commit -m "fix: add missing rename database reference"
```

This branch remains open because another missing rename reference will be added
later.

## Phase 19: Add Unique Reference, Reset It, Revert It, Then Drop It

This phase is intentionally about Git history manipulation.

### Add Unique Reference

```json
"unique": "ALTER TABLE table_name ADD UNIQUE(column_name);"
```

Command sequence:

```bash
git checkout feat/add-column-references
git rebase main
git status
git add sql_reference.json
git rebase --continue
git diff
git add sql_reference.json
git commit -m "feat: add unique reference"
```

### Undo the Commit with Reset

```bash
git reset HEAD~1
git log --oneline
git status
git diff
```

What happens:

- the commit disappears from the branch history
- the code change returns to the working tree
- the change is unstaged

This is a mixed reset, because no `--soft` or `--hard` flag is used.

| Reset Type | History | Staging | Working Tree |
| --- | --- | --- | --- |
| `git reset --soft HEAD~1` | moves back | keeps changes staged | keeps changes |
| `git reset HEAD~1` | moves back | unstages changes | keeps changes |
| `git reset --hard HEAD~1` | moves back | removes staged changes | removes working changes |

### Recommit the Unique Reference

```bash
git add sql_reference.json
git commit -m "feat: add unique reference"
```

### Revert the Commit

```bash
git revert HEAD
```

Git opens Nano with a default revert message. The workshop keeps the default
message, saves, and exits.

Conceptually, Nano shows:

```text
Revert "feat: add unique reference"

This reverts commit <hash>.
```

Save and exit:

```text
Ctrl+O
Enter
Ctrl+X
```

### Compare the Revert and Original Commit

```bash
git log --oneline
git show
git show HEAD~1
```

The revert commit has the opposite diff of the original commit. If the original
commit added a line, the revert commit removes that line.

### Drop Both Commits with Interactive Rebase

```bash
git rebase --interactive HEAD~2
```

Nano opens a todo list like:

```text
pick abc1111 feat: add unique reference
pick abc2222 Revert "feat: add unique reference"
```

Change both `pick` commands to `d`:

```text
d abc1111 feat: add unique reference
d abc2222 Revert "feat: add unique reference"
```

Save and exit. The two commits are removed from the branch history.

Important caution: this is history rewriting. It is appropriate here because
the work is local practice history, not shared public history.

## Phase 20: Reword a Commit with Interactive Rebase

### Command

```bash
git rebase --interactive --root
```

The workshop uses this to demonstrate rewording a commit message. In the todo
file, it changes the command beside:

```text
feat: add column reference
```

from:

```text
pick <hash> feat: add column reference
```

to:

```text
r <hash> feat: add column reference
```

or:

```text
reword <hash> feat: add column reference
```

Git opens Nano again for the commit message. The message becomes:

```text
feat: add column references
```

### Why `--root` Is Dangerous

Rebasing from `--root` can rewrite every commit hash from the beginning of the
repository. That makes the branch history diverge from `main`.

The workshop fixes this by rebasing against `main` again:

```bash
git rebase main
```

## Phase 21: Squash Column Commits

### Why Squash Is Used

The column branch has multiple small commits:

- add column
- drop column
- rename column
- primary key
- foreign key

Before merging into `main`, those commits are squashed into one cleaner commit.

### Command

```bash
git rebase --interactive HEAD~5
```

Nano todo file shape:

```text
pick abc1111 feat: add column references
pick abc2222 feat: add drop column reference
pick abc3333 feat: add rename column reference
pick abc4444 feat: add primary key reference
pick abc5555 feat: add foreign key reference
```

Change all but the first to `s`:

```text
pick abc1111 feat: add column references
s abc2222 feat: add drop column reference
s abc3333 feat: add rename column reference
s abc4444 feat: add primary key reference
s abc5555 feat: add foreign key reference
```

Git opens another Nano screen with combined commit messages. The workshop keeps
the generated messages and exits.

### Result

Before:

```text
abc5555 feat: add foreign key reference
abc4444 feat: add primary key reference
abc3333 feat: add rename column reference
abc2222 feat: add drop column reference
abc1111 feat: add column references
```

After:

```text
abc9999 feat: add column references
```

The final commit contains all the changes from the original five commits.

### Merge Column Branch

```bash
git checkout main
git merge feat/add-column-references
git branch -d feat/add-column-references
```

## Phase 22: Squash Missing Rename Fixes

### Continue the Rename Fix Branch

```bash
git checkout fix/add-missing-rename-references
git rebase main
git log -5 --oneline
```

### Add Table Rename

```json
"rename": "ALTER TABLE table_name RENAME TO new_name;"
```

Command sequence:

```bash
git diff
git add sql_reference.json
git commit -m "fix: add missing rename table reference"
git log -5 --oneline
```

### Squash the Two Fix Commits

```bash
git rebase --interactive HEAD~2
```

Todo file:

```text
pick abc1111 fix: add missing rename database reference
pick abc2222 fix: add missing rename table reference
```

Change the second line to squash:

```text
pick abc1111 fix: add missing rename database reference
s abc2222 fix: add missing rename table reference
```

In the next Nano screen, add a clean message at the top:

```text
fix: add missing rename references
```

Then save and exit.

### Merge the Fix Branch

```bash
git log -1
git checkout main
git merge fix/add-missing-rename-references
```

## Phase 23: Delete Completed Branches

### Command Sequence

```bash
git branch
git branch -d branch_name
git branch
```

Delete every completed branch except `main`.

Expected final branch list:

```text
* main
```

## Phase 24: Add `.gitignore` and `sample.env`

### Create the Branch

```bash
git checkout -b feat/add-gitignore
```

### Create a Secret File

```bash
touch .env
```

The workshop writes this into `.env`:

```text
SECRET=MY_SECRET
```

This is intentionally treated as sensitive local data.

### Create `.gitignore`

```bash
touch .gitignore
```

Add this line:

```text
.env
```

Now `git status` stops showing `.env`.

### Commit `.gitignore`

```bash
git status
git add .gitignore
git commit -m "feat: add .gitignore"
```

### Add a Safe Template

```bash
touch sample.env
```

`sample.env` contains:

```text
SECRET=
```

This file documents the required variable name without exposing a real value.

Commit it:

```bash
git status
git add sample.env
git commit -m "feat: add sample.env"
```

### Squash `.gitignore` and `sample.env`

```bash
git log -5 --oneline
git rebase --interactive HEAD~2
```

Todo file:

```text
pick abc1111 feat: add .gitignore
pick abc2222 feat: add sample.env
```

Change the second line to:

```text
s abc2222 feat: add sample.env
```

In the commit message Nano screen, add:

```text
feat: add .gitignore and sample.env
```

Then save and exit.

### Merge the Environment Branch

```bash
git log -1
git checkout main
git merge feat/add-gitignore
git branch -d feat/add-gitignore
```

## Final History Shape

The final `git log --oneline` should be clean and readable. Hashes will differ,
but the message sequence should look similar to:

```text
abc9999 feat: add .gitignore and sample.env
abc8888 fix: add missing rename references
abc7777 feat: add column references
abc6666 feat: add delete row reference
abc5555 feat: add update row reference
abc4444 feat: add insert row reference
abc3333 fix: create table syntax
abc2222 feat: add drop table reference
abc1111 feat: add create table reference
abc0003 feat: add drop database reference
abc0002 feat: add create database reference
abc0001 Initial commit
```

This history is useful because each commit message explains why the snapshot
exists.

## Final Repository State

Final tracked files:

```text
sql_reference/
├── .gitignore
├── README.md
├── sample.env
└── sql_reference.json
```

Final ignored local file:

```text
sql_reference/
└── .env
```

## Core Lessons

- `git status` should be checked constantly.
- `git diff` should be used before staging.
- `git add` prepares changes for the next commit.
- `git commit` records staged changes into history.
- Feature branches keep unfinished work away from `main`.
- Fix branches isolate corrections from unrelated feature work.
- `git merge` brings completed branch work into the current branch.
- `git rebase main` updates a branch by replaying its commits on top of the
  latest `main`.
- Conflicts require manual file repair, staging, and `git rebase --continue`.
- `git stash` is useful when work was started on the wrong branch.
- `git reset HEAD~1` removes a local commit but keeps its changes.
- `git revert HEAD` creates a new commit that undoes another commit.
- Interactive rebase can reword, drop, or squash commits.
- Squashing makes a branch easier to review before merging.
- `.gitignore` protects local files that should not be committed.
- `sample.env` documents required environment variables safely.
