# Terminal Work Log

## Purpose

This file documents the main terminal workflow used to complete the **Build a
World Cup Database** certification project.

It is not the final submission file. The final generated database dump is
`worldcup.sql`.

## Environment

- Platform: freeCodeCamp Codespaces
- Database client: `psql`
- PostgreSQL user: `freecodecamp`
- Starting database: `postgres`
- Final project database: `worldcup`
- Source data: `games.csv`

## Login and Database Setup

```bash
psql --username=freecodecamp --dbname=postgres
```

```sql
CREATE DATABASE worldcup;
\c worldcup
```

The database was created successfully and the `psql` session was connected to
`worldcup`.

## Table Structure

### `teams`

```sql
CREATE TABLE teams (
  team_id SERIAL PRIMARY KEY,
  name VARCHAR UNIQUE NOT NULL
);
```

### `games`

```sql
CREATE TABLE games (
  game_id SERIAL PRIMARY KEY,
  year INT NOT NULL,
  round VARCHAR NOT NULL,
  winner_id INT NOT NULL REFERENCES teams(team_id),
  opponent_id INT NOT NULL REFERENCES teams(team_id),
  winner_goals INT NOT NULL,
  opponent_goals INT NOT NULL
);
```

The table structure can be verified with:

```sql
\d teams
\d games
```

## Script Permissions

Both project scripts must be executable:

```bash
chmod +x insert_data.sh
chmod +x queries.sh
```

Without executable permissions, the project tests for both scripts can fail
even if the script content is correct.

## Data Import

Run the import script:

```bash
./insert_data.sh
```

The script:

1. truncates `teams` and `games`
2. resets serial IDs
3. reads `games.csv` once to insert each unique team
4. reads `games.csv` again to insert each game with the correct `winner_id` and
   `opponent_id`

Verification:

```sql
SELECT COUNT(*) FROM teams;
SELECT COUNT(*) FROM games;
```

Expected output:

```text
24
32
```

## Query Script

Run the query script:

```bash
./queries.sh
```

The script prints the required project answers, including:

- total winning goals
- total goals from both teams
- average winning goals
- rounded averages
- highest single-team goal count
- count of games where the winner scored more than two goals
- 2018 champion
- 2014 Eighth-Final participants
- unique winning teams
- champions by year
- teams starting with `Co`

## Test Database Mode

The import script supports the freeCodeCamp test database:

```bash
./insert_data.sh test
```

When the argument is `test`, the script uses:

```text
worldcuptest
```

Otherwise, it uses:

```text
worldcup
```

## Final Export

After the project tests pass, export the database from the Bash terminal:

```bash
pg_dump -cC --inserts -U freecodecamp worldcup > worldcup.sql
```

The generated dump can rebuild the database with:

```bash
psql -U postgres < worldcup.sql
```

The required freeCodeCamp repository submission files are:

- `worldcup.sql`
- `insert_data.sh`
- `queries.sh`
