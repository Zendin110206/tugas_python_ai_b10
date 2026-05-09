# Build a Castle

## Context

This document summarizes the **Build a Castle** workshop from the freeCodeCamp
Relational Databases Certification track.

The workshop was completed in **GitHub Codespaces** through the CodeRoad
extension. The original lesson is interactive and step-based, so this repository
keeps a cleaned learning record instead of raw copied prompts from the CodeRoad
interface.

Although this workshop appears in the Git section of the certification path,
the main topic practiced here is terminal-based file editing with Nano.

## Workshop Goal

Create and edit a small Bash script named `castle.sh` using Nano, then run the
script from the terminal to print ASCII-art castle output.

The workshop focuses on:

- creating a file from the terminal
- opening a file with Nano
- saving changes with `Ctrl+O`
- exiting Nano with `Ctrl+X`
- cutting and pasting lines with `Ctrl+K` and `Ctrl+U`
- editing a multi-line Bash `echo` string
- running a script with `bash filename`
- understanding the `^` and `M-` shortcut notation in Nano
- handling backslash edge cases inside quoted Bash output

## Environment

- Platform: freeCodeCamp Relational Databases Certification
- Workspace: GitHub Codespaces
- Tutorial runner: CodeRoad
- Shell: Bash
- Terminal editor: Nano

## Final File

| File | Purpose |
| --- | --- |
| `castle.sh` | Bash script that prints a welcome message and an ASCII-art castle. |

This repository does not include a standalone `castle.sh` artifact for this
workshop. The final script structure is documented below so the workshop can be
recreated without inventing a local artifact that was not copied from the
original CodeRoad workspace.

## Walkthrough

### 1. Confirm the Terminal Works

The workshop starts by opening a terminal and running a basic command:

```bash
echo hello nano
```

This verifies that the terminal can execute commands and print output.

### 2. Create the Script File

Create an empty script file:

```bash
touch castle.sh
```

Confirm the file exists:

```bash
ls
```

`touch` creates the file, and `ls` verifies that it appears in the current
directory.

### 3. Open the File with Nano

Open the script in Nano:

```bash
nano castle.sh
```

Nano opens directly inside the terminal. The bottom of the screen shows common
keyboard shortcuts.

Important shortcut notation:

| Notation | Meaning |
| --- | --- |
| `^O` | Press `Ctrl+O`. |
| `^X` | Press `Ctrl+X`. |
| `^K` | Press `Ctrl+K`. |
| `^U` | Press `Ctrl+U`. |
| `M-` | Press `Alt` plus the shown key, or press `Esc` then the key on some systems. |

Nano is keyboard-driven. The cursor is moved with the keyboard, not with the
mouse.

### 4. Add and Run the First Command

Inside `castle.sh`, add:

```bash
echo hello nano
```

Save the file:

```text
Ctrl+O
Enter
```

Exit Nano:

```text
Ctrl+X
```

Run the script:

```bash
bash castle.sh
```

This confirms that the command inside the file runs through Bash.

### 5. Start the Castle Drawing

Open the file again:

```bash
nano castle.sh
```

Remove the first line with `Ctrl+K`, then start a multi-line `echo` block:

```bash
echo "

"
```

The castle drawing will be placed between the quotes.

### 6. Add the Ground Level

Add twenty underscores between the quotes:

```bash
echo "
____________________
"
```

Then add vertical bars at both ends:

```bash
echo "
|____________________|
"
```

Save with `Ctrl+O`.

### 7. Add Castle Stories

Add empty wall rows above the ground level:

```bash
echo "
|                    |
|                    |
|                    |
|                    |
|                    |
|____________________|
"
```

This practices repeated line editing. The workshop specifically introduces:

| Shortcut | Purpose |
| --- | --- |
| `Ctrl+K` | Cut the current line. |
| `Ctrl+U` | Paste or uncut the most recently cut line. |

### 8. Shape the Roof

Change the top wall row into the roof base:

```bash
|  |______________|  |
```

Add tower sides above it:

```text
/  \              /  \
|  |______________|  |
```

Then add tower peaks:

```text
 /\                /\
/  \              /  \
```

### 9. Understand the Backslash Edge Case

The workshop intentionally exposes a Bash string edge case:

```text
 /\                /\
/  \              /  \
```

In a double-quoted multi-line string, a backslash at the very end of a line can
escape the newline. That makes the printed castle look broken.

The CodeRoad fix is to add one real space after the right-side backslash on the
affected roof lines. To avoid invisible trailing whitespace in this repository,
the required spaces are shown with `[space]` markers below:

```text
 /\                /\[space]
/  \              /  \[space]
```

When recreating the workshop in Nano, replace `[space]` with one actual space.

This detail matters because the visible character is the same, but Bash treats
the line differently when the final character is a backslash.

### 10. Add Windows and Door

Add three windows on one wall row:

```text
|   []    []    []   |
```

Then change the bottom two rows into a door:

```text
|         __         |
|________|  |________|
```

### 11. Add the Welcome Message

At the top of the file, add another `echo` block:

```bash
echo "
Welcome to my castle
"
```

Then keep the castle drawing in the second `echo` block.

## Final Script Shape

The final script has this structure:

```bash
echo "
Welcome to my castle
"

echo "
 /\                /\[space]
/  \              /  \[space]
|  |______________|  |
|                    |
|                    |
|   []    []    []   |
|         __         |
|________|  |________|
"
```

When recreating the actual `castle.sh` file in Nano, replace `[space]` with one
real space after each right-side backslash. The marker is only used in this
Markdown note so the whitespace is visible and reviewable.

## Command Reference

| Command | Purpose |
| --- | --- |
| `echo hello nano` | Print text to the terminal. |
| `touch castle.sh` | Create an empty script file. |
| `ls` | Confirm that the file exists. |
| `nano castle.sh` | Open the file in Nano. |
| `bash castle.sh` | Run the script with Bash. |

## Nano Shortcut Reference

| Shortcut | Meaning | Used for |
| --- | --- | --- |
| `Ctrl+O` | Write out | Save the current file. |
| `Enter` after `Ctrl+O` | Confirm filename | Save using the current file name. |
| `Ctrl+X` | Exit | Leave Nano and return to the terminal. |
| `Ctrl+K` | Cut text | Remove the current line. |
| `Ctrl+U` | Uncut text | Paste the most recently cut line. |
| Arrow keys | Move cursor | Navigate without a mouse. |

## Key Takeaways

- Nano is useful when a file needs to be edited directly from the terminal.
- `Ctrl+O`, `Enter`, and `Ctrl+X` are the core save-and-exit workflow.
- `Ctrl+K` and `Ctrl+U` make repeated line editing faster.
- Bash can run a script with `bash filename` even before executable permissions
  are introduced.
- Backslashes at the end of a double-quoted line need special attention because
  they can escape the newline.
- Invisible whitespace can affect program behavior, so notes should make those
  spaces visible when documenting an edge case.
