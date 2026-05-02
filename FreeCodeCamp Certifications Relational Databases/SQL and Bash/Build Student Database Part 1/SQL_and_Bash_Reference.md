# SQL and Bash Reference

This reference explains the Bash and PostgreSQL syntax used in the **Build a
Student Database: Part 1** workshop.

It is intentionally detailed. The purpose is to make the workflow understandable
even when revisiting it later from a beginner perspective.

## Big Picture

The workshop combines three layers:

```text
CSV files -> Bash script -> PostgreSQL database
```

Each layer has a role:

- CSV files provide the raw data.
- Bash reads each file line by line.
- PostgreSQL stores the cleaned, relational data.

The import script acts as the bridge:

```text
read one CSV row -> query the database -> insert missing data -> repeat
```

## PostgreSQL Login and Database Commands

Log in to PostgreSQL:

```bash
psql --username=freecodecamp --dbname=postgres
```

List databases:

```sql
\l
```

Create a database:

```sql
CREATE DATABASE students;
```

Connect to a database:

```sql
\c students
```

List tables:

```sql
\d
```

View table details:

```sql
\d students
\d majors
\d courses
\d majors_courses
```

## Creating Tables

The workshop starts with empty tables:

```sql
CREATE TABLE students();
CREATE TABLE majors();
CREATE TABLE courses();
CREATE TABLE majors_courses();
```

Then columns are added with `ALTER TABLE`.

## Adding Columns

General syntax:

```sql
ALTER TABLE table_name ADD COLUMN column_name DATA_TYPE;
```

Example:

```sql
ALTER TABLE students ADD COLUMN first_name VARCHAR(50);
```

Add a required column:

```sql
ALTER TABLE students ADD COLUMN first_name VARCHAR(50) NOT NULL;
```

Add a serial primary key:

```sql
ALTER TABLE students ADD COLUMN student_id SERIAL PRIMARY KEY;
```

## Data Types Used

### `SERIAL`

```sql
student_id SERIAL PRIMARY KEY
```

`SERIAL` creates an auto-incrementing integer. It is commonly used for primary
keys.

### `VARCHAR(n)`

```sql
first_name VARCHAR(50)
course VARCHAR(100)
```

`VARCHAR(n)` stores text with a maximum length.

In this workshop:

- names and majors use `VARCHAR(50)`
- courses use `VARCHAR(100)`

### `INT`

```sql
major_id INT
course_id INT
```

`INT` stores whole numbers. It is used for foreign key columns.

### `NUMERIC(2,1)`

```sql
gpa NUMERIC(2,1)
```

`NUMERIC(2,1)` stores a number with:

- 2 total digits
- 1 digit after the decimal point

Examples:

```text
2.5
3.8
4.0
```

## Constraints

### Primary Key

A primary key uniquely identifies each row.

```sql
ALTER TABLE students ADD PRIMARY KEY(student_id);
```

With `SERIAL`, the primary key can be added directly:

```sql
ALTER TABLE students ADD COLUMN student_id SERIAL PRIMARY KEY;
```

### Foreign Key

A foreign key points to a primary key in another table.

```sql
ALTER TABLE students
ADD FOREIGN KEY(major_id)
REFERENCES majors(major_id);
```

Meaning:

- `students.major_id` must match an existing `majors.major_id`
- or it can be `NULL` if the column allows null values

### Composite Primary Key

A composite primary key uses more than one column.

```sql
ALTER TABLE majors_courses
ADD PRIMARY KEY(major_id, course_id);
```

This is used because neither `major_id` nor `course_id` is unique alone in the
junction table, but the pair should be unique.

### `NOT NULL`

`NOT NULL` means the column must always have a value.

```sql
first_name VARCHAR(50) NOT NULL
```

This is used for student names, majors, and courses because those values are
required in their tables.

## Normalization

Normalization means organizing data to reduce repetition and make relationships
clear.

Instead of storing the major name repeatedly in every student row, the database
stores:

```text
majors.major_id
majors.major
students.major_id
```

This avoids repeated major text and makes relationships easier to maintain.

## One-to-Many Relationship

One major can have many students.

```text
majors.major_id -> students.major_id
```

Example:

```text
Database Administration -> Rhea Kellems
Database Administration -> Jimmy Felipe
Database Administration -> Maxine Hagenes
```

The foreign key is stored in the `students` table because each student has at
most one major.

## Many-to-Many Relationship

One major can have many courses, and one course can belong to many majors.

This requires a junction table:

```text
majors_courses
```

Example:

```text
Database Administration -> SQL
Database Administration -> Database Systems
Data Science -> SQL
```

The junction table stores IDs, not repeated text:

```sql
major_id INT REFERENCES majors(major_id),
course_id INT REFERENCES courses(course_id)
```

## Inserting Rows

Insert one major:

```sql
INSERT INTO majors(major)
VALUES('Database Administration');
```

Insert one course:

```sql
INSERT INTO courses(course)
VALUES('Data Structures and Algorithms');
```

Insert one major-course relationship:

```sql
INSERT INTO majors_courses(major_id, course_id)
VALUES(1, 1);
```

Insert one student:

```sql
INSERT INTO students(first_name, last_name, major_id, gpa)
VALUES('Rhea', 'Kellems', 1, 2.5);
```

Important rule:

- text values need single quotes
- numeric values do not need quotes
- SQL `NULL` should not be quoted

Correct:

```sql
VALUES('Emma', 'Gilbert', null, null);
```

Incorrect:

```sql
VALUES('Emma', 'Gilbert', 'null', 'null');
```

## Selecting Rows

Select all rows:

```sql
SELECT * FROM students;
```

Select one column:

```sql
SELECT major FROM majors;
```

Select with a condition:

```sql
SELECT major_id FROM majors WHERE major='Data Science';
```

Count rows:

```sql
SELECT COUNT(*) FROM students;
```

## Joining Tables

Join students to majors:

```sql
SELECT first_name, last_name, major, gpa
FROM students
LEFT JOIN majors USING(major_id);
```

Why `LEFT JOIN` is useful here:

- some students have no major
- `LEFT JOIN` keeps those students in the result
- their major appears as `NULL`

Join majors to courses through the junction table:

```sql
SELECT major, course
FROM majors
JOIN majors_courses USING(major_id)
JOIN courses USING(course_id);
```

This shows readable major-course pairs instead of only ID numbers.

## Truncating Tables

`TRUNCATE` removes all rows from a table.

```sql
TRUNCATE students;
```

When foreign keys are involved, related tables may need to be truncated
together:

```sql
TRUNCATE students, majors, courses, majors_courses;
```

This works because all related tables are included in the same statement.

Important note:

`TRUNCATE` does not reset `SERIAL` sequences unless `RESTART IDENTITY` is used.
That is why final IDs in the dump may not start at `1`.

## Bash Script Foundation

Every Bash script starts with:

```bash
#!/bin/bash
```

Make it executable:

```bash
chmod +x insert_data.sh
```

Run it:

```bash
./insert_data.sh
```

## Bash Variables

Create a variable:

```bash
MAJOR="Data Science"
```

Use a variable:

```bash
echo "$MAJOR"
```

No spaces are allowed around `=`.

Correct:

```bash
MAJOR="Data Science"
```

Incorrect:

```bash
MAJOR = "Data Science"
```

## The `PSQL` Variable

The script stores the reusable PostgreSQL command in a variable:

```bash
PSQL="psql -X --username=freecodecamp --dbname=students --no-align --tuples-only -c"
```

Then it can run SQL like this:

```bash
$PSQL "SELECT * FROM majors"
```

Or capture the result:

```bash
MAJOR_ID=$($PSQL "SELECT major_id FROM majors WHERE major='$MAJOR'")
```

The outer `$()` is command substitution. It runs the command and stores its
output in the variable.

## Command Substitution

Command substitution syntax:

```bash
VARIABLE=$(command)
```

Example:

```bash
CURRENT_DATE=$(date)
```

In this workshop:

```bash
MAJOR_ID=$($PSQL "SELECT major_id FROM majors WHERE major='$MAJOR'")
```

How to read it:

1. Run the SQL query with `psql`.
2. Capture the query result.
3. Store the result in `MAJOR_ID`.

## Reading CSV Files in Bash

The basic pattern:

```bash
cat courses.csv | while IFS="," read MAJOR COURSE
do
  echo "$MAJOR - $COURSE"
done
```

What happens:

1. `cat courses.csv` prints the file.
2. The pipe sends that output into the `while` loop.
3. `IFS=","` tells Bash to split each line by commas.
4. `read MAJOR COURSE` stores each column into variables.
5. The loop runs once per line.

## Why `IFS` Matters

`IFS` means Internal Field Separator.

By default, Bash splits text on:

- spaces
- tabs
- new lines

CSV files use commas, so the script changes `IFS` for the `read` command:

```bash
IFS=","
```

Without this, `Database Administration` would be split incorrectly because it
contains a space.

## Skipping CSV Headers

CSV files usually have a header row:

```csv
major,course
```

The script skips it:

```bash
if [[ $MAJOR != major ]]
then
  # process real rows only
fi
```

For `students.csv`:

```bash
if [[ $FIRST != first_name ]]
then
  # process real rows only
fi
```

## Checking for Empty Values

Use `-z` to check whether a variable is empty.

```bash
if [[ -z $MAJOR_ID ]]
then
  echo "Major was not found"
fi
```

Meaning:

- `-z` returns true if the variable has zero length
- this is used after a `SELECT` query
- if the query returns nothing, the row does not exist yet

## Lookup-Then-Insert Workflow

This is the most important pattern in the script.

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

Beginner explanation:

1. Try to find the major.
2. If it is not found, insert it.
3. Confirm the insert worked.
4. Query again to get the new ID.

The same pattern is used for courses.

## Insert Result Check

PostgreSQL returns this message after a successful insert:

```text
INSERT 0 1
```

The script checks for it:

```bash
if [[ $INSERT_MAJOR_RESULT == "INSERT 0 1" ]]
then
  echo "Inserted into majors, $MAJOR"
fi
```

This makes script output easier to follow.

## Handling `null` from CSV

The CSV file uses the text `null` to represent missing values.

For a missing major, the query returns no `major_id`:

```bash
MAJOR_ID=$($PSQL "SELECT major_id FROM majors WHERE major='$MAJOR'")
```

If no ID is found:

```bash
if [[ -z $MAJOR_ID ]]
then
  MAJOR_ID=null
fi
```

Then the insert uses `$MAJOR_ID` without quotes:

```bash
VALUES('$FIRST', '$LAST', $MAJOR_ID, $GPA)
```

This lets PostgreSQL receive actual SQL `NULL`.

## Quoting Rules in the Insert Script

Text values are quoted in SQL:

```bash
'$FIRST'
'$LAST'
'$MAJOR'
'$COURSE'
```

ID and numeric values are not quoted:

```bash
$MAJOR_ID
$COURSE_ID
$GPA
```

Reason:

- first names, last names, majors, and courses are text
- IDs are integers
- GPA is numeric
- `null` must remain unquoted to become SQL `NULL`

## Exporting with `pg_dump`

Final dump command:

```bash
pg_dump --clean --create --inserts --username=freecodecamp students > students.sql
```

What each part means:

- `pg_dump` exports a PostgreSQL database.
- `--clean` includes drop commands before create commands.
- `--create` includes the database creation command.
- `--inserts` exports row data as `INSERT` statements.
- `--username=freecodecamp` runs the command as the workshop user.
- `students` is the database name.
- `> students.sql` redirects the output into a file.

## Rebuilding from `students.sql`

A dump file can be used to rebuild the database:

```bash
psql -U postgres < students.sql
```

In the freeCodeCamp environment, the exact user may differ depending on the
workspace context. The important point is that `students.sql` contains the SQL
commands required to recreate the database.

## Common Beginner Mistakes

### Missing Space After the `PSQL` Variable

Incorrect:

```bash
$($PSQL"TRUNCATE students")
```

Correct:

```bash
$($PSQL "TRUNCATE students")
```

The space matters because the SQL query must be passed as a separate argument to
`psql`.

### Quoting SQL `null`

Incorrect:

```sql
VALUES('Emma', 'Gilbert', 'null', 'null');
```

Correct:

```sql
VALUES('Emma', 'Gilbert', null, null);
```

Quoted `'null'` is text. Unquoted `null` is SQL `NULL`.

### Forgetting `IFS=","`

Incorrect:

```bash
cat courses.csv | while read MAJOR COURSE
```

Correct:

```bash
cat courses.csv | while IFS="," read MAJOR COURSE
```

Without `IFS=","`, Bash splits on spaces and breaks values such as
`Database Administration`.

### Inserting Relationship Rows Before Lookup Rows

Incorrect order:

```text
insert majors_courses first
insert majors later
insert courses later
```

Correct order:

```text
insert majors
insert courses
insert majors_courses
```

Foreign keys require referenced rows to exist before relationship rows are
inserted.

### Expecting IDs to Restart After `TRUNCATE`

`TRUNCATE` removes rows, but it does not reset serial counters by default.

If reset behavior is needed, use:

```sql
TRUNCATE students, majors, courses, majors_courses RESTART IDENTITY;
```

The workshop does not require this reset because the final relationships remain
valid.

## Debugging Checklist

If the import script fails, check these items:

1. Is the database named `students` created?
2. Are the tables created with the expected columns?
3. Is the script executable?
4. Does the `PSQL` variable use the correct database name?
5. Is there a space between `$PSQL` and the SQL query?
6. Is `IFS=","` used before `read`?
7. Is the header row skipped?
8. Are text values quoted in SQL?
9. Are numeric and `null` values unquoted?
10. Are parent tables inserted before foreign key tables?

## Final Mental Model

Read the script in this order:

1. The `PSQL` variable defines how Bash talks to PostgreSQL.
2. `TRUNCATE` clears the tables.
3. The first loop reads `courses.csv`.
4. Each major is looked up or inserted.
5. Each course is looked up or inserted.
6. Each major-course relationship is inserted.
7. The second loop reads `students.csv`.
8. Each student's major is converted into a `major_id`.
9. Missing majors become SQL `NULL`.
10. Student rows are inserted.
11. `pg_dump` exports the finished database to `students.sql`.

That is the core workflow:

```text
CSV text -> Bash variables -> SQL commands -> relational tables -> SQL dump
```
