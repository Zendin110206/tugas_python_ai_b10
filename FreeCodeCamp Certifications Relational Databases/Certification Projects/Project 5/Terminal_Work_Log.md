# Terminal Work Log

## Purpose

This file documents the main terminal workflow used to complete the **Build a
Number Guessing Game** certification project.

It is not the final submission file. The final required submission files are
`number_guess.sql` and `number_guess.sh`.

## Environment

- Platform: freeCodeCamp Codespaces
- Database client: `psql`
- PostgreSQL user: `freecodecamp`
- Project database: `number_guess`
- Project folder: `number_guessing_game`
- Script file: `number_guess.sh`
- Final dump: `number_guess.sql`

## PostgreSQL Service

If PostgreSQL is not running in a local or containerized environment, start it
from the Bash terminal:

```bash
sudo service postgresql start
```

The freeCodeCamp Codespaces environment usually has PostgreSQL ready, but this
command is useful when rebuilding or testing manually.

## Project Folder Setup

The project requires a dedicated folder:

```bash
mkdir number_guessing_game
cd number_guessing_game
```

Inside the CodeRoad workspace, this folder also needs to be a Git repository:

```bash
git init
git checkout -b main
```

The first CodeRoad commit message must be:

```text
Initial commit
```

Later CodeRoad commit messages must start with one of:

```text
fix:
feat:
refactor:
chore:
test:
```

## Login and Database Setup

```bash
psql --username=freecodecamp --dbname=postgres
```

```sql
CREATE DATABASE number_guess;
\c number_guess
```

## Table Creation Plan

The database uses one table:

```sql
CREATE TABLE users();
```

The table was then structured to satisfy the project requirements.

## Final Table Structure

```sql
CREATE TABLE users (
  user_id SERIAL PRIMARY KEY,
  username VARCHAR(22) UNIQUE NOT NULL,
  games_played INT DEFAULT 0,
  best_game INT DEFAULT 0
);
```

The final dump may show this structure in expanded PostgreSQL form, with an
integer `user_id`, a sequence, and a default `nextval(...)` expression. That is
normal output from `pg_dump`.

## Script Setup

The script file was created as `number_guess.sh` and starts with a Bash
shebang:

```bash
#!/bin/bash
```

Executable permission is required:

```bash
chmod +x number_guess.sh
```

The script uses this reusable PostgreSQL command:

```bash
PSQL="psql --username=freecodecamp --dbname=number_guess -t --no-align -c"
```

## Main Script Flow

The submitted script follows this sequence:

1. Generate a random secret number from 1 to 1000.
2. Set the guess counter to zero.
3. Ask for the username.
4. Query the database for existing user statistics.
5. Insert a new user if the username does not exist.
6. Print the correct welcome message for a new or returning user.
7. Ask for the first guess.
8. Count each guess attempt.
9. Repeat until the user guesses the secret number.
10. Print invalid-integer, higher, or lower guidance when needed.
11. Print the final success message.
12. Increase `games_played`.
13. Update `best_game` only when the current score is better.

## Manual Test Flow

Run the script:

```bash
./number_guess.sh
```

Example new user input:

```text
zaenal
500
750
625
```

The secret number changes on each run, so the exact number of guesses and final
secret number cannot be predicted manually.

Example new user welcome:

```text
Welcome, zaenal! It looks like this is your first time here.
```

Example returning user welcome:

```text
Welcome back, zaenal! You have played 1 games, and your best game took 6 guesses.
```

Example invalid input:

```text
That is not an integer, guess again:
```

Example high/low guidance:

```text
It's higher than that, guess again:
It's lower than that, guess again:
```

Example final message:

```text
You guessed it in 6 tries. The secret number was 625. Nice job!
```

## Verification Queries

The final table structure can be checked with:

```sql
\d users
```

The stored user statistics can be checked with:

```sql
SELECT *
FROM users
ORDER BY user_id;
```

Check one user directly:

```sql
SELECT username, games_played, best_game
FROM users
WHERE username = 'zaenal';
```

## Final Export

After the database and script passed the project tests, the `psql` session was
closed:

```sql
\q
```

The database dump was created from the Bash terminal:

```bash
pg_dump -cC --inserts -U freecodecamp number_guess > number_guess.sql
```

The generated `number_guess.sql` file, together with `number_guess.sh`, is
required for the freeCodeCamp certification project submission.
