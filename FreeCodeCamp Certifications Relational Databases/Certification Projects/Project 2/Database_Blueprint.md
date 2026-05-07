# Database Blueprint

## Purpose

This file is the planning reference for the **Build a World Cup Database**
certification project.

The project uses the `games.csv` source file to populate a normalized
PostgreSQL database. The final submission is not this blueprint. The required
submission artifacts are `worldcup.sql`, `insert_data.sh`, and `queries.sh`.

## Project Scope

The database stores World Cup match results from the final three rounds of the
2014 and 2018 tournaments.

The CSV source contains:

- match year
- tournament round
- winning team
- opponent team
- winning team goals
- opponent team goals

The database separates teams from games so team names are stored once and game
rows reference them through IDs.

## Schema Blueprint

### 1. `teams`

| Column | Type | Constraint | Purpose |
| --- | --- | --- | --- |
| `team_id` | `SERIAL` | `PRIMARY KEY`, `NOT NULL` | Auto-incrementing unique team identifier. |
| `name` | `VARCHAR` | `UNIQUE`, `NOT NULL` | Team name. Unique because each team should appear only once. |

### 2. `games`

| Column | Type | Constraint | Purpose |
| --- | --- | --- | --- |
| `game_id` | `SERIAL` | `PRIMARY KEY`, `NOT NULL` | Auto-incrementing unique game identifier. |
| `year` | `INT` | `NOT NULL` | Tournament year. |
| `round` | `VARCHAR` | `NOT NULL` | Tournament round, such as `Final` or `Eighth-Final`. |
| `winner_id` | `INT` | `NOT NULL`, foreign key to `teams(team_id)` | Winning team ID. |
| `opponent_id` | `INT` | `NOT NULL`, foreign key to `teams(team_id)` | Opponent team ID. |
| `winner_goals` | `INT` | `NOT NULL` | Goals scored by the winner. |
| `opponent_goals` | `INT` | `NOT NULL` | Goals scored by the opponent. |

## Relationship Plan

The project uses two one-to-many relationships:

| Parent table | Child table | Foreign key | Meaning |
| --- | --- | --- | --- |
| `teams` | `games` | `games.winner_id` | One team can win many games. |
| `teams` | `games` | `games.opponent_id` | One team can appear as opponent in many games. |

Both `winner_id` and `opponent_id` reference `teams(team_id)` because each game
contains two team roles. The relationship stores the team once in `teams` and
uses numeric IDs in `games`.

## Why Team Names Are Separated

The CSV repeats team names across many rows. If the database stored team names
directly in every game row, the same text would be duplicated repeatedly.

The normalized design avoids that:

```text
teams.name       -> stored once per team
games.winner_id  -> references teams.team_id
games.opponent_id -> references teams.team_id
```

This design improves consistency. For example, if a team name needed correction,
it would be corrected once in `teams`, not in many game rows.

## Table Creation Plan

Create the database:

```sql
CREATE DATABASE worldcup;
\c worldcup
```

Create `teams`:

```sql
CREATE TABLE teams (
  team_id SERIAL PRIMARY KEY,
  name VARCHAR UNIQUE NOT NULL
);
```

Create `games`:

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

## Import Strategy

The import script reads `games.csv` line by line:

```text
year,round,winner,opponent,winner_goals,opponent_goals
```

For each non-header row:

1. Look up the winner in `teams`.
2. Insert the winner if it is missing.
3. Look up the winner ID again after insert.
4. Look up the opponent in `teams`.
5. Insert the opponent if it is missing.
6. Look up the opponent ID again after insert.
7. Insert the game row using `winner_id` and `opponent_id`.

The script must not hard-code team IDs because IDs depend on insert order.

## Expected Row Counts

After running `insert_data.sh`, the database should contain:

| Table | Expected rows | Source |
| --- | ---: | --- |
| `teams` | 24 | Unique winners and opponents from `games.csv`. |
| `games` | 32 | Every non-header row from `games.csv`. |

Verification queries:

```sql
SELECT COUNT(*) FROM teams;
SELECT COUNT(*) FROM games;
```

## Required Query Categories

The query script practices:

- aggregate totals with `SUM`
- averages with `AVG`
- rounded averages with `ROUND`
- maximum values with `MAX`
- conditional row counts with `COUNT`
- joins between `teams` and `games`
- distinct winning team names
- tournament champions by year
- pattern matching with `LIKE`
- combining winner and opponent team IDs with `UNION`

## Final Export

After the database passes the tests, export it from the Bash terminal:

```bash
pg_dump -cC --inserts -U freecodecamp worldcup > worldcup.sql
```

The dump can be restored with:

```bash
psql -U postgres < worldcup.sql
```
