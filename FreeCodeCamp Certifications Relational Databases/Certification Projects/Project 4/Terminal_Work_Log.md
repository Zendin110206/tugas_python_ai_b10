# Terminal Work Log

## Purpose

This file documents the main terminal workflow used to complete the **Build a
Periodic Table Database** certification project.

It is not the final submission file. The final required submission files are
`periodic_table.sql` and `element.sh`.

## Environment

- Platform: freeCodeCamp Codespaces
- Database client: `psql`
- PostgreSQL user: `freecodecamp`
- Project database: `periodic_table`
- Script file: `element.sh`
- Final dump: `periodic_table.sql`

## PostgreSQL Service

If PostgreSQL is not running in a local or containerized environment, start it
from the Bash terminal:

```bash
sudo service postgresql start
```

The freeCodeCamp Codespaces environment usually has PostgreSQL ready, but this
command is useful when rebuilding or testing manually.

## Login and Database Selection

```bash
psql --username=freecodecamp --dbname=postgres
```

```sql
\c periodic_table
```

## Schema Cleanup

The starter database already contained periodic table data, but several names,
constraints, and relationships needed to be corrected.

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

### Restrict Text Column Lengths

```sql
ALTER TABLE elements ALTER COLUMN symbol TYPE VARCHAR(2);
ALTER TABLE elements ALTER COLUMN name TYPE VARCHAR(40);
```

### Add Foreign Key from Properties to Elements

```sql
ALTER TABLE properties
ADD FOREIGN KEY(atomic_number) REFERENCES elements(atomic_number);
```

## Normalize Element Types

The original `properties.type` text column was replaced with a normalized
`types` table.

```sql
CREATE TABLE types();
ALTER TABLE types ADD COLUMN type_id SERIAL PRIMARY KEY;
ALTER TABLE types ADD COLUMN type VARCHAR NOT NULL;
```

```sql
INSERT INTO types(type) VALUES('metal');
INSERT INTO types(type) VALUES('nonmetal');
INSERT INTO types(type) VALUES('metalloid');
```

```sql
ALTER TABLE properties ADD COLUMN type_id INT;
UPDATE properties SET type_id = 1 WHERE type = 'metal';
UPDATE properties SET type_id = 2 WHERE type = 'nonmetal';
UPDATE properties SET type_id = 3 WHERE type = 'metalloid';
ALTER TABLE properties ALTER COLUMN type_id SET NOT NULL;
ALTER TABLE properties ADD FOREIGN KEY(type_id) REFERENCES types(type_id);
ALTER TABLE properties DROP COLUMN type;
```

## Data Cleanup

Symbols were updated to proper chemical capitalization:

```sql
UPDATE elements SET symbol = 'H' WHERE atomic_number = 1;
UPDATE elements SET symbol = 'He' WHERE atomic_number = 2;
UPDATE elements SET symbol = 'Li' WHERE atomic_number = 3;
UPDATE elements SET symbol = 'Be' WHERE atomic_number = 4;
UPDATE elements SET symbol = 'B' WHERE atomic_number = 5;
UPDATE elements SET symbol = 'C' WHERE atomic_number = 6;
UPDATE elements SET symbol = 'N' WHERE atomic_number = 7;
UPDATE elements SET symbol = 'O' WHERE atomic_number = 8;
```

Trailing zeroes were removed from `atomic_mass`:

```sql
UPDATE properties
SET atomic_mass = TRIM(TRAILING '0' FROM atomic_mass::TEXT)::DECIMAL;
```

The cleaned output was checked and saved in `atomic_mass.txt`:

```sql
SELECT atomic_number, atomic_mass
FROM properties
ORDER BY atomic_number;
```

## Insert Missing Elements

Fluorine:

```sql
INSERT INTO elements(atomic_number, symbol, name)
VALUES(9, 'F', 'Fluorine');

INSERT INTO properties(atomic_number, atomic_mass, melting_point_celsius, boiling_point_celsius, type_id)
VALUES(9, 18.998, -220, -188.1, 2);
```

Neon:

```sql
INSERT INTO elements(atomic_number, symbol, name)
VALUES(10, 'Ne', 'Neon');

INSERT INTO properties(atomic_number, atomic_mass, melting_point_celsius, boiling_point_celsius, type_id)
VALUES(10, 20.18, -248.6, -246.1, 2);
```

## Script Setup

The script file was created as `element.sh` and starts with a Bash shebang:

```bash
#!/bin/bash
```

Executable permission is required:

```bash
chmod +x element.sh
```

The script uses this reusable PostgreSQL command:

```bash
PSQL="psql --username=freecodecamp --dbname=periodic_table -t --no-align -c"
```

## Main Script Flow

The submitted script follows this sequence:

1. Check whether an argument was provided.
2. If no argument exists, print the required missing-argument message.
3. If the argument is numeric, query by `atomic_number`.
4. If the argument is not numeric, query by `symbol` or `name`.
5. If no row is found, print the required not-found message.
6. If a row is found, parse the pipe-separated query result.
7. Print the final element description in the required format.

## Manual Test Flow

Missing argument:

```bash
./element.sh
```

Expected result:

```text
Please provide an element as an argument.
```

Atomic number lookup:

```bash
./element.sh 1
```

Expected result:

```text
The element with atomic number 1 is Hydrogen (H). It's a nonmetal, with a mass of 1.008 amu. Hydrogen has a melting point of -259.1 celsius and a boiling point of -252.9 celsius.
```

Symbol lookup:

```bash
./element.sh Ne
```

Expected result:

```text
The element with atomic number 10 is Neon (Ne). It's a nonmetal, with a mass of 20.18 amu. Neon has a melting point of -248.6 celsius and a boiling point of -246.1 celsius.
```

Unknown element lookup:

```bash
./element.sh 999
```

Expected result:

```text
I could not find that element in the database.
```

## Verification Queries

The final table structure can be checked with:

```sql
\d elements
\d properties
\d types
```

The final joined data can be checked with:

```sql
SELECT atomic_number, symbol, name, type, atomic_mass, melting_point_celsius, boiling_point_celsius
FROM elements
JOIN properties USING(atomic_number)
JOIN types USING(type_id)
ORDER BY atomic_number;
```

## Final Export

After the database and script passed the project tests, the `psql` session was
closed:

```sql
\q
```

The database dump was created from the Bash terminal:

```bash
pg_dump -cC --inserts -U freecodecamp periodic_table > periodic_table.sql
```

The generated `periodic_table.sql` file, together with `element.sh`, is required
for the freeCodeCamp certification project submission.
