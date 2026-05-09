# Terminal Work Log

## Purpose

This file documents the main terminal workflow used to complete the **Build a
Salon Appointment Scheduler** certification project.

It is not the final submission file. The final required submission files are
`salon.sql` and `salon.sh`.

## Environment

- Platform: freeCodeCamp Codespaces
- Database client: `psql`
- PostgreSQL user: `freecodecamp`
- Starting database: `postgres`
- Final project database: `salon`
- Script file: `salon.sh`

## PostgreSQL Service

If PostgreSQL is not running in a local or containerized environment, start it
from the Bash terminal:

```bash
sudo service postgresql start
```

The freeCodeCamp Codespaces environment usually has PostgreSQL ready, but this
command is useful when rebuilding or testing the workflow manually.

## Login and Database Setup

```bash
psql --username=freecodecamp --dbname=postgres
```

```sql
CREATE DATABASE salon;
\c salon
```

The database was created successfully and the `psql` session was connected to
`salon`.

## Table Creation Plan

The database uses three tables:

```sql
CREATE TABLE customers();
CREATE TABLE services();
CREATE TABLE appointments();
```

The tables were then structured to satisfy the project requirements.

## Table Structure

### `customers`

```sql
CREATE TABLE customers (
  customer_id SERIAL PRIMARY KEY,
  phone VARCHAR UNIQUE NOT NULL,
  name VARCHAR NOT NULL
);
```

### `services`

```sql
CREATE TABLE services (
  service_id SERIAL PRIMARY KEY,
  name VARCHAR NOT NULL
);
```

### `appointments`

```sql
CREATE TABLE appointments (
  appointment_id SERIAL PRIMARY KEY,
  customer_id INT NOT NULL REFERENCES customers(customer_id),
  service_id INT NOT NULL REFERENCES services(service_id),
  time VARCHAR NOT NULL
);
```

The `appointments` table depends on both `customers` and `services`, so those
parent tables must exist before the foreign keys can be added.

## Seed Services

The final database dump contains the following services:

```sql
INSERT INTO services(name) VALUES('Haircut');
INSERT INTO services(name) VALUES('Coloring');
INSERT INTO services(name) VALUES('Perm');
INSERT INTO services(name) VALUES('Style');
INSERT INTO services(name) VALUES('Trim');
```

The first service receives `service_id = 1`, which satisfies the project
requirement.

## Script Setup

The script file was created as `salon.sh` and starts with a Bash shebang:

```bash
#!/bin/bash
```

Executable permission is required:

```bash
chmod +x salon.sh
```

The script uses this reusable PostgreSQL command:

```bash
PSQL="psql -X --username=freecodecamp --dbname=salon --tuples-only -c"
```

## Main Script Flow

The submitted script follows this sequence:

1. Print the salon title and welcome message.
2. Query and display the available services.
3. Read the selected service ID.
4. If the service ID does not exist, show the menu again.
5. Ask for the customer phone number.
6. Search for an existing customer by phone.
7. If no customer exists, ask for the customer name and insert it.
8. Ask for the appointment time.
9. Insert the appointment row.
10. Print the required confirmation message.

## Manual Test Flow

Example first-time customer flow:

```text
1
555-555-5555
Fabio
10:30
```

Expected result:

```text
I have put you down for a Haircut at 10:30, Fabio.
```

Example returning customer flow:

```text
2
555-555-5555
11am
```

Expected result:

```text
I have put you down for a Coloring at 11am, Fabio.
```

## Verification Queries

After running the script, the tables can be inspected with:

```sql
SELECT * FROM services ORDER BY service_id;
SELECT * FROM customers ORDER BY customer_id;
SELECT * FROM appointments ORDER BY appointment_id;
```

The table structure can be verified with:

```sql
\d customers
\d services
\d appointments
```

## Final Export

After the database and script passed the project tests, the `psql` session was
closed:

```sql
\q
```

The database dump was created from the Bash terminal:

```bash
pg_dump -cC --inserts -U freecodecamp salon > salon.sql
```

The generated `salon.sql` file, together with `salon.sh`, is required for the
freeCodeCamp certification project submission.
