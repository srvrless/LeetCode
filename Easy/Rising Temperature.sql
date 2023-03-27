SELECT name
FROM SalesPerson
WHERE sales_id NOT IN (
        SELECT Orders.sales_id
        FROM Orders
        WHERE Orders.com_id IN (
                SELECT com_id
                FROM Company
                WHERE name = 'RED'
            )
    )


-- join

select s.name from salesperson s
where s.name NOT IN
(select s.name from salesperson s
left join orders o on s.sales_id = o.sales_id
left join company c on c.com_id = o.com_id
where c.name = 'RED') 