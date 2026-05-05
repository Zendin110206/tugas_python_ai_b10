# Bike Rental Shop Reference

This reference documents the Bash and PostgreSQL syntax practiced in **Build a
Bike Rental Shop**.

It is intentionally practical: each section is organized around the exact kind
of problem that appears in the workshop, such as creating rental tables, calling
`psql` from Bash, validating numeric input, formatting PostgreSQL output, and
updating rental state.

## Database Schema Reference

| Goal | Syntax Pattern | Workshop Example |
| --- | --- | --- |
| Create a database | `CREATE DATABASE database_name;` | `CREATE DATABASE bikes;` |
| Connect to a database | `\c database_name` | `\c bikes` |
| Create an empty table | `CREATE TABLE table_name();` | `CREATE TABLE bikes();` |
| Add serial primary key | `ALTER TABLE table ADD COLUMN id SERIAL PRIMARY KEY;` | `ALTER TABLE bikes ADD COLUMN bike_id SERIAL PRIMARY KEY;` |
| Add required text | `ALTER TABLE table ADD COLUMN column VARCHAR(n) NOT NULL;` | `ALTER TABLE bikes ADD COLUMN type VARCHAR(50) NOT NULL;` |
| Add required integer | `ALTER TABLE table ADD COLUMN column INT NOT NULL;` | `ALTER TABLE bikes ADD COLUMN size INT NOT NULL;` |
| Add boolean default | `ALTER TABLE table ADD COLUMN column BOOLEAN NOT NULL DEFAULT true;` | `ALTER TABLE bikes ADD COLUMN available BOOLEAN NOT NULL DEFAULT true;` |
| Add unique text | `ALTER TABLE table ADD COLUMN column VARCHAR(n) UNIQUE NOT NULL;` | `ALTER TABLE customers ADD COLUMN phone VARCHAR(15) UNIQUE NOT NULL;` |
| Add foreign key | `ALTER TABLE child ADD FOREIGN KEY(column) REFERENCES parent(column);` | `ALTER TABLE rentals ADD FOREIGN KEY(bike_id) REFERENCES bikes(bike_id);` |
| Add date default | `ALTER TABLE table ADD COLUMN column DATE NOT NULL DEFAULT NOW();` | `ALTER TABLE rentals ADD COLUMN date_rented DATE NOT NULL DEFAULT NOW();` |
| Add nullable date | `ALTER TABLE table ADD COLUMN column DATE;` | `ALTER TABLE rentals ADD COLUMN date_returned DATE;` |

The completed relationship structure:

```text
customers.customer_id -> rentals.customer_id
bikes.bike_id         -> rentals.bike_id
```

## Why the Rental Table Exists

It may look like a rental could be stored directly in the `bikes` table, but
that would lose history. A bike can be rented many times over time, and a
customer can rent many bikes over time.

The `rentals` table solves this by storing an event:

```text
customer_id + bike_id + date_rented + date_returned
```

This makes it possible to answer questions such as:

- Which bikes are currently rented?
- Which customer rented a bike?
- When was the bike rented?
- Has the bike already been returned?
- How many rental records exist in the history?

`date_returned IS NULL` means the rental is still active.

## Inventory Insert Patterns

| Goal | Syntax Pattern | Example |
| --- | --- | --- |
| Insert one bike | `INSERT INTO bikes(type, size) VALUES('type', size);` | `INSERT INTO bikes(type, size) VALUES('Mountain', 27);` |
| Insert multiple bikes | `INSERT INTO bikes(type, size) VALUES(...), (...);` | `INSERT INTO bikes(type, size) VALUES('Road', 28), ('Road', 29);` |
| Inspect inventory | `SELECT * FROM bikes ORDER BY bike_id;` | `SELECT * FROM bikes ORDER BY bike_id;` |

The `available` column does not need to be included during insert because it has
a default value of `true`.

## `psql` from Bash

The workshop stores the reusable PostgreSQL command in a variable:

```bash
PSQL="psql -X --username=freecodecamp --dbname=bikes --tuples-only -c"
```

| Part | Meaning |
| --- | --- |
| `psql` | PostgreSQL command-line client. |
| `-X` | Ignore startup files so script output is more predictable. |
| `--username=freecodecamp` | Connect as the workshop user. |
| `--dbname=bikes` | Use the bike shop database. |
| `--tuples-only` | Print row data without headers and footers. |
| `-c` | Run one SQL command and exit. |

Run a query:

```bash
$PSQL "SELECT * FROM bikes;"
```

Capture a query result:

```bash
AVAILABLE_BIKES=$($PSQL "SELECT bike_id, type, size FROM bikes WHERE available = true ORDER BY bike_id")
```

Check whether a query returned no rows:

```bash
if [[ -z $AVAILABLE_BIKES ]]
then
  MAIN_MENU "Sorry, we don't have any bikes available right now."
fi
```

## Important Output Detail: `--tuples-only` Still Has Padding

In this workshop, `--tuples-only` removes headers and row-count footers, but it
does not necessarily remove aligned spacing. PostgreSQL can still return output
with padding around values:

```text
 1 | Mountain | 27
```

That is why the script uses patterns such as:

```bash
echo "$AVAILABLE_BIKES" | while read BIKE_ID BAR TYPE BAR SIZE
do
  echo "$BIKE_ID) $SIZE\" $TYPE Bike"
done
```

The `read` command splits the aligned output into fields:

```text
BIKE_ID -> 1
BAR     -> |
TYPE    -> Mountain
BAR     -> |
SIZE    -> 27
```

This works for the workshop data because each bike type is one word.

## Main Menu Function Pattern

| Goal | Bash Pattern |
| --- | --- |
| Define function | `MAIN_MENU() { ... }` |
| Print optional message | `if [[ $1 ]]; then echo -e "\n$1"; fi` |
| Read menu input | `read MAIN_MENU_SELECTION` |
| Route menu choice | `case $MAIN_MENU_SELECTION in ... esac` |
| Return invalid choice | `*) MAIN_MENU "Please enter a valid option." ;;` |

Example:

```bash
MAIN_MENU() {
  if [[ $1 ]]
  then
    echo -e "\n$1"
  fi

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

## `case` Statement Reference

| Goal | Syntax | Example |
| --- | --- | --- |
| Match exact choice | `pattern) command ;;` | `1) RENT_MENU ;;` |
| Match fallback | `*) command ;;` | `*) MAIN_MENU "Please enter a valid option." ;;` |
| End case block | `esac` | `esac` |

General pattern:

```bash
case $VARIABLE in
  pattern_1) COMMAND_1 ;;
  pattern_2) COMMAND_2 ;;
  *) FALLBACK_COMMAND ;;
esac
```

## Numeric Input Validation

The script must reject inputs such as `abc`, `1a`, and empty strings when a bike
ID is expected.

| Goal | Pattern | Meaning |
| --- | --- | --- |
| Contains at least one digit | `[[ value =~ [0-9] ]]` | Allows `a1`, so it is too loose. |
| Exactly one digit | `[[ value =~ ^[0-9]$ ]]` | Allows `1`, rejects `11`. |
| One or more digits only | `[[ value =~ ^[0-9]+$ ]]` | Allows `1`, `11`, `123`. |
| Not a positive integer | `[[ ! value =~ ^[0-9]+$ ]]` | Used for invalid input. |

Workshop pattern:

```bash
if [[ ! $BIKE_ID_TO_RENT =~ ^[0-9]+$ ]]
then
  MAIN_MENU "That is not a valid bike number."
fi
```

Regex meaning:

| Token | Meaning |
| --- | --- |
| `^` | Start of the input. |
| `[0-9]` | One digit. |
| `+` | One or more of the previous pattern. |
| `$` | End of the input. |

Without `^` and `$`, a value like `abc1def` could still match because it
contains a digit somewhere.

## Rent Flow SQL Patterns

| Goal | Query |
| --- | --- |
| Get available bikes | `SELECT bike_id, type, size FROM bikes WHERE available = true ORDER BY bike_id;` |
| Check one bike availability | `SELECT available FROM bikes WHERE bike_id = 1 AND available = true;` |
| Find customer by phone | `SELECT name FROM customers WHERE phone = '555-5555';` |
| Insert new customer | `INSERT INTO customers(name, phone) VALUES('Me', '555-5555');` |
| Get customer ID | `SELECT customer_id FROM customers WHERE phone = '555-5555';` |
| Insert rental row | `INSERT INTO rentals(customer_id, bike_id) VALUES(1, 1);` |
| Mark bike unavailable | `UPDATE bikes SET available = false WHERE bike_id = 1;` |
| Get bike message info | `SELECT size, type FROM bikes WHERE bike_id = 1;` |

Important state rule:

```text
Renting a bike inserts a rental row and sets bikes.available to false.
```

Both actions are needed. The rental row stores history, while the `available`
column controls whether the bike appears in the rent menu.

## Return Flow SQL Patterns

| Goal | Query |
| --- | --- |
| Find customer ID | `SELECT customer_id FROM customers WHERE phone = '555-5555';` |
| List active rentals | See query below. |
| Check selected rental | `SELECT rental_id FROM rentals INNER JOIN customers USING(customer_id) WHERE phone = '555-5555' AND bike_id = 1 AND date_returned IS NULL;` |
| Mark rental returned | `UPDATE rentals SET date_returned = NOW() WHERE rental_id = 1;` |
| Mark bike available | `UPDATE bikes SET available = true WHERE bike_id = 1;` |

Active rentals query:

```sql
SELECT bike_id, type, size
FROM bikes
INNER JOIN rentals USING(bike_id)
INNER JOIN customers USING(customer_id)
WHERE phone = '555-5555'
  AND date_returned IS NULL
ORDER BY bike_id;
```

Important state rule:

```text
Returning a bike updates date_returned and sets bikes.available back to true.
```

The rental row is not deleted. Keeping it preserves the rental history.

## `sed` Formatting Reference

Use single quotes around `sed` expressions unless Bash variable interpolation is
intentionally needed.

| Goal | Command to Use |
| --- | --- |
| Replace first matching space | See example 1 below. |
| Replace all spaces | See example 2 below. |
| Remove the separator before the bike type | See example 3 below. |
| Convert the separator into an inch mark | See example 4 below. |
| Remove trailing spaces | See example 5 below. |
| Remove leading and trailing spaces | See example 6 below. |

Example 1:

```bash
echo '28 | Mountain' | sed 's/ /=/'
```

Output:

```text
28=| Mountain
```

Example 2:

```bash
echo '28 | Mountain' | sed 's/ //g'
```

Output:

```text
28|Mountain
```

Example 3:

```bash
echo '28 | Mountain' | sed 's/ |//'
```

Output:

```text
28Mountain
```

Example 4:

```bash
echo '28 | Mountain' | sed 's/ |/"/'
```

Output:

```text
28" Mountain
```

Example 5:

```bash
echo 'M e   ' | sed 's/ *$//g'
```

Output:

```text
M e
```

Example 6:

```bash
echo '   M e   ' | sed -E 's/^ *| *$//g'
```

Output:

```text
M e
```

### Why `sed -E` Is Needed for the Trim Pattern

This command does not trim both sides correctly with basic `sed`:

```bash
echo "$(echo '   M e   ' | sed 's/^ *| *$//g')."
```

The `|` character is intended to mean OR, but basic `sed` does not treat it as
alternation in that form.

Use `-E` to enable extended regular expressions:

```bash
echo "$(echo '   M e   ' | sed -E 's/^ *| *$//g')."
```

Result:

```text
M e.
```

Pattern breakdown:

| Part | Meaning |
| --- | --- |
| `^ *` | Any number of spaces at the beginning. |
| `\|` | OR. |
| ` *$` | Any number of spaces at the end. |
| `//` | Replace matches with nothing. |
| `g` | Apply globally. |

This matters because `psql --tuples-only` can still return padded values. For
example, a customer name might be captured as `   Me` or `Me   ` depending on
output alignment. Trimming keeps the final message clean.

## Command Substitution and Quoting

| Goal | Pattern |
| --- | --- |
| Store query output | `VAR=$($PSQL "SQL")` |
| Store formatted text | `VAR=$(command \| sed 's/a/b/')` |
| Preserve spaces when printing | `echo "$VAR"` |
| Trim variable output | Use `sed -E` with the leading-or-trailing-space pattern. |

Examples:

```bash
CUSTOMER_ID=$($PSQL "SELECT customer_id FROM customers WHERE phone = '$PHONE_NUMBER'")
BIKE_INFO_FORMATTED=$(echo "$BIKE_INFO" | sed 's/ |/"/')
echo "$AVAILABLE_BIKES"
echo "$CUSTOMER_NAME" | sed -E 's/^ *| *$//g'
```

Prefer quoted variable expansion in Bash output:

```bash
echo "$BIKE_INFO"
```

This is easier to reason about than:

```bash
echo $BIKE_INFO
```

The workshop examples sometimes rely on word splitting because the data is
small and controlled. In documentation and future scripts, quoted output is the
clearer default unless word splitting is intentionally needed.

## Common Mistakes

| Problem | Likely Cause | Fix |
| --- | --- | --- |
| Menu does nothing after invalid input | Missing fallback in `case`. | Add `*) MAIN_MENU "Please enter a valid option." ;;`. |
| Non-numeric input reaches SQL | Regex validation is too loose. | Use `[[ ! $VALUE =~ ^[0-9]+$ ]]`. |
| Bike still appears as available after rental | `bikes.available` was not updated. | Run `UPDATE bikes SET available = false WHERE bike_id = ...;`. |
| Returned bike still appears as rented | `date_returned` was not updated. | Run `UPDATE rentals SET date_returned = NOW() WHERE rental_id = ...;`. |
| Returned bike cannot be rented again | `bikes.available` was not set back to true. | Run `UPDATE bikes SET available = true WHERE bike_id = ...;`. |
| Customer name has extra spaces | `psql` output kept aligned padding. | Trim with `sed -E 's/^ *| *$//g'`. |
| `sed` OR pattern does not work | Extended regex was not enabled. | Use `sed -E`. |
| SQL text value fails | Text was not quoted in SQL. | Use `WHERE phone = '$PHONE_NUMBER'`. |
| SQL boolean is stored incorrectly | Boolean was quoted as text. | Use `true` or `false` without SQL quotes. |

## Final Mental Model

The whole application follows this loop:

```text
Print menu
Read user input
Validate input
Query PostgreSQL
Check empty or non-empty result
Insert or update database state
Return to the menu with a clear message
```

That pattern is the foundation of many small Bash and database automation
programs.
