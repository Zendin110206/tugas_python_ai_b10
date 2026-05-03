# PostgreSQL SQL Cheatsheet

This cheatsheet is a quick lookup reference for PostgreSQL and SQL syntax
learned in the freeCodeCamp Relational Databases Certification track.

Use it when writing `psql` commands, table definitions, constraints, inserts,
queries, filters, joins, or database dumps.

## Terminal and `psql`

| Goal | Syntax | Example | Notes |
| --- | --- | --- | --- |
| Log in to PostgreSQL | `psql --username=user --dbname=database` | `psql --username=freecodecamp --dbname=postgres` | Enter from Bash terminal. |
| List databases | `\l` | `\l` | `psql` meta-command. |
| Connect to database | `\c database_name` | `\c students` | Switch current database. |
| List tables | `\d` | `\d` | Shows relations. |
| Inspect table | `\d table_name` | `\d students` | Shows columns and keys. |
| Exit `psql` | `\q` | `\q` | Leaves `psql`. |
| Run one SQL command from Bash | `psql ... -c "SQL"` | `psql --username=freecodecamp --dbname=students -c "SELECT * FROM majors"` | Useful in scripts. |
| Export dump | `pg_dump --clean --create --inserts --username=user database > file.sql` | `pg_dump --clean --create --inserts --username=freecodecamp students > students.sql` | Creates rebuild file. |

## Database Commands

| Goal | Syntax | Example | Notes |
| --- | --- | --- | --- |
| Create database | `CREATE DATABASE database_name;` | `CREATE DATABASE students;` | SQL command needs semicolon. |
| Rename database | `ALTER DATABASE old_name RENAME TO new_name;` | `ALTER DATABASE first_database RENAME TO mario_database;` | Used in PostgreSQL practice. |
| Drop database | `DROP DATABASE database_name;` | `DROP DATABASE second_database;` | Destructive. |
| Connect after creating | `\c database_name` | `\c universe` | `psql` command, no semicolon. |

## Table Commands

| Goal | Syntax | Example | Notes |
| --- | --- | --- | --- |
| Create empty table | `CREATE TABLE table_name();` | `CREATE TABLE students();` | Useful before adding columns step by step. |
| Create table with columns | `CREATE TABLE table_name (column TYPE, column TYPE);` | `CREATE TABLE majors (major_id SERIAL PRIMARY KEY, major VARCHAR(50) NOT NULL);` | Common final form. |
| Drop table | `DROP TABLE table_name;` | `DROP TABLE second_table;` | Destructive. |
| Drop multiple tables | `DROP TABLE table_1, table_2;` | `DROP TABLE first_table, second_table;` | Destructive. |
| View table structure | `\d table_name` | `\d majors_courses` | Use in `psql`. |

## Column Commands

| Goal | Syntax | Example | Notes |
| --- | --- | --- | --- |
| Add column | `ALTER TABLE table ADD COLUMN column TYPE;` | `ALTER TABLE students ADD COLUMN gpa NUMERIC(2,1);` | Adds a new field. |
| Add required column | `ALTER TABLE table ADD COLUMN column TYPE NOT NULL;` | `ALTER TABLE students ADD COLUMN first_name VARCHAR(50) NOT NULL;` | Existing table must support non-null data. |
| Add serial primary key | `ALTER TABLE table ADD COLUMN id SERIAL PRIMARY KEY;` | `ALTER TABLE students ADD COLUMN student_id SERIAL PRIMARY KEY;` | Auto-incrementing ID. |
| Rename column | `ALTER TABLE table RENAME COLUMN old TO new;` | `ALTER TABLE more_info RENAME COLUMN height TO height_in_cm;` | Metadata change. |
| Drop column | `ALTER TABLE table DROP COLUMN column;` | `ALTER TABLE second_table DROP COLUMN age;` | Destructive. |
| Set not null | `ALTER TABLE table ALTER COLUMN column SET NOT NULL;` | `ALTER TABLE more_info ALTER COLUMN character_id SET NOT NULL;` | Adds requirement. |

## Data Types

| Data Type | Meaning | Example | Best For |
| --- | --- | --- | --- |
| `SERIAL` | Auto-incrementing integer. | `student_id SERIAL` | Primary keys. |
| `INT` | Whole number. | `major_id INT` | Foreign keys, counts, years. |
| `VARCHAR(n)` | Text with max length. | `first_name VARCHAR(50)` | Names and short labels. |
| `VARCHAR` | Variable-length text. | `name VARCHAR` | FCC project `name` columns. |
| `TEXT` | Long text. | `description TEXT` | Descriptions. |
| `NUMERIC(p,s)` | Precise decimal. | `gpa NUMERIC(2,1)` | GPA, money-like values, measurements. |
| `NUMERIC` | Decimal without fixed precision. | `distance_from_earth_ly NUMERIC` | Large or flexible decimals. |
| `BOOLEAN` | True or false. | `has_life BOOLEAN` | Yes/no facts. |
| `DATE` | Date value. | `'1990-04-13'` | Dates. |

## Constraints and Keys

| Goal | Syntax | Example | Notes |
| --- | --- | --- | --- |
| Primary key in column | `column SERIAL PRIMARY KEY` | `course_id SERIAL PRIMARY KEY` | Most common ID pattern. |
| Add primary key later | `ALTER TABLE table ADD PRIMARY KEY(column);` | `ALTER TABLE galaxy ADD PRIMARY KEY(galaxy_id);` | Used after column exists. |
| Composite primary key | `ALTER TABLE table ADD PRIMARY KEY(col_1, col_2);` | `ALTER TABLE majors_courses ADD PRIMARY KEY(major_id, course_id);` | Junction table pattern. |
| Unique value | `ALTER TABLE table ADD UNIQUE(column);` | `ALTER TABLE galaxy ADD UNIQUE(name);` | Prevents duplicates. |
| Foreign key later | `ALTER TABLE child ADD FOREIGN KEY(column) REFERENCES parent(column);` | `ALTER TABLE students ADD FOREIGN KEY(major_id) REFERENCES majors(major_id);` | Connects child to parent. |
| Foreign key in column | `column INT REFERENCES parent(column)` | `major_id INT REFERENCES majors(major_id)` | Short form. |
| Drop constraint | `ALTER TABLE table DROP CONSTRAINT name;` | `ALTER TABLE characters DROP CONSTRAINT characters_pkey;` | Need actual constraint name. |

## Insert Data

| Goal | Syntax | Example | Notes |
| --- | --- | --- | --- |
| Insert one row | `INSERT INTO table(col_1, col_2) VALUES(value_1, value_2);` | `INSERT INTO majors(major) VALUES('Data Science');` | Text values need quotes. |
| Insert multiple rows | `INSERT INTO table(col_1, col_2) VALUES(...), (...);` | `INSERT INTO asteroid(name, diameter_in_km) VALUES('Ceres', 939.4), ('Vesta', 525.4);` | Good for seed data. |
| Insert foreign key row | `INSERT INTO child(fk_col) VALUES(parent_id);` | `INSERT INTO majors_courses(major_id, course_id) VALUES(36, 23);` | Parent row must exist. |
| Insert SQL null | `NULL` or `null` | `VALUES('Emma', 'Gilbert', null, null);` | Do not quote SQL null. |

## Update and Delete

| Goal | Syntax | Example | Notes |
| --- | --- | --- | --- |
| Update one column | `UPDATE table SET column=value WHERE condition;` | `UPDATE characters SET favorite_color='Orange' WHERE name='Daisy';` | Always use `WHERE` when targeting rows. |
| Update multiple columns | `UPDATE table SET col_1=value_1, col_2=value_2 WHERE condition;` | `UPDATE more_info SET height=160, weight=60.5 WHERE character_id=1;` | Separate assignments with commas. |
| Delete specific rows | `DELETE FROM table WHERE condition;` | `DELETE FROM students WHERE student_id=1;` | Destructive. |
| Delete all rows carefully | `TRUNCATE table;` | `TRUNCATE courses;` | Faster full-table delete. |
| Truncate related tables | `TRUNCATE table_1, table_2;` | `TRUNCATE students, majors, courses, majors_courses;` | Needed with foreign keys. |
| Truncate and reset IDs | `TRUNCATE table RESTART IDENTITY;` | `TRUNCATE students RESTART IDENTITY;` | Resets serial sequence. |

## Basic SELECT

| Goal | Syntax | Example | Notes |
| --- | --- | --- | --- |
| Select all columns | `SELECT * FROM table;` | `SELECT * FROM students;` | Quick inspection. |
| Select specific columns | `SELECT col_1, col_2 FROM table;` | `SELECT first_name, last_name FROM students;` | Cleaner output. |
| Rename output column | `SELECT column AS alias FROM table;` | `SELECT first_name AS name FROM students;` | Output label only. |
| Select unique values | `SELECT DISTINCT(column) FROM table;` | `SELECT DISTINCT(major_id) FROM students;` | Removes duplicate output values. |
| Count rows | `SELECT COUNT(*) FROM table;` | `SELECT COUNT(*) FROM students;` | Row count. |
| Limit rows | `SELECT columns FROM table LIMIT n;` | `SELECT * FROM students LIMIT 5;` | Preview data. |
| Sort ascending | `ORDER BY column ASC` | `SELECT * FROM students ORDER BY last_name ASC;` | `ASC` is default. |
| Sort descending | `ORDER BY column DESC` | `SELECT * FROM students ORDER BY gpa DESC;` | Highest first. |

## SQL Clause Order

| Clause | Purpose | Example |
| --- | --- | --- |
| `SELECT` | Choose output columns. | `SELECT first_name, gpa` |
| `FROM` | Choose source table. | `FROM students` |
| `JOIN` | Combine related tables. | `LEFT JOIN majors USING(major_id)` |
| `WHERE` | Filter rows before grouping. | `WHERE gpa IS NOT NULL` |
| `GROUP BY` | Build groups for aggregate results. | `GROUP BY major_id` |
| `HAVING` | Filter grouped results. | `HAVING COUNT(*) > 1` |
| `ORDER BY` | Sort final rows. | `ORDER BY gpa DESC` |
| `LIMIT` | Restrict row count. | `LIMIT 5` |

Pattern:

```sql
SELECT columns
FROM table
JOIN other_table ON condition
WHERE row_condition
GROUP BY grouped_columns
HAVING grouped_condition
ORDER BY sort_columns
LIMIT row_count;
```

## WHERE Conditions

| Goal | Syntax | Example | Notes |
| --- | --- | --- | --- |
| Exact match | `WHERE column = value` | `WHERE major='Data Science'` | Use quotes for text. |
| Not equal | `WHERE column != value` | `WHERE major != 'Game Design'` | Excludes exact value. |
| Greater than | `WHERE column > value` | `WHERE gpa > 3.5` | Numeric comparison. |
| Greater or equal | `WHERE column >= value` | `WHERE gpa >= 3.0` | Numeric comparison. |
| Less than | `WHERE column < value` | `WHERE gpa < 2.0` | Numeric comparison. |
| Less or equal | `WHERE column <= value` | `WHERE gpa <= 2.5` | Numeric comparison. |
| Between range | `WHERE column BETWEEN a AND b` | `WHERE gpa BETWEEN 3.0 AND 4.0` | Inclusive range. |
| Match any listed value | `WHERE column IN (...)` | `WHERE major IN ('Data Science', 'Web Development')` | Multiple accepted values. |
| Exclude listed values | `WHERE column NOT IN (...)` | `WHERE major NOT IN ('Game Design')` | Multiple excluded values. |
| Is null | `WHERE column IS NULL` | `WHERE major_id IS NULL` | Use for SQL null. |
| Is not null | `WHERE column IS NOT NULL` | `WHERE gpa IS NOT NULL` | Use for present values. |

## Text Filters with `LIKE`

| Goal | Syntax | Example | Meaning |
| --- | --- | --- | --- |
| Starts with D | `WHERE column LIKE 'D%'` | `WHERE major LIKE 'D%'` | Values beginning with `D`. |
| Ends with g | `WHERE column LIKE '%g'` | `WHERE major LIKE '%g'` | Values ending with `g`. |
| Contains Data | `WHERE column LIKE '%Data%'` | `WHERE major LIKE '%Data%'` | Values containing `Data`. |
| Case-insensitive contains | `WHERE column ILIKE '%text%'` | `WHERE major ILIKE '%data%'` | Matches `Data`, `data`, `DATA`. |
| Single unknown character | `WHERE column LIKE '_ata%'` | `WHERE major LIKE '_ata%'` | `_` matches one character. |
| Alphabetically before D | `WHERE column < 'D'` | `WHERE last_name < 'D'` | Text sorted before `D`. |
| Alphabetically from D onward | `WHERE column >= 'D'` | `WHERE last_name >= 'D'` | Text sorted at or after `D`. |
| Starts with D by range | `WHERE column >= 'D' AND column < 'E'` | `WHERE major >= 'D' AND major < 'E'` | Useful alternative to `LIKE 'D%'`. |

## Combining Conditions

| Goal | Syntax | Example |
| --- | --- | --- |
| Both must be true | `WHERE condition_1 AND condition_2` | `WHERE gpa >= 3.0 AND major_id IS NOT NULL` |
| One can be true | `WHERE condition_1 OR condition_2` | `WHERE major='Data Science' OR major='Web Development'` |
| Reverse a condition | `WHERE NOT condition` | `WHERE NOT major='Game Design'` |
| Group logic | `WHERE (condition_1 OR condition_2) AND condition_3` | `WHERE (major='Data Science' OR major='Web Development') AND gpa >= 3.0` |

## Aggregates and Grouping

| Goal | Syntax | Example | Notes |
| --- | --- | --- | --- |
| Count rows | `COUNT(*)` | `SELECT COUNT(*) FROM students;` | All rows. |
| Count non-null values | `COUNT(column)` | `SELECT COUNT(major_id) FROM students;` | Ignores null values in that column. |
| Average | `AVG(column)` | `SELECT AVG(gpa) FROM students;` | Ignores null values. |
| Minimum | `MIN(column)` | `SELECT MIN(gpa) FROM students;` | Lowest value. |
| Maximum | `MAX(column)` | `SELECT MAX(gpa) FROM students;` | Highest value. |
| Sum | `SUM(column)` | `SELECT SUM(major_id) FROM students;` | Adds numeric values. |
| Round value | `ROUND(value, decimals)` | `SELECT ROUND(AVG(gpa), 2) FROM students;` | Controls decimal places. |
| Round up | `CEIL(value)` | `SELECT CEIL(AVG(major_id)) FROM students;` | Nearest integer upward. |
| Round down | `FLOOR(value)` | `SELECT FLOOR(AVG(major_id)) FROM students;` | Nearest integer downward. |
| Group rows | `GROUP BY column` | `SELECT major_id, COUNT(*) FROM students GROUP BY major_id;` | One result per group. |
| Filter groups | `HAVING aggregate_condition` | `SELECT major_id, COUNT(*) FROM students GROUP BY major_id HAVING COUNT(*) > 3;` | `WHERE` filters rows, `HAVING` filters groups. |

## Joins

| Goal | Syntax | Example | Notes |
| --- | --- | --- | --- |
| Inner join | `FROM a JOIN b ON a.id = b.a_id` | `FROM students JOIN majors ON students.major_id = majors.major_id` | Keeps only matched rows. |
| Join with `USING` | `JOIN table USING(column)` | `LEFT JOIN majors USING(major_id)` | Works when both tables share column name. |
| Left join | `FROM a LEFT JOIN b ON ...` | `FROM students LEFT JOIN majors USING(major_id)` | Keeps all rows from left table. |
| Right join | `FROM a RIGHT JOIN b ON ...` | `FROM students RIGHT JOIN majors USING(major_id)` | Keeps all rows from right table. |
| Full join | `FROM a FULL JOIN b ON ...` | `FROM characters FULL JOIN more_info ON characters.character_id = more_info.character_id` | Keeps rows from both tables. |
| Join through junction | `a JOIN junction JOIN b` | See below | Many-to-many query. |
| Alias table | `FROM table AS alias` | `FROM students AS s` | Shortens long queries. |

Student-major query:

```sql
SELECT first_name, last_name, major, gpa
FROM students
LEFT JOIN majors USING(major_id)
ORDER BY student_id;
```

Major-course query:

```sql
SELECT major, course
FROM majors
JOIN majors_courses USING(major_id)
JOIN courses USING(course_id)
ORDER BY major, course;
```

Four-table student-course query:

```sql
SELECT first_name, last_name, major, course
FROM students
FULL JOIN majors USING(major_id)
FULL JOIN majors_courses USING(major_id)
FULL JOIN courses USING(course_id);
```

## Text Concatenation

Use concatenation when a condition needs to search combined text from multiple
columns.

| Goal | Pattern | Example |
| --- | --- | --- |
| Combine two columns | Use the SQL concatenation operator between columns. | See code block below. |
| Add a space between values | Concatenate a literal space between two columns. | See code block below. |
| Search combined values | Wrap the combined expression in a `WHERE` condition. | See code block below. |

Examples:

```sql
SELECT first_name || major
FROM students
FULL JOIN majors USING(major_id);
```

```sql
SELECT first_name || ' ' || last_name
FROM students;
```

```sql
SELECT first_name, major
FROM students
FULL JOIN majors USING(major_id)
WHERE (first_name || major) ILIKE '%ri%';
```

## Part 2 Report Query Patterns

| Report Goal | Query Pattern |
| --- | --- |
| Students with a 4.0 GPA | `SELECT first_name, last_name, gpa FROM students WHERE gpa = 4.0;` |
| Courses before D | `SELECT course FROM courses WHERE course < 'D';` |
| Last names R or later with GPA condition | `WHERE last_name >= 'R' AND (gpa > 3.8 OR gpa < 2.0)` |
| Last name contains case-insensitive `sa` | `WHERE last_name ILIKE '%sa%'` |
| Second-to-last letter is `r` | `WHERE last_name LIKE '%r_'` |
| No selected major | `WHERE major_id IS NULL` |
| Reverse alphabetical top five | `ORDER BY course DESC LIMIT 5` |
| Rounded average GPA | `SELECT ROUND(AVG(gpa), 2) FROM students;` |
| Grouped student count | `GROUP BY major_id HAVING COUNT(*) > 1` |
| Major with no students | `LEFT JOIN students ... WHERE student_id IS NULL` |
| Unique courses | `SELECT DISTINCT(course)` |
| Course with one student | `GROUP BY course HAVING COUNT(student_id) = 1` |

## Relationship Patterns

| Relationship | Table Design | Example |
| --- | --- | --- |
| One-to-one | One table has a unique foreign key to another. | `characters` to `more_info`. |
| One-to-many | Child table stores parent primary key as foreign key. | `students.major_id` references `majors.major_id`. |
| Many-to-many | Junction table stores two foreign keys. | `majors_courses(major_id, course_id)`. |

## `psql` from Bash

| Goal | Syntax | Example |
| --- | --- | --- |
| Store command | `PSQL="psql ... -c"` | `PSQL="psql -X --username=freecodecamp --dbname=students --no-align --tuples-only -c"` |
| Run query | `$PSQL "SQL"` | `$PSQL "SELECT * FROM majors"` |
| Capture query result | `VAR=$($PSQL "SQL")` | `MAJOR_ID=$($PSQL "SELECT major_id FROM majors WHERE major='$MAJOR'")` |
| Insert from Bash variable | `VALUES('$TEXT', $NUMBER)` | `VALUES('$FIRST', '$LAST', $MAJOR_ID, $GPA)` |

## Import and Export

| Goal | Syntax | Example | Notes |
| --- | --- | --- | --- |
| Export full database | `pg_dump --clean --create --inserts --username=user database > file.sql` | `pg_dump --clean --create --inserts --username=freecodecamp students > students.sql` | Produces SQL rebuild file. |
| Restore dump | `psql -U user < file.sql` | `psql -U postgres < students.sql` | User depends on environment. |
| Redirect output to file | `command > file` | `pg_dump ... > students.sql` | Overwrites file. |
| Append output to file | `command >> file` | `echo "text" >> notes.txt` | Adds to end. |

## Common Fixes

| Problem | Likely Cause | Fix |
| --- | --- | --- |
| `syntax error at or near` | Missing comma, semicolon, or wrong SQL order. | Recheck the exact SQL statement. |
| Foreign key insert fails | Referenced parent row does not exist. | Insert parent row first. |
| Duplicate key error | Same primary key or composite key already exists. | Check existing row before inserting. |
| Null check does not work | Used `= null`. | Use `IS NULL` or `IS NOT NULL`. |
| Text search misses case variants | Used `LIKE` when case differs. | Use `ILIKE`. |
| IDs do not restart after truncate | Sequence was not reset. | Use `TRUNCATE table RESTART IDENTITY;` when needed. |
| CSV `null` stored as text | Quoted `'null'`. | Insert unquoted `null`. |
