# SQL Syntax Reference

## Purpose

This file summarizes the PostgreSQL syntax patterns used while working on the
**Build a Celestial Bodies Database** certification project.

It is a syntax reference, not the final submission. The final database dump is
stored in `universe.sql`.

## Terminal and `psql` Commands

These commands are entered either in the Bash terminal or inside the `psql`
prompt.

| Goal | Syntax | Example |
| --- | --- | --- |
| Test the terminal | `echo text` | `echo hello PostgreSQL` |
| Log in to PostgreSQL | `psql --username=user --dbname=database` | `psql --username=freecodecamp --dbname=postgres` |
| List databases | `\l` | `\l` |
| Connect to a database | `\c database_name` | `\c universe` |
| List tables and relations | `\d` | `\d` |
| Inspect one table | `\d table_name` | `\d galaxy` |
| Exit `psql` | `\q` | `\q` |
| Export a database dump | `pg_dump -cC --inserts -U user database > file.sql` | `pg_dump -cC --inserts -U freecodecamp universe > universe.sql` |

## Database Operations

| Goal | Syntax | Example |
| --- | --- | --- |
| Create a database | `CREATE DATABASE database_name;` | `CREATE DATABASE universe;` |
| Rename a database | `ALTER DATABASE old_name RENAME TO new_name;` | `ALTER DATABASE first_database RENAME TO mario_database;` |
| Drop a database | `DROP DATABASE database_name;` | `DROP DATABASE second_database;` |

## Table Operations

| Goal | Syntax | Example |
| --- | --- | --- |
| Create an empty table | `CREATE TABLE table_name();` | `CREATE TABLE galaxy();` |
| Create a table with one column | `CREATE TABLE table_name(column_name DATA_TYPE CONSTRAINT);` | `CREATE TABLE asteroid(asteroid_id SERIAL PRIMARY KEY);` |
| Create a table with multiple columns | `CREATE TABLE table_name (column_1 TYPE, column_2 TYPE);` | `CREATE TABLE planet (planet_id SERIAL PRIMARY KEY, name VARCHAR UNIQUE NOT NULL);` |
| Drop one table | `DROP TABLE table_name;` | `DROP TABLE second_table;` |
| Drop multiple tables | `DROP TABLE table_1, table_2;` | `DROP TABLE second_table, first_table;` |

## Column Operations

| Goal | Syntax | Example |
| --- | --- | --- |
| Add one column | `ALTER TABLE table_name ADD COLUMN column_name DATA_TYPE;` | `ALTER TABLE galaxy ADD COLUMN description TEXT;` |
| Add one column with constraints | `ALTER TABLE table_name ADD COLUMN column_name DATA_TYPE CONSTRAINT;` | `ALTER TABLE galaxy ADD COLUMN name VARCHAR UNIQUE NOT NULL;` |
| Add multiple columns | `ALTER TABLE table_name ADD COLUMN col_1 TYPE, ADD COLUMN col_2 TYPE;` | `ALTER TABLE galaxy ADD COLUMN galaxy_id SERIAL, ADD COLUMN name VARCHAR UNIQUE NOT NULL;` |
| Drop a column | `ALTER TABLE table_name DROP COLUMN column_name;` | `ALTER TABLE second_table DROP COLUMN age;` |
| Rename a column | `ALTER TABLE table_name RENAME COLUMN old_name TO new_name;` | `ALTER TABLE more_info RENAME COLUMN height TO height_in_cm;` |

## Constraints and Keys

| Goal | Syntax | Example |
| --- | --- | --- |
| Add a primary key | `ALTER TABLE table_name ADD PRIMARY KEY(column_name);` | `ALTER TABLE galaxy ADD PRIMARY KEY(galaxy_id);` |
| Add a composite primary key | `ALTER TABLE table_name ADD PRIMARY KEY(column_1, column_2);` | `ALTER TABLE character_actions ADD PRIMARY KEY(character_id, action_id);` |
| Drop a named constraint | `ALTER TABLE table_name DROP CONSTRAINT constraint_name;` | `ALTER TABLE characters DROP CONSTRAINT characters_pkey;` |
| Add a unique constraint | `ALTER TABLE table_name ADD UNIQUE(column_name);` | `ALTER TABLE galaxy ADD UNIQUE(name);` |
| Require non-null values | `ALTER TABLE table_name ALTER COLUMN column_name SET NOT NULL;` | `ALTER TABLE more_info ALTER COLUMN character_id SET NOT NULL;` |
| Add a foreign key while creating a column | `ALTER TABLE table_name ADD COLUMN column_name DATA_TYPE REFERENCES referenced_table(referenced_column);` | `ALTER TABLE more_info ADD COLUMN character_id INT REFERENCES characters(character_id);` |
| Add a foreign key to an existing column | `ALTER TABLE table_name ADD FOREIGN KEY(column_name) REFERENCES referenced_table(referenced_column);` | `ALTER TABLE planet ADD FOREIGN KEY(star_id) REFERENCES star(star_id);` |

## Common Data Types

| Data type | Meaning | Example |
| --- | --- | --- |
| `INT` | Whole number. | `temperature_in_kelvin INT` |
| `SERIAL` | Auto-incrementing integer, commonly used for IDs. | `galaxy_id SERIAL` |
| `VARCHAR(n)` | Text with a maximum length. | `name VARCHAR(30)` |
| `VARCHAR` | Variable-length text. | `name VARCHAR` |
| `TEXT` | Long text with no specific length limit. | `description TEXT` |
| `DATE` | Date value. | `'1990-04-13'` |
| `NUMERIC(p, s)` | Precise decimal number with precision and scale. | `NUMERIC(4, 1)` |
| `NUMERIC` | Decimal number without explicitly specified precision. | `distance_from_earth_ly NUMERIC` |
| `BOOLEAN` | True or false value. | `has_life BOOLEAN` |

## Row Operations

| Goal | Syntax | Example |
| --- | --- | --- |
| Insert one row | `INSERT INTO table_name(column_1, column_2) VALUES(value_1, value_2);` | `INSERT INTO asteroid(name, diameter_in_km) VALUES('Ceres', 939.4);` |
| Insert multiple rows | `INSERT INTO table_name(column_1, column_2) VALUES(value_1, value_2), (value_3, value_4);` | `INSERT INTO asteroid(name, diameter_in_km) VALUES('Ceres', 939.4), ('Vesta', 525.4);` |
| Update rows | `UPDATE table_name SET column_name=new_value WHERE condition;` | `UPDATE characters SET favorite_color='Orange' WHERE name='Daisy';` |
| Update multiple columns | `UPDATE table_name SET col_1=value_1, col_2=value_2 WHERE condition;` | `UPDATE more_info SET height=160, weight=60.5 WHERE character_id=1;` |
| Delete rows | `DELETE FROM table_name WHERE condition;` | `DELETE FROM second_table WHERE username='Luigi';` |

## Querying Data

| Goal | Syntax | Example |
| --- | --- | --- |
| View all columns and rows | `SELECT * FROM table_name;` | `SELECT * FROM galaxy;` |
| View specific columns | `SELECT column_1, column_2 FROM table_name;` | `SELECT galaxy_id, name FROM galaxy;` |
| Filter rows | `SELECT columns FROM table_name WHERE condition;` | `SELECT planet_id, name FROM planet WHERE star_id=1;` |
| Sort results | `SELECT columns FROM table_name ORDER BY column_name;` | `SELECT * FROM moon ORDER BY moon_id;` |
| Limit results | `SELECT columns FROM table_name LIMIT number;` | `SELECT name FROM planet LIMIT 5;` |

## Join Patterns

| Goal | Syntax | Example |
| --- | --- | --- |
| Join two related tables | `SELECT columns FROM table_1 FULL JOIN table_2 ON table_1.primary_key = table_2.foreign_key;` | `SELECT * FROM characters FULL JOIN more_info ON characters.character_id = more_info.character_id;` |
| Join through a junction table | `SELECT columns FROM junction_table FULL JOIN table_1 ON junction_table.fk_1 = table_1.pk FULL JOIN table_2 ON junction_table.fk_2 = table_2.pk;` | `SELECT * FROM character_actions FULL JOIN characters ON character_actions.character_id = characters.character_id FULL JOIN actions ON character_actions.action_id = actions.action_id;` |
| Join with filtering and sorting | `SELECT columns FROM table_1 JOIN table_2 ON condition WHERE condition ORDER BY column;` | `SELECT characters.name, actions.action FROM character_actions FULL JOIN characters ON character_actions.character_id = characters.character_id FULL JOIN actions ON character_actions.action_id = actions.action_id WHERE characters.name='Mario' ORDER BY actions.action;` |

## Project-Specific Reminders

- SQL commands need semicolons.
- `psql` meta-commands such as `\l`, `\c`, `\d`, and `\q` do not need semicolons.
- Create parent tables before child tables when foreign keys are involved.
- Insert parent rows before child rows when foreign keys are involved.
- The `name` column must be `VARCHAR` in every table for this project.
- Each primary key should follow the `table_name_id` pattern.
- Each foreign key column should use the same name as the referenced column.
- Use specific `WHERE` clauses when updating or deleting data.
