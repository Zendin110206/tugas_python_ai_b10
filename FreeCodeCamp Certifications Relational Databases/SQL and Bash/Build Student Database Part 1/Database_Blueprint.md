# Student Database Blueprint

This file documents the schema design for the **Build a Student Database:
Part 1** workshop.

It is a compact reference for the final database structure, the data sources,
and the relationships between tables.

## Database Name

```sql
students
```

## Source Files

| File | Role |
| --- | --- |
| `courses.csv` | Provides major-course pairs. |
| `students.csv` | Provides student profile rows. |

## Entities

The source data contains three main entities:

- students
- majors
- courses

It also contains one relationship that needs its own table:

- majors to courses

## Tables

### `students`

Stores student records.

| Column | Type | Constraint | Purpose |
| --- | --- | --- | --- |
| `student_id` | `SERIAL` | Primary key | Unique student identifier. |
| `first_name` | `VARCHAR(50)` | `NOT NULL` | Student first name. |
| `last_name` | `VARCHAR(50)` | `NOT NULL` | Student last name. |
| `major_id` | `INT` | Foreign key to `majors(major_id)` | Optional major reference. |
| `gpa` | `NUMERIC(2,1)` | Nullable | Optional GPA value. |

Why `major_id` is nullable:

- Some rows in `students.csv` have `null` for the major.
- Those students should still be stored.
- A nullable foreign key allows students without a known major.

Why `gpa` is nullable:

- Some rows in `students.csv` have `null` for GPA.
- `NUMERIC(2,1)` fits values such as `2.5`, `3.8`, and `4.0`.

### `majors`

Stores unique major names.

| Column | Type | Constraint | Purpose |
| --- | --- | --- | --- |
| `major_id` | `SERIAL` | Primary key | Unique major identifier. |
| `major` | `VARCHAR(50)` | `NOT NULL` | Major name. |

Why this table exists:

- The same major appears many times in the CSV files.
- Storing each major once avoids repeated text data.
- `students.major_id` and `majors_courses.major_id` can reference this table.

### `courses`

Stores unique course names.

| Column | Type | Constraint | Purpose |
| --- | --- | --- | --- |
| `course_id` | `SERIAL` | Primary key | Unique course identifier. |
| `course` | `VARCHAR(100)` | `NOT NULL` | Course name. |

Why `VARCHAR(100)` is used:

- Course names are longer than student or major names.
- Examples include `Data Structures and Algorithms` and
  `Object-Oriented Programming`.

### `majors_courses`

Stores the relationship between majors and courses.

| Column | Type | Constraint | Purpose |
| --- | --- | --- | --- |
| `major_id` | `INT` | Foreign key to `majors(major_id)` | Major side of the relationship. |
| `course_id` | `INT` | Foreign key to `courses(course_id)` | Course side of the relationship. |

Composite primary key:

```sql
PRIMARY KEY (major_id, course_id)
```

Why this table exists:

- A major can include many courses.
- A course can belong to many majors.
- This is a many-to-many relationship.
- A junction table is the normalized way to store many-to-many data.

Why the primary key uses two columns:

- `major_id` alone cannot be unique because one major appears with many courses.
- `course_id` alone cannot be unique because one course appears with many
  majors.
- The pair `(major_id, course_id)` should be unique.

## Relationship Map

```text
majors.major_id
  -> students.major_id

majors.major_id
  -> majors_courses.major_id

courses.course_id
  -> majors_courses.course_id
```

Human-readable version:

```text
One major can have many students.
One major can have many courses.
One course can belong to many majors.
```

## Final Row Counts

| Table | Expected final rows | Source |
| --- | ---: | --- |
| `majors` | 7 | Unique major values from both CSV workflows. |
| `courses` | 17 | Unique course values from `courses.csv`. |
| `majors_courses` | 28 | One row per data row in `courses.csv`, excluding the header. |
| `students` | 31 | One row per data row in `students.csv`, excluding the header. |

## Import Order

The import order matters because of foreign keys:

1. Insert `majors`.
2. Insert `courses`.
3. Insert `majors_courses`.
4. Insert `students`.

Why:

- `majors_courses` needs existing `major_id` and `course_id` values.
- `students` needs existing `major_id` values when a student has a major.

The script reads `courses.csv` first because that file is enough to populate
all majors, courses, and major-course relationships before student rows are
inserted.

## Null Handling

CSV value:

```csv
null
```

SQL value:

```sql
NULL
```

The import script intentionally inserts `major_id` and `gpa` without quotes:

```sql
VALUES('Emma', 'Gilbert', null, null)
```

If `null` were quoted, PostgreSQL would treat it as text:

```sql
'null'
```

That would be wrong for `major_id` and `gpa`.

## Verification Queries

Count all final rows:

```sql
SELECT COUNT(*) FROM majors;
SELECT COUNT(*) FROM courses;
SELECT COUNT(*) FROM majors_courses;
SELECT COUNT(*) FROM students;
```

Inspect student data with major names:

```sql
SELECT first_name, last_name, major, gpa
FROM students
LEFT JOIN majors USING(major_id)
ORDER BY student_id;
```

Inspect the major-course map:

```sql
SELECT major, course
FROM majors
JOIN majors_courses USING(major_id)
JOIN courses USING(course_id)
ORDER BY major, course;
```

Find students without a major:

```sql
SELECT first_name, last_name, gpa
FROM students
WHERE major_id IS NULL;
```

Find students without a GPA:

```sql
SELECT first_name, last_name, major_id
FROM students
WHERE gpa IS NULL;
```

## Sequence Note

The `students.sql` dump may show IDs that do not start from `1`.

This happened because the workshop used test inserts and truncation before the
final full import. PostgreSQL sequences continue increasing unless they are
reset explicitly with `RESTART IDENTITY`.

This is acceptable for the workshop output because:

- primary keys are still unique
- foreign keys still point to the correct rows
- the database can still be rebuilt from `students.sql`
