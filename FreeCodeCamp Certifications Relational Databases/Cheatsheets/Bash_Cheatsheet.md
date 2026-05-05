# Bash Cheatsheet

This cheatsheet is a quick lookup reference for Bash syntax learned in the
freeCodeCamp Relational Databases Certification track.

Use it when writing terminal commands, Bash scripts, loops, conditions, CSV
readers, or scripts that call PostgreSQL with `psql`.

## Script Setup

| Goal | Syntax | Example | Notes |
| --- | --- | --- | --- |
| Create a file | `touch file.sh` | `touch insert_data.sh` | Creates an empty script file. |
| Add Bash shebang | `#!/bin/bash` | `#!/bin/bash` | Must be the first line when running with `./file.sh`. |
| Make executable | `chmod +x file.sh` | `chmod +x insert_data.sh` | Adds execute permission. |
| Run with Bash | `bash file.sh` | `bash insert_data.sh` | Runs through Bash without needing executable permission. |
| Run directly | `./file.sh` | `./insert_data.sh` | Requires executable permission and uses the shebang. |
| Check permissions | `ls -l` | `ls -l insert_data.sh` | Look for `x` in the permission string. |
| Find Bash path | `which bash` | `which bash` | Useful when confirming the shebang path. |

## Output and Formatting

| Goal | Syntax | Example | Notes |
| --- | --- | --- | --- |
| Print text | `echo "text"` | `echo "Hello Bash"` | Use quotes for predictable output. |
| Print a variable | `echo "$VARIABLE"` | `echo "$NAME"` | Quoting preserves spaces. |
| Print with blank lines | `echo -e "\ntext\n"` | `echo -e "\n~~ Menu ~~\n"` | `-e` enables `\n`. |
| Print command result | `echo "$(command)"` | `echo "$(date)"` | Runs the command first. |
| Print exit status | `echo $?` | `echo $?` | Shows previous command status. |

## Standard Streams and Redirection

| Goal | Syntax | Example | Notes |
| --- | --- | --- | --- |
| Redirect standard output and overwrite | `command > file` | `echo hello > stdout.txt` | Creates or replaces the file. |
| Redirect standard output and append | `command >> file` | `echo hello >> stdout.txt` | Adds output to the end. |
| Explicitly redirect standard output | `command 1> file` | `echo hello 1> stdout.txt` | Same stream as `>`. |
| Redirect standard error | `command 2> file` | `bad_command 2> stderr.txt` | Captures error output. |
| Redirect standard input from a file | `command < file` | `read NAME < name.txt` | Reads input from the file instead of the keyboard. |
| Empty a file | `> file` | `> stdout.txt` | Overwrites the file with no content. |

Stream numbers:

| Stream | Number | Meaning |
| --- | ---: | --- |
| `stdin` | `0` | Input stream. |
| `stdout` | `1` | Successful output stream. |
| `stderr` | `2` | Error output stream. |

Capture output and errors separately:

```bash
./script.sh < name.txt 1> stdout.txt 2> stderr.txt
```

## Comments

| Goal | Syntax | Example | Notes |
| --- | --- | --- | --- |
| Single-line comment | `# comment` | `# Insert student rows` | Ignored by Bash. |
| Multi-line comment pattern | `: ' ... '` | See below | Useful for temporarily disabling a block. |

```bash
: '
for (( i = 10; i >= 0; i-- ))
do
  echo "$i"
done
'
```

## Variables

| Goal | Syntax | Example | Notes |
| --- | --- | --- | --- |
| Create variable | `NAME=value` | `COUNT=5` | No spaces around `=`. |
| Store text | `NAME="text value"` | `MAJOR="Data Science"` | Use quotes when value has spaces. |
| Read variable | `$NAME` | `echo "$MAJOR"` | `$` gets the stored value. |
| Assign command output | `VAR=$(command)` | `TODAY=$(date)` | Called command substitution. |
| Assign arithmetic result | `VAR=$(( expression ))` | `N=$(( RANDOM % 6 ))` | Use when a calculation must produce a value. |

Common mistake:

```bash
NAME = "Alice"   # wrong
NAME="Alice"     # correct
```

## User Input

| Goal | Syntax | Example | Notes |
| --- | --- | --- | --- |
| Read one input | `read VARIABLE` | `read NAME` | Waits for user input. |
| Prompt then read | `echo "Question"; read VAR` | `echo "Name?"; read NAME` | Used in questionnaire scripts. |
| Read input safely | `read -r VARIABLE` | `read -r ANSWER` | Prevents backslash interpretation. |

Example:

```bash
echo "What's your name?"
read -r NAME
echo "Hello $NAME."
```

## Pipes and Subshells

A pipe sends `stdout` from the command on the left into `stdin` of the command
on the right.

| Goal | Syntax | Example |
| --- | --- | --- |
| Pipe output into another command | `command_1 \| command_2` | `echo text \| cat` |
| Count piped lines | `command \| wc -l` | `grep -o "cat" file.txt \| wc -l` |
| Transform piped text | `command \| sed "s/a/b/"` | `cat file.txt \| sed "s/cat/dog/"` |

Important behavior:

```bash
echo Alice | read NAME
echo "$NAME"
```

The variable may not remain available because `read` runs in a subshell in this
pipeline pattern. Use input redirection when the variable must stay in the
current shell:

```bash
read NAME < name.txt
```

## Script Arguments

| Goal | Syntax | Example | Notes |
| --- | --- | --- | --- |
| First argument | `$1` | `./countdown.sh 5` -> `$1` is `5` | Used for command-line input. |
| Second argument | `$2` | `./script.sh a b` -> `$2` is `b` | Arguments are positional. |
| All arguments | `$*` | `echo "$*"` | Expands all arguments as one value. |
| All arguments safely | `"$@"` | `for item in "$@"` | Preserves each argument separately. |

Example:

```bash
if [[ $1 -gt 0 ]]
then
  echo "The first argument is positive."
fi
```

## Conditions with `[[ ... ]]`

Use `[[ ... ]]` for true-or-false checks.

| Goal | Syntax | Example | Notes |
| --- | --- | --- | --- |
| Equal string | `[[ "$A" == "$B" ]]` | `[[ "$NAME" == "Mario" ]]` | Text comparison. |
| Not equal string | `[[ "$A" != "$B" ]]` | `[[ "$MAJOR" != "major" ]]` | Useful for skipping CSV headers. |
| Regex match | `[[ "$A" =~ pattern ]]` | `[[ "$QUESTION" =~ \?$ ]]` | Pattern should usually not be quoted. |
| Empty variable | `[[ -z "$A" ]]` | `[[ -z "$MAJOR_ID" ]]` | True if variable is empty. |
| Not empty variable | `[[ -n "$A" ]]` | `[[ -n "$COURSE_ID" ]]` | True if variable has content. |
| Variable is missing | `[[ ! $1 ]]` | `[[ ! $1 ]]` | Used to check no function argument. |

Spacing rule:

```bash
[[ "$MAJOR" != "major" ]]   # correct
[["$MAJOR" != "major"]]     # wrong
```

## Numeric Conditions

| Goal | Syntax | Example | Notes |
| --- | --- | --- | --- |
| Equal | `[[ A -eq B ]]` | `[[ $COUNT -eq 5 ]]` | Integer comparison. |
| Not equal | `[[ A -ne B ]]` | `[[ $COUNT -ne 0 ]]` | Integer comparison. |
| Less than | `[[ A -lt B ]]` | `[[ $COUNT -lt 10 ]]` | Integer comparison. |
| Less or equal | `[[ A -le B ]]` | `[[ $COUNT -le 10 ]]` | Integer comparison. |
| Greater than | `[[ A -gt B ]]` | `[[ $COUNT -gt 0 ]]` | Integer comparison. |
| Greater or equal | `[[ A -ge B ]]` | `[[ $COUNT -ge 0 ]]` | Integer comparison. |

## File Conditions

| Goal | Syntax | Example | Notes |
| --- | --- | --- | --- |
| Path exists | `[[ -e path ]]` | `[[ -e students.csv ]]` | File or directory. |
| Regular file exists | `[[ -f file ]]` | `[[ -f insert_data.sh ]]` | File only. |
| Directory exists | `[[ -d directory ]]` | `[[ -d data ]]` | Directory only. |
| File is readable | `[[ -r file ]]` | `[[ -r students.csv ]]` | Read permission. |
| File is writable | `[[ -w file ]]` | `[[ -w insert_data.sh ]]` | Write permission. |
| File is executable | `[[ -x file ]]` | `[[ -x insert_data.sh ]]` | Execute permission. |

## Logical Conditions

These examples are not shown as a table because the OR operator contains pipe
characters and can make Markdown tables harder to read.

AND: both conditions must be true.

```bash
[[ -x insert_data.sh && -f students.csv ]]
```

OR: at least one condition must be true.

```bash
[[ "$MAJOR" == "Data Science" || "$MAJOR" == "Web Development" ]]
```

NOT: reverse the condition.

```bash
[[ ! $1 ]]
```

## Arithmetic with `(( ... ))`

Use `(( ... ))` when changing numbers or checking numeric conditions.

| Goal | Syntax | Example | Notes |
| --- | --- | --- | --- |
| Increment | `(( VAR++ ))` | `(( COUNT++ ))` | Adds 1. |
| Decrement | `(( VAR-- ))` | `(( I-- ))` | Subtracts 1. |
| Add and assign | `(( VAR += N ))` | `(( COUNT += 5 ))` | Updates variable. |
| Subtract and assign | `(( VAR -= N ))` | `(( COUNT -= 1 ))` | Updates variable. |
| Compare number | `(( A <= B ))` | `(( NUMBER <= 15 ))` | Good inside `if`. |

Inside `(( ... ))`, variables do not need `$`.

```bash
if (( NUMBER <= 15 ))
then
  echo "B:$NUMBER"
fi
```

## Arithmetic Expansion with `$(( ... ))`

Use `$(( ... ))` when the calculation result must be used as a value.

| Goal | Syntax | Example | Notes |
| --- | --- | --- | --- |
| Calculate value | `$(( expression ))` | `echo "$(( 5 + 5 ))"` | Prints `10`. |
| Store result | `VAR=$(( expression ))` | `TOTAL=$(( PRICE * QTY ))` | Assigns result. |
| Random index | `N=$(( RANDOM % size ))` | `N=$(( RANDOM % 6 ))` | Range `0` to `5`. |
| Random 1 to max | `N=$(( RANDOM % max + 1 ))` | `NUMBER=$(( RANDOM % 75 + 1 ))` | Range `1` to `75`. |

## `if`, `elif`, `else`

| Goal | Syntax Pattern | Example |
| --- | --- | --- |
| Basic if | `if [[ condition ]]; then ... fi` | See below |
| If with else | `if [[ condition ]]; then ... else ... fi` | See below |
| Multiple branches | `if ... elif ... else ... fi` | Bingo number mapping |

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

## Text Processing Commands

| Goal | Syntax | Example | Notes |
| --- | --- | --- | --- |
| Print a file | `cat file` | `cat kitty_ipsum_1.txt` | Sends file content to `stdout`. |
| Count lines, words, and bytes | `wc file` | `wc kitty_ipsum_1.txt` | Prints all three counts and the filename. |
| Count lines only | `wc -l file` | `wc -l kitty_ipsum_1.txt` | Use with `<` or a pipe for count-only output. |
| Count words only | `wc -w file` | `wc -w kitty_ipsum_1.txt` | Useful for text reports. |
| Count characters only | `wc -m file` | `wc -m kitty_ipsum_1.txt` | Counts characters, not bytes. |
| Search matching lines | `grep "pattern" file` | `grep "meow" kitty_ipsum_1.txt` | Prints each matching line. |
| Show match line numbers | `grep -n "pattern" file` | `grep -n "meow" kitty_ipsum_1.txt` | Prefixes each match with a line number. |
| Highlight matches | `grep --color "pattern" file` | `grep --color "meow" kitty_ipsum_1.txt` | Helpful for manual inspection. |
| Print only matched text | `grep -o "pattern" file` | `grep -o "meow[a-z]*" kitty_ipsum_1.txt` | One match per output line. |
| Count matching lines | `grep -c "pattern" file` | `grep -c "meow" kitty_ipsum_1.txt` | Counts lines, not every occurrence. |
| Replace first match per line | `sed "s/old/new/" file` | `sed "s/r/2/" name.txt` | Writes transformed text to `stdout`. |
| Replace all matches per line | `sed "s/old/new/g" file` | `sed "s/cat/dog/g" file.txt` | `g` means global. |
| Use extended regex in `sed` | `sed -E "s/pattern/new/" file` | See below | Enables `+`, capture groups, and alternation. |
| Compare two files | `diff file_1 file_2` | `diff kitty.txt doggy.txt` | Shows changed lines. |
| Compare two files with color | `diff --color file_1 file_2` | `diff --color kitty.txt doggy.txt` | Easier to inspect in terminal. |

Count total matches instead of matching lines:

```bash
grep -o "meow[a-z]*" kitty_ipsum_1.txt | wc -l
```

Extract only line numbers from `grep -n` output:

```bash
grep -n "meow[a-z]*" kitty_ipsum_1.txt | sed -E "s/([0-9]+).*/\1/"
```

Use multiple `sed` replacements in one command:

```bash
sed -E "s/catnip/dogchow/g; s/cat/dog/g; s/meow|meowzer/woof/g"
```

Translator script pattern:

```bash
cat $1 | sed -E "s/catnip/dogchow/g; s/cat/dog/g; s/meow|meowzer/woof/g"
```

## Loops

| Goal | Syntax | Example Use |
| --- | --- | --- |
| Count with known range | `for (( init; condition; update ))` | Countdown timer. |
| Repeat while true | `while [[ condition ]]` | Count down while `I >= 0`. |
| Repeat until true | `until [[ condition ]]` | Ask until input ends with `?`. |
| Read file line by line | Use `cat`, pipe, `while`, and `read` together. | CSV import script. |

### `for` loop

```bash
for (( i = 10; i >= 0; i-- ))
do
  echo "$i"
done
```

### `while` loop

```bash
I=$1
while [[ $I -ge 0 ]]
do
  echo "$I"
  (( I-- ))
  sleep 1
done
```

### `until` loop

```bash
until [[ "$QUESTION" =~ \?$ ]]
do
  echo "Try again. Make sure it ends with a question mark:"
  read -r QUESTION
done
```

## Arrays

| Goal | Syntax | Example |
| --- | --- | --- |
| Create array | `ARRAY=("a" "b" "c")` | `RESPONSES=("Yes" "No" "Maybe")` |
| Read by index | `${ARRAY[index]}` | `${RESPONSES[0]}` |
| Read by variable index | `${ARRAY[$N]}` | `${RESPONSES[$N]}` |
| Print all values | `${ARRAY[@]}` | `echo "${RESPONSES[@]}"` |
| Inspect array | `declare -p ARRAY` | `declare -p RESPONSES` |

## Functions

| Goal | Syntax | Example |
| --- | --- | --- |
| Define function | `NAME() { commands; }` | `GET_FORTUNE() { ... }` |
| Call function | `NAME` | `GET_FORTUNE` |
| Pass argument | `NAME value` | `GET_FORTUNE again` |
| Read function argument | `$1` | `[[ ! $1 ]]` |

```bash
GET_FORTUNE() {
  if [[ ! $1 ]]
  then
    echo "Ask a yes or no question:"
  else
    echo "Try again. Make sure it ends with a question mark:"
  fi

  read -r QUESTION
}
```

## CSV Reading

| Goal | Syntax | Example | Notes |
| --- | --- | --- | --- |
| Read comma-separated file | Use `cat`, pipe, `while`, `IFS`, and `read` together. | See code block below. | Kept outside the table so Markdown preview stays stable. |
| Skip header row | `if [[ "$COL" != "header" ]]` | `if [[ "$MAJOR" != "major" ]]` | Prevents inserting column names. |
| Read four columns | `read -r A B C D` | `read -r FIRST LAST MAJOR GPA` | One variable per CSV column. |

Readable pattern:

```bash
cat courses.csv | while IFS="," read -r MAJOR COURSE
do
  if [[ "$MAJOR" != "major" ]]
  then
    echo "$MAJOR -> $COURSE"
  fi
done
```

## Running PostgreSQL from Bash

| Goal | Syntax | Example | Notes |
| --- | --- | --- | --- |
| Store `psql` command | `PSQL="psql ... -c"` | See below | Reused for every query. |
| Run SQL command | `$PSQL "SQL"` | `$PSQL "SELECT * FROM majors"` | Executes one SQL command. |
| Store SQL result | `VAR=$($PSQL "SQL")` | `MAJOR_ID=$($PSQL "SELECT major_id FROM majors WHERE major='$MAJOR'")` | Command substitution. |
| Print SQL result | `echo "$($PSQL "SQL")"` | `echo "$($PSQL "SELECT first_name FROM students")"` | Useful for report scripts. |
| Check empty result | `[[ -z "$VAR" ]]` | `[[ -z "$MAJOR_ID" ]]` | Used before inserting missing rows. |

```bash
PSQL="psql -X --username=freecodecamp --dbname=students --no-align --tuples-only -c"
```

Flag meaning:

| Flag | Meaning |
| --- | --- |
| `-X` | Ignore startup files for predictable script behavior. |
| `--username=freecodecamp` | Connect as the workshop user. |
| `--dbname=students` | Connect to the `students` database. |
| `--no-align` | Remove aligned output formatting. |
| `--tuples-only` | Print data only, without headers or footers. |
| `-c` | Run one SQL command and exit. |

## Lookup-Then-Insert Pattern

| Step | Bash / SQL Pattern | Purpose |
| --- | --- | --- |
| Query existing ID | `ID=$($PSQL "SELECT id FROM table WHERE name='$VALUE'")` | Checks whether row already exists. |
| Check missing ID | `if [[ -z "$ID" ]]` | Runs insert only when missing. |
| Insert row | `INSERT_RESULT=$($PSQL "INSERT INTO table(name) VALUES('$VALUE')")` | Adds missing row. |
| Confirm insert | `[[ "$INSERT_RESULT" == "INSERT 0 1" ]]` | Confirms one row was inserted. |
| Query new ID | `ID=$($PSQL "SELECT id FROM table WHERE name='$VALUE'")` | Gets the generated primary key. |

Example:

```bash
MAJOR_ID=$($PSQL "SELECT major_id FROM majors WHERE major='$MAJOR'")

if [[ -z "$MAJOR_ID" ]]
then
  INSERT_MAJOR_RESULT=$($PSQL "INSERT INTO majors(major) VALUES('$MAJOR')")

  if [[ "$INSERT_MAJOR_RESULT" == "INSERT 0 1" ]]
  then
    echo "Inserted into majors, $MAJOR"
  fi

  MAJOR_ID=$($PSQL "SELECT major_id FROM majors WHERE major='$MAJOR'")
fi
```

## SQL `NULL` from Bash

| Goal | Syntax | Example | Notes |
| --- | --- | --- | --- |
| Set SQL null in Bash variable | `VAR=null` | `MAJOR_ID=null` | Do not quote it in SQL. |
| Insert text | `'$TEXT_VAR'` | `'$FIRST'` | Text needs SQL quotes. |
| Insert number or null | `$NUMBER_VAR` | `$MAJOR_ID`, `$GPA` | Leave unquoted. |

Correct:

```bash
INSERT_STUDENT_RESULT=$($PSQL "INSERT INTO students(first_name, last_name, major_id, gpa) VALUES('$FIRST', '$LAST', $MAJOR_ID, $GPA)")
```

## SQL Report Script Pattern

Use this pattern when a Bash script needs to print a title and then display a
query result from PostgreSQL.

| Goal | Syntax | Example |
| --- | --- | --- |
| Print section title | `echo -e "\nTitle:"` | `echo -e "\nAverage GPA:"` |
| Print query output | `echo "$($PSQL "SELECT ...")"` | `echo "$($PSQL "SELECT ROUND(AVG(gpa), 2) FROM students")"` |
| Keep output readable | Quote the command substitution. | `echo "$($PSQL "SELECT course FROM courses")"` |

Example:

```bash
echo -e "\nAverage GPA of all students rounded to two decimal places:"
echo "$($PSQL "SELECT ROUND(AVG(gpa), 2) FROM students")"
```

## Useful Debugging Commands

| Goal | Command |
| --- | --- |
| Show current directory | `pwd` |
| List files | `ls` |
| List files with permissions | `ls -l` |
| Print environment variables | `printenv` |
| Print shell variables | `declare -p` |
| Inspect one variable | `declare -p VARIABLE` |
| Find command type | `type command_name` |
| Open Bash help | `help command_name` |
| Open manual page | `man command_name` |
| Clear terminal | `clear` |
| Exit terminal or `psql` session | `exit` |

## Common Fixes

| Problem | Likely Cause | Fix |
| --- | --- | --- |
| `Permission denied` when running `./script.sh` | Script is not executable. | `chmod +x script.sh` |
| CSV row splits at spaces | Missing `IFS=","`. | Use `while IFS="," read -r ...` |
| Header row inserted into database | Header was not skipped. | Add `if [[ "$COL" != "header" ]]`. |
| `psql` query does not run | Missing space after `$PSQL`. | Use `$PSQL "SELECT ..."` |
| `null` inserted as text | Quoted `'null'`. | Use unquoted `null`. |
| Infinite loop | Loop variable never changes. | Add update such as `(( I-- ))`. |
