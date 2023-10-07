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
    price DECIMAL NOT NULL,
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
    reservation_id INT NOT NULL,
    rate INT NOT NULL,
    
    FOREIGN KEY (reservation_id) REFERENCES reservations (id)
);
