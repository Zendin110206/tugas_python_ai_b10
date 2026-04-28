# Build a Database of Video Game Characters

## Context

This document summarizes the **Build a Database of Video Game Characters**
workshop from the freeCodeCamp Relational Databases Certification track.

The workshop was completed in **GitHub Codespaces** through the CodeRoad
extension. The original lesson is interactive and step-based, so this repository
keeps a cleaned learning record instead of raw copied prompts from the
CodeRoad interface.

The goal of this note is to make the workshop reproducible and understandable:
what was built, which PostgreSQL commands were used, why each table exists, how
the relationships work, and how the final joins connect the data.

## Workshop Goal

Build a PostgreSQL database named `mario_database` that stores video game
characters and related information.

The workshop focuses on:

- using the `psql` terminal application
- creating, renaming, connecting to, and dropping databases
- creating and altering tables
- adding columns with appropriate data types
- inserting, updating, deleting, and selecting rows
- defining primary keys and foreign keys
- modeling one-to-one, one-to-many, and many-to-many relationships
- using a junction table for many-to-many data
- joining related tables to view combined information

## Environment

- Platform: freeCodeCamp Relational Databases Certification
- Workspace: GitHub Codespaces
- Tutorial runner: CodeRoad
- Database system: PostgreSQL
- Database client: `psql`
- User used in the workshop: `freecodecamp`

## Database Design Overview

The final database contains five main tables:

| Table | Purpose | Main key |
| --- | --- | --- |
| `characters` | Stores the core character records. | `character_id` |
| `more_info` | Stores one extra profile row for each character. | `more_info_id` |
| `sounds` | Stores sound filenames connected to characters. | `sound_id` |
| `actions` | Stores the list of possible actions. | `action_id` |
| `character_actions` | Connects characters and actions. | `(character_id, action_id)` |

Expected relationship types:

| Relationship | Tables | Meaning |
| --- | --- | --- |
| One-to-one | `characters` to `more_info` | One character has one extra info row. |
| One-to-many | `characters` to `sounds` | One character can have many sounds. |
| Many-to-many | `characters` to `actions` through `character_actions` | Many characters can perform many actions. |

## Relationship Notes

### Primary Key

A primary key uniquely identifies a row in a table.

In this workshop, columns such as `character_id`, `more_info_id`, `sound_id`,
and `action_id` are used as primary keys because they are stable identifiers.
Names are readable, but they are not the best primary key choice because names
can change.

That idea appears in the workshop when `name` is first tested as a primary key,
then replaced with `character_id`.

### Foreign Key

A foreign key stores a value that points to a primary key in another table.

For example, `sounds.character_id` points to `characters.character_id`. This
means every sound row must belong to a valid character.

### One-to-One Relationship

The `more_info` table has a `character_id` foreign key that references
`characters(character_id)`.

The relationship becomes one-to-one because `more_info.character_id` is both:

- `NOT NULL`, so every `more_info` row must belong to a character
- `UNIQUE`, so one character can appear only once in `more_info`

Without `UNIQUE`, one character could have multiple `more_info` rows, which
would make it one-to-many instead.

### One-to-Many Relationship

The `sounds` table also has a `character_id` foreign key, but it does **not**
have a `UNIQUE` constraint.

That is intentional. A single character can have multiple sound files, such as
Mario having both `its-a-me.wav` and `yippee.wav`.

The foreign key belongs on the "many" side of the relationship, so
`sounds.character_id` points back to the one character that owns each sound.

### Many-to-Many Relationship and Junction Table

Characters and actions form a many-to-many relationship:

- one character can perform many actions
- one action can be performed by many characters

Putting `character_id` directly in the `actions` table would not work cleanly
because the action `run` belongs to many characters, not just one. Putting
multiple action columns directly in the `characters` table would also be a poor
design because it creates repeated columns and makes the database harder to
query.

The professional relational design is to use a **junction table**:
`character_actions`.

The junction table stores pairs:

```text
character_id + action_id
```

Each row means: "this character can perform this action."

The composite primary key `(character_id, action_id)` prevents duplicate pairs.
For example, Mario can have `(1, 1)` for `run`, but the same pair should not be
inserted twice.

## Walkthrough

### 1. Start `psql` and Inspect Existing Databases

Open the terminal in the Codespaces workspace and log in to PostgreSQL.

```bash
psql --username=freecodecamp --dbname=postgres
```

Inside the `psql` prompt, list existing databases.

```sql
\l
```

What this verifies:

- PostgreSQL is installed and running.
- The `freecodecamp` user can connect to the default `postgres` database.
- `\l` is a `psql` meta-command for listing databases.

### 2. Practice Database Creation and Connection

The workshop starts with temporary practice databases before building the final
Mario database.

```sql
CREATE DATABASE first_database;
\l

CREATE DATABASE second_database;
\l

\c second_database
\d
```

Important details:

- SQL commands need a semicolon.
- `\c database_name` connects to another database.
- `\d` displays tables and relations in the current database.

### 3. Practice Table and Column Operations

Create temporary tables in `second_database`.

```sql
CREATE TABLE first_table();
CREATE TABLE second_table();
\d
```

Add, inspect, rename, and remove columns.

```sql
ALTER TABLE second_table ADD COLUMN first_column INT;
ALTER TABLE second_table ADD COLUMN id INT;
ALTER TABLE second_table ADD COLUMN age INT;
\d second_table

ALTER TABLE second_table DROP COLUMN age;
ALTER TABLE second_table DROP COLUMN first_column;

ALTER TABLE second_table ADD COLUMN name VARCHAR(30);
ALTER TABLE second_table RENAME COLUMN name TO username;
\d second_table
```

What this practices:

- `ALTER TABLE ... ADD COLUMN` changes a table structure.
- `ALTER TABLE ... DROP COLUMN` removes a column.
- `VARCHAR(30)` stores text up to 30 characters.
- `RENAME COLUMN` changes a column name without recreating the table.

### 4. Practice Insert, Select, Delete, and Cleanup

Insert temporary rows.

```sql
INSERT INTO second_table(id, username) VALUES(1, 'Samus');
INSERT INTO second_table(id, username) VALUES(2, 'Mario');
INSERT INTO second_table(id, username) VALUES(3, 'Luigi');

SELECT * FROM second_table;
```

Delete the temporary rows.

```sql
DELETE FROM second_table WHERE username='Luigi';
DELETE FROM second_table WHERE username='Mario';
DELETE FROM second_table WHERE username='Samus';

SELECT * FROM second_table;
```

Clean up the temporary tables.

```sql
ALTER TABLE second_table DROP COLUMN username;
ALTER TABLE second_table DROP COLUMN id;

DROP TABLE second_table;
DROP TABLE first_table;
```

The temporary section is useful because it introduces common SQL operations
before the final database is created.

### 5. Rename the Final Database and Remove Temporary Database

The workshop uses the earlier `first_database` as the final Mario database.

```sql
\l
ALTER DATABASE first_database RENAME TO mario_database;
\l

\c mario_database
DROP DATABASE second_database;
\l
\d
```

At this point, the working database is `mario_database`.

### 6. Create the `characters` Table

Create the table and add the main columns.

```sql
CREATE TABLE characters();

ALTER TABLE characters ADD COLUMN character_id SERIAL;
ALTER TABLE characters ADD COLUMN name VARCHAR(30) NOT NULL;
ALTER TABLE characters ADD COLUMN homeland VARCHAR(60);
ALTER TABLE characters ADD COLUMN favorite_color VARCHAR(30);

\d characters
```

Why `SERIAL` is used:

- It creates an integer column.
- It automatically increments when new rows are inserted.
- It is useful for ID columns.

### 7. Insert and Correct Character Data

Insert the initial character rows.

```sql
INSERT INTO characters(name, homeland, favorite_color)
VALUES('Mario', 'Mushroom Kingdom', 'Red');

INSERT INTO characters(name, homeland, favorite_color)
VALUES('Luigi', 'Mushroom Kingdom', 'Green');

INSERT INTO characters(name, homeland, favorite_color)
VALUES('Peach', 'Mushroom Kingdom', 'Pink');

INSERT INTO characters(name, homeland, favorite_color)
VALUES
  ('Toadstool', 'Mushroom Kingdom', 'Red'),
  ('Bowser', 'Mushroom Kingdom', 'Green');

INSERT INTO characters(name, homeland, favorite_color)
VALUES
  ('Daisy', 'Sarasaland', 'Yellow'),
  ('Yoshi', 'Dinosaur Land', 'Green');

SELECT * FROM characters;
```

Update incorrect values.

```sql
UPDATE characters SET favorite_color='Orange' WHERE name='Daisy';
```

The workshop intentionally demonstrates an unsafe update condition:

```sql
UPDATE characters SET name='Toad' WHERE favorite_color='Red';
```

That changes both Toadstool and Mario because both rows have
`favorite_color='Red'`. This is an important reminder: a `WHERE` condition
should target the intended row as specifically as possible.

Fix Mario and complete the remaining corrections.

```sql
UPDATE characters SET name='Mario' WHERE character_id=1;
UPDATE characters SET favorite_color='Blue' WHERE name='Toad';
UPDATE characters SET favorite_color='Yellow' WHERE name='Bowser';
UPDATE characters SET homeland='Koopa Kingdom' WHERE name='Bowser';

SELECT * FROM characters ORDER BY character_id;
```

Expected `characters` rows:

| character_id | name | homeland | favorite_color |
| ---: | --- | --- | --- |
| 1 | Mario | Mushroom Kingdom | Red |
| 2 | Luigi | Mushroom Kingdom | Green |
| 3 | Peach | Mushroom Kingdom | Pink |
| 4 | Toad | Mushroom Kingdom | Blue |
| 5 | Bowser | Koopa Kingdom | Yellow |
| 6 | Daisy | Sarasaland | Orange |
| 7 | Yoshi | Dinosaur Land | Green |

### 8. Set the Primary Key on `characters`

The workshop first tests `name` as a primary key, then replaces it with the more
appropriate `character_id`.

```sql
ALTER TABLE characters ADD PRIMARY KEY(name);
\d characters

ALTER TABLE characters DROP CONSTRAINT characters_pkey;
\d characters

ALTER TABLE characters ADD PRIMARY KEY(character_id);
\d characters
```

Why `character_id` is better:

- It is stable.
- It is automatically generated.
- It does not depend on a human-readable value that might change.

### 9. Create `more_info` for a One-to-One Relationship

Create the table and add profile columns.

```sql
CREATE TABLE more_info();

ALTER TABLE more_info ADD COLUMN more_info_id SERIAL;
ALTER TABLE more_info ADD PRIMARY KEY(more_info_id);
ALTER TABLE more_info ADD COLUMN birthday DATE;
ALTER TABLE more_info ADD COLUMN height INT;
ALTER TABLE more_info ADD COLUMN weight NUMERIC(4, 1);

\d more_info
```

Add the foreign key to connect each profile row to a character.

```sql
ALTER TABLE more_info
ADD COLUMN character_id INT REFERENCES characters(character_id);

ALTER TABLE more_info ADD UNIQUE(character_id);
ALTER TABLE more_info ALTER COLUMN character_id SET NOT NULL;

\d more_info
```

Why this creates one-to-one:

- `character_id` references an existing character.
- `UNIQUE(character_id)` prevents two profile rows for the same character.
- `NOT NULL` prevents profile rows that belong to no character.

### 10. Insert Character Profile Data

Check character IDs before inserting foreign key values.

```sql
SELECT character_id, name FROM characters ORDER BY character_id;
```

Insert the profile records.

```sql
INSERT INTO more_info(birthday, height, weight, character_id)
VALUES('1981-07-09', 155, 64.5, 1);

INSERT INTO more_info(birthday, height, weight, character_id)
VALUES('1983-07-14', 175, 48.8, 2);

INSERT INTO more_info(birthday, height, weight, character_id)
VALUES('1985-10-18', 173, 52.2, 3);

INSERT INTO more_info(birthday, height, weight, character_id)
VALUES('1950-01-10', 66, 35.6, 4);

INSERT INTO more_info(birthday, height, weight, character_id)
VALUES('1990-10-29', 258, 300, 5);

INSERT INTO more_info(birthday, height, weight, character_id)
VALUES('1989-07-31', NULL, NULL, 6);

INSERT INTO more_info(birthday, height, weight, character_id)
VALUES('1990-04-13', 162, 59.1, 7);

SELECT * FROM more_info;
```

Rename measurement columns so the units are clear.

```sql
ALTER TABLE more_info RENAME COLUMN height TO height_in_cm;
ALTER TABLE more_info RENAME COLUMN weight TO weight_in_kg;

SELECT * FROM more_info;
```

### 11. Create `sounds` for a One-to-Many Relationship

Create the table and define the sound file column.

```sql
CREATE TABLE sounds(sound_id SERIAL PRIMARY KEY);

ALTER TABLE sounds
ADD COLUMN filename VARCHAR(40) UNIQUE NOT NULL;
```

Add the foreign key.

```sql
ALTER TABLE sounds
ADD COLUMN character_id INT NOT NULL REFERENCES characters(character_id);

\d sounds
```

Why this creates one-to-many:

- each sound row has one `character_id`
- a character can appear in many sound rows
- `sounds.character_id` is not unique

Insert sound data.

```sql
INSERT INTO sounds(filename, character_id)
VALUES('its-a-me.wav', 1);

INSERT INTO sounds(filename, character_id)
VALUES('yippee.wav', 1);

INSERT INTO sounds(filename, character_id)
VALUES('ha-ha.wav', 2);

INSERT INTO sounds(filename, character_id)
VALUES('oh-yeah.wav', 2);

INSERT INTO sounds(filename, character_id)
VALUES
  ('yay.wav', 3),
  ('woo-hoo.wav', 3);

INSERT INTO sounds(filename, character_id)
VALUES
  ('mm-hmm.wav', 3),
  ('yahoo.wav', 1);

SELECT * FROM sounds;
```

### 12. Create `actions`

Create a lookup table for the available actions.

```sql
CREATE TABLE actions(action_id SERIAL PRIMARY KEY);

ALTER TABLE actions
ADD COLUMN action VARCHAR(20) UNIQUE NOT NULL;

INSERT INTO actions(action) VALUES('run');
INSERT INTO actions(action) VALUES('jump');
INSERT INTO actions(action) VALUES('duck');

SELECT * FROM actions;
```

The `actions` table does not directly reference `characters` because the
relationship is many-to-many. The connection is made through the junction table
in the next step.

### 13. Create the `character_actions` Junction Table

Create the junction table.

```sql
CREATE TABLE character_actions();
```

Add the foreign key columns.

```sql
ALTER TABLE character_actions
ADD COLUMN character_id INT NOT NULL;

ALTER TABLE character_actions
ADD FOREIGN KEY(character_id) REFERENCES characters(character_id);

ALTER TABLE character_actions
ADD COLUMN action_id INT NOT NULL;

ALTER TABLE character_actions
ADD FOREIGN KEY(action_id) REFERENCES actions(action_id);

\d character_actions
```

Add a composite primary key.

```sql
ALTER TABLE character_actions
ADD PRIMARY KEY(character_id, action_id);

\d character_actions
```

Why the composite key matters:

- `character_id` alone is not unique because one character can have many actions.
- `action_id` alone is not unique because one action can belong to many
  characters.
- `(character_id, action_id)` is unique because the same character-action pair
  should appear only once.

### 14. Insert Character Actions

In this workshop, each character can perform all three actions.

```sql
INSERT INTO character_actions(character_id, action_id)
VALUES
  (7, 1), (7, 2), (7, 3),
  (6, 1), (6, 2), (6, 3),
  (5, 1), (5, 2), (5, 3),
  (4, 1), (4, 2), (4, 3),
  (3, 1), (3, 2), (3, 3),
  (2, 1), (2, 2), (2, 3),
  (1, 1), (1, 2), (1, 3);

SELECT * FROM character_actions;
```

Expected row count:

```text
7 characters x 3 actions = 21 rows
```

### 15. Inspect the Final Database

Display all tables and inspect the main data.

```sql
\d

SELECT * FROM characters;
SELECT * FROM more_info;
SELECT * FROM sounds;
SELECT * FROM actions;
SELECT * FROM character_actions;
```

The final project should have five main data tables:

```text
characters
more_info
sounds
actions
character_actions
```

PostgreSQL also creates sequence relations for `SERIAL` columns, such as
`characters_character_id_seq`. Those are expected and are used to generate the
next auto-increment value.

## Join Queries

### Join `characters` and `more_info`

```sql
SELECT *
FROM characters
FULL JOIN more_info
ON characters.character_id = more_info.character_id;
```

This demonstrates the one-to-one relationship. Each character should match one
row in `more_info`.

### Join `characters` and `sounds`

```sql
SELECT *
FROM characters
FULL JOIN sounds
ON characters.character_id = sounds.character_id;
```

This demonstrates the one-to-many relationship. Some characters appear multiple
times because they have multiple sound rows.

### Join `character_actions`, `characters`, and `actions`

The course query uses `FULL JOIN` to connect all three tables:

```sql
SELECT *
FROM character_actions
FULL JOIN characters
ON character_actions.character_id = characters.character_id
FULL JOIN actions
ON character_actions.action_id = actions.action_id;
```

For documentation, adding `ORDER BY` makes the output deterministic:

```sql
SELECT *
FROM character_actions
FULL JOIN characters
ON character_actions.character_id = characters.character_id
FULL JOIN actions
ON character_actions.action_id = actions.action_id
ORDER BY character_actions.character_id DESC, character_actions.action_id;
```

Expected final output:

```text
+--------------+-----------+--------------+--------+------------------+----------------+-----------+--------+
| character_id | action_id | character_id |  name  |     homeland     | favorite_color | action_id | action |
+--------------+-----------+--------------+--------+------------------+----------------+-----------+--------+
|            7 |         1 |            7 | Yoshi  | Dinosaur Land    | Green          |         1 | run    |
|            7 |         2 |            7 | Yoshi  | Dinosaur Land    | Green          |         2 | jump   |
|            7 |         3 |            7 | Yoshi  | Dinosaur Land    | Green          |         3 | duck   |
|            6 |         1 |            6 | Daisy  | Sarasaland       | Orange         |         1 | run    |
|            6 |         2 |            6 | Daisy  | Sarasaland       | Orange         |         2 | jump   |
|            6 |         3 |            6 | Daisy  | Sarasaland       | Orange         |         3 | duck   |
|            5 |         1 |            5 | Bowser | Koopa Kingdom    | Yellow         |         1 | run    |
|            5 |         2 |            5 | Bowser | Koopa Kingdom    | Yellow         |         2 | jump   |
|            5 |         3 |            5 | Bowser | Koopa Kingdom    | Yellow         |         3 | duck   |
|            4 |         1 |            4 | Toad   | Mushroom Kingdom | Blue           |         1 | run    |
|            4 |         2 |            4 | Toad   | Mushroom Kingdom | Blue           |         2 | jump   |
|            4 |         3 |            4 | Toad   | Mushroom Kingdom | Blue           |         3 | duck   |
|            3 |         1 |            3 | Peach  | Mushroom Kingdom | Pink           |         1 | run    |
|            3 |         2 |            3 | Peach  | Mushroom Kingdom | Pink           |         2 | jump   |
|            3 |         3 |            3 | Peach  | Mushroom Kingdom | Pink           |         3 | duck   |
|            2 |         1 |            2 | Luigi  | Mushroom Kingdom | Green          |         1 | run    |
|            2 |         2 |            2 | Luigi  | Mushroom Kingdom | Green          |         2 | jump   |
|            2 |         3 |            2 | Luigi  | Mushroom Kingdom | Green          |         3 | duck   |
|            1 |         1 |            1 | Mario  | Mushroom Kingdom | Red            |         1 | run    |
|            1 |         2 |            1 | Mario  | Mushroom Kingdom | Red            |         2 | jump   |
|            1 |         3 |            1 | Mario  | Mushroom Kingdom | Red            |         3 | duck   |
+--------------+-----------+--------------+--------+------------------+----------------+-----------+--------+
(21 rows)
```

## Command Reference

| Command or SQL pattern | Purpose |
| --- | --- |
| `psql --username=freecodecamp --dbname=postgres` | Log in to PostgreSQL through `psql`. |
| `\l` | List databases. |
| `\c database_name` | Connect to a database. |
| `\d` | Display relations in the current database. |
| `\d table_name` | Display details for a specific table. |
| `CREATE DATABASE name;` | Create a database. |
| `ALTER DATABASE old_name RENAME TO new_name;` | Rename a database. |
| `DROP DATABASE name;` | Delete a database. |
| `CREATE TABLE table_name();` | Create an empty table. |
| `CREATE TABLE table_name(column_name DATATYPE CONSTRAINT);` | Create a table with columns. |
| `ALTER TABLE table_name ADD COLUMN column_name DATATYPE;` | Add a column. |
| `ALTER TABLE table_name DROP COLUMN column_name;` | Drop a column. |
| `ALTER TABLE table_name RENAME COLUMN old_name TO new_name;` | Rename a column. |
| `INSERT INTO table_name(columns) VALUES(values);` | Insert rows. |
| `SELECT columns FROM table_name;` | Query data. |
| `SELECT * FROM table_name;` | Query all columns. |
| `UPDATE table_name SET column=value WHERE condition;` | Update rows that match a condition. |
| `DELETE FROM table_name WHERE condition;` | Delete rows that match a condition. |
| `ALTER TABLE table_name ADD PRIMARY KEY(column_name);` | Add a primary key. |
| `ALTER TABLE table_name DROP CONSTRAINT constraint_name;` | Drop a named constraint. |
| `REFERENCES table_name(column_name)` | Define a foreign key reference. |
| `ALTER TABLE table_name ADD UNIQUE(column_name);` | Add a unique constraint. |
| `ALTER TABLE table_name ALTER COLUMN column_name SET NOT NULL;` | Require a column value. |
| `FULL JOIN ... ON ...` | Join tables while keeping unmatched rows from both sides. |
| `ORDER BY column_name` | Sort query output. |

## Key Takeaways

- PostgreSQL work should be verified frequently with `\l`, `\d`, and `SELECT`.
- `SERIAL` is useful for generated ID columns, but it also creates sequence
  relations behind the scenes.
- Primary keys identify rows. Foreign keys connect rows across tables.
- A one-to-one relationship can be enforced with a foreign key plus `UNIQUE` and
  `NOT NULL`.
- A one-to-many relationship usually stores the foreign key on the "many" table.
- A many-to-many relationship should use a junction table instead of repeating
  columns or duplicating lookup values.
- Composite primary keys are useful in junction tables because the combination
  of two foreign keys can uniquely identify a relationship.
- `WHERE` conditions must be written carefully. A broad condition can update or
  delete more rows than intended.
- Professional database documentation should explain both the commands and the
  reason behind the schema design.
