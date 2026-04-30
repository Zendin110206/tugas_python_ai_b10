# Database Blueprint

## Purpose

This file is the planning reference used before writing the SQL statements for
the **Build a Celestial Bodies Database** certification project.

The SQL was still written manually in the terminal. This blueprint only defines
the schema, required columns, relationships, and seed data needed to satisfy the
freeCodeCamp tests.

## Important Naming Constraint

For this specific freeCodeCamp project, the tests require singular table names:

- `galaxy`
- `star`
- `planet`
- `moon`

The table names should not be changed to plural forms such as `galaxies` or
`planets`, even though plural names may be used in other database projects.

## Schema Blueprint

### 1. `galaxy`

Minimum requirement: at least five columns.

| Column | Type | Constraint | Purpose |
| --- | --- | --- | --- |
| `galaxy_id` | `SERIAL` | `PRIMARY KEY` | Auto-incrementing unique identifier. |
| `name` | `VARCHAR` | `UNIQUE`, `NOT NULL` | Galaxy name. Required by the project. |
| `description` | `TEXT` | - | Satisfies the required `TEXT` data type. |
| `age_in_millions_of_years` | `INT` | `NOT NULL` | Satisfies one required non-key `INT` column. |
| `distance_from_earth_ly` | `NUMERIC` | - | Satisfies the required `NUMERIC` data type. |

### 2. `star`

Minimum requirement: at least five columns.

| Column | Type | Constraint | Purpose |
| --- | --- | --- | --- |
| `star_id` | `SERIAL` | `PRIMARY KEY` | Auto-incrementing unique identifier. |
| `name` | `VARCHAR` | `UNIQUE`, `NOT NULL` | Star name. Required by the project. |
| `galaxy_id` | `INT` | `NOT NULL`, foreign key to `galaxy(galaxy_id)` | Connects each star to one galaxy. |
| `is_binary` | `BOOLEAN` | - | Satisfies one required `BOOLEAN` column. |
| `temperature_in_kelvin` | `INT` | - | Stores approximate star temperature. |

### 3. `planet`

Minimum requirement: at least five columns.

| Column | Type | Constraint | Purpose |
| --- | --- | --- | --- |
| `planet_id` | `SERIAL` | `PRIMARY KEY` | Auto-incrementing unique identifier. |
| `name` | `VARCHAR` | `UNIQUE`, `NOT NULL` | Planet name. Required by the project. |
| `star_id` | `INT` | `NOT NULL`, foreign key to `star(star_id)` | Connects each planet to one star. |
| `has_life` | `BOOLEAN` | - | Satisfies another required `BOOLEAN` column. |
| `is_spherical` | `BOOLEAN` | `NOT NULL` | Indicates whether the body is spherical. |

### 4. `moon`

Minimum requirement: at least five columns.

| Column | Type | Constraint | Purpose |
| --- | --- | --- | --- |
| `moon_id` | `SERIAL` | `PRIMARY KEY` | Auto-incrementing unique identifier. |
| `name` | `VARCHAR` | `UNIQUE`, `NOT NULL` | Moon name. Required by the project. |
| `planet_id` | `INT` | `NOT NULL`, foreign key to `planet(planet_id)` | Connects each moon to one planet. |
| `discovery_year` | `INT` | - | Stores the year the moon was discovered. |
| `orbital_period_in_days` | `NUMERIC` | - | Stores orbital period as a decimal value. |

### 5. `asteroid`

Additional table requirement: the project needs at least five tables, so this
table is added as the fifth table.

| Column | Type | Constraint | Purpose |
| --- | --- | --- | --- |
| `asteroid_id` | `SERIAL` | `PRIMARY KEY` | Auto-incrementing unique identifier. |
| `name` | `VARCHAR` | `UNIQUE`, `NOT NULL` | Asteroid name. |
| `diameter_in_km` | `NUMERIC` | `NOT NULL` | Approximate asteroid diameter. |

## Relationship Plan

The schema uses three main one-to-many relationships:

| Parent table | Child table | Foreign key | Meaning |
| --- | --- | --- | --- |
| `galaxy` | `star` | `star.galaxy_id` | One galaxy can contain many stars. |
| `star` | `planet` | `planet.star_id` | One star can have many planets. |
| `planet` | `moon` | `moon.planet_id` | One planet can have many moons. |

The foreign key columns intentionally use the same name as the referenced
primary key columns, which is required by the project tests.

## Seed Data

### `galaxy`

Minimum requirement: at least six rows.

| name | description | age_in_millions_of_years | distance_from_earth_ly |
| --- | --- | ---: | ---: |
| Milky Way | Our home galaxy | 13600 | 0.0 |
| Andromeda | Nearest major galaxy | 10000 | 2537000.0 |
| Triangulum | Spiral galaxy in Local Group | 10000 | 2730000.0 |
| Sombrero | Unbarred spiral galaxy | 9000 | 31000000.0 |
| Pinwheel | Face-on spiral galaxy | 10000 | 21000000.0 |
| Cartwheel | Ring galaxy | 12000 | 500000000.0 |

### `star`

Minimum requirement: at least six rows.

Assumed IDs:

- `galaxy_id = 1`: Milky Way
- `galaxy_id = 2`: Andromeda

| name | galaxy_id | is_binary | temperature_in_kelvin |
| --- | ---: | --- | ---: |
| Sun | 1 | `FALSE` | 5778 |
| Sirius | 1 | `TRUE` | 9940 |
| Betelgeuse | 1 | `FALSE` | 3600 |
| Rigel | 1 | `FALSE` | 12100 |
| Alpheratz | 2 | `TRUE` | 13800 |
| Mirach | 2 | `FALSE` | 3300 |

### `planet`

Minimum requirement: at least twelve rows.

Assumed IDs:

- `star_id = 1`: Sun
- `star_id = 2`: Sirius
- `star_id = 3`: Betelgeuse

| name | star_id | has_life | is_spherical |
| --- | ---: | --- | --- |
| Mercury | 1 | `FALSE` | `TRUE` |
| Venus | 1 | `FALSE` | `TRUE` |
| Earth | 1 | `TRUE` | `TRUE` |
| Mars | 1 | `FALSE` | `TRUE` |
| Jupiter | 1 | `FALSE` | `TRUE` |
| Saturn | 1 | `FALSE` | `TRUE` |
| Uranus | 1 | `FALSE` | `TRUE` |
| Neptune | 1 | `FALSE` | `TRUE` |
| Kepler-186f | 2 | `FALSE` | `TRUE` |
| Kepler-22b | 2 | `FALSE` | `TRUE` |
| Kepler-452b | 3 | `FALSE` | `TRUE` |
| Proxima b | 3 | `FALSE` | `TRUE` |

### `moon`

Minimum requirement: at least twenty rows.

Assumed IDs:

- `planet_id = 3`: Earth
- `planet_id = 4`: Mars
- `planet_id = 5`: Jupiter
- `planet_id = 6`: Saturn
- `planet_id = 7`: Uranus
- `planet_id = 8`: Neptune

| name | planet_id | discovery_year | orbital_period_in_days |
| --- | ---: | ---: | ---: |
| Luna | 3 | `NULL` | 27.3 |
| Phobos | 4 | 1877 | 0.3 |
| Deimos | 4 | 1877 | 1.2 |
| Io | 5 | 1610 | 1.7 |
| Europa | 5 | 1610 | 3.5 |
| Ganymede | 5 | 1610 | 7.1 |
| Callisto | 5 | 1610 | 16.6 |
| Mimas | 6 | 1789 | 0.9 |
| Enceladus | 6 | 1789 | 1.3 |
| Tethys | 6 | 1684 | 1.8 |
| Dione | 6 | 1684 | 2.7 |
| Rhea | 6 | 1672 | 4.5 |
| Titan | 6 | 1655 | 15.9 |
| Iapetus | 6 | 1671 | 79.3 |
| Miranda | 7 | 1948 | 1.4 |
| Ariel | 7 | 1851 | 2.5 |
| Umbriel | 7 | 1851 | 4.1 |
| Titania | 7 | 1787 | 8.7 |
| Oberon | 7 | 1787 | 13.4 |
| Triton | 8 | 1846 | 5.8 |

### `asteroid`

Minimum requirement: at least three rows.

| name | diameter_in_km |
| --- | ---: |
| Ceres | 939.4 |
| Vesta | 525.4 |
| Pallas | 512.0 |

## Execution Strategy

The SQL should be written in dependency order:

1. Create the `universe` database.
2. Connect to `universe`.
3. Create parent tables first: `galaxy`, then `star`, then `planet`, then
   `moon`.
4. Create the additional `asteroid` table.
5. Add primary keys and foreign keys.
6. Insert data in relationship order:
   - `galaxy`
   - `star`
   - `planet`
   - `moon`
   - `asteroid`
7. Verify table structure with `\d table_name`.
8. Verify data with `SELECT * FROM table_name;`.
9. Export the final passing database to `universe.sql`.

The order matters because foreign keys cannot reference tables or columns that
do not exist yet.
