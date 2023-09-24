SELECT
  rooms.host_id AS host_id,
  users.name AS host_name,
  AVG(CAST(reviews.rate AS NUMERIC)) AS average_rating
FROM
  rooms
LEFT JOIN
  users ON rooms.host_id = users.id
LEFT JOIN
  reviews ON rooms.id = reviews.room_id
GROUP BY
  rooms.host_id, users.name
ORDER BY
  average_rating DESC
LIMIT 1;
