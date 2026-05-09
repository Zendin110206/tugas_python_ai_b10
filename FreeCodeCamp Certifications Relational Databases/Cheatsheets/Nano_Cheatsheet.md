# Nano Cheatsheet

This cheatsheet is a quick lookup reference for Nano terminal editing syntax
and shortcuts learned in the freeCodeCamp Relational Databases Certification
track.

Use it when editing files directly from a terminal session.

## Open and Create Files

| Goal | Command | Example | Notes |
| --- | --- | --- | --- |
| Open a file | `nano filename` | `nano castle.sh` | Opens the file in Nano. |
| Create a file before editing | `touch filename` | `touch castle.sh` | Creates an empty file. |
| Create through Nano | `nano new_file` | `nano notes.txt` | File is created when saved. |
| Run a Bash file | `bash filename` | `bash castle.sh` | Runs the file with Bash. |

## Shortcut Notation

| Nano Notation | Actual Keys | Meaning |
| --- | --- | --- |
| `^O` | `Ctrl+O` | Write out, or save. |
| `^X` | `Ctrl+X` | Exit Nano. |
| `^K` | `Ctrl+K` | Cut current line. |
| `^U` | `Ctrl+U` | Paste or uncut. |
| `^W` | `Ctrl+W` | Search. |
| `M-` | `Alt` key, or `Esc` then key | Meta shortcut. |

## Save and Exit

| Goal | Shortcut Sequence | Notes |
| --- | --- | --- |
| Save current file | `Ctrl+O`, then `Enter` | `Enter` confirms the filename. |
| Exit after saving | `Ctrl+O`, `Enter`, `Ctrl+X` | Standard safe workflow. |
| Exit without changes | `Ctrl+X` | If there are unsaved edits, Nano asks whether to save. |
| Cancel a prompt | `Ctrl+C` | Useful if the save/search prompt was opened by mistake. |

## Editing Lines

| Goal | Shortcut | Example Use |
| --- | --- | --- |
| Cut one line | `Ctrl+K` | Remove `echo hello nano`. |
| Paste a cut line | `Ctrl+U` | Duplicate a castle wall row. |
| Duplicate current line | `Ctrl+K`, `Ctrl+U`, `Ctrl+U` | Cut once and paste twice. |
| Move around | Arrow keys | Position cursor before editing. |

## Multi-Line Output Pattern

| Goal | Pattern | Example |
| --- | --- | --- |
| Print several lines | `echo " ... "` | See below. |

```bash
echo "
|                    |
|____________________|
"
```

This pattern prints the line breaks inside the quoted text.

## Backslash Edge Case

| Situation | Risk | Fix |
| --- | --- | --- |
| A line ends with `\` inside double quotes | Bash can escape the newline. | Add one real space after the final `\`, or use a safer output style. |

Documentation-safe notation:

```text
/  \              /  \[space]
```

`[space]` means one actual space after the final backslash. It is shown as text
because invisible trailing spaces are hard to review in Markdown files.

## Beginner Checklist

| Step | Action |
| --- | --- |
| 1 | Open the file with `nano filename`. |
| 2 | Edit using keyboard navigation. |
| 3 | Save with `Ctrl+O`. |
| 4 | Confirm filename with `Enter`. |
| 5 | Exit with `Ctrl+X`. |
| 6 | Run or inspect the file from the terminal. |
