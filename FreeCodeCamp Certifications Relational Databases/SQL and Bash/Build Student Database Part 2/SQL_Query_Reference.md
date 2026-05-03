# SQL Query Reference

This reference documents the SQL query patterns practiced in **Build a Student
Database: Part 2**.

Part 1 focused on schema design and data import. Part 2 focuses on asking
questions from the database with `SELECT`, filtering, sorting, aggregates,
grouping, joins, and report-style Bash output.

## Query Structure

| Goal | Syntax | Example |
| --- | --- | --- |
| Select everything | `SELECT * FROM table;` | `SELECT * FROM students;` |
| Select specific columns | `SELECT column_1, column_2 FROM table;` | `SELECT first_name, last_name FROM students;` |
| Filter rows | `SELECT columns FROM table WHERE condition;` | `SELECT first_name, gpa FROM students WHERE gpa = 4.0;` |
| Sort rows | `SELECT columns FROM table ORDER BY column;` | `SELECT course FROM courses ORDER BY course;` |
| Limit rows | `SELECT columns FROM table LIMIT number;` | `SELECT course FROM courses LIMIT 5;` |

Full clause order:

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

## Numeric Filters

| Goal | Syntax | Example |
| --- | --- | --- |
| Equal to a number | `WHERE column = number` | `WHERE gpa = 4.0` |
| Not equal to a number | `WHERE column != number` | `WHERE gpa != 4.0` |
| Less than | `WHERE column < number` | `WHERE gpa < 2.5` |
| Less than or equal | `WHERE column <= number` | `WHERE gpa <= 2.5` |
| Greater than | `WHERE column > number` | `WHERE gpa > 3.8` |
| Greater than or equal | `WHERE column >= number` | `WHERE gpa >= 3.8` |
| Between two values | `WHERE column BETWEEN low AND high` | `WHERE gpa BETWEEN 3.0 AND 4.0` |

Example:

```sql
SELECT first_name, last_name, gpa
FROM students
WHERE gpa >= 3.8;
```

## Text Filters

| Goal | Syntax | Example |
| --- | --- | --- |
| Exact text | `WHERE column = 'text'` | `WHERE major = 'Game Design'` |
| Not exact text | `WHERE column != 'text'` | `WHERE major != 'Game Design'` |
| Alphabetically after text | `WHERE column > 'text'` | `WHERE major > 'Game Design'` |
| Alphabetically at or after text | `WHERE column >= 'text'` | `WHERE last_name >= 'R'` |
| Alphabetically before letter | `WHERE column < 'letter'` | `WHERE course < 'D'` |
| Alphabetically before next letter | `WHERE column >= 'D' AND column < 'E'` | `WHERE major >= 'D' AND major < 'E'` |

Text comparisons are useful when filtering by alphabetical order.

## Pattern Matching with `LIKE`

| Goal | Syntax | Example | Meaning |
| --- | --- | --- | --- |
| Starts with text | `WHERE column LIKE 'text%'` | `WHERE course LIKE 'Web%'` | Any value beginning with `Web`. |
| Ends with text | `WHERE column LIKE '%text'` | `WHERE course LIKE '%s'` | Any value ending with `s`. |
| Contains text | `WHERE column LIKE '%text%'` | `WHERE course LIKE '%Algorithms%'` | Any value containing `Algorithms`. |
| Exact unknown first character | `WHERE column LIKE '_text%'` | `WHERE course LIKE '_e%'` | Second character is `e`. |
| Contains a space | `WHERE column LIKE '% %'` | `WHERE course LIKE '% %'` | Values with a space. |
| Does not contain a space | `WHERE column NOT LIKE '% %'` | `WHERE course NOT LIKE '% %'` | Values without spaces. |

Wildcard meaning:

| Symbol | Meaning |
| --- | --- |
| `%` | Any number of characters, including zero. |
| `_` | Exactly one character. |

## Case-Insensitive Pattern Matching with `ILIKE`

| Goal | Syntax | Example |
| --- | --- | --- |
| Case-insensitive contains | `WHERE column ILIKE '%text%'` | `WHERE last_name ILIKE '%sa%'` |
| Case-insensitive starts with | `WHERE column ILIKE 'text%'` | `WHERE first_name ILIKE 'ma%'` |
| Case-insensitive not contains | `WHERE column NOT ILIKE '%text%'` | `WHERE course NOT ILIKE '%a%'` |

Use `LIKE` when case matters. Use `ILIKE` when case should not matter.

## Combining Conditions

| Goal | Syntax | Example |
| --- | --- | --- |
| Both conditions must be true | `WHERE condition_1 AND condition_2` | `WHERE major_id IS NULL AND gpa > 3.0` |
| Either condition can be true | `WHERE condition_1 OR condition_2` | `WHERE first_name LIKE 'D%' OR gpa > 3.0` |
| Group condition logic | `WHERE condition_1 AND (condition_2 OR condition_3)` | `WHERE last_name >= 'R' AND (gpa > 3.8 OR gpa < 2.0)` |

Parentheses are important when mixing `AND` and `OR`.

Without parentheses:

```sql
WHERE last_name >= 'R' AND gpa > 3.8 OR gpa < 2.0
```

The final `OR` can include rows with low GPA even if the last name does not
match the intended range.

With parentheses:

```sql
WHERE last_name >= 'R'
  AND (gpa > 3.8 OR gpa < 2.0)
```

The last-name condition applies to both GPA conditions.

## Null Checks

| Goal | Syntax | Example |
| --- | --- | --- |
| Column is null | `WHERE column IS NULL` | `WHERE major_id IS NULL` |
| Column is not null | `WHERE column IS NOT NULL` | `WHERE gpa IS NOT NULL` |
| Null plus another condition | `WHERE column IS NULL AND condition` | `WHERE major_id IS NULL AND gpa > 3.0` |

Do not use `= NULL`.

Incorrect:

```sql
WHERE major_id = NULL
```

Correct:

```sql
WHERE major_id IS NULL
```

## Sorting and Limiting

| Goal | Syntax | Example |
| --- | --- | --- |
| Sort ascending | `ORDER BY column` | `ORDER BY course` |
| Sort ascending explicitly | `ORDER BY column ASC` | `ORDER BY gpa ASC` |
| Sort descending | `ORDER BY column DESC` | `ORDER BY course DESC` |
| Sort by multiple columns | `ORDER BY column_1 DESC, column_2` | `ORDER BY gpa DESC, first_name` |
| Limit rows | `LIMIT number` | `LIMIT 5` |

Example:

```sql
SELECT course
FROM courses
WHERE course LIKE '_e%' OR course LIKE '%s'
ORDER BY course DESC
LIMIT 5;
```

`WHERE` comes before `ORDER BY`, and `LIMIT` comes after `ORDER BY`.

## Aggregate Functions

| Goal | Syntax | Example |
| --- | --- | --- |
| Minimum value | `MIN(column)` | `SELECT MIN(gpa) FROM students;` |
| Maximum value | `MAX(column)` | `SELECT MAX(gpa) FROM students;` |
| Sum values | `SUM(column)` | `SELECT SUM(major_id) FROM students;` |
| Average value | `AVG(column)` | `SELECT AVG(gpa) FROM students;` |
| Count all rows | `COUNT(*)` | `SELECT COUNT(*) FROM students;` |
| Count non-null values | `COUNT(column)` | `SELECT COUNT(major_id) FROM students;` |

Important difference:

- `COUNT(*)` counts rows.
- `COUNT(column)` counts only rows where that column is not `NULL`.

## Rounding Functions

| Goal | Syntax | Example |
| --- | --- | --- |
| Round up | `CEIL(number)` | `SELECT CEIL(AVG(major_id)) FROM students;` |
| Round down | `FLOOR(number)` | `SELECT FLOOR(AVG(major_id)) FROM students;` |
| Round to nearest whole number | `ROUND(number)` | `SELECT ROUND(AVG(major_id)) FROM students;` |
| Round to decimal places | `ROUND(number, decimal_places)` | `SELECT ROUND(AVG(gpa), 2) FROM students;` |

Example:

```sql
SELECT ROUND(AVG(gpa), 2)
FROM students;
```

## Aliases with `AS`

| Goal | Syntax | Example |
| --- | --- | --- |
| Rename output column | `SELECT expression AS alias` | `SELECT COUNT(*) AS number_of_students FROM students;` |
| Rename aggregate output | `SELECT ROUND(AVG(gpa), 2) AS average_gpa` | `SELECT ROUND(AVG(gpa), 2) AS average_gpa FROM students;` |
| Rename table | `FROM table AS alias` | `FROM students AS s` |

Column aliases make report output easier to understand.

Table aliases make long join queries easier to write.

## Distinct Values

| Goal | Syntax | Example |
| --- | --- | --- |
| Unique values | `SELECT DISTINCT(column) FROM table;` | `SELECT DISTINCT(major_id) FROM students;` |
| Unique joined values | `SELECT DISTINCT(column) FROM joined_tables;` | `SELECT DISTINCT(course) FROM students RIGHT JOIN majors USING(major_id) ...` |

Use `DISTINCT` when duplicates are possible but only unique results should be
shown.

## Grouping with `GROUP BY`

| Goal | Syntax | Example |
| --- | --- | --- |
| Group by one column | `GROUP BY column` | `GROUP BY major_id` |
| Count rows per group | `SELECT column, COUNT(*) FROM table GROUP BY column;` | `SELECT major_id, COUNT(*) FROM students GROUP BY major_id;` |
| Aggregate per group | `SELECT column, MIN(value), MAX(value) FROM table GROUP BY column;` | `SELECT major_id, MIN(gpa), MAX(gpa) FROM students GROUP BY major_id;` |

Rule:

Every non-aggregated column in `SELECT` must appear in `GROUP BY`.

Correct:

```sql
SELECT major_id, COUNT(*)
FROM students
GROUP BY major_id;
```

Incorrect:

```sql
SELECT major_id, first_name, COUNT(*)
FROM students
GROUP BY major_id;
```

`first_name` is neither grouped nor aggregated.

## Filtering Groups with `HAVING`

| Goal | Syntax | Example |
| --- | --- | --- |
| Keep groups by count | `HAVING COUNT(*) > number` | `HAVING COUNT(*) > 1` |
| Keep groups by max value | `HAVING MAX(column) = value` | `HAVING MAX(gpa) = 4.0` |
| Keep groups by exact count | `HAVING COUNT(column) = number` | `HAVING COUNT(student_id) = 1` |

Example:

```sql
SELECT major_id,
       COUNT(*) AS number_of_students,
       ROUND(AVG(gpa), 2) AS average_gpa
FROM students
GROUP BY major_id
HAVING COUNT(*) > 1;
```

Use `WHERE` before grouping. Use `HAVING` after grouping.

## Join Types

| Join Type | Syntax | Keeps |
| --- | --- | --- |
| `INNER JOIN` | `FROM a INNER JOIN b ON a.id = b.id` | Only matching rows from both tables. |
| `LEFT JOIN` | `FROM a LEFT JOIN b ON a.id = b.id` | All rows from the left table, matched rows from the right table. |
| `RIGHT JOIN` | `FROM a RIGHT JOIN b ON a.id = b.id` | All rows from the right table, matched rows from the left table. |
| `FULL JOIN` | `FROM a FULL JOIN b ON a.id = b.id` | All rows from both tables, matched or unmatched. |

Student-major example:

```sql
SELECT first_name, last_name, major, gpa
FROM students
LEFT JOIN majors ON students.major_id = majors.major_id;
```

## Joining with `USING`

Use `USING(column)` when both joined tables have the same column name.

| Goal | Syntax | Example |
| --- | --- | --- |
| Join by shared column | `JOIN table USING(column)` | `FULL JOIN majors USING(major_id)` |
| Continue through junction table | `JOIN junction USING(shared_column)` | `JOIN majors_courses USING(major_id)` |
| Join to final table | `JOIN table USING(other_shared_column)` | `JOIN courses USING(course_id)` |

Example:

```sql
SELECT *
FROM students
FULL JOIN majors USING(major_id)
FULL JOIN majors_courses USING(major_id)
FULL JOIN courses USING(course_id);
```

`USING` also avoids duplicate output columns for the shared join key.

## Table Aliases

| Goal | Syntax | Example |
| --- | --- | --- |
| Alias one table | `FROM table AS alias` | `FROM students AS s` |
| Alias joined table | `JOIN table AS alias` | `FULL JOIN majors AS m` |
| Reference aliased column | `alias.column` | `s.major_id` |

Example:

```sql
SELECT s.major_id
FROM students AS s
FULL JOIN majors AS m ON s.major_id = m.major_id;
```

Aliases are useful when:

- multiple tables have columns with the same name
- a query becomes long
- table names need to be shortened for readability

## Concatenation

Concatenation joins text values together. This section uses code blocks instead
of a Markdown table because the SQL concatenation operator contains pipe
characters.

Combine two columns:

```sql
first_name || major
```

Search combined text:

```sql
(first_name || major) ILIKE '%ri%'
```

Add a space between values:

```sql
first_name || ' ' || last_name
```

Example:

```sql
SELECT first_name, major
FROM students
FULL JOIN majors USING(major_id)
WHERE (first_name || major) ILIKE '%ri%';
```

## Part 2 Query Patterns

| Report Goal | Query Pattern |
| --- | --- |
| Students with perfect GPA | `SELECT first_name, last_name, gpa FROM students WHERE gpa = 4.0;` |
| Courses before D | `SELECT course FROM courses WHERE course < 'D';` |
| Last name range plus GPA group | `WHERE last_name >= 'R' AND (gpa > 3.8 OR gpa < 2.0)` |
| Case-insensitive name search | `WHERE last_name ILIKE '%sa%'` |
| Second-to-last character | `WHERE last_name LIKE '%r_'` |
| No major selected | `WHERE major_id IS NULL` |
| Reverse alphabetical top five | `ORDER BY course DESC LIMIT 5` |
| Rounded average GPA | `SELECT ROUND(AVG(gpa), 2) FROM students;` |
| Grouped student counts | `GROUP BY major_id HAVING COUNT(*) > 1` |
| Majors with no students | `LEFT JOIN students ... WHERE student_id IS NULL` |
| Unique courses | `SELECT DISTINCT(course)` |
| Courses with one student | `GROUP BY course HAVING COUNT(student_id) = 1` |
