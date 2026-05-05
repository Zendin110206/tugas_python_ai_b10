# Bash and SQL Review

This review summarizes the main ideas practiced in the freeCodeCamp
Relational Databases **SQL and Bash** section.

The section connects PostgreSQL with Bash scripts. The goal is to move from
manual database commands to repeatable command-line workflows that can import
data, print reports, transform text, and update database state.

## Core Mental Model

The general pattern is:

```text
Bash script -> psql command -> SQL query -> captured output -> next Bash action
```

For interactive programs, the pattern expands to:

```text
Print menu
Read user input
Validate input
Run SQL through psql
Check the query result
Insert, update, or display data
Return to the menu with a clear message
```

This is the foundation of the Student Database import scripts, the query report
script, the Kitty Ipsum text-processing workshop, and the Bike Rental Shop
program.

## Database Normalization

Normalization is the process of organizing a relational database to reduce
duplicate data and preserve integrity.

Benefits:

- repeated data is moved into the correct table
- relationships are represented with primary and foreign keys
- updates are easier because each fact has one logical place
- data is less likely to become inconsistent

### Normal Forms

| Normal Form | Main Idea | Simple Example |
| --- | --- | --- |
| 1NF | Each cell stores one atomic value, and each row is uniquely identifiable. | Store one phone number per row instead of multiple phone numbers in one cell. |
| 2NF | Every non-key column depends on the full key, not only part of a composite key. | Split order header data from order item data. |
| 3NF | Non-key columns do not depend on other non-key columns. | Store city details in a separate table instead of repeating them in every customer row. |
| BCNF | Every determinant is a candidate key. | A stricter form used when functional dependencies become more complex. |

For the workshops in this repository, aiming for 3NF is usually a good practical
target.

## Relationship Patterns

| Relationship | Design Pattern | Workshop Example |
| --- | --- | --- |
| One-to-many | Child table stores the parent table primary key as a foreign key. | `students.major_id` references `majors.major_id`. |
| Many-to-many | Junction table stores two foreign keys. | `majors_courses` connects `majors` and `courses`. |
| Event/history table | Table stores a relationship plus date or status columns. | `rentals` connects `customers` and `bikes` over time. |

The Bike Rental Shop workshop is a good example of an event/history table.
Instead of deleting rental rows when a bike is returned, the script updates
`date_returned`. This preserves the history while still allowing the bike to be
marked available again.

## Running PostgreSQL from Bash

A common pattern is storing the `psql` command in a variable:

```bash
PSQL="psql -X --username=freecodecamp --dbname=students --no-align --tuples-only -c"
```

or, for the Bike Rental Shop workshop:

```bash
PSQL="psql -X --username=freecodecamp --dbname=bikes --tuples-only -c"
```

Flag meaning:

| Flag | Meaning |
| --- | --- |
| `-X` | Ignore startup files for predictable script behavior. |
| `--username=freecodecamp` | Connect as the workshop database user. |
| `--dbname=...` | Select the database. |
| `--no-align` | Remove aligned output formatting. |
| `--tuples-only` | Hide headers and row-count footers. |
| `-c` | Run one SQL command and exit. |

Run a query:

```bash
$PSQL "SELECT * FROM students;"
```

Capture a query result:

```bash
MAJOR_ID=$($PSQL "SELECT major_id FROM majors WHERE major='$MAJOR'")
```

Check whether the query returned nothing:

```bash
if [[ -z $MAJOR_ID ]]
then
  echo "Missing major"
fi
```

## Output Shapes from `psql`

`psql` output shape matters because Bash scripts often parse query results.

With `--no-align --tuples-only`, output is compact:

```text
Data Science|Web Development
```

With `--tuples-only` but without `--no-align`, output can still contain aligned
spacing:

```text
 1 | Mountain | 27
```

That padding is why the Bike Rental Shop script uses two different techniques:

- `while read ...` to split displayed bike rows
- `sed` to trim or reformat captured values

## Importing CSV Data

The Student Database Part 1 workflow uses `cat`, `while`, `IFS`, and `read` to
process CSV rows:

```bash
cat students.csv | while IFS="," read FIRST LAST MAJOR GPA
do
  if [[ "$FIRST" != "first_name" ]]
  then
    echo "$FIRST $LAST"
  fi
done
```

Important details:

- `IFS=","` tells Bash to split columns by comma.
- The header row should be skipped.
- SQL text values need quotes.
- SQL numeric values and `null` should not be quoted.

## Lookup-Then-Insert Pattern

This pattern prevents duplicate lookup-table rows:

```bash
MAJOR_ID=$($PSQL "SELECT major_id FROM majors WHERE major='$MAJOR'")

if [[ -z $MAJOR_ID ]]
then
  INSERT_MAJOR_RESULT=$($PSQL "INSERT INTO majors(major) VALUES('$MAJOR')")
  MAJOR_ID=$($PSQL "SELECT major_id FROM majors WHERE major='$MAJOR'")
fi
```

The same idea appears in Bike Rental Shop:

```bash
CUSTOMER_NAME=$($PSQL "SELECT name FROM customers WHERE phone = '$PHONE_NUMBER'")

if [[ -z $CUSTOMER_NAME ]]
then
  INSERT_CUSTOMER_RESULT=$($PSQL "INSERT INTO customers(name, phone) VALUES('$CUSTOMER_NAME', '$PHONE_NUMBER')")
fi
```

First check whether the row exists. Insert only when the query result is empty.

## Query Reports

Student Database Part 2 focuses on report-style queries:

```bash
echo -e "\nAverage GPA:"
echo "$($PSQL "SELECT ROUND(AVG(gpa), 2) FROM students")"
```

Common SQL patterns:

| Goal | SQL Pattern |
| --- | --- |
| Filter rows | `WHERE condition` |
| Sort rows | `ORDER BY column DESC` |
| Limit output | `LIMIT 5` |
| Count rows | `COUNT(*)` |
| Group rows | `GROUP BY column` |
| Filter groups | `HAVING COUNT(*) > 1` |
| Join related tables | `JOIN other_table USING(column)` |
| Remove duplicates | `SELECT DISTINCT(column)` |

## Joins

Use joins when one answer requires columns from multiple tables.

Student Database example:

```sql
SELECT major, course
FROM majors
JOIN majors_courses USING(major_id)
JOIN courses USING(course_id)
ORDER BY major, course;
```

Bike Rental Shop active rentals example:

```sql
SELECT bike_id, type, size
FROM bikes
INNER JOIN rentals USING(bike_id)
INNER JOIN customers USING(customer_id)
WHERE phone = '555-5555'
  AND date_returned IS NULL
ORDER BY bike_id;
```

`USING(column)` is convenient when both tables share the same join column name.

## Menu Scripts

The Bike Rental Shop workshop uses function-based menus:

```bash
MAIN_MENU() {
  echo "How may I help you?"
  echo -e "\n1. Rent a bike\n2. Return a bike\n3. Exit"
  read MAIN_MENU_SELECTION

  case $MAIN_MENU_SELECTION in
    1) RENT_MENU ;;
    2) RETURN_MENU ;;
    3) EXIT ;;
    *) MAIN_MENU "Please enter a valid option." ;;
  esac
}
```

This design keeps each part of the program focused:

- `MAIN_MENU` routes the user
- `RENT_MENU` handles rental logic
- `RETURN_MENU` handles return logic
- `EXIT` ends the program

## Input Validation

Use regex matching in `[[ ... ]]` to check numeric input:

```bash
if [[ ! $BIKE_ID_TO_RENT =~ ^[0-9]+$ ]]
then
  MAIN_MENU "That is not a valid bike number."
fi
```

Pattern meaning:

| Token | Meaning |
| --- | --- |
| `^` | Start of input. |
| `[0-9]` | One digit. |
| `+` | One or more digits. |
| `$` | End of input. |

This prevents inputs such as `abc`, `a1`, and empty values from being used in
numeric SQL conditions.

## Text Processing with `grep`, `sed`, `wc`, and `diff`

The Kitty Ipsum workshop focuses on standard streams and text transformation:

| Command | Main Use |
| --- | --- |
| `grep` | Search matching lines or patterns. |
| `grep -o` | Print only each match. |
| `wc -l` | Count lines, often after `grep -o`. |
| `sed` | Replace or transform text. |
| `diff` | Compare original and transformed files. |

Example:

```bash
grep -o 'meow[a-z]*' kitty_ipsum_1.txt | wc -l
```

Example with `sed`:

```bash
sed -E 's/catnip/dogchow/g; s/cat/dog/g; s/meow|meowzer/woof/g'
```

Use single quotes around `sed` expressions unless Bash variable interpolation is
needed.

## Trimming `psql` Padding with `sed`

PostgreSQL output may include leading or trailing spaces even with
`--tuples-only`.

Check trailing spaces visually by adding a period:

```bash
echo "$(echo '   M e ')."
```

Remove one trailing space:

```bash
echo "$(echo '   M e ' | sed 's/ $//g')."
```

Remove all leading and trailing spaces:

```bash
echo "$(echo '   M e   ' | sed -E 's/^ *| *$//g')."
```

The `-E` flag is necessary because the trim pattern uses `|` as OR.

## SQL Injection Reminder

The workshop scripts use direct string interpolation because they are learning
exercises in a controlled environment:

```bash
$PSQL "SELECT name FROM customers WHERE phone = '$PHONE_NUMBER'"
```

In production applications, direct interpolation can be unsafe if user input is
not trusted. Prefer prepared statements or a database library that supports
parameter binding.

## Common Review Checklist

- Does each table have a primary key?
- Are repeated categories moved into their own table when needed?
- Are foreign keys used to protect relationships?
- Does the Bash script quote output variables when preserving spaces matters?
- Does the script check empty query results with `[[ -z ... ]]`?
- Does numeric user input pass through regex validation before reaching SQL?
- Does a rental return update both `rentals.date_returned` and
  `bikes.available`?
- Does `sed` use single-quoted expressions unless Bash interpolation is needed?
- Does a trim pattern that uses `|` enable extended regex with `sed -E`?
