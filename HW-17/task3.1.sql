SELECT
  users.id AS user_id,
  users.name AS user_name,
  COUNT(reservations.id) AS reservation_count
FROM
  users
LEFT JOIN
  reservations ON users.id = reservations.reservator_id
GROUP BY
  users.id, users.name
ORDER BY
  reservation_count DESC
LIMIT 1;


