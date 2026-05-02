# Build a Student Database: Part 1

## Context

This document summarizes the **Build a Student Database: Part 1** workshop from
the freeCodeCamp Relational Databases Certification track.

The workshop was completed in **GitHub Codespaces** through the CodeRoad
extension. The original lesson is interactive and step-based, so this repository
keeps a cleaned learning record instead of raw copied prompts from the CodeRoad
interface.

The goal of this note is to make the workshop reproducible and understandable:
what database was built, how the CSV files were imported, how Bash was used to
run SQL commands, and how the final `students.sql` dump can rebuild the
database.

## Workshop Goal

Create a PostgreSQL database named `students`, then write a Bash script that
reads two CSV files and inserts the data into normalized relational tables.

The workshop focuses on:

- creating a PostgreSQL database
- designing normalized tables
- using primary keys and foreign keys
- using a junction table for a many-to-many relationship
- reading CSV files in Bash
- changing `IFS` so Bash reads comma-separated values correctly
- using `psql` from inside a Bash script
- using command substitution to capture SQL results
- inserting only missing lookup rows
- handling `null` values from CSV data
- exporting the final database with `pg_dump`

## Environment

- Platform: freeCodeCamp Relational Databases Certification
- Workspace: GitHub Codespaces
- Tutorial runner: CodeRoad
- Shell: Bash
- Database system: PostgreSQL
- Database client: `psql`
- Database user: `freecodecamp`

## Final Files

| File | Purpose |
| --- | --- |
| `courses.csv` | Source CSV containing major-course relationships. |
| `students.csv` | Source CSV containing student records. |
| `insert_data.sh` | Bash script that imports both CSV files into PostgreSQL. |
| `students.sql` | PostgreSQL dump that can recreate the completed database. |
| `Build_Student_Database_Part_1.md` | Cleaned workshop documentation. |
| `Database_Blueprint.md` | Schema and relationship reference for the database. |
| `SQL_and_Bash_Reference.md` | Detailed syntax reference for the SQL and Bash concepts used. |

## Source Data

### `courses.csv`

The file contains two columns:

```csv
major,course
Database Administration,Data Structures and Algorithms
Web Development,Web Programming
```

This file does not store one entity only. Each row describes a relationship:
one major includes one course.

The final import produces:

- 7 unique majors
- 17 unique courses
- 28 major-course relationships

### `students.csv`

The file contains four columns:

```csv
first_name,last_name,major,gpa
Rhea,Kellems,Database Administration,2.5
Emma,Gilbert,null,null
```

The final import produces 31 student rows.

Some students have `null` as their major or GPA. In the database, those values
must be inserted as SQL `NULL`, not as the text string `'null'`.

## Database Design

The workshop uses four tables:

| Table | Purpose |
| --- | --- |
| `students` | Stores student names, optional major references, and GPA values. |
| `majors` | Stores one row for each unique major. |
| `courses` | Stores one row for each unique course. |
| `majors_courses` | Connects majors and courses. |

The relationship structure is:

```text
majors 1 ---- many students
majors many ---- many courses
```

The many-to-many relationship between majors and courses is modeled through the
`majors_courses` junction table.

## Why the Junction Table Is Needed

A major can include many courses:

```text
Database Administration -> SQL
Database Administration -> Database Systems
Database Administration -> Web Applications
```

A course can also belong to many majors:

```text
Data Structures and Algorithms -> Database Administration
Data Structures and Algorithms -> Data Science
Data Structures and Algorithms -> Web Development
```

That is a many-to-many relationship. A single foreign key column cannot model it
cleanly without repeating data or creating multiple course columns.

The normalized solution is:

```text
majors
courses
majors_courses
```

Each row in `majors_courses` stores one valid pair:

```text
major_id + course_id
```

Together, those two columns form a composite primary key so the same pair cannot
be inserted twice.

## Manual Database Setup

Log in to PostgreSQL:

```bash
psql --username=freecodecamp --dbname=postgres
```

Create and connect to the database:

```sql
CREATE DATABASE students;
\c students
```

Create the base tables:

```sql
CREATE TABLE students();
CREATE TABLE majors();
CREATE TABLE courses();
CREATE TABLE majors_courses();
```

The workshop first creates empty tables, then adds columns and constraints with
`ALTER TABLE`.

## Final Schema

### `students`

```sql
CREATE TABLE students (
  student_id SERIAL PRIMARY KEY,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  major_id INT REFERENCES majors(major_id),
  gpa NUMERIC(2,1)
);
```

Notes:

- `student_id` is the primary key.
- `first_name` and `last_name` are required.
- `major_id` can be `NULL` because some students have no major in the CSV.
- `gpa` can be `NULL` because some students have no GPA in the CSV.

### `majors`

```sql
CREATE TABLE majors (
  major_id SERIAL PRIMARY KEY,
  major VARCHAR(50) NOT NULL
);
```

Notes:

- One row represents one unique major.
- The script checks this table before inserting a new major.

### `courses`

```sql
CREATE TABLE courses (
  course_id SERIAL PRIMARY KEY,
  course VARCHAR(100) NOT NULL
);
```

Notes:

- One row represents one unique course.
- `VARCHAR(100)` is used because course names can be longer than student or
  major names.

### `majors_courses`

```sql
CREATE TABLE majors_courses (
  major_id INT REFERENCES majors(major_id),
  course_id INT REFERENCES courses(course_id),
  PRIMARY KEY (major_id, course_id)
);
```

Notes:

- `major_id` references `majors`.
- `course_id` references `courses`.
- The composite primary key prevents duplicate major-course pairs.

## Import Script Overview

The final script is `insert_data.sh`.

It starts by defining a reusable `psql` command:

```bash
PSQL="psql -X --username=freecodecamp --dbname=students --no-align --tuples-only -c"
```

The flags matter:

- `-X` prevents reading startup files, making script output more predictable.
- `--username=freecodecamp` selects the database user.
- `--dbname=students` connects to the target database.
- `--no-align` removes aligned table formatting.
- `--tuples-only` removes headers and row-count footers.
- `-c` runs one SQL command and exits.

The script imports `courses.csv` first because the `students` table needs
`major_id` values that come from the `majors` table.

High-level flow:

1. Truncate the target tables.
2. Read `courses.csv`.
3. Insert each missing major.
4. Insert each missing course.
5. Insert each major-course relationship.
6. Read `students.csv`.
7. Find each student's `major_id`.
8. Convert missing major IDs to SQL `NULL`.
9. Insert each student.

## CSV Reading Pattern

The script uses:

```bash
cat courses.csv | while IFS="," read MAJOR COURSE
do
  ...
done
```

Why `IFS=","` is required:

- Bash normally splits input on spaces, tabs, and new lines.
- CSV files separate columns with commas.
- Without changing `IFS`, a major such as `Database Administration` would be
  split into two words.

Using comma as the field separator allows Bash to read:

```csv
Database Administration,SQL
```

as:

```text
MAJOR="Database Administration"
COURSE="SQL"
```

## Header Row Handling

CSV files include a header row:

```csv
major,course
```

That row is not real data, so the script skips it:

```bash
if [[ $MAJOR != major ]]
then
  ...
fi
```

The students import uses the same idea:

```bash
if [[ $FIRST != first_name ]]
then
  ...
fi
```

## Lookup-Then-Insert Pattern

The script repeatedly uses this pattern:

1. Query for an existing ID.
2. If the result is empty, insert the missing row.
3. Query again to get the new ID.

Example for majors:

```bash
MAJOR_ID=$($PSQL "SELECT major_id FROM majors WHERE major='$MAJOR'")

if [[ -z $MAJOR_ID ]]
then
  INSERT_MAJOR_RESULT=$($PSQL "INSERT INTO majors(major) VALUES('$MAJOR')")

  if [[ $INSERT_MAJOR_RESULT == "INSERT 0 1" ]]
  then
    echo "Inserted into majors, $MAJOR"
  fi

  MAJOR_ID=$($PSQL "SELECT major_id FROM majors WHERE major='$MAJOR'")
fi
```

Why this is useful:

- It avoids duplicate majors.
- It keeps the database normalized.
- It gives the script the `major_id` needed for related inserts.

## Handling SQL `NULL`

In `students.csv`, some students have `null` as the major:

```csv
Emma,Gilbert,null,null
```

When the script searches for a major named `null`, no row is found in the
`majors` table. The script then sets:

```bash
MAJOR_ID=null
```

This is intentionally not quoted in the SQL insert:

```bash
VALUES('$FIRST', '$LAST', $MAJOR_ID, $GPA)
```

That allows PostgreSQL to treat it as SQL `NULL`.

The same approach works for GPA because `GPA` is also inserted without quotes.
When the CSV value is `null`, the SQL command receives `null`.

## Exporting the Database

After the import is complete, the database is exported with:

```bash
pg_dump --clean --create --inserts --username=freecodecamp students > students.sql
```

The flags mean:

- `--clean` adds commands to drop existing objects before recreating them.
- `--create` includes the `CREATE DATABASE` command.
- `--inserts` writes row data as `INSERT` statements.
- `--username=freecodecamp` selects the PostgreSQL user.
- `students` is the database being dumped.
- `> students.sql` redirects the dump output into a file.

The resulting `students.sql` file can rebuild the database.

## Final Data Counts

The final dump contains:

| Table | Rows |
| --- | ---: |
| `majors` | 7 |
| `courses` | 17 |
| `majors_courses` | 28 |
| `students` | 31 |

The sequence values in `students.sql` do not start at `1` because the workshop
included test inserts and truncation before the final import. This is not a
problem: the IDs are still valid, and the foreign key relationships match the
final data.

## Verification Queries

Useful checks after running the import:

```sql
SELECT * FROM majors;
SELECT * FROM courses;
SELECT * FROM majors_courses;
SELECT * FROM students;
```

Count rows:

```sql
SELECT COUNT(*) FROM majors;
SELECT COUNT(*) FROM courses;
SELECT COUNT(*) FROM majors_courses;
SELECT COUNT(*) FROM students;
```

Check student-major relationships:

```sql
SELECT first_name, last_name, major, gpa
FROM students
LEFT JOIN majors USING(major_id)
ORDER BY student_id;
```

Check major-course relationships:

```sql
SELECT major, course
FROM majors
JOIN majors_courses USING(major_id)
JOIN courses USING(course_id)
ORDER BY major, course;
```

## Completion Notes

This workshop connects Bash scripting and SQL in a practical way. The final
result is not only a database schema, but also an automated import script that
can rebuild the database content from CSV files.

The most important learning outcome is understanding the bridge between Bash
and PostgreSQL:

```text
CSV file -> Bash loop -> psql command -> SQL query -> PostgreSQL table
```

That flow appears repeatedly in real data-loading and automation tasks.
