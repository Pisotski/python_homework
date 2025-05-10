SELECT o.order_id,
SUM(p.price * li.quantity) AS total_price
FROM orders AS o
JOIN line_items AS li 
ON o.order_id = li.order_id
JOIN products AS p
ON li.product_id = p.product_id
GROUP BY o.order_id
ORDER BY total_price DESC
LIMIT 5;


-- # For each customer, find the average price of their orders.
-- # This can be done with a subquery. 
-- # You compute the price of each order as in part 1,
-- # but you return the customer_id and the total_price.
-- # That's the subquery. You need to return the total price using AS total_price,
-- # and you need to return the customer_id with AS customer_id_b,
-- # for reasons that will be clear in a moment.

-- # In your main statement, you left join the customer table with the results of the subquery,
-- # using ON customer_id = customer_id_b.
-- # You aliased the customer_id column in the subquery
-- # so that the column names wouldn't collide.
-- # Then group by customer_id -- this GROUP BY comes after the subquery --
-- # and get the average of the total price of the customer orders.
-- # Return the customer name and the average_total_price.

SELECT customer_name,
    AVG(total_price) as average_total_price
FROM customers
LEFT JOIN (
    SELECT 
        o.customer_id AS customer_id_b,
        SUM(p.price * li.quantity) AS total_price
    FROM orders AS o
    JOIN line_items AS li ON o.order_id = li.order_id
    JOIN products AS p ON li.product_id = p.product_id
    GROUP BY o.order_id
) AS order_totals
ON customer_id = customer_id_b
GROUP BY customer_id;

-- # You want to create a new order for the customer named Perez and Sons.

-- # The employee creating the order is Miranda Harris.

-- # The customer wants 10 of each of the 5 least expensive products.  

-- # You first need to do a SELECT statement to retrieve 
-- # the customer_id, another to retrieve the product_ids of 
-- # the 5 least expensive products, and another to retrieve the employee_id.  
-- # 
-- # Then, you create the order record and the 5 line_item records comprising 
-- # the order.  You have to use the customer_id, employee_id, and product_id 
-- # values you obtained from the SELECT statements.

-- # You have to use the order_id for the order record you created in 
-- # the line_items records. The inserts must occur within the scope of 
-- # one transaction. 

-- # Then, using a SELECT with a JOIN, print out the list of 
-- # line_item_ids for the order along with the quantity and product name for each.

-- # You want to make sure that the foreign keys in the INSERT statements 
-- # are valid.  So, add this line to your script, 
-- # right after the database connection:

-- # conn.execute("PRAGMA foreign_keys = 1")
-- # In general, when creating a record, you don't want to specify the primary key.
-- # So leave that column name off your insert statements.  
-- # SQLite will assign a unique primary key for you.  
-- # But, you need the order_id for the order record you insert to be able 
-- # to insert line_item records for that order. 
-- # You can have this value returned by adding the following clause 
-- # to the INSERT statement for the order:

-- # RETURNING order_id

SELECT customer_id 
FROM customers
WHERE customer_name = 'Perez and Sons';

SELECT product_id
FROM products 
ORDER BY price 
LIMIT 5;

SELECT employee_id
FROM employees
WHERE first_name = 'Miranda' AND last_name = 'Harris';

-- for loop second table
-- insert into orders customer_id, employee_id, date?
-- insert into line_items order_id, product_id, quantity=10

-- # TASK #4
-- # Find all employees associated with more than 5 orders.  
-- # You want the first_name, the last_name, and the count of orders.  
-- # You need to do a JOIN on the employees and orders tables, 
-- # and then use GROUP BY, COUNT, and HAVING.

SELECT first_name, last_name, 
    COUNT(o.employee_id) AS total_orders
FROM employees AS e
JOIN orders AS o
ON o.employee_id = e.employee_id
GROUP BY o.employee_id
HAVING COUNT(o.employee_id) > 5
ORDER BY total_orders DESC;