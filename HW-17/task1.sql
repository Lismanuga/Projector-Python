DROP TABLE IF EXISTS reviews;
DROP TABLE IF EXISTS reservations;
DROP TABLE IF EXISTS rooms;
DROP TABLE IF EXISTS users;


CREATE TABLE users (
    id serial PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    age INT NOT NULL,
    is_host BOOLEAN NOT NULL
);

CREATE TABLE rooms (
    id serial PRIMARY KEY,
    host_id INT NOT NULL,
    amount_of_residents INT NOT NULL,
    price INT NOT NULL,
    refregirator BOOLEAN NOT NULL,
    ac BOOLEAN NOT NULL,

    FOREIGN KEY (host_id) REFERENCES users (id)
);

CREATE TABLE reservations (
    id serial PRIMARY KEY,
    reservator_id INT NOT NULL,
    reserved_room_id INT NOT NULL,
    time DATE NOT NULL,
    is_paid BOOLEAN NOT NULL,

    FOREIGN KEY (reservator_id) REFERENCES users (id),
    FOREIGN KEY (reserved_room_id) REFERENCES rooms (id)
);


CREATE TABLE reviews (
    id serial PRIMARY KEY,
    reviewer_id INT NOT NULL,
    room_id INT NOT NULL,
    rate INT NOT NULL,
    
    FOREIGN KEY (reviewer_id) REFERENCES users (id),
    FOREIGN KEY (room_id) REFERENCES rooms (id)
);
