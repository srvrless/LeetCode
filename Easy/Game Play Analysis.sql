SELECT player_id,
    MIN(first_login) AS first_login
FROM (
        SELECT player_id,
            event_date AS first_login
        FROM activity
        ORDER BY event_date
    ) AS subquery
GROUP BY player_id;