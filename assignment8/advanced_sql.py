# This should open the database,
# issue the SQL statement, print out the result,
# and close the database.
import os
import sqlite3

import pandas as pd

current_path = os.path.abspath(__file__)
root_path = current_path[
    : current_path.index("python_homework") + len("python_homework")
]
db_path = os.path.join(root_path, "db", "lesson.db")

with sqlite3.connect(db_path) as conn:
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()

    print("Database created and connected successfully.")

cursor = conn.cursor()


# Find the total price of each of the first 5 orders.
# There are several steps.  You need to join the orders table with
# the line_items table and the products table.
# You need to GROUP_BY the order_id.
# You need to select the order_id and the SUM of
# the product price times the line_item quantity.
# Then, you ORDER BY order_id and LIMIT 5.
# You don't need a subquery.
# Print out the order_id and the total price for each of the rows returned.
def highest_grossing_orders(cursor):
    cursor.execute(
        """
            SELECT o.order_id,
                SUM(p.price * li.quantity) AS total_price
            FROM orders AS o
            JOIN line_items AS li 
            ON o.order_id = li.order_id
            JOIN products AS p
            ON li.product_id = p.product_id
            GROUP BY o.order_id
            ORDER BY total_price DESC
            LIMIT 5
        """
    )
    results = cursor.fetchall()
    # print(results)


highest_grossing_orders(cursor)

# For each customer, find the average price of their orders.
# This can be done with a subquery.
# You compute the price of each order as in part 1,
# but you return the customer_id and the total_price.
# That's the subquery. You need to return the total price using AS total_price,
# and you need to return the customer_id with AS customer_id_b,
# for reasons that will be clear in a moment.

# In your main statement, you left join the customer table with the results of the subquery,
# using ON customer_id = customer_id_b.
# You aliased the customer_id column in the subquery
# so that the column names wouldn't collide.
# Then group by customer_id -- this GROUP BY comes after the subquery --
# and get the average of the total price of the customer orders.
# Return the customer name and the average_total_price.


def average_spending_per_customer():
    cursor.execute(
        """
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
            GROUP BY customer_id
    """
    )
    results = cursor.fetchall()
    # print(results)


average_spending_per_customer()

# TASK #3
# You want to create a new order for the customer named Perez and Sons.

# The employee creating the order is Miranda Harris.

# The customer wants 10 of each of the 5 least expensive products.

# You first need to do a SELECT statement to retrieve
# the customer_id, another to retrieve the product_ids of
# the 5 least expensive products, and another to retrieve the employee_id.
#
# Then, you create the order record and the 5 line_item records comprising
# the order.  You have to use the customer_id, employee_id, and product_id
# values you obtained from the SELECT statements.

# You have to use the order_id for the order record you created in
# the line_items records. The inserts must occur within the scope of
# one transaction.

# Then, using a SELECT with a JOIN, print out the list of
# line_item_ids for the order along with the quantity and product name for each.

# You want to make sure that the foreign keys in the INSERT statements
# are valid.  So, add this line to your script,
# right after the database connection:

# conn.execute("PRAGMA foreign_keys = 1")
# In general, when creating a record, you don't want to specify the primary key.
# So leave that column name off your insert statements.
# SQLite will assign a unique primary key for you.
# But, you need the order_id for the order record you insert to be able
# to insert line_item records for that order.
# You can have this value returned by adding the following clause
# to the INSERT statement for the order:

# RETURNING order_id


def get_lowest_priced_products(cursor, amount):
    cursor.execute(
        """
            SELECT product_id
            FROM products 
            ORDER BY price
            LIMIT ?;
        """,
        (amount,),
    )
    results = cursor.fetchall()
    return results


def find_employee(cursor, agent_first_name, agent_last_name):
    cursor.execute(
        """
            SELECT employee_id
            FROM employees
            WHERE first_name = ? AND last_name = ?;
        """,
        (agent_first_name, agent_last_name),
    )
    employee_id = cursor.fetchall()[0][0]
    return employee_id


def find_customer(cursor, customer_name):
    cursor.execute(
        """
            SELECT customer_id 
            FROM customers
            WHERE customer_name = ?;
        """,
        (customer_name,),
    )
    customer_id = cursor.fetchall()[0][0]
    return customer_id


def add_new_order(cursor, customer_id, employee_id, products_list, quantity):
    cursor.execute(
        """INSERT INTO orders (customer_id, employee_id, date) VALUES (?, ?, CURRENT_TIMESTAMP);""",
        (customer_id, employee_id),
    )
    order_id = cursor.lastrowid
    try:
        for product in products_list:
            product_id = product[0]
            cursor.execute(
                """INSERT INTO line_items (order_id, product_id, quantity) VALUES (?, ?, ?);""",
                (order_id, product_id, quantity),
            )
        conn.commit()
    except Exception as e:
        conn.rollback()
        print("Error:", e)


def view_order(cursor, employee_id, customer_id):
    cursor.execute(
        """
            SELECT o.order_id, e.first_name, e.last_name, c.customer_name, p.product_name, li.quantity, p.price FROM line_items AS li
            JOIN orders AS o
            ON li.order_id = o.order_id
            JOIN products AS p
            ON li.product_id = p.product_id
            JOIN employees AS e
            ON o.employee_id = e.employee_id
            JOIN customers AS c
            ON o.customer_id = c.customer_id
            WHERE o.employee_id = ? AND o.customer_id = ?
        """,
        (employee_id, customer_id),
    )
    rows = cursor.fetchall()
    df = pd.DataFrame(rows)
    print(df)


def delete_order(cursor, employee_id, customer_id):
    cursor.execute(
        """
        SELECT order_id FROM orders
        WHERE employee_id = ? AND customer_id = ?;
        """,
        (employee_id, customer_id),
    )
    order_ids = [row[0] for row in cursor.fetchall()]

    for order_id in order_ids:
        cursor.execute(
            """
            DELETE FROM line_items
            WHERE order_id = ?;
            """,
            (order_id,),
        )

    cursor.execute(
        """
        DELETE FROM orders
        WHERE employee_id = ? AND customer_id = ?;
        """,
        (employee_id, customer_id),
    )
    conn.commit()


cheapest5 = get_lowest_priced_products(cursor, 5)
employee_id = find_employee(cursor, "Miranda", "Harris")
customer_id = find_customer(cursor, "Perez and Sons")
# UNCOMMENT TO ADD
# add_new_order(cursor, customer_id, employee_id, cheapest5, 10)
view_order(cursor, employee_id, customer_id)
# UNCOMMENT TO DELETE
# delete_order(cursor, 16, 7)
conn.commit()


# TASK #4
# Find all employees associated with more than 5 orders.
# You want the first_name, the last_name, and the count of orders.
# You need to do a JOIN on the employees and orders tables,
# and then use GROUP BY, COUNT, and HAVING.
def high_performing_agents(cursor):
    cursor.execute(
        """
            SELECT first_name, last_name, 
                COUNT(o.employee_id) AS total_orders
            FROM employees AS e
            JOIN orders AS o
            ON o.employee_id = e.employee_id
            GROUP BY o.employee_id
            HAVING COUNT(o.employee_id) > 5
            ORDER BY total_orders DESC;
        """,
    )
    rows = cursor.fetchall()
    df = pd.DataFrame(rows)
    print(df)
    return rows


high_performing_agents(cursor)
