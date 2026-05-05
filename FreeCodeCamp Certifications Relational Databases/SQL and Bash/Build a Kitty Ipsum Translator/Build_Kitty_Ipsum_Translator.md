# Build a Kitty Ipsum Translator

## Context

This document summarizes the **Build a Kitty Ipsum Translator** workshop from
the freeCodeCamp Relational Databases Certification track.

The workshop was completed in **GitHub Codespaces** through the CodeRoad
extension. The original lesson is interactive and step-based, so this repository
keeps a cleaned learning record instead of raw copied prompts from the CodeRoad
interface.

This workshop belongs to the SQL and Bash section, but the main focus is
advanced Bash command-line behavior rather than SQL. It explains how commands
receive input, produce output, handle errors, and can be chained together to
process text files.

## Workshop Goal

Build a small Bash translator that converts two `kitty_ipsum` text files into
`doggy_ipsum` text files.

The workshop focuses on:

- standard streams: `stdin`, `stdout`, and `stderr`
- output redirection with `>`, `>>`, `1>`, and `2>`
- input redirection with `<`
- pipes with `|`
- how pipes can create subshell behavior
- using `read` with keyboard input, redirected input, and piped input
- creating executable Bash scripts
- inspecting files with `cat`
- counting lines, words, bytes, and characters with `wc`
- searching text with `grep`
- using regular expressions in `grep`
- extracting only matches with `grep -o`
- replacing text with `sed`
- using extended regular expressions with `sed -E`
- using capture groups in `sed`
- comparing files with `diff`

## Environment

- Platform: freeCodeCamp Relational Databases Certification
- Workspace: GitHub Codespaces
- Tutorial runner: CodeRoad
- Shell: Bash

## Final Files

| File | Purpose |
| --- | --- |
| `kitty_ipsum_1.txt` | First source text file containing kitty-themed placeholder text. |
| `kitty_ipsum_2.txt` | Second source text file containing kitty-themed placeholder text. |
| `doggy_ipsum_1.txt` | Translated output generated from `kitty_ipsum_1.txt`. |
| `doggy_ipsum_2.txt` | Translated output generated from `kitty_ipsum_2.txt`. |
| `kitty_info.txt` | Summary report containing line, word, character, and pattern counts. |
| `name.txt` | Small input file used to practice `stdin` redirection. |
| `stdout.txt` | Captured standard output from the stream practice script. |
| `stderr.txt` | Captured standard error from the stream practice script. |
| `script.sh` | Practice script for `stdin`, `stdout`, and `stderr`. |
| `translate.sh` | Final translator script. |
| `Build_Kitty_Ipsum_Translator.md` | Cleaned workshop documentation. |
| `Bash_Text_Processing_Reference.md` | Detailed syntax reference for the Bash concepts used in this workshop. |

## Standard Stream Practice

Bash commands commonly interact with three streams:

| Stream | Number | Default behavior | Example |
| --- | ---: | --- | --- |
| `stdin` | `0` | Reads input from the keyboard. | `read NAME` |
| `stdout` | `1` | Prints successful output to the terminal. | `echo hello bash` |
| `stderr` | `2` | Prints error output to the terminal. | `bad_command` |

The workshop starts by redirecting successful output:

```bash
echo hello bash > stdout.txt
echo hello bash >> stdout.txt
echo hello bash 1> stdout.txt
```

Important behavior:

- `>` creates or overwrites a file.
- `>>` appends to the end of a file.
- `1>` explicitly redirects `stdout`.
- `> stdout.txt` with no command output empties the file.

The workshop then redirects errors:

```bash
bad_command 2> stderr.txt
```

This matters because `bad_command` does not produce normal `stdout`; it produces
`stderr`. A regular `>` redirection does not capture that error stream.

## Input Redirection and Pipes

The `read` command takes input from `stdin`:

```bash
read NAME
echo "$NAME"
```

Input can come from a file:

```bash
echo freeCodeCamp > name.txt
read NAME < name.txt
echo "$NAME"
```

Input can also come from another command through a pipe:

```bash
echo Zaenal | cat
```

The workshop also demonstrates a subtle point:

```bash
echo Zaenal | read NAME
echo "$NAME"
```

In this case, `read NAME` runs in a subshell, so the variable does not remain set
in the parent shell. This is an important distinction when writing scripts that
depend on variables.

## Practice Script for Streams

The workshop creates `script.sh`:

```bash
#!/bin/bash
read NAME
echo Hello $NAME
bad_command
```

The script intentionally contains `bad_command` so the workshop can demonstrate
how successful output and error output are separated.

Run it with keyboard input:

```bash
./script.sh
```

Run it with piped input:

```bash
echo freeCodeCamp | ./script.sh
```

Capture only errors:

```bash
echo freeCodeCamp | ./script.sh 2> stderr.txt
```

Capture errors and successful output separately:

```bash
echo freeCodeCamp | ./script.sh 2> stderr.txt 1> stdout.txt
```

Run it with file input:

```bash
./script.sh < name.txt 2> stderr.txt 1> stdout.txt
```

## Counting Text with `wc`

The source files are inspected with `cat`:

```bash
cat kitty_ipsum_1.txt
cat kitty_ipsum_2.txt
```

Then the workshop uses `wc`:

```bash
wc kitty_ipsum_1.txt
wc -l kitty_ipsum_1.txt
wc -w kitty_ipsum_1.txt
wc -m kitty_ipsum_1.txt
```

The important options are:

| Option | Meaning |
| --- | --- |
| `-l` | Count lines. |
| `-w` | Count words. |
| `-m` | Count characters. |
| `-c` | Count bytes. |

Input method changes the shape of the output:

```bash
wc -l kitty_ipsum_1.txt
cat kitty_ipsum_1.txt | wc -l
wc -l < kitty_ipsum_1.txt
```

When the filename is passed as an argument, `wc` includes the filename in the
output. With a pipe or input redirection, it prints only the count, which is
cleaner when appending numbers to a report file.

## Building `kitty_info.txt`

The report starts with a heading:

```bash
echo "~~ kitty_ipsum_1.txt info ~~" > kitty_info.txt
```

Append labels and counts:

```bash
echo -e "\nNumber of lines:" >> kitty_info.txt
cat kitty_ipsum_1.txt | wc -l >> kitty_info.txt

echo -e "\nNumber of words:" >> kitty_info.txt
cat kitty_ipsum_1.txt | wc -w >> kitty_info.txt

echo -e "\nNumber of characters:" >> kitty_info.txt
wc -m < kitty_ipsum_1.txt >> kitty_info.txt
```

The same pattern is repeated for `kitty_ipsum_2.txt`.

## Searching Text with `grep`

The workshop searches for words beginning with `meow`:

```bash
grep --color -n 'meow[a-z]*' kitty_ipsum_1.txt
```

The pattern means:

| Part | Meaning |
| --- | --- |
| `meow` | Match the exact text `meow`. |
| `[a-z]` | Match one lowercase letter. |
| `*` | Match zero or more of the previous pattern. |

So `meow[a-z]*` matches both `meow` and `meowzer`.

To count total matches, use `grep -o` and `wc -l`:

```bash
grep -o 'meow[a-z]*' kitty_ipsum_1.txt | wc -l
```

This is more accurate than `grep -c` when multiple matches can appear on the
same line, because `grep -c` counts matching lines, not individual matches.

The same approach is used for words beginning with `cat`:

```bash
grep -o 'cat[a-z]*' kitty_ipsum_1.txt | wc -l
```

## Extracting Line Numbers with `sed`

`grep -n` prints line numbers and matching lines:

```bash
grep -n 'meow[a-z]*' kitty_ipsum_1.txt
```

The output still includes the text after each line number. To keep only the
numbers, the workshop uses `sed` with an extended regular expression:

```bash
grep -n 'meow[a-z]*' kitty_ipsum_1.txt | sed -E 's/([0-9]+).*/\1/'
```

How it works:

| Pattern part | Meaning |
| --- | --- |
| `([0-9]+)` | Capture one or more digits. |
| `.*` | Match the rest of the line. |
| `\1` | Replace the whole line with the first captured group. |

Append the extracted line numbers to the report:

```bash
grep -n 'meow[a-z]*' kitty_ipsum_1.txt | sed -E 's/([0-9]+).*/\1/' >> kitty_info.txt
```

## Translator Script

The final script is `translate.sh`:

```bash
#!/bin/bash

cat $1 | sed -E 's/catnip/dogchow/g; s/cat/dog/g; s/meow|meowzer/woof/g'
```

The script supports the three input styles practiced in the workshop:

```bash
./translate.sh kitty_ipsum_1.txt
./translate.sh < kitty_ipsum_1.txt
cat kitty_ipsum_1.txt | ./translate.sh
```

The substitutions are ordered intentionally:

| Replacement | Reason |
| --- | --- |
| `catnip` -> `dogchow` | Must happen before replacing `cat`, otherwise `catnip` would become `dognip`. |
| `cat` -> `dog` | Translates `cat` and words beginning with `cat`. |
| `meow\|meowzer` -> `woof` | Uses extended regex alternation so both words become `woof`. |

The `g` flag is required so every match on a line is replaced, not only the
first match.

## Creating Doggy Ipsum Files

Translate the first file:

```bash
./translate.sh kitty_ipsum_1.txt > doggy_ipsum_1.txt
```

Translate the second file:

```bash
./translate.sh kitty_ipsum_2.txt > doggy_ipsum_2.txt
```

Check the output:

```bash
cat doggy_ipsum_1.txt
cat doggy_ipsum_2.txt
```

Compare source and translated files:

```bash
diff --color kitty_ipsum_1.txt doggy_ipsum_1.txt
diff --color kitty_ipsum_2.txt doggy_ipsum_2.txt
```

`diff` shows which lines changed. With `--color`, removed source lines and added
translated lines are easier to inspect.

## Completion Notes

This workshop is about understanding how command-line programs connect:

```text
stdin -> command -> stdout
                 -> stderr
```

The final translator is small, but it combines several important Bash skills:

```text
file input -> cat -> sed replacements -> redirected output -> diff validation
```

That pattern is useful far beyond this workshop because many automation tasks
are built by connecting small commands through streams, pipes, and redirection.
