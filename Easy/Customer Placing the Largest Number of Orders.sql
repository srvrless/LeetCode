SELECT customer_number
FROM orders
GROUP BY customer_number
HAVING COUNT(*) = (
        SELECT MAX(num_orders)
        FROM (
                SELECT customer_number,
                    COUNT(*) AS num_orders
                FROM orders
                GROUP BY customer_number
            ) AS order_counts
    );