# Bash Text Processing Reference

This reference documents the Bash syntax practiced in **Build a Kitty Ipsum
Translator**.

The goal is to make the command patterns easy to reuse when working with text
files, stream redirection, pattern matching, replacements, and file comparison.

## Standard Streams

Every command can interact with three standard streams.

| Stream | Number | Direction | Default source or destination |
| --- | ---: | --- | --- |
| `stdin` | `0` | Input | Keyboard |
| `stdout` | `1` | Successful output | Terminal |
| `stderr` | `2` | Error output | Terminal |

Example:

```bash
read NAME
echo "Hello $NAME"
bad_command
```

In that example:

- `read NAME` uses `stdin`
- `echo` writes to `stdout`
- `bad_command` writes to `stderr`

## Redirection Quick Reference

| Goal | Syntax | Example | Notes |
| --- | --- | --- | --- |
| Redirect `stdout` and overwrite file | `command > file` | `echo hello > stdout.txt` | Creates or replaces the file. |
| Redirect `stdout` and append file | `command >> file` | `echo hello >> stdout.txt` | Adds output to the end. |
| Explicitly redirect `stdout` | `command 1> file` | `echo hello 1> stdout.txt` | Same stream as `>`. |
| Redirect `stderr` | `command 2> file` | `bad_command 2> stderr.txt` | Captures error output. |
| Redirect `stdin` from file | `command < file` | `read NAME < name.txt` | Reads input from a file. |
| Empty a file | `> file` | `> stdout.txt` | Overwrites file with nothing. |

## Combining Redirections

Capture successful output and errors separately:

```bash
./script.sh 1> stdout.txt 2> stderr.txt
```

Use file input while capturing both output streams:

```bash
./script.sh < name.txt 1> stdout.txt 2> stderr.txt
```

The order used in the workshop is also valid:

```bash
./script.sh < name.txt 2> stderr.txt 1> stdout.txt
```

## `read`

`read` takes one line from `stdin` and stores it in a variable.

| Goal | Syntax | Example |
| --- | --- | --- |
| Read keyboard input | `read VARIABLE` | `read NAME` |
| Read from a file | `read VARIABLE < file` | `read NAME < name.txt` |
| Print the variable | `echo "$VARIABLE"` | `echo "$NAME"` |

Safer script pattern:

```bash
read -r NAME
echo "Hello $NAME"
```

`-r` prevents backslash escaping. The freeCodeCamp workshop uses plain `read`
because the goal is to focus on stream behavior first.

## Pipes

A pipe sends `stdout` from the command on the left into `stdin` of the command
on the right.

```bash
echo freeCodeCamp | cat
```

Pipe pattern:

```text
command_1 stdout -> command_2 stdin
```

Important subshell behavior:

```bash
echo freeCodeCamp | read NAME
echo "$NAME"
```

The `read` command runs in a subshell in this pattern, so the variable does not
remain available in the parent shell.

## `cat`

| Goal | Syntax | Example | Notes |
| --- | --- | --- | --- |
| Print a file | `cat file` | `cat name.txt` | Reads file argument. |
| Read from redirected input | `cat < file` | `cat < name.txt` | Reads from `stdin`. |
| Read from a pipe | `command \| cat` | `echo text \| cat` | Prints piped input. |
| Use inside a script | `cat $1` | `cat $1 \| sed ...` | Reads the first argument; with no argument, it can read `stdin`. |

The final `translate.sh` uses `cat $1` so the script can support both file
arguments and redirected or piped input.

## `wc`

`wc` counts lines, words, bytes, or characters.

| Goal | Syntax | Example |
| --- | --- | --- |
| Count lines, words, bytes | `wc file` | `wc kitty_ipsum_1.txt` |
| Count lines only | `wc -l file` | `wc -l kitty_ipsum_1.txt` |
| Count words only | `wc -w file` | `wc -w kitty_ipsum_1.txt` |
| Count characters only | `wc -m file` | `wc -m kitty_ipsum_1.txt` |
| Count bytes only | `wc -c file` | `wc -c kitty_ipsum_1.txt` |

Input style affects output:

```bash
wc -l kitty_ipsum_1.txt
cat kitty_ipsum_1.txt | wc -l
wc -l < kitty_ipsum_1.txt
```

When a filename is passed, `wc` prints the count and filename. With a pipe or
`stdin` redirection, it prints only the count. The count-only output is better
when writing a report file.

## `grep`

`grep` searches for lines that match a text pattern or regular expression.

| Goal | Syntax | Example | Notes |
| --- | --- | --- | --- |
| Search text | `grep 'pattern' file` | `grep 'meow' kitty_ipsum_1.txt` | Prints matching lines. |
| Highlight matches | `grep --color 'pattern' file` | `grep --color 'meow' kitty_ipsum_1.txt` | Useful for manual inspection. |
| Show line numbers | `grep -n 'pattern' file` | `grep -n 'meow' kitty_ipsum_1.txt` | Prefixes output with line numbers. |
| Count matching lines | `grep -c 'pattern' file` | `grep -c 'meow' kitty_ipsum_1.txt` | Counts lines, not total matches. |
| Print only matches | `grep -o 'pattern' file` | `grep -o 'meow[a-z]*' kitty_ipsum_1.txt` | One match per output line. |
| Use extended regex | `grep -E 'pattern' file` | See below | Required for alternation with `\|`. |

Extended regex example:

```bash
grep --color -E 'dog[a-z]*|woof[a-z]*' doggy_ipsum_1.txt
```

## Regex Patterns Used

| Pattern | Meaning | Example match |
| --- | --- | --- |
| `meow` | Exact text. | `meow` |
| `meow[a-z]*` | `meow` followed by zero or more lowercase letters. | `meowzer` |
| `cat[a-z]*` | `cat` followed by zero or more lowercase letters. | `catnip` |
| `[0-9]` | One digit. | `7` |
| `[0-9]+` | One or more digits. | `123` |
| `.*` | Any remaining characters on the line. | `: text after line number` |

## Counting Total Matches

`grep -c` counts matching lines. It does not count every occurrence.

For total occurrences, use `grep -o` and `wc -l`:

```bash
grep -o 'meow[a-z]*' kitty_ipsum_1.txt | wc -l
grep -o 'cat[a-z]*' kitty_ipsum_1.txt | wc -l
```

Why this works:

1. `grep -o` prints each match on its own line.
2. `wc -l` counts those output lines.

## `sed`

`sed` reads text, transforms it, and writes the transformed result to `stdout`.
By default, it does not modify the source file.

Basic substitution:

```bash
sed 's/free/f233/' name.txt
```

| Goal | Syntax | Example | Notes |
| --- | --- | --- | --- |
| Replace first match per line | `sed 's/old/new/' file` | `sed 's/r/2/' name.txt` | Default behavior. |
| Replace all matches per line | `sed 's/old/new/g' file` | `sed 's/cat/dog/g' file.txt` | `g` means global. |
| Ignore case | `sed 's/old/new/i' file` | `sed 's/free/f233/i' name.txt` | Case-insensitive match. |
| Use extended regex | `sed -E 's/pattern/new/' file` | See below | Enables `+`, groups, and alternation. |
| Read from redirected input | `sed 's/old/new/' < file` | `sed 's/r/2/' < name.txt` | Uses `stdin`. |
| Read from pipe | `command \| sed 's/old/new/'` | `cat name.txt \| sed 's/r/2/'` | Uses piped input. |

## Multiple `sed` Replacements

Multiple substitutions can be placed in one `sed` command by separating them
with semicolons:

```bash
sed -E 's/catnip/dogchow/g; s/cat/dog/g; s/meow|meowzer/woof/g'
```

Replacement order matters. In this workshop, `catnip` must be replaced before
`cat`; otherwise, `catnip` would become `dognip`.

## Capture Groups in `sed`

Capture a line number and remove the rest of the line:

```bash
grep -n 'meow[a-z]*' kitty_ipsum_1.txt | sed -E 's/([0-9]+).*/\1/'
```

| Part | Meaning |
| --- | --- |
| `-E` | Enables extended regular expressions. |
| `([0-9]+)` | Captures one or more digits. |
| `.*` | Matches the rest of the line. |
| `\1` | Reuses the first captured group. |

This is how the workshop turns output like this:

```text
4:kitty text with meow
```

into this:

```text
4
```

## Report File Pattern

Use `echo -e`, `grep`, `sed`, and `wc` to append a formatted report.

```bash
echo -e "\nNumber of times meow or meowzer appears:" >> kitty_info.txt
grep -o 'meow[a-z]*' kitty_ipsum_1.txt | wc -l >> kitty_info.txt

echo -e "\nLines that they appear on:" >> kitty_info.txt
grep -n 'meow[a-z]*' kitty_ipsum_1.txt | sed -E 's/([0-9]+).*/\1/' >> kitty_info.txt
```

The same pattern can be reused for other search terms by changing the regex.

## Final Translator Pattern

```bash
#!/bin/bash

cat $1 | sed -E 's/catnip/dogchow/g; s/cat/dog/g; s/meow|meowzer/woof/g'
```

Run with a file argument:

```bash
./translate.sh kitty_ipsum_1.txt
```

Run with redirected input:

```bash
./translate.sh < kitty_ipsum_1.txt
```

Run with piped input:

```bash
cat kitty_ipsum_1.txt | ./translate.sh
```

Write translated output to a file:

```bash
./translate.sh kitty_ipsum_1.txt > doggy_ipsum_1.txt
./translate.sh kitty_ipsum_2.txt > doggy_ipsum_2.txt
```

## `diff`

`diff` compares two files.

| Goal | Syntax | Example |
| --- | --- | --- |
| Compare files | `diff file_1 file_2` | `diff kitty_ipsum_1.txt doggy_ipsum_1.txt` |
| Compare with color | `diff --color file_1 file_2` | `diff --color kitty_ipsum_1.txt doggy_ipsum_1.txt` |

Use `diff` after a transformation to confirm exactly which lines changed.

## Common Mistakes

| Problem | Likely cause | Fix |
| --- | --- | --- |
| Error output still appears in terminal | Redirected `stdout` instead of `stderr`. | Use `2> stderr.txt`. |
| File was overwritten accidentally | Used `>` instead of `>>`. | Use `>>` when appending. |
| `grep -c` count is lower than expected | It counted matching lines, not all matches. | Use `grep -o ... \| wc -l`. |
| `sed` did not understand `+` or `\|` | Extended regex was not enabled. | Use `sed -E`. |
| Only first match changed on each line | Missing global flag. | Add `g` at the end of the substitution. |
| `catnip` became `dognip` | `cat` was replaced before `catnip`. | Replace longer/specific words first. |
| Variable from `read` after a pipe is missing | `read` ran in a subshell. | Use input redirection when the variable must remain in the current shell. |
