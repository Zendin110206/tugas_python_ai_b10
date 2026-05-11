# CodeRoad Instructions

## Project Context

This file records the cleaned freeCodeCamp requirements and workflow for the
**Build a Number Guessing Game** certification project.

The project runs in a virtual Linux environment through GitHub Codespaces,
CodeRoad, or an equivalent local Dev Container setup. The final required
submission files are:

- `number_guess.sql`
- `number_guess.sh`

`number_guess.sql` is created with `pg_dump` after the database passes all
project tests. `number_guess.sh` is the terminal game script that generates a
random number, reads guesses, and stores user statistics in PostgreSQL.

## Required Workflow

1. Open the project environment.
2. Start CodeRoad inside VS Code.
3. Create a folder named `number_guessing_game` inside the project folder.
4. Create the `number_guess` PostgreSQL database.
5. Create the required user statistics table.
6. Write an executable Bash script named `number_guess.sh`.
7. Turn the `number_guessing_game` folder into a Git repository for the
   CodeRoad project requirement.
8. Make at least five commits inside that CodeRoad project repository.
9. Finish the CodeRoad project on the `main` branch with a clean working tree.
10. Test the script with new users, returning users, invalid guesses, higher
    guesses, lower guesses, and correct guesses.
11. Pass all automated project tests.
12. Export the database dump to `number_guess.sql`.
13. Save both `number_guess.sql` and `number_guess.sh` in a public repository
    and submit the repository URL to freeCodeCamp.

## PostgreSQL Login

Run this command from the Bash terminal:

```bash
psql --username=freecodecamp --dbname=postgres
```

After creating the project database, connect to it:

```sql
\c number_guess
```

If PostgreSQL is not running in a local or containerized environment, start it
first:

```bash
sudo service postgresql start
```

## Script Query Pattern

The project allows SQL queries to be executed from the Bash script with this
pattern:

```bash
psql --username=freecodecamp --dbname=number_guess -t --no-align -c "SQL QUERY HERE"
```

The submitted script stores that command in a reusable variable:

```bash
PSQL="psql --username=freecodecamp --dbname=number_guess -t --no-align -c"
```

`-t` and `--no-align` keep query output compact, which makes it easier for the
script to read values such as `games_played` and `best_game`.

## Database Dump Command

After all tests pass, run this command from the Bash terminal, not from inside
the `psql` prompt:

```bash
pg_dump -cC --inserts -U freecodecamp number_guess > number_guess.sql
```

The resulting dump can rebuild the project database with:

```bash
psql -U postgres < number_guess.sql
```

## User Stories and Test Requirements

The project must satisfy the following requirements:

- Create a folder named `number_guessing_game`.
- Create `number_guess.sh` inside `number_guessing_game`.
- Give `number_guess.sh` executable permissions.
- Add a Bash shebang to the top of `number_guess.sh`.
- Turn `number_guessing_game` into a Git repository in the CodeRoad workspace.
- Make at least five commits inside that CodeRoad repository.
- Use `Initial commit` as the first commit message.
- Start the remaining CodeRoad commit messages with `fix:`, `feat:`,
  `refactor:`, `chore:`, or `test:`.
- Finish the CodeRoad project on the `main` branch with no uncommitted changes.
- Create a `number_guess` database.
- Store user information in the database.
- Allow usernames up to 22 characters.
- Randomly generate a secret number between 1 and 1000.
- Prompt for a username with:

```text
Enter your username:
```

- If the username is new, print:

```text
Welcome, <username>! It looks like this is your first time here.
```

- If the username already exists, print:

```text
Welcome back, <username>! You have played <games_played> games, and your best game took <best_game> guesses.
```

- Prompt for the first guess with:

```text
Guess the secret number between 1 and 1000:
```

- If the guess is not an integer, print:

```text
That is not an integer, guess again:
```

- If the guess is lower than the secret number, print:

```text
It's higher than that, guess again:
```

- If the guess is higher than the secret number, print:

```text
It's lower than that, guess again:
```

- When the player guesses correctly, print:

```text
You guessed it in <number_of_guesses> tries. The secret number was <secret_number>. Nice job!
```

- After a completed game, update the player's total games played.
- After a completed game, update the player's best game if the new guess count
  is better than the previous best.
- The script should only ask for username and guesses, with no extra prompts.

## Required Submission Link

freeCodeCamp asks for the public repository URL that contains the required
files. For this repository, the most precise public link for the required
submission files is the `number_guessing_game` folder URL after the commit has
been pushed:

```text
https://github.com/Zendin110206/tugas_python_ai_b10/tree/main/FreeCodeCamp%20Certifications%20Relational%20Databases/Certification%20Projects/Project%205/number_guessing_game
```

That folder contains:

- `number_guess.sql`
- `number_guess.sh`

## Notes

- `number_guess.sql` is the final exported database dump. It should not be
  hand-edited unless the database is intentionally rebuilt and exported again.
- `number_guess.sh` is the final executable script used by the tests.
- The local Git repository requirement belongs to the CodeRoad project
  workspace. This main learning repository stores the final artifact and
  cleaned supporting documentation.
- The freeCodeCamp tests are strict about file names, executable permission,
  prompt wording, output wording, database persistence, and final Git state
  inside the CodeRoad workspace.
