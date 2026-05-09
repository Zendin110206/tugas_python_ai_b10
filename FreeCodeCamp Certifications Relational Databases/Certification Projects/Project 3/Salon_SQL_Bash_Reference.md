# Salon SQL and Bash Reference

## Purpose

This reference documents the PostgreSQL and Bash patterns used in the **Build a
Salon Appointment Scheduler** certification project.

It focuses on the syntax needed to understand, rebuild, and debug the submitted
`salon.sh` workflow without changing the final project behavior.

## Project Files

| File | Purpose |
| --- | --- |
| `CodeRoad_Instructions.md` | Cleaned version of the project requirements. |
| `Database_Blueprint.md` | Schema and relationship planning notes. |
| `Terminal_Work_Log.md` | Main terminal workflow used to complete the project. |
| `examples.txt` | Reference output examples from the project. |
| `salon.sh` | Final interactive Bash script. |
| `salon.sql` | Final database dump required for submission. |

## Reusable `psql` Command

The script stores the PostgreSQL command in one variable:

```bash
PSQL="psql -X --username=freecodecamp --dbname=salon --tuples-only -c"
```

| Part | Meaning |
| --- | --- |
| `psql` | Runs the PostgreSQL command-line client. |
| `-X` | Prevents user startup files from changing command behavior. |
| `--username=freecodecamp` | Connects with the freeCodeCamp database user. |
| `--dbname=salon` | Runs queries against the `salon` database. |
| `--tuples-only` | Prints row values without headers or row-count footers. |
| `-c` | Runs one SQL command from Bash. |

Using a variable keeps every SQL call shorter:

```bash
SERVICE_NAME_LIST=$($PSQL "SELECT service_id, name FROM services ORDER BY service_id")
```

## Service Menu Query

The project requires a numbered service list before the first input prompt:

```bash
SERVICE_NAME_LIST=$($PSQL "SELECT service_id, name FROM services ORDER BY service_id")
echo "$SERVICE_NAME_LIST" | while read SERVICE_ID BAR NAME
do
  echo "$SERVICE_ID) $NAME"
done
```

| Part | Meaning |
| --- | --- |
| `SELECT service_id, name` | Gets the ID and service name needed for menu display. |
| `ORDER BY service_id` | Keeps the menu stable and predictable. |
| `while read SERVICE_ID BAR NAME` | Splits each output line into the service ID, separator, and service name. |
| `echo "$SERVICE_ID) $NAME"` | Prints the required menu format. |

The middle variable `BAR` receives the pipe separator from aligned `psql`
output. It is not used in the final display.

## Invalid Service Handling

After the user selects a service ID, the script checks whether the ID exists:

```bash
SERVICE_EXIST=$($PSQL "SELECT service_id FROM services WHERE service_id = $SERVICE_ID_SELECTED")

if [[ -z $SERVICE_EXIST ]]
then
  MAIN_MENU "I could not find that service. What would you like today?"
fi
```

| Expression | Meaning |
| --- | --- |
| `SELECT service_id ...` | Returns a value only if the service exists. |
| `[[ -z $SERVICE_EXIST ]]` | Checks whether the query result is empty. |
| `MAIN_MENU "message"` | Shows the service menu again with the required error message. |

This recursive menu call works for this small project because each invalid
selection simply restarts the menu flow.

## Customer Lookup and Insert

The phone number is used to find an existing customer:

```bash
CUSTOMER_NAME=$($PSQL "SELECT name FROM customers WHERE phone = '$CUSTOMER_PHONE'")
```

If the phone number is new, the script asks for the customer name and inserts a
new customer:

```bash
if [[ -z $CUSTOMER_NAME ]]
then
  echo -e "\nI don't have a record for that phone number, what's your name?"
  read CUSTOMER_NAME
  INSERT_CUSTOMER_RESULT=$($PSQL "INSERT INTO customers(phone, name) VALUES('$CUSTOMER_PHONE', '$CUSTOMER_NAME')")
fi
```

The `customers.phone` column is unique, so one phone number should map to one
customer record.

## Trimming `psql` Output

`--tuples-only` removes headers and footers, but aligned `psql` output can
still contain leading or trailing spaces. The script trims selected values:

```bash
CUSTOMER_NAME_FORMATTED=$(echo $CUSTOMER_NAME | sed -E 's/^ +| +$//g')
SERVICE_NAME_FORMATTED=$(echo $SERVICE_NAME | sed -E 's/^ +| +$//g')
```

| Pattern | Meaning |
| --- | --- |
| `sed -E` | Enables extended regular expressions. |
| `^ +` | Matches spaces at the beginning of the value. |
| ` +$` | Matches spaces at the end of the value. |
| `\|` | Means "or" inside the regular expression. |
| `g` | Applies the replacement globally. |

The practical effect:

```bash
echo "$(echo '   Fabio   ' | sed -E 's/^ +| +$//g')."
```

Output:

```text
Fabio.
```

This is important because the final confirmation message must be clean:

```text
I have put you down for a Haircut at 10:30, Fabio.
```

## Appointment Insert

After the service, customer, and time are known, the script inserts an
appointment:

```bash
CUSTOMER_ID=$($PSQL "SELECT customer_id FROM customers WHERE phone='$CUSTOMER_PHONE'")

INSERT_APPOINTMENT_RESULT=$($PSQL "INSERT INTO appointments(customer_id, service_id, time) VALUES($CUSTOMER_ID, $SERVICE_ID_SELECTED, '$SERVICE_TIME')")
```

Important quoting rules:

| Value | SQL Quoting |
| --- | --- |
| `CUSTOMER_ID` | Unquoted, because it is an integer foreign key. |
| `SERVICE_ID_SELECTED` | Unquoted, because it is an integer foreign key. |
| `SERVICE_TIME` | Quoted, because it is text. |

## Final Confirmation Message

The script finishes with the required output:

```bash
echo -e "\nI have put you down for a $SERVICE_NAME_FORMATTED at $SERVICE_TIME, $CUSTOMER_NAME_FORMATTED."
```

The message must include:

- selected service name
- appointment time
- customer name

The script must exit after this message so the freeCodeCamp tests can finish.

## Verification Queries

Use these commands inside `psql` to inspect the final database:

```sql
\d customers
\d services
\d appointments
```

```sql
SELECT * FROM services ORDER BY service_id;
SELECT * FROM customers ORDER BY customer_id;
SELECT * FROM appointments ORDER BY appointment_id;
```

Expected service seed count:

```sql
SELECT COUNT(*) FROM services;
```

The final dump contains five service rows.

## Common Mistakes

| Problem | Likely Cause | Fix |
| --- | --- | --- |
| Tests cannot run the script | `salon.sh` is not executable. | Run `chmod +x salon.sh`. |
| Menu output disappears | Script uses `clear`. | Remove `clear`; tests inspect output. |
| Invalid service does not repeat menu | Missing recursive or loop-based menu flow. | Show the service list again when service ID is invalid. |
| Customer inserted every time | Existing phone lookup is not checked. | Query `customers` by phone before inserting. |
| Appointment insert fails | Missing customer or service foreign key. | Verify both IDs exist before inserting. |
| Confirmation has extra spaces | Raw `psql` output was printed directly. | Trim selected text with `sed -E 's/^ +| +$//g'`. |
| Script keeps running after booking | Menu loop does not exit. | Let the function finish after the success message. |
