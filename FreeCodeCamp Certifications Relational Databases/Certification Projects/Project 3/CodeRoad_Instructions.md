# CodeRoad Instructions

## Project Context

This file records the original freeCodeCamp project requirements for the
**Build a Salon Appointment Scheduler** certification project.

The project runs in a virtual Linux environment through GitHub Codespaces,
CodeRoad, or an equivalent local Dev Container setup. The final required
submission files are:

- `salon.sql`
- `salon.sh`

`salon.sql` is created with `pg_dump` after the database passes all project
tests. `salon.sh` is the interactive Bash program used to schedule salon
appointments.

## Required Workflow

1. Open the project environment.
2. Start CodeRoad inside VS Code.
3. Log in to PostgreSQL from the Bash terminal.
4. Create a database named `salon`.
5. Create the required tables, columns, keys, and seed services.
6. Write an executable Bash script named `salon.sh`.
7. Run the script until appointments can be created successfully.
8. Pass all automated project tests.
9. Export the database dump to `salon.sql`.
10. Save both `salon.sql` and `salon.sh` in a public repository and submit the
    repository URL to freeCodeCamp.

## PostgreSQL Login

Run this command from the Bash terminal:

```bash
psql --username=freecodecamp --dbname=postgres
```

After creating the project database, connect to it:

```sql
\c salon
```

## Script Query Pattern

The project allows SQL queries to be executed from the Bash script with this
pattern:

```bash
psql --username=freecodecamp --dbname=salon -c "SQL QUERY HERE"
```

The submitted script stores that command in a reusable variable:

```bash
PSQL="psql -X --username=freecodecamp --dbname=salon --tuples-only -c"
```

`--tuples-only` is useful because it removes the table header and row-count
footer from `psql` output. The result can still include padding spaces, so the
script trims selected values with `sed -E 's/^ +| +$//g'`.

## Database Dump Command

After all tests pass, run this command from the Bash terminal, not from inside
the `psql` prompt:

```bash
pg_dump -cC --inserts -U freecodecamp salon > salon.sql
```

The resulting `salon.sql` file can rebuild the database with:

```bash
psql -U postgres < salon.sql
```

## User Stories and Test Requirements

The project must satisfy the following requirements:

- Create a database named `salon`.
- Connect to `salon`.
- Create tables named `customers`, `appointments`, and `services`.
- Each table must have a primary key column that automatically increments.
- Each primary key must follow the `table_name_id` naming convention:
  - `customer_id`
  - `appointment_id`
  - `service_id`
- `appointments.customer_id` must reference `customers.customer_id`.
- `appointments.service_id` must reference `services.service_id`.
- `customers.phone` must be a `VARCHAR` column and must be unique.
- `customers` and `services` must each have a `name` column.
- `appointments` must have a `time` column with type `VARCHAR`.
- The `services` table must contain at least three service rows.
- One service row must have `service_id = 1`.
- Create a script file named `salon.sh` in the project folder.
- `salon.sh` must use a Bash shebang.
- `salon.sh` must have executable permissions.
- The script must not use the `clear` command, because the tests inspect
  terminal output.
- Before the first input prompt, the script must display a numbered service
  list using the format `#) service`.
- If the selected service does not exist, the script must show the service list
  again.
- The script must read input into these variables:
  - `SERVICE_ID_SELECTED`
  - `CUSTOMER_PHONE`
  - `CUSTOMER_NAME`
  - `SERVICE_TIME`
- If the entered phone number does not exist, the script must ask for the
  customer name and insert the new customer.
- If the phone number already exists, the script should reuse the existing
  customer.
- The script must insert a row into `appointments` using the selected service,
  customer, and time.
- After the appointment is inserted, the script must print this message pattern:

```text
I have put you down for a <service> at <time>, <name>.
```

- The script must finish running after completing each task flow.

## Notes

- `examples.txt` is kept as the reference output format provided by the
  freeCodeCamp project.
- The database dump in `salon.sql` is the final project artifact. It should not
  be hand-edited unless the database is intentionally rebuilt and exported
  again.
- The freeCodeCamp tests are strict about output order, prompt wording, file
  names, executable permissions, and whether the script exits cleanly.
