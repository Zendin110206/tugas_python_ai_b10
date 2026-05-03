# Build a Student Database: Part 2

## Context

This document summarizes the **Build a Student Database: Part 2** workshop from
the freeCodeCamp Relational Databases Certification track.

The workshop was completed in **GitHub Codespaces** through the CodeRoad
extension. The original lesson is interactive and step-based, so this repository
keeps a cleaned learning record instead of raw copied prompts from the CodeRoad
interface.

Part 1 focused on building the `students` database and importing CSV data with
Bash. Part 2 uses the same database to practice deeper SQL query patterns and
build a Bash reporting script named `student_info.sh`.

## Workshop Goal

Rebuild the `students` database from the Part 1 dump, then write a Bash script
that prints useful reports by running PostgreSQL queries through `psql`.

The workshop focuses on:

- restoring a database from a `.sql` dump
- selecting specific columns
- filtering rows with `WHERE`
- comparing numbers and text
- combining conditions with `AND`, `OR`, and parentheses
- matching text with `LIKE`, `ILIKE`, and wildcards
- checking `NULL` values
- sorting with `ORDER BY`
- limiting results with `LIMIT`
- using aggregate functions such as `MIN`, `MAX`, `SUM`, `AVG`, and `COUNT`
- rounding values with `ROUND`, `CEIL`, and `FLOOR`
- grouping rows with `GROUP BY`
- filtering groups with `HAVING`
- renaming output columns with `AS`
- using `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, and `FULL JOIN`
- using table aliases
- joining related tables with `USING`
- querying many-to-many relationships through a junction table

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
| `students.sql` | Database dump from Part 1 used to rebuild the `students` database. |
| `student_info.sh` | Bash reporting script that prints query results from the database. |
| `Build_Student_Database_Part_2.md` | Cleaned workshop documentation. |
| `SQL_Query_Reference.md` | Detailed SQL query reference for the syntax practiced in Part 2. |

## Rebuild the Database

Part 2 starts from the `students.sql` dump created at the end of Part 1.

From the Bash terminal:

```bash
psql -U postgres < students.sql
```

What this does:

- reads the SQL commands stored in `students.sql`
- recreates the `students` database
- recreates the tables, sequences, constraints, and inserted rows

After rebuilding, log in to PostgreSQL:

```bash
psql --username=freecodecamp --dbname=postgres
```

Confirm the database exists:

```sql
\l
```

Connect to it:

```sql
\c students
```

Inspect the tables:

```sql
\d
\d students
SELECT * FROM students;
```

## Reporting Script Setup

Create the script:

```bash
touch student_info.sh
chmod +x student_info.sh
```

Start the script with a shebang and title:

```bash
#!/bin/bash

# Info about my computer science students from the students database

echo -e "\n~~ My Computer Science Students ~~\n"
```

Add the reusable `psql` command:

```bash
PSQL="psql -X --username=freecodecamp --dbname=students --no-align --tuples-only -c"
```

The script prints query results with this pattern:

```bash
echo "$($PSQL "SELECT ...")"
```

The outer `$()` runs the SQL command and captures the output. Quoting the whole
command substitution keeps multi-line query output readable.

## Query Report Sections

### 1. Students with a 4.0 GPA

Goal:

```text
First name, last name, and GPA of students with a 4.0 GPA.
```

Query:

```sql
SELECT first_name, last_name, gpa
FROM students
WHERE gpa = 4.0;
```

Concepts:

- selecting specific columns
- filtering numeric values with `=`

### 2. Courses Before `D`

Goal:

```text
All course names whose first letter is before D in the alphabet.
```

Query:

```sql
SELECT course
FROM courses
WHERE course < 'D';
```

Concepts:

- text comparison
- alphabetical ordering behavior in `WHERE`

### 3. Students After `R` with GPA Rules

Goal:

```text
First name, last name, and GPA of students whose last name begins with R or
after and have a GPA greater than 3.8 or less than 2.0.
```

Query:

```sql
SELECT first_name, last_name, gpa
FROM students
WHERE last_name >= 'R'
  AND (gpa > 3.8 OR gpa < 2.0);
```

Concepts:

- text comparison with `>=`
- grouped conditions with parentheses
- combining `AND` and `OR`

Parentheses are important here. Without them, the final `OR` could return rows
that do not match the intended last-name condition.

### 4. Last Name Pattern Matching

Goal:

```text
Last name of students whose last name contains a case-insensitive "sa" or has
an "r" as the second-to-last letter.
```

Query:

```sql
SELECT last_name
FROM students
WHERE last_name ILIKE '%sa%'
   OR last_name LIKE '%r_';
```

Concepts:

- `ILIKE` for case-insensitive matching
- `%` wildcard for any number of characters
- `_` wildcard for exactly one character

### 5. Students Without a Major and Extra Conditions

Goal:

```text
First name, last name, and GPA of students who have not selected a major and
either their first name begins with D or they have a GPA greater than 3.0.
```

Query:

```sql
SELECT first_name, last_name, gpa
FROM students
WHERE major_id IS NULL
  AND (first_name LIKE 'D%' OR gpa > 3.0);
```

Concepts:

- `IS NULL`
- `LIKE 'D%'`
- grouped `OR` conditions

### 6. First Five Courses by Reverse Alphabetical Order

Goal:

```text
Course name of the first five courses, in reverse alphabetical order, that have
an e as the second letter or end with s.
```

Query:

```sql
SELECT course
FROM courses
WHERE course LIKE '_e%'
   OR course LIKE '%s'
ORDER BY course DESC
LIMIT 5;
```

Concepts:

- `_` wildcard for one character
- `%` wildcard for any number of characters
- `ORDER BY ... DESC`
- `LIMIT`

### 7. Average GPA Rounded to Two Decimal Places

Goal:

```text
Average GPA of all students rounded to two decimal places.
```

Query:

```sql
SELECT ROUND(AVG(gpa), 2)
FROM students;
```

Concepts:

- `AVG`
- `ROUND(value, decimal_places)`
- aggregate functions ignoring `NULL` values

### 8. Student Counts and Average GPA by Major ID

Goal:

```text
Major ID, total number of students as number_of_students, and average GPA
rounded to two decimal places as average_gpa, for each major ID having more
than one student.
```

Query:

```sql
SELECT major_id,
       COUNT(*) AS number_of_students,
       ROUND(AVG(gpa), 2) AS average_gpa
FROM students
GROUP BY major_id
HAVING COUNT(*) > 1;
```

Concepts:

- `COUNT(*)`
- `AVG`
- `ROUND`
- `AS` aliases
- `GROUP BY`
- `HAVING`

`WHERE` filters rows before grouping. `HAVING` filters grouped results after
aggregation.

### 9. Majors with No Students or a Matching Student Name

Goal:

```text
List of majors, in alphabetical order, that either no student is taking or has a
student whose first name contains a case-insensitive "ma".
```

Query:

```sql
SELECT major
FROM majors
LEFT JOIN students ON majors.major_id = students.major_id
WHERE student_id IS NULL
   OR first_name ILIKE '%ma%'
ORDER BY major;
```

Concepts:

- `LEFT JOIN`
- filtering unmatched rows with `student_id IS NULL`
- case-insensitive text matching
- sorting

### 10. Unique Courses No Student or Obie Hilpert Is Taking

Goal:

```text
List of unique courses, in reverse alphabetical order, that no student or Obie
Hilpert is taking.
```

Query:

```sql
SELECT DISTINCT(course)
FROM students
RIGHT JOIN majors USING(major_id)
INNER JOIN majors_courses USING(major_id)
INNER JOIN courses USING(course_id)
WHERE (first_name = 'Obie' AND last_name = 'Hilpert')
   OR student_id IS NULL
ORDER BY course DESC;
```

Concepts:

- `DISTINCT`
- `RIGHT JOIN`
- `INNER JOIN`
- `USING`
- many-to-many table traversal
- filtering by a specific student or unmatched students

The join path is:

```text
students -> majors -> majors_courses -> courses
```

### 11. Courses with Only One Student Enrolled

Goal:

```text
List of courses, in alphabetical order, with only one student enrolled.
```

Query:

```sql
SELECT course
FROM students
FULL JOIN majors ON students.major_id = majors.major_id
FULL JOIN majors_courses ON majors.major_id = majors_courses.major_id
FULL JOIN courses USING(course_id)
GROUP BY course
HAVING COUNT(student_id) = 1
ORDER BY course;
```

Concepts:

- multi-table joins
- `GROUP BY`
- `HAVING COUNT(...)`
- sorted grouped output

## Query Order Reminder

SQL clauses must appear in a specific order:

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

Not every query needs every clause, but when they are used together, this order
matters.

## Completion Notes

Part 2 turns the Part 1 database into a reporting exercise. The key learning
shift is moving from "how do I insert data?" to "how do I ask the database good
questions?"

The main pattern is:

```text
Bash script -> psql command -> SELECT query -> readable report output
```

This is a useful foundation for command-line reporting, database inspection,
and small automation scripts.
