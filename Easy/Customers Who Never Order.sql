select name as customers
from customers
    left join orders on customers.id = orders.customerid
where orders.id is null