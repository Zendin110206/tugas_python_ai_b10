# Build Five Programs

## Context

This document summarizes the **Build Five Programs** workshop from the
freeCodeCamp Relational Databases Certification track.

The workshop was completed in **GitHub Codespaces** through the CodeRoad
extension. The original lesson is interactive and step-based, so this repository
keeps a cleaned learning record instead of raw copied prompts from the CodeRoad
interface.

The goal of this note is to make the workshop reproducible and easy to review:
what was built, which Bash concepts were practiced, how each script works, and
how the final program runner connects the smaller programs together.

## Workshop Goal

Build five small Bash programs while learning how terminal commands can be
combined into executable scripts.

The workshop focuses on:

- creating and running Bash scripts
- using a shebang to select the Bash interpreter
- managing executable file permissions
- reading user input
- using script arguments
- writing conditional logic
- using `for`, `while`, and `until` loops
- working with arithmetic expansion
- generating random values
- using arrays and functions
- validating text input with pattern matching
- running several scripts from one parent script

## Environment

- Platform: freeCodeCamp Relational Databases Certification
- Workspace: GitHub Codespaces
- Tutorial runner: CodeRoad
- Shell: Bash
- Operating system context: Linux virtual machine

## Final Files

| File | Purpose | Main concepts |
| --- | --- | --- |
| `questionnaire.sh` | Collects a user's name, location, and favorite coding website. | Variables, `echo`, `read`, formatted output |
| `countdown.sh` | Counts down from a positive integer argument to zero. | Script arguments, conditionals, loops, arithmetic decrement, `sleep` |
| `bingo.sh` | Generates a random Bingo call from `B:1` through `O:75`. | `$RANDOM`, arithmetic expansion, `if` / `elif` / `else` |
| `fortune.sh` | Asks a yes-or-no question and returns a random response. | Arrays, functions, `until` loops, regex matching |
| `five.sh` | Runs the other four scripts in sequence. | Script orchestration and executable program flow |

## Setup Commands

The files are Bash scripts, so they need executable permissions in the
Codespaces Linux environment:

```bash
chmod +x questionnaire.sh
chmod +x countdown.sh
chmod +x bingo.sh
chmod +x fortune.sh
chmod +x five.sh
```

Each script can be executed directly from the project folder:

```bash
./questionnaire.sh
./countdown.sh 3
./bingo.sh
./fortune.sh
./five.sh
```

The `./` prefix means "run the executable file from the current directory."

## Walkthrough

### 1. Create the Questionnaire Program

The first script introduces the basic structure of an executable Bash program.

Key steps:

1. Create `questionnaire.sh`.
2. Add the Bash shebang.
3. Make the file executable.
4. Store question text in variables.
5. Print each question with `echo`.
6. Capture user input with `read`.
7. Print a final response using the collected values.

Important commands and syntax:

```bash
#!/bin/bash
chmod +x questionnaire.sh
./questionnaire.sh
QUESTION1="What's your name?"
read NAME
echo "Hello $NAME."
```

This program is intentionally simple. Its purpose is to show that a Bash script
can behave like a small interactive command-line application.

### 2. Create the Countdown Timer

The second script introduces script arguments, conditional logic, and loops.

The program expects a positive integer as its first argument:

```bash
./countdown.sh 5
```

The script checks the first argument with `$1`:

```bash
if [[ $1 -gt 0 ]]
then
  # countdown logic
else
  echo "Include a positive integer as the first argument."
fi
```

The workshop first introduces a `for` loop, then keeps that version as a
multi-line comment while replacing it with a `while` loop. This makes the file a
useful comparison between two valid loop styles.

Final loop pattern:

```bash
I=$1
while [[ $I -ge 0 ]]
do
  echo $I
  (( I-- ))
  sleep 1
done
```

The important idea is that the loop variable must change inside the loop.
Without `(( I-- ))`, the condition would remain true forever and the script
would become an infinite loop.

### 3. Create the Bingo Number Generator

The third script introduces random numbers and range-based conditional output.

The number is generated with:

```bash
NUMBER=$(( RANDOM % 75 + 1 ))
```

Why this works:

- `$RANDOM` returns a random integer from `0` through `32767`.
- `% 75` limits the result to `0` through `74`.
- `+ 1` shifts the final range to `1` through `75`.

The script then maps the number to a Bingo letter:

| Number range | Letter |
| --- | --- |
| 1-15 | `B` |
| 16-30 | `I` |
| 31-45 | `N` |
| 46-60 | `G` |
| 61-75 | `O` |

This is a practical example of using `if`, `elif`, and `else` to convert raw
numeric data into a more meaningful output format.

### 4. Create the Fortune Teller

The fourth script introduces arrays, functions, regex matching, and an `until`
loop.

The responses are stored in an array:

```bash
RESPONSES=("Yes" "No" "Maybe" "Outlook good" "Don't count on it" "Ask again later")
```

A random index chooses one response:

```bash
N=$(( RANDOM % 6 ))
echo "${RESPONSES[$N]}"
```

The script uses a function to ask for input:

```bash
GET_FORTUNE() {
  echo "Ask a yes or no question:"
  read QUESTION
}
```

The input is validated with an `until` loop:

```bash
until [[ $QUESTION =~ \?$ ]]
do
  GET_FORTUNE again
done
```

The regex pattern `\?$` checks whether the input ends with a literal question
mark. This is useful because the program should only answer after the user has
entered a question.

### 5. Create the Program Runner

The final script, `five.sh`, runs the four previous programs in order:

```bash
./questionnaire.sh
./countdown.sh 3
./bingo.sh
./fortune.sh
```

This is the simplest form of workflow orchestration in Bash. One script can
call other scripts and pass arguments when needed.

## Supporting Commands Practiced

The workshop also uses several terminal commands to understand how Bash works:

```bash
which bash
ls -l
chmod +x script.sh
help
help if
help [[
help let
man echo
man sleep
printenv
declare -p
type echo
type read
type bash
echo $?
```

Important distinctions:

- `help` is useful for Bash built-ins and keywords.
- `man` is useful for external commands with manual pages.
- `type` shows whether a command is a built-in, keyword, executable file, or
  script.
- `$?` shows the exit status of the previous command.

## Completion Notes

The final workshop output is a set of five executable Bash scripts. The scripts
are small, but they cover several core Bash scripting patterns that appear often
in real command-line automation:

- collecting input
- validating arguments
- looping until a condition is met
- producing random output
- organizing repeated logic in functions
- composing multiple scripts into one workflow

These files are kept as workshop artifacts and learning documentation for the
freeCodeCamp Relational Databases Certification track.
