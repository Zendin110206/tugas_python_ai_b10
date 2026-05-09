# Nano Editing Reference

## Purpose

This reference documents the Nano editor concepts practiced in the **Build a
Castle** workshop.

It is written as a beginner-friendly lookup guide for editing files directly in
the terminal.

## What Nano Is

Nano is a terminal-based text editor. It lets a user open, edit, save, and exit
files without leaving the command line.

This is useful in freeCodeCamp Codespaces because many workshop tasks happen
inside a Linux terminal environment.

## Opening a File

| Goal | Command | Example |
| --- | --- | --- |
| Open an existing file | `nano filename` | `nano castle.sh` |
| Create and open a new file | `nano new_file` | `nano notes.txt` |
| Create an empty file before editing | `touch filename` | `touch castle.sh` |

If the file does not exist, `nano filename` can create it when the file is
saved.

## Reading Nano Shortcut Notation

Nano shows shortcuts at the bottom of the editor.

| Notation | Meaning | Example |
| --- | --- | --- |
| `^` | Press `Ctrl` with the shown key. | `^O` means `Ctrl+O`. |
| `M-` | Press `Alt` with the shown key, or `Esc` then the key. | `M-U` means `Alt+U` or `Esc`, then `U`. |

The `M-` notation stands for "meta". On some systems the `Alt` key works. On
others, pressing `Esc` first is more reliable.

## Core Save and Exit Workflow

| Goal | Shortcut | What Happens |
| --- | --- | --- |
| Save file | `Ctrl+O` | Nano writes the current buffer to a file. |
| Confirm file name | `Enter` | Keeps the current filename when saving. |
| Exit editor | `Ctrl+X` | Returns to the terminal. |
| Cancel a prompt | `Ctrl+C` | Cancels the current Nano prompt. |

Normal workflow:

```text
Ctrl+O
Enter
Ctrl+X
```

This means:

1. Save the file.
2. Confirm the filename.
3. Exit Nano.

## Moving Around

| Goal | Key |
| --- | --- |
| Move left, right, up, or down | Arrow keys |
| Move to previous page | `Ctrl+Y` |
| Move to next page | `Ctrl+V` |
| Search text | `Ctrl+W` |

Nano is designed for keyboard navigation. In many terminal sessions, mouse
clicking does not move the editing cursor.

## Cutting and Pasting Lines

| Goal | Shortcut | Notes |
| --- | --- | --- |
| Cut current line | `Ctrl+K` | Removes the line where the cursor is located. |
| Paste cut line | `Ctrl+U` | Inserts the most recently cut line. |
| Duplicate a line | `Ctrl+K`, then `Ctrl+U`, `Ctrl+U` | Cut once, then paste twice. |

The Build a Castle workshop uses this pattern to create repeated wall rows:

```text
|                    |
|                    |
|                    |
```

## Editing a Bash Script with Nano

Basic workflow:

```bash
touch castle.sh
nano castle.sh
bash castle.sh
```

Inside the file:

```bash
echo hello nano
```

Save and exit:

```text
Ctrl+O
Enter
Ctrl+X
```

Run the script:

```bash
bash castle.sh
```

## Multi-Line `echo` Pattern

The workshop uses a multi-line double-quoted string:

```bash
echo "
line one
line two
"
```

Everything between the quotes is printed, including line breaks.

This is why the castle can be drawn inside one `echo` command:

```bash
echo "
|                    |
|____________________|
"
```

## Backslash at End of Line

A backslash at the very end of a line inside a double-quoted Bash string can
escape the newline.

Problem shape:

```text
/  \              /  \
```

The final character is a backslash, so Bash can treat the newline specially.

Workshop fix:

```text
/  \              /  \[space]
```

`[space]` means one real space after the final backslash. The marker is shown
only so the invisible space is clear in documentation.

Alternative professional approaches outside the workshop:

| Approach | Example | Why It Helps |
| --- | --- | --- |
| Use single quotes | `echo '/  \              /  \'` | Backslashes are treated more literally. |
| Use `printf` | `printf '%s\n' '/  \              /  \'` | More predictable for formatted output. |

The workshop keeps the original `echo` style because the goal is to learn Nano,
not to optimize Bash output formatting.

## Common Beginner Mistakes

| Problem | Likely Cause | Fix |
| --- | --- | --- |
| File changes disappear | Exited without saving. | Use `Ctrl+O`, `Enter`, then `Ctrl+X`. |
| Pressing `Ctrl+O` seems unfinished | Nano is asking for the filename. | Press `Enter` to confirm. |
| Cursor does not move with mouse | Terminal cursor is keyboard-based. | Use arrow keys. |
| Script prints broken roof lines | A line ends with a backslash. | Add a real trailing space or use a different output style. |
| Script does not run as expected | File was edited but not saved. | Save before running `bash castle.sh`. |

## Practical Checklist

Use this checklist when editing a small file in Nano:

1. Open the file with `nano filename`.
2. Make the edit.
3. Save with `Ctrl+O`.
4. Confirm with `Enter`.
5. Exit with `Ctrl+X`.
6. Run or inspect the file from the terminal.

For scripts, test after each meaningful change:

```bash
bash castle.sh
```
