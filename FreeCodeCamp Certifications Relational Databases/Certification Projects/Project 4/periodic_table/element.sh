#!/bin/bash

PSQL="psql --username=freecodecamp --dbname=periodic_table -t --no-align -c"

if [[ -z $1 ]]
then
  echo "Please provide an element as an argument."

else
  if [[ $1 =~ ^[0-9]+$ ]]
  then
    # Get atomic number
    GET_ATOMIC_NUMBER=$($PSQL "SELECT name, symbol, type, atomic_mass, melting_point_celsius, boiling_point_celsius FROM elements JOIN properties USING(atomic_number) JOIN types USING(type_id) WHERE atomic_number = $1")

    if [[ -z $GET_ATOMIC_NUMBER ]]
    then
      echo "I could not find that element in the database."

    else
      echo "$GET_ATOMIC_NUMBER" | while IFS="|" read NAME SYMBOL TYPE ATOMIC_MASS MELTING BOILING
      do
        echo "The element with atomic number $1 is $NAME ($SYMBOL). It's a $TYPE, with a mass of $ATOMIC_MASS amu. $NAME has a melting point of $MELTING celsius and a boiling point of $BOILING celsius."
      done
    fi

  else
    GET_SYMBOL_NAME=$($PSQL "SELECT atomic_number, name, symbol, type, atomic_mass, melting_point_celsius, boiling_point_celsius FROM elements JOIN properties USING(atomic_number) JOIN types USING(type_id) WHERE symbol = '$1' OR name = '$1'")

    if [[ -z $GET_SYMBOL_NAME ]]
    then
      echo "I could not find that element in the database."

    else
      echo "$GET_SYMBOL_NAME" | while IFS="|" read ATOMIC_NUMBER NAME SYMBOL TYPE ATOMIC_MASS MELTING BOILING
      do
        echo "The element with atomic number $ATOMIC_NUMBER is $NAME ($SYMBOL). It's a $TYPE, with a mass of $ATOMIC_MASS amu. $NAME has a melting point of $MELTING celsius and a boiling point of $BOILING celsius."
      done
    fi
  fi
fi
