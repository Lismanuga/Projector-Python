SELECT
    u.id AS host_id,
    u.name AS hostname,
    AVG(rev.rate) AS average_rating
FROM
    users u
JOIN
    rooms r ON u.id = r.host_id
JOIN
    reservations res ON r.id = res.reserved_room_id
JOIN
    reviews rev ON res.id = rev.reservation_id
GROUP BY
    u.id, u.name
ORDER BY
    AVG(rev.rate) DESC
LIMIT 1;
