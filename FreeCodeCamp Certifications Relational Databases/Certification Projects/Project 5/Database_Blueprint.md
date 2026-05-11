# Database Blueprint

## Purpose

This blueprint documents the final database design for the **Build a Number
Guessing Game** certification project.

The project combines a Bash terminal game with PostgreSQL persistence. The game
generates a secret number, asks the player to guess it, and stores each user's
long-term statistics so returning players can see their progress.

## Final Project Files

| File | Purpose |
| --- | --- |
| `CodeRoad_Instructions.md` | Cleaned project requirements and submission workflow. |
| `Database_Blueprint.md` | Final schema, state, and data design notes. |
| `Number_Guessing_SQL_Bash_Reference.md` | SQL and Bash syntax reference used by this project. |
| `Terminal_Work_Log.md` | Main terminal workflow used to complete and verify the project. |
| `number_guessing_game/number_guess.sh` | Final Bash game script. |
| `number_guessing_game/number_guess.sql` | Final database dump required by freeCodeCamp. |

## Project Goal

The game needs to remember player statistics between runs:

1. The player enters a username.
2. The script checks whether the username already exists.
3. New users receive a first-time welcome message.
4. Returning users receive their total games played and best game.
5. The script generates a secret number from 1 to 1000.
6. The player keeps guessing until the correct number is entered.
7. The script counts every guess attempt.
8. At the end of the game, the database updates the user's total games played.
9. If the current guess count is better than the stored best game, the database
   updates the best game value.

The database therefore needs one persistent table for users and game summary
statistics.

## Schema Blueprint

### `users`

| Column | Type | Constraint | Purpose |
| --- | --- | --- | --- |
| `user_id` | `SERIAL` / integer sequence | Primary key | Auto-incrementing user identifier. |
| `username` | `VARCHAR(22)` | Unique, not null | Stable player name entered at the start of the game. |
| `games_played` | `INTEGER` | Default `0` | Total completed games for the player. |
| `best_game` | `INTEGER` | Default `0` | Fewest guesses used by the player to win a game. |

## Why One Table Is Enough

This certification project only needs to report two aggregated values:

- how many games the user has completed
- the user's lowest number of guesses in a completed game

Because the project does not require a full history of every game, those two
summary values can live directly in the `users` table.

A more detailed production design could use a separate `games` table with one
row per completed game, then calculate `COUNT(*)` and `MIN(guesses)` with SQL.
For this project, the simpler summary-table design is enough and matches the
final submitted dump.

## State Rules

| State | Stored Value |
| --- | --- |
| New user | Insert username with `games_played = 0` and `best_game = 0`. |
| Completed game | Increase `games_played` by one. |
| First completed game | Replace `best_game = 0` with the current guess count. |
| Better completed game | Replace `best_game` when the new guess count is lower. |
| Worse completed game | Keep the previous `best_game`. |

## Username Rules

The username column uses `VARCHAR(22)` because the project explicitly requires
usernames up to 22 characters:

```sql
username VARCHAR(22) UNIQUE NOT NULL
```

The unique constraint is important because the username is the lookup key. If
two rows had the same username, the script could not reliably know which
statistics to display or update.

## Script Query Plan

The submitted script uses these database operations:

| Step | Query Purpose |
| --- | --- |
| User lookup | Select `games_played` and `best_game` for the entered username. |
| New user insert | Insert the username if no existing row is found. |
| Games played update | Increase `games_played` after the player wins. |
| Best game lookup | Select the current `best_game`. |
| Best game update | Store the current guess count if it is better. |

## Final Output Patterns

New user:

```text
Welcome, zaenal! It looks like this is your first time here.
```

Returning user:

```text
Welcome back, zaenal! You have played 3 games, and your best game took 7 guesses.
```

Correct guess:

```text
You guessed it in 7 tries. The secret number was 500. Nice job!
```

The output wording is part of the project contract. Even small punctuation or
spacing differences can cause the automated tests to fail.
