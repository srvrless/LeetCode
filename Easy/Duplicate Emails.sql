SELECT a.email
FROM Person a
    JOIN (
        SELECT email,
            COUNT(*)
        FROM Person
        GROUP BY email
        HAVING count(*) > 1
    ) b ON a.email = b.email
GROUP BY a.email