# Database Blueprint

## Purpose

This blueprint documents the final database design for the **Build a Periodic
Table Database** certification project.

The goal is to keep chemical element identity data, physical property data, and
element type data in a normalized PostgreSQL schema that can be queried by the
`element.sh` Bash program.

## Final Project Files

| File | Purpose |
| --- | --- |
| `CodeRoad_Instructions.md` | Cleaned project requirements and submission workflow. |
| `Database_Blueprint.md` | Final schema, relationship, and data design notes. |
| `Periodic_Table_SQL_Bash_Reference.md` | SQL and Bash syntax reference used by this project. |
| `Terminal_Work_Log.md` | Main terminal workflow used to complete and verify the project. |
| `atomic_mass.txt` | Verification output for cleaned atomic mass values. |
| `periodic_table/element.sh` | Final Bash search script. |
| `periodic_table/periodic_table.sql` | Final database dump required by freeCodeCamp. |

## Entity Overview

The final schema uses three tables:

| Table | Role |
| --- | --- |
| `elements` | Stores stable identity fields for each chemical element. |
| `properties` | Stores numeric physical properties for each element. |
| `types` | Stores normalized element category labels. |

This design separates element identity, measurable properties, and type labels.
That makes the schema easier to validate and avoids repeating raw text type
values in every row of `properties`.

## `elements` Table

| Column | Type | Constraint | Purpose |
| --- | --- | --- | --- |
| `atomic_number` | `INTEGER` | Primary key, unique, not null | Main identifier for each element. |
| `symbol` | `VARCHAR(2)` | Unique, not null | One-letter or two-letter element symbol. |
| `name` | `VARCHAR(40)` | Unique, not null | Full element name. |

### Final Rows

| atomic_number | symbol | name |
| --- | --- | --- |
| 1 | H | Hydrogen |
| 2 | He | Helium |
| 3 | Li | Lithium |
| 4 | Be | Beryllium |
| 5 | B | Boron |
| 6 | C | Carbon |
| 7 | N | Nitrogen |
| 8 | O | Oxygen |
| 9 | F | Fluorine |
| 10 | Ne | Neon |

## `types` Table

| Column | Type | Constraint | Purpose |
| --- | --- | --- | --- |
| `type_id` | `INTEGER` | Primary key, not null | Numeric identifier for the type category. |
| `type` | `VARCHAR` | Not null | Human-readable type label. |

### Final Rows

| type_id | type |
| --- | --- |
| 1 | metal |
| 2 | nonmetal |
| 3 | metalloid |

The `types` table is used so the same category text does not need to be stored
repeatedly in `properties`. Instead, `properties.type_id` points to the
normalized lookup row.

## `properties` Table

| Column | Type | Constraint | Purpose |
| --- | --- | --- | --- |
| `atomic_number` | `INTEGER` | Unique, not null, foreign key | Connects each property row to one element. |
| `atomic_mass` | `NUMERIC` | Not null | Atomic mass in atomic mass units. |
| `melting_point_celsius` | `NUMERIC` | Not null | Melting point in Celsius. |
| `boiling_point_celsius` | `NUMERIC` | Not null | Boiling point in Celsius. |
| `type_id` | `INTEGER` | Not null, foreign key | Connects each element to its type category. |

### Relationship Rules

| Relationship | Implementation | Reason |
| --- | --- | --- |
| `elements` to `properties` | `properties.atomic_number` references `elements.atomic_number` | Each property row belongs to one known element. |
| `types` to `properties` | `properties.type_id` references `types.type_id` | Each property row uses one normalized type value. |

`properties.atomic_number` is unique, so one element has one property row in the
final project data.

## Atomic Mass Cleanup

The project requires unnecessary trailing zeroes to be removed from
`atomic_mass`. The cleanup command is:

```sql
UPDATE properties
SET atomic_mass = TRIM(TRAILING '0' FROM atomic_mass::TEXT)::DECIMAL;
```

What happens in the command:

| Part | Meaning |
| --- | --- |
| `atomic_mass::TEXT` | Temporarily converts the numeric value to text so text trimming can be used. |
| `TRIM(TRAILING '0' FROM ...)` | Removes only zeroes at the end of the text value. |
| `::DECIMAL` | Converts the cleaned text back to a decimal value. |
| `UPDATE properties SET atomic_mass = ...` | Stores the cleaned value back in the table. |

The verification output is stored in `atomic_mass.txt`.

## Script Query Plan

The final script supports three lookup styles:

| Input Type | Example | Query Condition |
| --- | --- | --- |
| Atomic number | `./element.sh 1` | `WHERE atomic_number = 1` |
| Symbol | `./element.sh H` | `WHERE symbol = 'H'` |
| Name | `./element.sh Hydrogen` | `WHERE name = 'Hydrogen'` |

The script joins all three tables so the final message can include identity,
type, atomic mass, melting point, and boiling point in one output line.

## Final Output Pattern

For a found element, the output must follow this exact structure:

```text
The element with atomic number 1 is Hydrogen (H). It's a nonmetal, with a mass of 1.008 amu. Hydrogen has a melting point of -259.1 celsius and a boiling point of -252.9 celsius.
```

For an unknown element:

```text
I could not find that element in the database.
```

For a missing argument:

```text
Please provide an element as an argument.
```
