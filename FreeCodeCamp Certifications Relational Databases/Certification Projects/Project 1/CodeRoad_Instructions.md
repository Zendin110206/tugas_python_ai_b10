# CodeRoad Instructions

## Project Context

This file records the original freeCodeCamp project requirements for the
**Build a Celestial Bodies Database** certification project.

The project runs in a virtual Linux environment through GitHub Codespaces and
CodeRoad. The final required submission file is `universe.sql`, which is created
with `pg_dump` after all project tests pass.

## Required Workflow

1. Open the project in GitHub Codespaces.
2. Start CodeRoad inside VS Code.
3. Log in to PostgreSQL with `psql`.
4. Create a database named `universe`.
5. Build the required schema and data.
6. Pass all automated project tests.
7. Export the database dump to `universe.sql`.
8. Save `universe.sql` in a public repository and submit the repository URL to
   freeCodeCamp.

## PostgreSQL Login

Run this command in the terminal:

```bash
psql --username=freecodecamp --dbname=postgres
```

After creating the database, connect to it:

```sql
\c universe
```

## Database Dump Command

After all tests pass, run this command from the Bash terminal, not from inside
the `psql` prompt:

```bash
pg_dump -cC --inserts -U freecodecamp universe > universe.sql
```

The resulting `universe.sql` file can rebuild the database with:

```bash
psql -U postgres < universe.sql
```

## User Stories and Test Requirements

The project must satisfy the following requirements:

- Create a database named `universe`.
- Connect to the `universe` database.
- Add tables named `galaxy`, `star`, `planet`, and `moon`.
- Each table must have a primary key.
- Each primary key must automatically increment.
- Each table must have a `name` column.
- Use the `INT` data type for at least two columns that are not primary keys or
  foreign keys.
- Use the `NUMERIC` data type at least once.
- Use the `TEXT` data type at least once.
- Use the `BOOLEAN` data type on at least two columns.
- Each row in `star` must have a foreign key referencing a row in `galaxy`.
- Each row in `planet` must have a foreign key referencing a row in `star`.
- Each row in `moon` must have a foreign key referencing a row in `planet`.
- The database must have at least five tables.
- Each table must have at least three rows.
- The `galaxy` and `star` tables must each have at least six rows.
- The `planet` table must have at least twelve rows.
- The `moon` table must have at least twenty rows.
- Each table must have at least three columns.
- The `galaxy`, `star`, `planet`, and `moon` tables must each have at least
  five columns.
- At least two columns per table must not accept `NULL` values.
- At least one column from each table must be required to be `UNIQUE`.
- All columns named `name` must be type `VARCHAR`.
- Each primary key column must follow the `table_name_id` naming convention.
  For example, the `moon` table must have a primary key named `moon_id`.
- Each foreign key column must have the same name as the column it references.

## Notes

The freeCodeCamp tests are strict about table and column names. For this
project, the required table names are singular:

- `galaxy`
- `star`
- `planet`
- `moon`

Although plural table names are common in some projects, the singular names are
used here because they are required by the certification tests.
