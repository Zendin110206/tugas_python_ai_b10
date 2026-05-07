# CodeRoad Instructions

## Project Context

This file records the original freeCodeCamp project requirements for the
**Build a World Cup Database** certification project.

The project runs in a virtual Linux environment through GitHub Codespaces and
CodeRoad. The required submission files are:

- `worldcup.sql`
- `insert_data.sh`
- `queries.sh`

The `worldcup.sql` file is created with `pg_dump` after the database schema,
data import script, and query script pass the automated tests.

## Required Workflow

1. Open the project in GitHub Codespaces.
2. Start CodeRoad inside VS Code.
3. Log in to PostgreSQL with `psql`.
4. Create a database named `worldcup`.
5. Create the `teams` and `games` tables according to the user stories.
6. Complete `insert_data.sh` so it imports every game from `games.csv`.
7. Complete `queries.sh` so every output matches `expected_output.txt`.
8. Make both shell scripts executable.
9. Run the project tests until all user stories pass.
10. Export the database dump to `worldcup.sql`.
11. Save `worldcup.sql`, `insert_data.sh`, and `queries.sh` in a public
    repository and submit the repository URL to freeCodeCamp.

## PostgreSQL Login

Run this command in the terminal:

```bash
psql --username=freecodecamp --dbname=postgres
```

After creating the project database, connect to it:

```sql
\c worldcup
```

## Database Dump Command

After all tests pass, run this command from the Bash terminal, not from inside
the `psql` prompt:

```bash
pg_dump -cC --inserts -U freecodecamp worldcup > worldcup.sql
```

The resulting `worldcup.sql` file can rebuild the database with:

```bash
psql -U postgres < worldcup.sql
```

## Project Parts

### Part 1: Create the Database

Create the database structure manually in PostgreSQL.

The database must be named:

```sql
worldcup
```

The database must contain:

- a `teams` table
- a `games` table

### Part 2: Insert the Data

Complete `insert_data.sh` so it reads `games.csv` and inserts:

- every unique team into `teams`
- every game row into `games`

The starter code above the marked line in `insert_data.sh` must not be changed.
The script should use the provided `PSQL` variable for database queries.

The project tests have a time limit, so the script should avoid unnecessary
queries where possible. The tables can be emptied and reset with:

```sql
TRUNCATE teams, games RESTART IDENTITY;
```

### Part 3: Query the Database

Complete `queries.sh` so each command prints exactly the expected answer.

The starter code defines a `PSQL` variable. Each answer should be produced by a
single command substitution pattern:

```bash
echo "$($PSQL "SELECT ...")"
```

The query script depends on the database already being filled with correct data
from `insert_data.sh`.

## User Stories and Test Requirements

The project must satisfy the following requirements:

- Create a database named `worldcup`.
- Connect to the `worldcup` database.
- Create tables named `teams` and `games`.
- The `teams` table must have a `team_id` column of type `SERIAL`.
- `teams.team_id` must be the primary key.
- The `teams` table must have a `name` column.
- `teams.name` must be unique.
- The `games` table must have a `game_id` column of type `SERIAL`.
- `games.game_id` must be the primary key.
- The `games` table must have a `year` column of type `INT`.
- The `games` table must have a `round` column of type `VARCHAR`.
- The `games` table must have `winner_id` and `opponent_id` foreign key
  columns.
- Both foreign key columns must reference `teams(team_id)`.
- The `games` table must have `winner_goals` and `opponent_goals` columns of
  type `INT`.
- All columns in both tables must have the `NOT NULL` constraint.
- `insert_data.sh` and `queries.sh` must have executable permissions.
- Running `insert_data.sh` must add each unique team to `teams`.
- The `teams` table must contain exactly 24 rows after import.
- Running `insert_data.sh` must add one game row for each non-header row in
  `games.csv`.
- The `games` table must contain exactly 32 rows after import.
- Game rows must use the correct team IDs from the `teams` table.
- Team IDs must not be hard-coded.
- `queries.sh` must produce output matching `expected_output.txt` exactly.
- Decimal-place formatting must match the expected output.

## Final Submission Notes

The required files for public repository submission are:

| File | Purpose |
| --- | --- |
| `worldcup.sql` | Database dump that rebuilds the completed project database. |
| `insert_data.sh` | Bash script that imports data from `games.csv`. |
| `queries.sh` | Bash script that answers the required SQL questions. |
| `expected_output.txt` | Reference output used to verify `queries.sh`. |

The `games.csv` file is kept in this repository as supporting source data for
the import script.
