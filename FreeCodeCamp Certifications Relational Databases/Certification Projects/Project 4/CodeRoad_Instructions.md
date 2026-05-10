# CodeRoad Instructions

## Project Context

This file records the cleaned freeCodeCamp requirements and workflow for the
**Build a Periodic Table Database** certification project.

The project runs in a virtual Linux environment through GitHub Codespaces,
CodeRoad, or an equivalent local Dev Container setup. The final required
submission files are:

- `periodic_table.sql`
- `element.sh`

`periodic_table.sql` is created with `pg_dump` after the database passes all
project tests. `element.sh` is the Bash program used to search the periodic
table database by atomic number, symbol, or element name.

## Required Workflow

1. Open the project environment.
2. Start CodeRoad inside VS Code.
3. Log in to PostgreSQL from the Bash terminal.
4. Connect to the `periodic_table` database.
5. Normalize and clean the existing database schema.
6. Add missing constraints, keys, and reference data.
7. Add the required element data for fluorine and neon.
8. Write an executable Bash script named `element.sh`.
9. Test the script with atomic number, symbol, name, missing argument, and
   unknown element inputs.
10. Pass all automated project tests.
11. Export the database dump to `periodic_table.sql`.
12. Save both `periodic_table.sql` and `element.sh` in a public repository and
    submit the repository URL to freeCodeCamp.

## PostgreSQL Login

Run this command from the Bash terminal:

```bash
psql --username=freecodecamp --dbname=postgres
```

Connect to the project database:

```sql
\c periodic_table
```

If PostgreSQL is not running in a local or containerized environment, start it
first:

```bash
sudo service postgresql start
```

## Database Dump Command

After all tests pass, run this command from the Bash terminal, not from inside
the `psql` prompt:

```bash
pg_dump -cC --inserts -U freecodecamp periodic_table > periodic_table.sql
```

The resulting dump can rebuild the project database with:

```bash
psql -U postgres < periodic_table.sql
```

## User Stories and Test Requirements

The project must satisfy the following requirements:

- Connect to the `periodic_table` database.
- Rename the `weight` column to `atomic_mass`.
- Rename the `melting_point` column to `melting_point_celsius`.
- Rename the `boiling_point` column to `boiling_point_celsius`.
- Set `melting_point_celsius` as `NOT NULL`.
- Set `boiling_point_celsius` as `NOT NULL`.
- Add a unique constraint to `elements.symbol`.
- Add a unique constraint to `elements.name`.
- Set `elements.symbol` to `VARCHAR(2)`.
- Set `elements.name` to `VARCHAR(40)`.
- Set `properties.atomic_number` as a foreign key that references
  `elements.atomic_number`.
- Create a `types` table.
- Add `type_id` as the primary key of `types`.
- Add a `type` column in `types`.
- Set `types.type` as `NOT NULL`.
- Insert the required `metal`, `nonmetal`, and `metalloid` type rows.
- Add a `type_id` column to `properties`.
- Populate `properties.type_id` from the original element type values.
- Set `properties.type_id` as `NOT NULL`.
- Set `properties.type_id` as a foreign key that references `types.type_id`.
- Remove the original text-based `type` column from `properties`.
- Capitalize the first letter of all element symbols.
- Remove unnecessary trailing zeroes from `atomic_mass`.
- Add fluorine to the database.
- Add neon to the database.
- Create `element.sh` in the project folder.
- Add a Bash shebang to `element.sh`.
- Make `element.sh` executable.
- If the script is run without an argument, print:

```text
Please provide an element as an argument.
```

- If the script cannot find the requested element, print:

```text
I could not find that element in the database.
```

- If the argument is an atomic number, symbol, or element name, print the
  matching element information with this exact pattern:

```text
The element with atomic number <number> is <name> (<symbol>). It's a <type>, with a mass of <mass> amu. <name> has a melting point of <melting> celsius and a boiling point of <boiling> celsius.
```

## Required Submission Link

freeCodeCamp asks for the public repository URL that contains the required
files. For this repository, the most precise public link for the required
submission files is the `periodic_table` folder URL after the commit has been
pushed:

```text
https://github.com/Zendin110206/tugas_python_ai_b10/tree/main/FreeCodeCamp%20Certifications%20Relational%20Databases/Certification%20Projects/Project%204/periodic_table
```

That folder contains:

- `periodic_table.sql`
- `element.sh`

## Notes

- `periodic_table.sql` is the final exported database dump. It should not be
  hand-edited unless the database is intentionally rebuilt and exported again.
- `element.sh` is the final executable script used by the tests.
- `atomic_mass.txt` is kept as a small verification note showing the cleaned
  `atomic_mass` values after trailing zero removal.
- The freeCodeCamp tests are strict about file names, executable permission,
  output wording, schema constraints, and query results.
