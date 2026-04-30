# Terminal Work Log

## Purpose

This file documents the main terminal workflow used to complete the
**Build a Celestial Bodies Database** certification project.

It is not the final submission file. The final generated database dump is
`universe.sql`.

## Environment

- Platform: freeCodeCamp Codespaces
- Database client: `psql`
- PostgreSQL user: `freecodecamp`
- Starting database: `postgres`
- Final project database: `universe`

## Login and Database Setup

```bash
psql --username=freecodecamp --dbname=postgres
```

```sql
CREATE DATABASE universe;
\c universe
```

The database was created successfully and the `psql` session was connected to
`universe`.

## Initial Table Creation

```sql
CREATE TABLE galaxy();
CREATE TABLE star();
CREATE TABLE planet();
CREATE TABLE moon();
\d
```

At this point, the database contained the required base tables:

```text
galaxy
star
planet
moon
```

## Table Structure

### `galaxy`

```sql
ALTER TABLE galaxy
ADD COLUMN galaxy_id SERIAL,
ADD COLUMN name VARCHAR UNIQUE NOT NULL,
ADD COLUMN description TEXT,
ADD COLUMN age_in_millions_of_years INT NOT NULL,
ADD COLUMN distance_from_earth_ly NUMERIC;
```

### `star`

```sql
ALTER TABLE star
ADD COLUMN star_id SERIAL,
ADD COLUMN name VARCHAR UNIQUE NOT NULL,
ADD COLUMN galaxy_id INT NOT NULL,
ADD COLUMN is_binary BOOLEAN,
ADD COLUMN temperature_in_kelvin INT;
```

### `planet`

```sql
ALTER TABLE planet
ADD COLUMN planet_id SERIAL,
ADD COLUMN name VARCHAR UNIQUE NOT NULL,
ADD COLUMN star_id INT NOT NULL,
ADD COLUMN has_life BOOLEAN,
ADD COLUMN is_spherical BOOLEAN NOT NULL;
```

### `moon`

```sql
ALTER TABLE moon
ADD COLUMN moon_id SERIAL,
ADD COLUMN name VARCHAR UNIQUE NOT NULL,
ADD COLUMN planet_id INT NOT NULL,
ADD COLUMN discovery_year INT,
ADD COLUMN orbital_period_in_days NUMERIC;
```

### `asteroid`

```sql
CREATE TABLE asteroid(asteroid_id SERIAL PRIMARY KEY);

ALTER TABLE asteroid
ADD COLUMN name VARCHAR UNIQUE NOT NULL,
ADD COLUMN diameter_in_km NUMERIC NOT NULL;
```

The `asteroid` table was added as the fifth table because the project requires
at least five tables.

## Primary Keys

```sql
ALTER TABLE galaxy ADD PRIMARY KEY(galaxy_id);
ALTER TABLE star ADD PRIMARY KEY(star_id);
ALTER TABLE planet ADD PRIMARY KEY(planet_id);
ALTER TABLE moon ADD PRIMARY KEY(moon_id);
```

Each primary key follows the required `table_name_id` naming convention.

## Foreign Keys

```sql
ALTER TABLE star
ADD FOREIGN KEY(galaxy_id) REFERENCES galaxy(galaxy_id);
```

While working, I first tried the wrong referenced table for `planet.star_id`:

```sql
ALTER TABLE planet ADD FOREIGN KEY(star_id) REFERENCES galaxy(star_id);
```

PostgreSQL rejected it because `galaxy` does not have a `star_id` column. The
correct relationship is `planet.star_id -> star.star_id`, so the corrected
command was:

```sql
ALTER TABLE planet
ADD FOREIGN KEY(star_id) REFERENCES star(star_id);
```

The moon relationship was added after that:

```sql
ALTER TABLE moon
ADD FOREIGN KEY(planet_id) REFERENCES planet(planet_id);
```

This correction is useful to document because it shows why foreign keys must
reference the correct parent table and parent key.

## Data Inserts

### `galaxy`

```sql
INSERT INTO galaxy (name, description, age_in_millions_of_years, distance_from_earth_ly)
VALUES
  ('Milky Way', 'Our home galaxy', 13600, 0.0),
  ('Andromeda', 'Nearest major galaxy', 10000, 2537000.0),
  ('Triangulum', 'Spiral galaxy in Local Group', 10000, 2730000.0),
  ('Sombrero', 'Unbarred spiral galaxy', 9000, 31000000.0),
  ('Pinwheel', 'Face-on spiral galaxy', 10000, 21000000.0),
  ('Cartwheel', 'Ring galaxy', 12000, 500000000.0);
```

### `star`

```sql
INSERT INTO star (name, galaxy_id, is_binary, temperature_in_kelvin)
VALUES
  ('Sun', 1, FALSE, 5778),
  ('Sirius', 1, TRUE, 9940),
  ('Betelgeuse', 1, FALSE, 3600),
  ('Rigel', 1, FALSE, 12100),
  ('Alpheratz', 2, TRUE, 13800),
  ('Mirach', 2, FALSE, 3300);
```

### `planet`

```sql
INSERT INTO planet (name, star_id, has_life, is_spherical)
VALUES
  ('Mercury', 1, FALSE, TRUE),
  ('Venus', 1, FALSE, TRUE),
  ('Earth', 1, TRUE, TRUE),
  ('Mars', 1, FALSE, TRUE),
  ('Jupiter', 1, FALSE, TRUE),
  ('Saturn', 1, FALSE, TRUE),
  ('Uranus', 1, FALSE, TRUE),
  ('Neptune', 1, FALSE, TRUE),
  ('Kepler-186f', 2, FALSE, TRUE),
  ('Kepler-22b', 2, FALSE, TRUE),
  ('Kepler-452b', 3, FALSE, TRUE),
  ('Proxima b', 3, FALSE, TRUE);
```

### `moon`

```sql
INSERT INTO moon (name, planet_id, discovery_year, orbital_period_in_days)
VALUES
  ('Luna', 3, NULL, 27.3),
  ('Phobos', 4, 1877, 0.3),
  ('Deimos', 4, 1877, 1.2),
  ('Io', 5, 1610, 1.7),
  ('Europa', 5, 1610, 3.5),
  ('Ganymede', 5, 1610, 7.1),
  ('Callisto', 5, 1610, 16.6),
  ('Mimas', 6, 1789, 0.9),
  ('Enceladus', 6, 1789, 1.3),
  ('Tethys', 6, 1684, 1.8),
  ('Dione', 6, 1684, 2.7),
  ('Rhea', 6, 1672, 4.5),
  ('Titan', 6, 1655, 15.9),
  ('Iapetus', 6, 1671, 79.3),
  ('Miranda', 7, 1948, 1.4),
  ('Ariel', 7, 1851, 2.5),
  ('Umbriel', 7, 1851, 4.1),
  ('Titania', 7, 1787, 8.7),
  ('Oberon', 7, 1787, 13.4),
  ('Triton', 8, 1846, 5.8);
```

### `asteroid`

```sql
INSERT INTO asteroid (name, diameter_in_km)
VALUES
  ('Ceres', 939.4),
  ('Vesta', 525.4),
  ('Pallas', 512.0);
```

## Verification Queries

After creating the schema and inserting the data, each table was inspected with:

```sql
\d galaxy
\d star
\d planet
\d moon
\d asteroid
```

The data was verified with:

```sql
SELECT * FROM galaxy;
SELECT * FROM star;
SELECT * FROM planet;
SELECT * FROM moon;
SELECT * FROM asteroid;
```

Expected row counts:

| Table | Expected rows |
| --- | ---: |
| `galaxy` | 6 |
| `star` | 6 |
| `planet` | 12 |
| `moon` | 20 |
| `asteroid` | 3 |

## Final Export

After the database passed the project requirements, the `psql` session was
closed:

```sql
\q
```

The database dump was created from the Bash terminal:

```bash
pg_dump -cC --inserts -U freecodecamp universe > universe.sql
```

The generated `universe.sql` file is the required freeCodeCamp submission file.
