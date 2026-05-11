#!/bin/bash

PSQL="psql --username=freecodecamp --dbname=number_guess -t --no-align -c"

SECRET_NUMBER=$(( RANDOM % 1000 + 1 ))
GUESS_COUNT=0

echo -e "\nEnter your username:"
read USERNAME

GET_USERNAME=$($PSQL "SELECT games_played, best_game FROM users WHERE username = '$USERNAME'")

if [[ -z "$GET_USERNAME" ]]
then
  echo -e "\nWelcome, $USERNAME! It looks like this is your first time here."
  INSERT_USERNAME_PLAYER=$($PSQL "INSERT INTO users(username) VALUES('$USERNAME')")

else
  echo "$GET_USERNAME" | while IFS="|" read GAME_PLAYED BEST_GAME
  do
    echo -e "\nWelcome back, $USERNAME! You have played $GAME_PLAYED games, and your best game took $BEST_GAME guesses."
  done

fi

echo -e "\nGuess the secret number between 1 and 1000:"
read GUESS
(( GUESS_COUNT++ ))

while (( GUESS != SECRET_NUMBER ))
do
  if [[ ! $GUESS =~ ^[0-9]+$ ]]
  then
    echo -e "\nThat is not an integer, guess again:"

  elif (( GUESS < SECRET_NUMBER ))
  then
    echo -e "\nIt's higher than that, guess again:"

  else
    echo -e "\nIt's lower than that, guess again:"
  fi

  read GUESS
  (( GUESS_COUNT++ ))

done

echo -e "\nYou guessed it in $GUESS_COUNT tries. The secret number was $SECRET_NUMBER. Nice job!"
USERNAME_TOTAL_PLAYED=$($PSQL "UPDATE users SET games_played = games_played + 1 WHERE username = '$USERNAME'")

GET_USERNAME_BEST_GAME=$($PSQL "SELECT best_game FROM users WHERE username = '$USERNAME'")

if (( GET_USERNAME_BEST_GAME == 0 || GUESS_COUNT < GET_USERNAME_BEST_GAME ))
then
  UPDATE_USERNAME_BEST_GAME=$($PSQL "UPDATE users SET best_game = $GUESS_COUNT WHERE username = '$USERNAME'")
fi
