-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS spaces CASCADE;
DROP TABLE IF EXISTS bookings CASCADE;

-- Then, we recreate them
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL
);

CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    space_name TEXT NOT NULL,
    space_location TEXT NOT NULL,
    space_description TEXT NOT NULL,
    price_per_night INTEGER NOT NULL,
    available_from DATE NOT NULL,
    available_to DATE NOT NULL
);

CREATE TABLE bookings(
    id SERIAL PRIMARY KEY,
    space_id INTEGER REFERENCES spaces(id),
    user_id INTEGER REFERENCES users(id),
    booking_date DATE NOT NULL,
    booking_status TEXT NOT NULL DEFAULT 'pending'

);

TRUNCATE TABLE users RESTART IDENTITY CASCADE;

INSERT INTO users
(email, password_hash)
VALUES (
    'test@test.com',
    'hashed_password'
    );

INSERT INTO spaces
(
    user_id,
    space_name,
    space_location,
    space_description,
    price_per_night,
    available_from,
    available_to
)
VALUES (
    1,
    'Test Space',
    'Test Location',
    'Test Description',
    100,
    '2026-05-19',
    '2026-05-30'
);

INSERT INTO bookings
(
    space_id,
    user_id,
    booking_date,
    booking_status
)
VALUES(
    1,
    1,
    '2026-05-20',
    'approved'
);