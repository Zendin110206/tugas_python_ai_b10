# Number Guessing SQL and Bash Reference

## Purpose

This reference documents the PostgreSQL and Bash patterns used in the **Build a
Number Guessing Game** certification project.

It focuses on the syntax needed to understand, rebuild, and debug the submitted
`number_guess.sh` workflow without changing the final project behavior.

## Project Files

| File | Purpose |
| --- | --- |
| `CodeRoad_Instructions.md` | Cleaned version of the project requirements. |
| `Database_Blueprint.md` | Schema and state planning notes. |
| `Terminal_Work_Log.md` | Main terminal workflow used to complete the project. |
| `number_guessing_game/number_guess.sh` | Final executable Bash script. |
| `number_guessing_game/number_guess.sql` | Final database dump required for submission. |

## Reusable `psql` Command

The script stores the PostgreSQL command in one variable:

```bash
PSQL="psql --username=freecodecamp --dbname=number_guess -t --no-align -c"
```

| Part | Meaning |
| --- | --- |
| `psql` | Runs the PostgreSQL command-line client. |
| `--username=freecodecamp` | Connects with the freeCodeCamp database user. |
| `--dbname=number_guess` | Runs queries against the `number_guess` database. |
| `-t` | Prints tuples only, without table headers or row-count footers. |
| `--no-align` | Prints compact values without padded table formatting. |
| `-c` | Runs one SQL command from Bash. |

Using one variable keeps every query shorter:

```bash
GET_USERNAME=$($PSQL "SELECT games_played, best_game FROM users WHERE username = '$USERNAME'")
```

## Secret Number Generation

The game generates a random number from 1 to 1000:

```bash
SECRET_NUMBER=$(( RANDOM % 1000 + 1 ))
```

| Part | Meaning |
| --- | --- |
| `RANDOM` | Bash built-in value from 0 to 32767. |
| `% 1000` | Keeps the value in the range 0 to 999. |
| `+ 1` | Shifts the range to 1 to 1000. |
| `$(( ... ))` | Runs arithmetic expansion and returns the result. |

The secret number is generated once per script run.

## Guess Counter

The submitted script starts the counter at zero:

```bash
GUESS_COUNT=0
```

Each guess increments the counter:

```bash
(( GUESS_COUNT++ ))
```

This includes invalid guesses, because the project says the final message
should report the number of tries, and every entered guess is part of the game
attempt.

## Username Input

The script asks for a username:

```bash
echo -e "\nEnter your username:"
read USERNAME
```

The database lookup checks whether the username already exists:

```bash
GET_USERNAME=$($PSQL "SELECT games_played, best_game FROM users WHERE username = '$USERNAME'")
```

If the result is empty, the player is new:

```bash
if [[ -z "$GET_USERNAME" ]]
then
  echo -e "\nWelcome, $USERNAME! It looks like this is your first time here."
  INSERT_USERNAME_PLAYER=$($PSQL "INSERT INTO users(username) VALUES('$USERNAME')")
fi
```

The `users` table has default values, so a new insert only needs the username.

## Returning User Output

For an existing username, the query returns two values:

```text
games_played|best_game
```

The script splits those values with `IFS="|"`:

```bash
echo "$GET_USERNAME" | while IFS="|" read GAME_PLAYED BEST_GAME
do
  echo -e "\nWelcome back, $USERNAME! You have played $GAME_PLAYED games, and your best game took $BEST_GAME guesses."
done
```

| Part | Meaning |
| --- | --- |
| `echo "$GET_USERNAME"` | Sends the query output into the loop. |
| `IFS="|"` | Uses the pipe character as the field separator. |
| `read GAME_PLAYED BEST_GAME` | Assigns the two query values to Bash variables. |

## Guess Input and Loop

The first prompt is:

```bash
echo -e "\nGuess the secret number between 1 and 1000:"
read GUESS
(( GUESS_COUNT++ ))
```

The loop continues while the current guess is not the secret number:

```bash
while (( GUESS != SECRET_NUMBER ))
do
  # Validate and guide the next guess.
done
```

`(( ... ))` is arithmetic evaluation. Inside this syntax, variables do not need
the `$` prefix.

## Integer Validation

The project requires a special message when the player enters a non-integer
guess:

```bash
if [[ ! $GUESS =~ ^[0-9]+$ ]]
then
  echo -e "\nThat is not an integer, guess again:"
fi
```

| Pattern | Meaning |
| --- | --- |
| `!` | Reverses the result. |
| `=~` | Tests the value against a regular expression. |
| `^` | Start of the string. |
| `[0-9]+` | One or more digits. |
| `$` | End of the string. |

So the condition means: if the input is not made only of digits, print the
invalid-input message.

## Higher and Lower Guidance

If the guess is lower than the secret number:

```bash
elif (( GUESS < SECRET_NUMBER ))
then
  echo -e "\nIt's higher than that, guess again:"
```

If the guess is higher than the secret number:

```bash
else
  echo -e "\nIt's lower than that, guess again:"
fi
```

The wording is from the perspective of the secret number:

| Player Guess | Secret Number | Message |
| --- | --- | --- |
| Too low | Higher than guess | `It's higher than that, guess again:` |
| Too high | Lower than guess | `It's lower than that, guess again:` |

## Winning Message

When the loop ends, the current guess equals the secret number:

```bash
echo -e "\nYou guessed it in $GUESS_COUNT tries. The secret number was $SECRET_NUMBER. Nice job!"
```

The script then updates the database.

## Updating Games Played

After a completed game, the total number of games is increased:

```bash
USERNAME_TOTAL_PLAYED=$($PSQL "UPDATE users SET games_played = games_played + 1 WHERE username = '$USERNAME'")
```

The assignment `USERNAME_TOTAL_PLAYED=...` captures the query result even though
the result text is not printed. This keeps the terminal output aligned with the
strict freeCodeCamp output requirements.

## Updating Best Game

The script reads the current best game:

```bash
GET_USERNAME_BEST_GAME=$($PSQL "SELECT best_game FROM users WHERE username = '$USERNAME'")
```

Then it updates `best_game` only when needed:

```bash
if (( GET_USERNAME_BEST_GAME == 0 || GUESS_COUNT < GET_USERNAME_BEST_GAME ))
then
  UPDATE_USERNAME_BEST_GAME=$($PSQL "UPDATE users SET best_game = $GUESS_COUNT WHERE username = '$USERNAME'")
fi
```

| Condition | Meaning |
| --- | --- |
| `GET_USERNAME_BEST_GAME == 0` | The user has no completed best game yet. |
| `GUESS_COUNT < GET_USERNAME_BEST_GAME` | The current game used fewer guesses than the stored best. |

This keeps the best score stable when a later game takes more guesses.

## Final Table Design

The final dump stores this table:

```sql
CREATE TABLE users (
  user_id SERIAL PRIMARY KEY,
  username VARCHAR(22) UNIQUE NOT NULL,
  games_played INT DEFAULT 0,
  best_game INT DEFAULT 0
);
```

The final `pg_dump` expands `SERIAL` into an integer column, a sequence, and a
default `nextval(...)` expression. That is normal PostgreSQL dump behavior.

## Manual Script Tests

Run the script:

```bash
./number_guess.sh
```

Example new user flow:

```text
Enter your username:
zaenal
Welcome, zaenal! It looks like this is your first time here.
Guess the secret number between 1 and 1000:
```

Example returning user message:

```text
Welcome back, zaenal! You have played 2 games, and your best game took 8 guesses.
```

Example invalid input response:

```text
That is not an integer, guess again:
```

Example win response:

```text
You guessed it in 8 tries. The secret number was 500. Nice job!
```

## Verification Queries

Use these commands inside `psql` to inspect the final database:

```sql
\d users
```

```sql
SELECT *
FROM users
ORDER BY user_id;
```

```sql
SELECT username, games_played, best_game
FROM users
WHERE username = 'zaenal';
```

## Common Mistakes

| Problem | Likely Cause | Fix |
| --- | --- | --- |
| Tests cannot run the script | `number_guess.sh` is not executable. | Run `chmod +x number_guess.sh`. |
| Username is rejected too early | `username` column is shorter than 22 characters. | Use `VARCHAR(22)`. |
| Returning user message is wrong | Query did not select both `games_played` and `best_game`. | Select both values and split them in the same order. |
| Extra database output appears | Raw `psql` update output was printed. | Capture update results in variables. |
| Invalid guesses are not counted | Counter increments only for valid guesses. | Increment after every input attempt. |
| Best game becomes worse | Script always updates `best_game`. | Update only when the new guess count is lower or stored best is `0`. |
| Tests reject the final message | Output text differs from the required sentence. | Match punctuation, spelling, and value order exactly. |
