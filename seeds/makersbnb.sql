DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS spaces;
DROP TABLE IF EXISTS users;

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

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    space_id INTEGER REFERENCES spaces(id),
    user_id INTEGER REFERENCES users(id),
    booking_date DATE NOT NULL,
    booking_status TEXT NOT NULL DEFAULT 'pending'
);


INSERT INTO users (email, password_hash) VALUES
    ('emma.thornton@gmail.com', '$2b$12$LQv3c1yqBweJTgPoXc5vQORtLx7XjG1mYv3wKfR8TqZdN7mVk9Hxy'),
    ('james.nakamura@outlook.com', '$2b$12$9XwZkVpFgj2mN5qWxTcYvuBbN8hLkJpQrS1tY3uV7wX0zA1B2cD3e'),
    ('sofia.mueller@yahoo.com', '$2b$12$KpL4mN6oQrS8tUvWxYz0A1B2cD3eF4gH5iJ6kL7mN8oP9qR0sT1uV'),
    ('marcus.oyelaran@proton.me', '$2b$12$4fG5hI6jK7lM8nO9pQ0rS1tU2vW3xY4zA5bC6dE7fG8hI9jK0lM1n'),
    ('lily.chen@icloud.com', '$2b$12$R2sT3uV4wX5yZ6aB7cD8eF9gH0iJ1kL2mN3oP4qR5sT6uV7wX8yZ9');


INSERT INTO spaces (user_id, space_name, space_location, space_description, price_per_night, available_from, available_to) VALUES
    (1, 'Cosy Camden Loft', 'Camden, London', 'Bright open-plan loft with exposed brick walls, skylights, and a private rooftop terrace overlooking the canal.', 145, '2026-05-20', '2026-08-31'),
    (1, 'Seaside Cottage Retreat', 'Whitstable, Kent', 'Charming 2-bedroom fisherman''s cottage steps from the beach. Wood-burning stove and fully equipped kitchen.', 120, '2026-06-01', '2026-09-15'),
    (2, 'Modern City Studio', 'Manchester City Centre', 'Sleek studio apartment in a converted warehouse. Walking distance to Northern Quarter restaurants and bars.', 85, '2026-05-25', '2026-12-31'),
    (3, 'Highland Cabin', 'Aviemore, Scotland', 'Remote wooden cabin surrounded by Cairngorms National Park. Perfect for hiking, stargazing, and complete digital detox.', 175, '2026-06-15', '2026-10-30'),
    (4, 'Georgian Townhouse Room', 'Bath, Somerset', 'Elegant private room in a Grade II listed townhouse. Original period features with modern comforts.', 95, '2026-05-19', '2026-07-31'),
    (5, 'Artist''s Narrowboat', 'Little Venice, London', 'Unique stay aboard a beautifully converted 60ft narrowboat. Cosy interiors and peaceful waterside living.', 110, '2026-06-10', '2026-09-30');


INSERT INTO bookings (space_id, user_id, booking_date, booking_status) VALUES
    (1, 3, '2026-05-22', 'approved'),
    (1, 3, '2026-05-23', 'approved'),
    (1, 3, '2026-05-24', 'approved'),
    (3, 5, '2026-06-01', 'approved'),
    (3, 5, '2026-06-02', 'approved'),
    (4, 1, '2026-07-10', 'pending'),
    (4, 1, '2026-07-11', 'pending'),
    (4, 1, '2026-07-12', 'pending'),
    (5, 2, '2026-06-05', 'approved'),
    (2, 4, '2026-06-20', 'pending'),
    (2, 4, '2026-06-21', 'pending'),
    (6, 3, '2026-06-15', 'declined');
