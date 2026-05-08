#! /bin/bash

if [[ $1 == "test" ]]
then
  PSQL="psql --username=postgres --dbname=worldcuptest -t --no-align -c"
else
  PSQL="psql --username=freecodecamp --dbname=worldcup -t --no-align -c"
fi

# Do not change code above this line. Use the PSQL variable above to query your database.

echo "$($PSQL "TRUNCATE teams, games RESTART IDENTITY")"

# This project keeps the original two-pass import workflow:
# first insert unique teams, then insert games with the generated team IDs.
cat games.csv | while IFS="," read -r YEAR ROUND WINNER OPPONENT WINNER_GOALS OPPONENT_GOALS
do
  # Skip column name
  if [[ "$WINNER" != "winner" ]]
  then
    TEAM_ID_WINNER=$($PSQL "SELECT team_id FROM teams WHERE name='$WINNER'")
    TEAM_ID_OPPONENT=$($PSQL "SELECT team_id FROM teams WHERE name='$OPPONENT'")

    if [[ -z $TEAM_ID_WINNER ]]
    then
      TEAMS_WINNER=$($PSQL "INSERT INTO teams(name) VALUES('$WINNER')")
      echo "Inserted team: $WINNER"
    else
      echo "Team already exist : $WINNER, SKIPPED"
    fi

    if [[ -z $TEAM_ID_OPPONENT ]]
    then
      TEAMS_WINNER=$($PSQL "INSERT INTO teams(name) VALUES('$OPPONENT')")
      echo "Inserted team: $OPPONENT"
    else
      echo "Team already exist : $OPPONENT, SKIPPED"
    fi
  fi
done

cat games.csv | while IFS="," read -r YEAR ROUND WINNER OPPONENT WINNER_GOALS OPPONENT_GOALS
do
  # Skip column name
  if [[ "$YEAR" != "year" ]]
  then
    TEAM_ID_WINNER=$($PSQL "SELECT team_id FROM teams WHERE name='$WINNER'")
    TEAM_ID_OPPONENT=$($PSQL "SELECT team_id FROM teams WHERE name='$OPPONENT'")

    INSERT_MATCHES_RESULT=$($PSQL "INSERT INTO games(year, round, winner_id, opponent_id, winner_goals, opponent_goals) VALUES($YEAR, '$ROUND', $TEAM_ID_WINNER, $TEAM_ID_OPPONENT, $WINNER_GOALS, $OPPONENT_GOALS)")
  fi
done
