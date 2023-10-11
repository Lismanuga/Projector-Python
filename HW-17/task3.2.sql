SELECT
  rooms.host_id AS host_id,
  users.name AS host_name,
  SUM(rooms.price) AS total_earnings
FROM
  rooms
LEFT JOIN
  users ON rooms.host_id = users.id
LEFT JOIN
  reservations ON rooms.id = reservations.reserved_room_id
GROUP BY
  rooms.host_id, users.name
ORDER BY
  total_earnings DESC
LIMIT 1;