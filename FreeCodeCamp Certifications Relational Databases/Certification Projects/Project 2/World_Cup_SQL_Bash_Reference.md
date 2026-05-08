# World Cup SQL and Bash Reference

## Purpose

This reference documents the PostgreSQL and Bash patterns used in the **Build a
World Cup Database** certification project.

It focuses on syntax that is useful when rebuilding the project, debugging the
import script, or understanding why each query in `queries.sh` works.

## Project Files

| File | Purpose |
| --- | --- |
| `games.csv` | Source data for the import script. |
| `insert_data.sh` | Reads CSV data and inserts teams and games into PostgreSQL. |
| `queries.sh` | Prints the required query answers. |
| `expected_output.txt` | Expected output used to verify `queries.sh`. |
| `worldcup.sql` | Final database dump used for freeCodeCamp submission. |

## Script Database Selection

`insert_data.sh` supports both the real project database and the test database:

```bash
if [[ $1 == "test" ]]
then
  PSQL="psql --username=postgres --dbname=worldcuptest -t --no-align -c"
else
  PSQL="psql --username=freecodecamp --dbname=worldcup -t --no-align -c"
fi
```

This matters because freeCodeCamp tests may run the script against
`worldcuptest`, while normal project execution uses `worldcup`.

## Reset Tables Before Import

The import script starts by clearing old rows and resetting serial IDs:

```bash
echo "$($PSQL "TRUNCATE teams, games RESTART IDENTITY")"
```

| Part | Meaning |
| --- | --- |
| `TRUNCATE teams, games` | Removes rows from both tables. |
| `RESTART IDENTITY` | Resets `SERIAL` sequences back to the beginning. |

Resetting identities keeps repeated test runs predictable.

## CSV Reading Pattern

The CSV file is read with `IFS=","` so each comma-separated column is assigned
to a Bash variable:

```bash
cat games.csv | while IFS="," read -r YEAR ROUND WINNER OPPONENT WINNER_GOALS OPPONENT_GOALS
do
  if [[ $YEAR != "year" ]]
  then
    echo "$YEAR - $WINNER vs $OPPONENT"
  fi
done
```

| Part | Meaning |
| --- | --- |
| `cat games.csv` | Sends the CSV file content into the loop. |
| `IFS=","` | Split each row by comma. |
| `read -r` | Read a row without treating backslashes as escapes. |
| `YEAR ROUND ...` | Variables that receive CSV columns. |
| `[[ $YEAR != "year" ]]` | Skips the header row. |

This keeps the same style used while completing the freeCodeCamp project.

An input-redirection version is also valid and avoids the extra `cat` process:

```bash
while IFS="," read -r YEAR ROUND WINNER OPPONENT WINNER_GOALS OPPONENT_GOALS
do
  if [[ $YEAR != "year" ]]
  then
    echo "$YEAR - $WINNER vs $OPPONENT"
  fi
done < games.csv
```

## Lookup-Then-Insert Team Pattern

The import script should insert each team only once. In the submitted workflow,
this is done in a first pass over `games.csv`, before inserting game rows in a
second pass.

```bash
WINNER_ID=$($PSQL "SELECT team_id FROM teams WHERE name='$WINNER'")

if [[ -z $WINNER_ID ]]
then
  INSERT_WINNER_RESULT=$($PSQL "INSERT INTO teams(name) VALUES('$WINNER')")
  WINNER_ID=$($PSQL "SELECT team_id FROM teams WHERE name='$WINNER'")
fi
```

The same pattern is used for the opponent.

Why the ID is queried again:

- before insert, the ID is empty
- after insert, PostgreSQL generates the `SERIAL` ID
- the game row needs that generated ID for its foreign key

The two-pass approach is easy to trace while learning:

1. Build the `teams` table from all winners and opponents.
2. Read the CSV again and insert `games` rows using the generated team IDs.

A one-pass version can be more efficient, but the two-pass version is kept here
because it reflects the completed project workflow.

## Insert Game Pattern

After both team IDs are known, the game row can be inserted:

```bash
INSERT_GAME_RESULT=$($PSQL "INSERT INTO games(year, round, winner_id, opponent_id, winner_goals, opponent_goals) VALUES($YEAR, '$ROUND', $WINNER_ID, $OPPONENT_ID, $WINNER_GOALS, $OPPONENT_GOALS)")
```

Important quoting rules:

| Value | SQL Quoting |
| --- | --- |
| `YEAR` | Unquoted, because it is an integer. |
| `ROUND` | Quoted, because it is text. |
| `WINNER_ID` | Unquoted, because it is an integer foreign key. |
| `OPPONENT_ID` | Unquoted, because it is an integer foreign key. |
| `WINNER_GOALS` | Unquoted, because it is an integer. |
| `OPPONENT_GOALS` | Unquoted, because it is an integer. |

## Query Script Pattern

Each answer in `queries.sh` uses this structure:

```bash
echo -e "\nQuestion title:"
echo "$($PSQL "SELECT ...")"
```

The first `echo` prints the label expected by the project. The second `echo`
runs a SQL query and prints only the result.

## Aggregate Query Patterns

| Goal | Query |
| --- | --- |
| Total winning goals | `SELECT SUM(winner_goals) FROM games;` |
| Total goals from both teams | `SELECT SUM(winner_goals + opponent_goals) FROM games;` |
| Average winning goals | `SELECT AVG(winner_goals) FROM games;` |
| Rounded average winning goals | `SELECT ROUND(AVG(winner_goals), 2) FROM games;` |
| Average total goals per game | `SELECT AVG(winner_goals + opponent_goals) FROM games;` |
| Maximum goals by one team | `SELECT MAX(winner_goals) FROM games;` |
| Count games by condition | `SELECT COUNT(*) FROM games WHERE winner_goals > 2;` |

## Join Query Patterns

Find the 2018 champion:

```sql
SELECT name
FROM teams
INNER JOIN games ON teams.team_id = games.winner_id
WHERE year = 2018
  AND round = 'Final';
```

List all champions:

```sql
SELECT year, name
FROM teams
INNER JOIN games ON teams.team_id = games.winner_id
WHERE round = 'Final'
ORDER BY year;
```

The `games` table stores team IDs, not team names. The join is required to
translate `winner_id` into `teams.name`.

## Winner and Opponent Team List Pattern

To list teams that played in a round, both `winner_id` and `opponent_id` must be
considered.

The submitted query uses an `OR` condition in the join:

```sql
SELECT name
FROM teams
JOIN games ON teams.team_id = games.winner_id
          OR teams.team_id = games.opponent_id
WHERE year = 2014
  AND round = 'Eighth-Final'
ORDER BY name;
```

This matches the required output for the project.

An alternative version can use `UNION`:

```sql
SELECT name
FROM teams
WHERE team_id IN (
  SELECT winner_id FROM games WHERE year = 2014 AND round = 'Eighth-Final'
  UNION
  SELECT opponent_id FROM games WHERE year = 2014 AND round = 'Eighth-Final'
)
ORDER BY name;
```

Why the `UNION` version can be useful:

- it combines winner IDs and opponent IDs into one result set
- it removes duplicates by default
- it avoids an `OR` join condition that can be harder to reason about

## Distinct Winners

List each team that won at least one game:

```sql
SELECT DISTINCT(name)
FROM teams
INNER JOIN games ON teams.team_id = games.winner_id
ORDER BY name;
```

`DISTINCT` is needed because a team can win more than one game.

## Text Pattern Query

Find teams whose names start with `Co`:

```sql
SELECT name
FROM teams
WHERE name LIKE 'Co%'
ORDER BY name;
```

| Pattern | Meaning |
| --- | --- |
| `Co%` | Starts with `Co`. |
| `%Co` | Ends with `Co`. |
| `%Co%` | Contains `Co`. |

## Verification Queries

Use these after running `insert_data.sh`:

```sql
SELECT COUNT(*) FROM teams;
SELECT COUNT(*) FROM games;
SELECT * FROM teams ORDER BY team_id;
SELECT * FROM games ORDER BY game_id;
```

Expected row counts:

```text
teams: 24
games: 32
```

## Common Mistakes

| Problem | Likely Cause | Fix |
| --- | --- | --- |
| Duplicate team names fail insert | Team was inserted without checking if it already exists. | Query `teams` first and insert only if the ID is empty. |
| Game insert fails with foreign key error | Winner or opponent was not inserted before the game row. | Insert or look up both teams before inserting the game. |
| Header row appears in database | CSV header was not skipped. | Check `[[ $YEAR != "year" ]]`. |
| Text values fail in SQL | Text variables were not quoted. | Use `'$ROUND'` and `'$WINNER'`. |
| Number values become text | Integer values were quoted unnecessarily. | Keep years, IDs, and goals unquoted. |
| Query output has extra formatting | Missing `--no-align` or `--tuples-only`. | Use the provided `PSQL` variable. |
| Tests fail after repeated imports | Old rows or serial IDs were not reset. | Use `TRUNCATE teams, games RESTART IDENTITY`. |
