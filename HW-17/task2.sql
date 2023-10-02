INSERT INTO users (name, email, age, is_host) VALUES
  ('Bohdan Hryshchenko', 'bohdan@gmail.com', 21, false),
  ('Irina Hryshchenko', 'irina@gmail.com', 27, false),
  ('Natalia Hryshchenko', 'natalia@gmail.com', 50, true),
  ('Anatoliy Hryshchenko', 'anatoliy@gmail.com', 56, true);

INSERT INTO rooms (host_id, amount_of_residents, price, refregirator, ac) VALUES
  (3, 2, 100, false, false),
  (3, 3, 150, true, true),
  (4, 2, 120, true, false),
  (4, 3, 200, true, true);

INSERT INTO reservations (reservator_id, reserved_room_id, time, is_paid) VALUES
  (1, 1, '2023-10-24', false),
  (2, 2, '2023-10-25', true),
  (2, 3, '2023-10-26', true),
  (2, 4, '2023-10-27', true);

INSERT INTO reviews (reservation_id, rate)
VALUES
  (1, 5),
  (2, 4),
  (3, 6),
  (4, 9);