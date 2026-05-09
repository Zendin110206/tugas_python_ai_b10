# Database Blueprint

## Purpose

This file documents the schema plan for the **Build a Salon Appointment
Scheduler** certification project.

The final database dump is stored in `salon.sql`. This blueprint explains the
table design, relationship logic, and why each table is needed.

## Project Goal

The project models a small salon appointment workflow:

1. The customer chooses a service.
2. The script checks whether the selected service exists.
3. The customer enters a phone number.
4. If the phone number is new, the customer is inserted into the database.
5. The customer chooses an appointment time.
6. The appointment is inserted by connecting the customer and service through
   foreign keys.

The database therefore needs to store three separate concepts:

- available salon services
- customers
- appointments

## Schema Blueprint

### 1. `services`

This table stores the list of salon services that can be selected from the
Bash program.

| Column | Type | Constraint | Purpose |
| --- | --- | --- | --- |
| `service_id` | `SERIAL` / integer sequence | `PRIMARY KEY` | Auto-incrementing service identifier. |
| `name` | `VARCHAR` | `NOT NULL` | Service name displayed in the menu. |

Seed services in the final dump:

| service_id | name |
| ---: | --- |
| 1 | Haircut |
| 2 | Coloring |
| 3 | Perm |
| 4 | Style |
| 5 | Trim |

The project only requires at least three services, but five services make the
menu closer to the sample output and easier to test.

### 2. `customers`

This table stores customer identity information.

| Column | Type | Constraint | Purpose |
| --- | --- | --- | --- |
| `customer_id` | `SERIAL` / integer sequence | `PRIMARY KEY` | Auto-incrementing customer identifier. |
| `phone` | `VARCHAR` | `UNIQUE`, `NOT NULL` | Stable lookup value entered by the customer. |
| `name` | `VARCHAR` | `NOT NULL` | Customer name used in the final confirmation message. |

The phone number is unique because it is used as the lookup key. If the same
phone number is entered again, the script should reuse the existing customer
instead of creating a duplicate customer row.

### 3. `appointments`

This table stores scheduled appointments.

| Column | Type | Constraint | Purpose |
| --- | --- | --- | --- |
| `appointment_id` | `SERIAL` / integer sequence | `PRIMARY KEY` | Auto-incrementing appointment identifier. |
| `customer_id` | `INT` | `NOT NULL`, foreign key to `customers(customer_id)` | Connects the appointment to one customer. |
| `service_id` | `INT` | `NOT NULL`, foreign key to `services(service_id)` | Connects the appointment to one service. |
| `time` | `VARCHAR` | `NOT NULL` | Stores the time value entered in the script. |

The `time` column is stored as `VARCHAR` because freeCodeCamp requires it. In a
production scheduler, a timestamp or date/time structure would usually be more
appropriate, but the certification project intentionally uses a simpler input
model.

## Relationship Plan

| Parent table | Child table | Foreign key | Meaning |
| --- | --- | --- | --- |
| `customers` | `appointments` | `appointments.customer_id` | One customer can have many appointments. |
| `services` | `appointments` | `appointments.service_id` | One service can be booked many times. |

`appointments` is the transaction table. It stores the actual booking and links
the customer to the selected service.

## Why Foreign Keys Are Needed

Without foreign keys, an appointment could accidentally point to a customer or
service that does not exist. The two foreign keys protect the data model:

- `appointments.customer_id` must match an existing `customers.customer_id`
- `appointments.service_id` must match an existing `services.service_id`

That keeps every appointment connected to valid database records.

## Execution Strategy

The database should be built in dependency order:

1. Create the `salon` database.
2. Create `customers`.
3. Create `services`.
4. Create `appointments`.
5. Add the primary keys.
6. Add the unique constraint on `customers.phone`.
7. Add the foreign keys from `appointments`.
8. Insert the seed services.
9. Verify the structure with `\d table_name`.
10. Run `salon.sh` to create test appointments.
11. Export the final passing database to `salon.sql`.

This order matters because `appointments` depends on both `customers` and
`services`.
