# Periodic Table SQL and Bash Reference

## Purpose

This reference documents the PostgreSQL and Bash patterns used in the **Build a
Periodic Table Database** certification project.

It focuses on the syntax needed to understand, rebuild, and debug the submitted
`element.sh` workflow without changing the final project behavior.

## Project Files

| File | Purpose |
| --- | --- |
| `CodeRoad_Instructions.md` | Cleaned version of the project requirements. |
| `Database_Blueprint.md` | Schema and relationship planning notes. |
| `Terminal_Work_Log.md` | Main terminal workflow used to complete the project. |
| `atomic_mass.txt` | Verification output for cleaned atomic mass values. |
| `periodic_table/element.sh` | Final executable Bash script. |
| `periodic_table/periodic_table.sql` | Final database dump required for submission. |

## Reusable `psql` Command

The script stores the PostgreSQL command in one variable:

```bash
PSQL="psql --username=freecodecamp --dbname=periodic_table -t --no-align -c"
```

| Part | Meaning |
| --- | --- |
| `psql` | Runs the PostgreSQL command-line client. |
| `--username=freecodecamp` | Connects with the freeCodeCamp database user. |
| `--dbname=periodic_table` | Runs queries against the `periodic_table` database. |
| `-t` | Prints tuples only, without table headers or row-count footers. |
| `--no-align` | Prints output without padded table formatting. |
| `-c` | Runs one SQL command from Bash. |

`--no-align` is useful in this project because each selected row is later split
with `IFS="|" read ...`.

## Missing Argument Check

The script must stop early when no argument is provided:

```bash
if [[ -z $1 ]]
then
  echo "Please provide an element as an argument."
fi
```

| Expression | Meaning |
| --- | --- |
| `$1` | First command-line argument passed to the script. |
| `[[ -z $1 ]]` | True when the first argument is empty. |
| `echo ...` | Prints the exact message required by the tests. |

Example:

```bash
./element.sh
```

Expected output:

```text
Please provide an element as an argument.
```

## Numeric Input Detection

The script checks whether the argument is an atomic number:

```bash
if [[ $1 =~ ^[0-9]+$ ]]
then
  # Query by atomic number.
fi
```

| Pattern | Meaning |
| --- | --- |
| `=~` | Tests a value against a regular expression. |
| `^` | Start of the string. |
| `[0-9]+` | One or more digits. |
| `$` | End of the string. |

This means `1`, `2`, and `10` are treated as atomic numbers, while `H`,
`Hydrogen`, and `Neon` are treated as symbol or name inputs.

## Query by Atomic Number

When the input is numeric, the script queries by `atomic_number`:

```bash
GET_ATOMIC_NUMBER=$($PSQL "SELECT name, symbol, type, atomic_mass, melting_point_celsius, boiling_point_celsius FROM elements JOIN properties USING(atomic_number) JOIN types USING(type_id) WHERE atomic_number = $1")
```

The selected columns are ordered to match the `read` variables:

```bash
echo "$GET_ATOMIC_NUMBER" | while IFS="|" read NAME SYMBOL TYPE ATOMIC_MASS MELTING BOILING
do
  echo "The element with atomic number $1 is $NAME ($SYMBOL). It's a $TYPE, with a mass of $ATOMIC_MASS amu. $NAME has a melting point of $MELTING celsius and a boiling point of $BOILING celsius."
done
```

| Part | Meaning |
| --- | --- |
| `JOIN properties USING(atomic_number)` | Combines element identity with physical properties. |
| `JOIN types USING(type_id)` | Adds the normalized type label. |
| `WHERE atomic_number = $1` | Filters to the requested atomic number. |
| `IFS="|"` | Uses the pipe character as the field separator. |
| `read NAME SYMBOL ...` | Assigns each selected field to a Bash variable. |

## Query by Symbol or Name

When the input is not numeric, the script searches both `symbol` and `name`:

```bash
GET_SYMBOL_NAME=$($PSQL "SELECT atomic_number, name, symbol, type, atomic_mass, melting_point_celsius, boiling_point_celsius FROM elements JOIN properties USING(atomic_number) JOIN types USING(type_id) WHERE symbol = '$1' OR name = '$1'")
```

The output is parsed with variables in the same order as the `SELECT` list:

```bash
echo "$GET_SYMBOL_NAME" | while IFS="|" read ATOMIC_NUMBER NAME SYMBOL TYPE ATOMIC_MASS MELTING BOILING
do
  echo "The element with atomic number $ATOMIC_NUMBER is $NAME ($SYMBOL). It's a $TYPE, with a mass of $ATOMIC_MASS amu. $NAME has a melting point of $MELTING celsius and a boiling point of $BOILING celsius."
done
```

Text values in SQL conditions are wrapped in single quotes:

```sql
WHERE symbol = 'H' OR name = 'Hydrogen'
```

## Empty Query Result Handling

Both lookup branches check whether the query returned nothing:

```bash
if [[ -z $GET_SYMBOL_NAME ]]
then
  echo "I could not find that element in the database."
fi
```

This protects the script from printing a malformed success message when the
database does not contain the requested element.

## Schema Cleanup Commands

The original database needed several structural changes before it matched the
project requirements.

### Rename Columns

```sql
ALTER TABLE properties RENAME COLUMN weight TO atomic_mass;
ALTER TABLE properties RENAME COLUMN melting_point TO melting_point_celsius;
ALTER TABLE properties RENAME COLUMN boiling_point TO boiling_point_celsius;
```

### Add Required Constraints

```sql
ALTER TABLE properties ALTER COLUMN melting_point_celsius SET NOT NULL;
ALTER TABLE properties ALTER COLUMN boiling_point_celsius SET NOT NULL;
ALTER TABLE elements ADD UNIQUE(symbol);
ALTER TABLE elements ADD UNIQUE(name);
```

### Change Column Types

```sql
ALTER TABLE elements ALTER COLUMN symbol TYPE VARCHAR(2);
ALTER TABLE elements ALTER COLUMN name TYPE VARCHAR(40);
```

If a type change is more complex, PostgreSQL can use `USING` to explain how the
old value should become the new value:

```sql
ALTER TABLE table_name
ALTER COLUMN column_name TYPE new_type
USING column_name::new_type;
```

## Normalized `types` Table

The original table stored element type as repeated text in `properties`.
The normalized design moves type names into their own table:

```sql
CREATE TABLE types();
ALTER TABLE types ADD COLUMN type_id SERIAL PRIMARY KEY;
ALTER TABLE types ADD COLUMN type VARCHAR NOT NULL;
```

Seed the valid type rows:

```sql
INSERT INTO types(type) VALUES('metal');
INSERT INTO types(type) VALUES('nonmetal');
INSERT INTO types(type) VALUES('metalloid');
```

Add and populate the foreign key column in `properties`:

```sql
ALTER TABLE properties ADD COLUMN type_id INT;

UPDATE properties SET type_id = 1 WHERE type = 'metal';
UPDATE properties SET type_id = 2 WHERE type = 'nonmetal';
UPDATE properties SET type_id = 3 WHERE type = 'metalloid';

ALTER TABLE properties ALTER COLUMN type_id SET NOT NULL;
ALTER TABLE properties ADD FOREIGN KEY(type_id) REFERENCES types(type_id);
ALTER TABLE properties DROP COLUMN type;
```

This makes `types.type` the single source of truth for type labels.

## Foreign Key Relationship

The `properties` table connects back to `elements` through `atomic_number`:

```sql
ALTER TABLE properties
ADD FOREIGN KEY(atomic_number) REFERENCES elements(atomic_number);
```

The relationship prevents a property row from referring to an element that does
not exist.

## Symbol Capitalization

The project requires symbols to use standard chemical capitalization, such as
`H`, `He`, and `Li`.

Direct targeted updates are easy to audit:

```sql
UPDATE elements SET symbol = 'H' WHERE atomic_number = 1;
UPDATE elements SET symbol = 'He' WHERE atomic_number = 2;
UPDATE elements SET symbol = 'Li' WHERE atomic_number = 3;
```

## Atomic Mass Cleanup

The project requires unnecessary trailing zeroes to be removed from
`atomic_mass`.

```sql
UPDATE properties
SET atomic_mass = TRIM(TRAILING '0' FROM atomic_mass::TEXT)::DECIMAL;
```

| Part | Meaning |
| --- | --- |
| `atomic_mass::TEXT` | Temporarily converts the numeric value to text. |
| `TRIM(TRAILING '0' FROM ...)` | Removes zero characters only from the end of the text. |
| `::DECIMAL` | Converts the cleaned text back into a decimal value. |

This pattern is useful when a project test checks displayed numeric formatting,
not only the mathematical value.

## Insert Missing Elements

Fluorine and neon must exist in both `elements` and `properties`:

```sql
INSERT INTO elements(atomic_number, symbol, name)
VALUES(9, 'F', 'Fluorine');

INSERT INTO properties(atomic_number, atomic_mass, melting_point_celsius, boiling_point_celsius, type_id)
VALUES(9, 18.998, -220, -188.1, 2);
```

```sql
INSERT INTO elements(atomic_number, symbol, name)
VALUES(10, 'Ne', 'Neon');

INSERT INTO properties(atomic_number, atomic_mass, melting_point_celsius, boiling_point_celsius, type_id)
VALUES(10, 20.18, -248.6, -246.1, 2);
```

Both are nonmetals, so their `type_id` is `2`.

## Manual Script Tests

Use these script calls after the database and script are ready:

```bash
./element.sh
./element.sh 1
./element.sh H
./element.sh Hydrogen
./element.sh 10
./element.sh Ne
./element.sh Neon
./element.sh 999
```

Expected successful output for hydrogen:

```text
The element with atomic number 1 is Hydrogen (H). It's a nonmetal, with a mass of 1.008 amu. Hydrogen has a melting point of -259.1 celsius and a boiling point of -252.9 celsius.
```

Expected output for an unknown element:

```text
I could not find that element in the database.
```

## Common Mistakes

| Problem | Likely Cause | Fix |
| --- | --- | --- |
| Script cannot run | `element.sh` is not executable. | Run `chmod +x element.sh`. |
| Query output has unexpected spaces | `psql` aligned output was used. | Use `-t --no-align` or trim the values. |
| Symbol lookup fails | Symbols are lowercase or not capitalized. | Update symbols to standard capitalization. |
| Type text is missing | `properties.type` was dropped before `type_id` was populated. | Populate `type_id` before dropping the old column. |
| Atomic mass still shows trailing zeroes | Numeric cleanup was not applied. | Run the `TRIM(TRAILING '0' ...)::DECIMAL` update. |
| Foreign key add fails | Child rows do not match parent rows. | Check that every `properties.atomic_number` exists in `elements`. |
| Tests reject the final message | Output text differs from the required sentence. | Match punctuation, spelling, and value order exactly. |
