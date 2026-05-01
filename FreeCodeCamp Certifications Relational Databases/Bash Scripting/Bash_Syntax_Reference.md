# Bash Syntax Reference

This reference supports the **Build Five Programs** workshop from the
freeCodeCamp Relational Databases Certification track.

The goal is to make the Bash syntax understandable from the beginning. It is
written for review after completing the workshop, but it also works as a
beginner-friendly guide when the syntax starts to feel confusing.

## How to Think About Bash

Bash is a command language. A Bash script is a text file that contains commands
that Bash can run from top to bottom.

In this workshop, Bash is used to create five small programs:

- `questionnaire.sh` asks for user input and prints a response.
- `countdown.sh` accepts a number and counts down to zero.
- `bingo.sh` generates a random Bingo number.
- `fortune.sh` asks a question and returns a random answer.
- `five.sh` runs the other four programs in sequence.

The important idea is that almost anything typed manually in the terminal can
also be placed inside a `.sh` file and executed as a script.

## Basic Script Structure

A simple Bash script usually has this shape:

```bash
#!/bin/bash

# Short description of the script

VARIABLE="value"

echo "Some output"
```

Each part has a purpose:

- `#!/bin/bash` is the shebang. It tells the operating system to run the file
  with Bash.
- Lines beginning with `#` are comments. They are ignored by Bash.
- Variables store values for later use.
- Commands such as `echo`, `read`, and `sleep` are executed in order.

## Creating and Running Script Files

### Create a File

```bash
touch questionnaire.sh
```

`touch` creates an empty file if it does not exist. If the file already exists,
it updates the file timestamp.

### Add the Shebang

```bash
#!/bin/bash
```

The shebang must be the first line of the file. If it is not at the top, the
operating system may not know which interpreter should run the script.

### Check File Permissions

```bash
ls -l
```

Example output:

```bash
-rw-r--r-- 1 user user 120 questionnaire.sh
```

How to read the permission section:

- `r` means read.
- `w` means write.
- `x` means execute.
- If there is no `x`, the file cannot be run directly with `./file.sh`.

### Add Execute Permission

```bash
chmod +x questionnaire.sh
```

`chmod +x` adds execute permission so the file can be run as a program.

### Run a Script

There are several ways to run a script:

```bash
sh questionnaire.sh
bash questionnaire.sh
./questionnaire.sh
```

The difference:

- `sh questionnaire.sh` runs the script with `sh`.
- `bash questionnaire.sh` runs the script with Bash.
- `./questionnaire.sh` runs the file directly and uses the shebang.

For this workshop, `./script.sh` is the most important pattern because it
confirms the file is executable and has a valid shebang.

## Terminal Commands Used for Learning

These commands help inspect the environment and understand Bash behavior.

```bash
which bash
ls -l
chmod +x file.sh
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

What each one is used for:

- `which bash` shows where Bash is installed.
- `ls -l` shows files with detailed permissions.
- `chmod +x file.sh` makes a script executable.
- `help` lists Bash built-ins.
- `help if` explains the `if` syntax.
- `help [[` explains conditional expressions.
- `help let` shows arithmetic operators.
- `man echo` opens the manual page for `echo`.
- `man sleep` opens the manual page for `sleep`.
- `printenv` prints environment variables.
- `declare -p` prints shell variables and arrays.
- `type command_name` shows whether a command is a built-in, keyword,
  executable, or script.
- `echo $?` prints the exit status of the previous command.

## Variables

Variables store values.

```bash
NAME="Alice"
LOCATION="Bandung"
COUNT=5
```

Rules:

- Do not put spaces around `=`.
- Use quotes when the value contains spaces.
- Use `$VARIABLE_NAME` to read the value.

Correct:

```bash
NAME="Alice"
echo "$NAME"
```

Incorrect:

```bash
NAME = "Alice"
```

The incorrect version fails because Bash thinks `NAME` is a command, `=` is an
argument, and `"Alice"` is another argument.

## Quoting Variables

Use quotes around variables when printing or passing them into commands.

```bash
echo "$NAME"
echo "Hello $NAME from $LOCATION."
```

Why quotes matter:

- They preserve spaces in user input.
- They make output more predictable.
- They reduce bugs when a value is empty.

Example:

```bash
LOCATION="New York"
echo "$LOCATION"
```

Without quotes, Bash may split the value into separate words.

## Reading User Input

Use `read` to collect input from the user.

```bash
echo "What's your name?"
read NAME
echo "Hello $NAME."
```

How it works:

1. `echo` prints the question.
2. `read NAME` waits for the user to type something.
3. The typed value is stored in the `NAME` variable.
4. The script can use `$NAME` later.

This is the main pattern used in `questionnaire.sh`.

## Formatted Output with `echo -e`

`echo` prints text. The `-e` option allows escape sequences such as `\n`.

```bash
echo -e "\n~~ Questionnaire ~~\n"
```

`\n` means new line. The output has a blank line before and after the title.

This pattern is used in the workshop to make each program title easier to read.

## Comments

Single-line comments start with `#`.

```bash
# Program that counts down to zero from a given argument
```

Comments explain the purpose of code without changing how the script runs.

The shebang is a special case:

```bash
#!/bin/bash
```

It begins with `#`, but Bash treats it as an interpreter instruction when the
file is executed directly.

## Multi-line Comments

Bash does not have a true built-in block comment syntax like some languages, but
this pattern is commonly used:

```bash
: '
for (( i = 10; i >= 0; i-- ))
do
  echo "$i"
done
'
```

In the workshop, this is used to keep the `for` loop version inside
`countdown.sh` while switching the active logic to a `while` loop.

## Script Arguments

Script arguments are values typed after the script name.

```bash
./countdown.sh 5
```

In this command, `5` is the first argument.

Common argument variables:

| Syntax | Meaning |
| --- | --- |
| `$1` | First argument |
| `$2` | Second argument |
| `$3` | Third argument |
| `$*` | All arguments as one expanded value |
| `$@` | All arguments as separate values |

Example:

```bash
echo "First argument: $1"
echo "All arguments: $*"
```

In `countdown.sh`, `$1` is the number used as the countdown starting point.

## Exit Status

Every command returns an exit status.

```bash
echo $?
```

Common meanings:

| Status | Meaning |
| --- | --- |
| `0` | Success, true, or no error |
| `1` | General failure or false |
| `127` | Command not found |

Examples:

```bash
[[ 4 -le 5 ]]
echo $?
```

The result is `0` because the expression is true.

```bash
[[ 4 -ge 5 ]]
echo $?
```

The result is `1` because the expression is false.

This matters because `if`, `while`, and `until` use command success or failure
to decide what to do next.

## Conditional Expressions with `[[ ... ]]`

Use `[[ ... ]]` when checking conditions.

```bash
if [[ $1 -gt 0 ]]
then
  echo "Positive number"
fi
```

Spacing is required:

```bash
[[ $1 -gt 0 ]]   # valid
[[$1 -gt 0]]     # invalid
```

Think of `[[ ... ]]` as a test box. The expression inside the box is evaluated
as true or false.

### Numeric Comparisons

Use these operators when comparing integers:

| Operator | Meaning | Example |
| --- | --- | --- |
| `-eq` | Equal | `[[ $COUNT -eq 5 ]]` |
| `-ne` | Not equal | `[[ $COUNT -ne 0 ]]` |
| `-lt` | Less than | `[[ $COUNT -lt 10 ]]` |
| `-le` | Less than or equal | `[[ $COUNT -le 10 ]]` |
| `-gt` | Greater than | `[[ $COUNT -gt 0 ]]` |
| `-ge` | Greater than or equal | `[[ $COUNT -ge 0 ]]` |

Example:

```bash
if [[ $1 -gt 0 ]]
then
  echo "The argument is positive."
else
  echo "Include a positive integer as the first argument."
fi
```

### String Comparisons

Use these operators when comparing text:

| Operator | Meaning | Example |
| --- | --- | --- |
| `==` | Same text | `[[ $NAME == "Alice" ]]` |
| `!=` | Different text | `[[ $NAME != "Bob" ]]` |
| `=~` | Matches a pattern | `[[ $QUESTION =~ \?$ ]]` |

Example:

```bash
if [[ $NAME == "Alice" ]]
then
  echo "Name matched."
fi
```

### File Checks

Use file test operators to check file status.

| Operator | Meaning | Example |
| --- | --- | --- |
| `-e` | Path exists | `[[ -e script.sh ]]` |
| `-f` | Regular file exists | `[[ -f script.sh ]]` |
| `-d` | Directory exists | `[[ -d folder ]]` |
| `-r` | File is readable | `[[ -r script.sh ]]` |
| `-w` | File is writable | `[[ -w script.sh ]]` |
| `-x` | File is executable | `[[ -x script.sh ]]` |

Example:

```bash
if [[ -x countdown.sh ]]
then
  echo "The script is executable."
fi
```

### Logical Operators

Logical operators combine or reverse conditions. This section intentionally uses
code blocks instead of a Markdown table because the OR operator contains pipe
characters that can break table rendering.

AND means both conditions must be true:

```bash
[[ -x countdown.sh && $1 -gt 0 ]]
```

OR means at least one condition must be true:

```bash
[[ $NAME == "Alice" || $NAME == "Bob" ]]
```

NOT reverses a condition:

```bash
[[ ! $1 ]]
```

In the fortune teller program, `[[ ! $1 ]]` checks whether the function was
called without an argument.

## Arithmetic with `(( ... ))`

Use `(( ... ))` for arithmetic operations.

```bash
(( I-- ))
(( COUNT += 1 ))
(( TOTAL = PRICE * QUANTITY ))
```

Inside `(( ... ))`, variables do not need `$`.

```bash
(( NUMBER <= 15 ))
```

This checks whether `NUMBER` is less than or equal to `15`.

Common arithmetic operators:

| Operator | Meaning |
| --- | --- |
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Integer division |
| `%` | Modulo or remainder |
| `++` | Increment by one |
| `--` | Decrement by one |
| `+=` | Add and assign |
| `-=` | Subtract and assign |
| `*=` | Multiply and assign |
| `/=` | Divide and assign |
| `%=` | Modulo and assign |

Examples:

```bash
I=5
(( I-- ))
echo "$I"
```

The output is `4`.

```bash
COUNT=10
(( COUNT += 5 ))
echo "$COUNT"
```

The output is `15`.

## Arithmetic Expansion with `$(( ... ))`

Use `$(( ... ))` when the result of a calculation must be printed, assigned, or
inserted into another command.

```bash
RESULT=$(( 5 + 5 ))
echo "$RESULT"
```

The output is `10`.

Difference between `(( ... ))` and `$(( ... ))`:

- `(( I++ ))` changes the value of `I` and prints nothing.
- `echo $(( I + 4 ))` calculates a value and prints the result.

Random number examples:

```bash
N=$(( RANDOM % 6 ))
BINGO_NUMBER=$(( RANDOM % 75 + 1 ))
```

Why `RANDOM % 75 + 1` is used:

1. `$RANDOM` gives a number from `0` to `32767`.
2. `% 75` limits the result to `0` through `74`.
3. `+ 1` changes the final range to `1` through `75`.

## Conditional Flow

### Basic `if`

```bash
if [[ CONDITION ]]
then
  COMMANDS
fi
```

### `if` with `else`

```bash
if [[ $1 -gt 0 ]]
then
  echo "Valid input"
else
  echo "Invalid input"
fi
```

### `if`, `elif`, and `else`

```bash
if (( NUMBER <= 15 ))
then
  echo "B:$NUMBER"
elif [[ $NUMBER -le 30 ]]
then
  echo "I:$NUMBER"
elif (( NUMBER < 46 ))
then
  echo "N:$NUMBER"
elif [[ $NUMBER -lt 61 ]]
then
  echo "G:$NUMBER"
else
  echo "O:$NUMBER"
fi
```

How to read it:

1. Check the first condition.
2. If it is true, run that block and skip the rest.
3. If it is false, check the next `elif`.
4. If no condition matches, run the `else` block.
5. `fi` closes the entire conditional statement.

This pattern is used in `bingo.sh` to decide which Bingo letter belongs to the
random number.

## Loops

Loops repeat commands.

### `for` Loop

A `for` loop is useful when the number of iterations is clear.

```bash
for (( i = 10; i >= 0; i-- ))
do
  echo "$i"
  sleep 1
done
```

How to read it:

- `i = 10` starts the loop at `10`.
- `i >= 0` keeps the loop running while `i` is at least `0`.
- `i--` subtracts one after each loop.
- `do` starts the repeated block.
- `done` ends the repeated block.

### `while` Loop

A `while` loop runs while the condition is true.

```bash
I=5
while [[ $I -ge 0 ]]
do
  echo "$I"
  (( I-- ))
  sleep 1
done
```

This is the final countdown pattern used in `countdown.sh`.

Important warning:

If `(( I-- ))` is removed, `I` never changes. The condition stays true forever,
which creates an infinite loop.

### `until` Loop

An `until` loop runs until the condition becomes true.

```bash
until [[ $QUESTION =~ \?$ ]]
do
  echo "Try again. Make sure it ends with a question mark:"
  read QUESTION
done
```

This is useful for input validation. In `fortune.sh`, the script keeps asking
until the user enters a question that ends with `?`.

## Arrays

Arrays store several values in one variable.

```bash
RESPONSES=("Yes" "No" "Maybe" "Outlook good" "Don't count on it" "Ask again later")
```

Important rules:

- Array values are separated by spaces.
- Values with spaces must be quoted.
- The first item is at index `0`.

Access one item:

```bash
echo "${RESPONSES[0]}"
echo "${RESPONSES[1]}"
```

Access one item with a variable index:

```bash
N=$(( RANDOM % 6 ))
echo "${RESPONSES[$N]}"
```

Print all items:

```bash
echo "${RESPONSES[@]}"
echo "${RESPONSES[*]}"
```

Inspect an array:

```bash
declare -p RESPONSES
```

Arrays are used in `fortune.sh` to store possible answers.

## Functions

Functions group commands so they can be reused.

```bash
GET_FORTUNE() {
  echo "Ask a yes or no question:"
  read QUESTION
}
```

Call the function by writing its name:

```bash
GET_FORTUNE
```

Functions can receive arguments:

```bash
GET_FORTUNE again
```

Inside the function, `$1` is the first function argument.

```bash
GET_FORTUNE() {
  if [[ ! $1 ]]
  then
    echo "Ask a yes or no question:"
  else
    echo "Try again. Make sure it ends with a question mark:"
  fi

  read QUESTION
}
```

How this works in `fortune.sh`:

- The first call uses `GET_FORTUNE`, so `$1` is empty and the script prints the
  first question prompt.
- Later calls use `GET_FORTUNE again`, so `$1` is not empty and the script
  prints the retry prompt.

## Pattern Matching with `=~`

The `=~` operator checks whether a string matches a pattern.

```bash
[[ "hello" =~ el ]]
[[ "hello world" =~ ^h.+d$ ]]
[[ "test?" =~ \?$ ]]
```

Pattern symbols:

| Pattern | Meaning |
| --- | --- |
| `^` | Start of string |
| `$` | End of string |
| `.` | Any single character |
| `+` | One or more of the previous pattern |
| `\?` | Literal question mark |

Example from `fortune.sh`:

```bash
[[ $QUESTION =~ \?$ ]]
```

This means: "Does the value of `QUESTION` end with a question mark?"

For regex matching, do not quote the regex pattern when using regex
metacharacters.

## Random Values

Bash provides a built-in variable named `RANDOM`.

```bash
echo "$RANDOM"
```

It returns a random number from `0` through `32767`.

To limit the range, use modulo arithmetic.

Random index from `0` through `5`:

```bash
N=$(( RANDOM % 6 ))
```

Random Bingo number from `1` through `75`:

```bash
NUMBER=$(( RANDOM % 75 + 1 ))
```

The `%` operator gives the remainder after division, which is why it is useful
for keeping random numbers inside a chosen range.

## Command Types

Use `type` to inspect what a command is.

```bash
type echo
type read
type if
type then
type bash
type ./five.sh
```

Common results:

- `shell builtin`: the command is built into Bash.
- `shell keyword`: the word is part of Bash syntax.
- `is /path/to/command`: the command is an external executable.
- `is ./file.sh`: the command is a file in the current directory.

This explains why some commands are documented with `help` and others are
documented with `man`.

## Built-ins vs External Commands

Built-ins are part of Bash itself:

```bash
echo
read
if
while
until
function
```

External commands are executable programs on the system:

```bash
ls
sleep
bash
psql
```

Use this rule:

- Try `help command_name` for Bash built-ins or keywords.
- Try `man command_name` for external programs.
- Use `type command_name` when unsure.

## Workshop Program Patterns

### Questionnaire Pattern

Purpose: ask questions, store answers, and print a final message.

```bash
QUESTION1="What's your name?"
echo "$QUESTION1"

read NAME
echo "Hello $NAME."
```

Main concepts:

- Variables store question text.
- `read` stores user input.
- Quoted `echo` output keeps names and locations readable even with spaces.

### Countdown Pattern

Purpose: validate a numeric argument and count down to zero.

```bash
if [[ $1 -gt 0 ]]
then
  I=$1
  while [[ $I -ge 0 ]]
  do
    echo "$I"
    (( I-- ))
    sleep 1
  done
else
  echo "Include a positive integer as the first argument."
fi
```

Main concepts:

- `$1` reads the first script argument.
- `[[ $1 -gt 0 ]]` validates the argument.
- `while` repeats while the counter is greater than or equal to zero.
- `(( I-- ))` reduces the counter.
- `sleep 1` pauses for one second.

### Bingo Pattern

Purpose: generate one random number and map it to a Bingo letter.

```bash
NUMBER=$(( RANDOM % 75 + 1 ))
TEXT="The next number is, "
```

```bash
if (( NUMBER <= 15 ))
then
  echo "${TEXT}B:$NUMBER"
elif [[ $NUMBER -le 30 ]]
then
  echo "${TEXT}I:$NUMBER"
elif (( NUMBER < 46 ))
then
  echo "${TEXT}N:$NUMBER"
elif [[ $NUMBER -lt 61 ]]
then
  echo "${TEXT}G:$NUMBER"
else
  echo "${TEXT}O:$NUMBER"
fi
```

Main concepts:

- `$RANDOM` generates a random number.
- `$(( ... ))` calculates the limited range.
- `if`, `elif`, and `else` map ranges to output labels.

### Fortune Teller Pattern

Purpose: ask a valid yes-or-no question and return a random answer.

```bash
RESPONSES=("Yes" "No" "Maybe" "Outlook good" "Don't count on it" "Ask again later")
N=$(( RANDOM % 6 ))
```

```bash
GET_FORTUNE() {
  if [[ ! $1 ]]
  then
    echo "Ask a yes or no question:"
  else
    echo "Try again. Make sure it ends with a question mark:"
  fi
  read QUESTION
}
```

```bash
GET_FORTUNE

until [[ $QUESTION =~ \?$ ]]
do
  GET_FORTUNE again
done

echo -e "\n${RESPONSES[$N]}"
```

Main concepts:

- Arrays store possible answers.
- A function avoids repeating the same input logic.
- `until` repeats until the input is valid.
- Regex checks whether the question ends with `?`.

### Program Runner Pattern

Purpose: run several scripts from one file.

```bash
./questionnaire.sh
./countdown.sh 3
./bingo.sh
./fortune.sh
```

Main concepts:

- One script can call other scripts.
- Arguments can be passed to a child script, as shown with `./countdown.sh 3`.
- The scripts run in order from top to bottom.

## Common Beginner Mistakes

### Adding Spaces Around `=`

Incorrect:

```bash
NAME = "Alice"
```

Correct:

```bash
NAME="Alice"
```

### Forgetting Spaces Inside `[[ ... ]]`

Incorrect:

```bash
[[$1 -gt 0]]
```

Correct:

```bash
[[ $1 -gt 0 ]]
```

### Forgetting Execute Permission

Problem:

```bash
./questionnaire.sh
```

Output:

```bash
Permission denied
```

Fix:

```bash
chmod +x questionnaire.sh
```

### Forgetting to Change a Loop Variable

Problem:

```bash
I=5
while [[ $I -ge 0 ]]
do
  echo "$I"
done
```

This never ends because `I` never changes.

Fix:

```bash
I=5
while [[ $I -ge 0 ]]
do
  echo "$I"
  (( I-- ))
done
```

### Quoting Regex Patterns Incorrectly

Usually valid:

```bash
[[ $QUESTION =~ \?$ ]]
```

Avoid quoting regex patterns when using regex metacharacters:

```bash
[[ $QUESTION =~ "\?$" ]]
```

The quoted version may behave differently because Bash treats it more
literally.

### Confusing `(( ... ))` and `$(( ... ))`

Use this to change a value:

```bash
(( I-- ))
```

Use this to produce a calculated value:

```bash
echo "$(( I - 1 ))"
```

## Quick Decision Guide

Use `[[ ... ]]` when asking a true or false question:

```bash
[[ $1 -gt 0 ]]
[[ -x file.sh ]]
[[ $QUESTION =~ \?$ ]]
```

Use `(( ... ))` when changing or comparing numbers arithmetically:

```bash
(( I-- ))
(( NUMBER <= 15 ))
```

Use `$(( ... ))` when the calculated result is needed as a value:

```bash
NUMBER=$(( RANDOM % 75 + 1 ))
```

Use `read` when the user must type input:

```bash
read NAME
```

Use an array when there are multiple possible values:

```bash
RESPONSES=("Yes" "No" "Maybe")
```

Use a function when the same logic should be reused:

```bash
ASK_QUESTION() {
  echo "Question:"
  read ANSWER
}
```

Use `until` when the script should keep asking until input becomes valid:

```bash
until [[ $ANSWER =~ \?$ ]]
do
  read ANSWER
done
```

## Final Mental Model

When reading a Bash script, use this order:

1. Check the shebang to know which interpreter runs the file.
2. Read the comments to understand the program purpose.
3. Look for variables and arrays near the top.
4. Look for functions, because they may be called later.
5. Find the main commands at the bottom.
6. Follow the script from top to bottom.
7. For each condition, ask whether it returns exit status `0` or non-zero.
8. For each loop, check what changes so the loop can eventually stop.

This approach makes the five workshop scripts easier to understand and easier
to debug.
