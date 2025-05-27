# We want to find out how many times each product has been ordered, and what was the total price paid by product.

# Read data into a DataFrame, as described in the lesson. The SQL statement should retrieve the
#
# line_item_id, quantity, product_id, product_name, and price
#
# from a JOIN of the line_items table and the product table.
# Hint: Your ON statement would be ON line_items.product_id = products.product_id.
import os
import pandas as pd
import sqlite3

current_path = os.path.abspath(__file__)
root_path = current_path[
    : current_path.index("python_homework") + len("python_homework")
]
db_path = os.path.join(root_path, "db", "lesson.db")

with sqlite3.connect(db_path) as conn:
    sql_statement = """
    SELECT li.line_item_id AS li_id, li.quantity, p.product_name, p.product_id AS p_id, p.price 
    FROM line_items li 
    JOIN products p 
    ON li.product_id = p.product_id
    ;"""
    df = pd.read_sql_query(sql_statement, conn)
    # Print the first 5 lines of the resulting DataFrame. Run the program to make sure this much works.
    print(df.head(5))

#    li_id  quantity             product_name  p_id  price
# 0      1         6  Handcrafted Wooden Fish    45   8.95
# 1      2        20           Steel Sausages    49   5.35
# 2      3        11                    Pants    51   9.89
# 3      4        17    Licensed Plastic Bike    54   9.30
# 4      5         7                    Pants    51   9.89
# Line item 1: somebody bought 6 pairs of Handcrafted Wooden Fish
# Line item 2: somebody bought 20 pairs of Steel Sausages
# Line item 3: somebody bought 11 pairs of Pants

# Add a column to the DataFrame called "total". This is the quantity times the price.
# (This is easy: df['total'] = df['quantity'] * df['price'].)
# Print out the first 5 lines of the DataFrame to make sure this works.
df["total"] = df["quantity"] * df["price"]
df["total"] = df["total"].round(2)

print(f"******************______________________***************")
print(df.head(5))

# Add groupby() code to group by the product_id.
# Use an agg() method that specifies 'count' for the line_item_id column,
# 'sum' for the total column, and 'first' for the 'product_name'.

# Group By: How many times one item was ordered, total price and name of product

sales_count = df.groupby("p_id").agg(
    {"li_id": "count", "total": "sum", "product_name": "first"}
)


#       li_id    total           product_name
# p_id
# 1        21   506.25        Fantastic Shoes
# 2        28  1780.17  For repair Soft Table
# 3        19   986.44               Sausages
# 4        21  2058.71  Ergonomic Wooden Soap
# 5        20  1767.30           Wooden Shoes

# Print out the first 5 lines of the resulting DataFrame.
print(f"******************______________________***************")
print(sales_count.head(5))

# Run the program to see if it is correct so far.
# Sort the DataFrame by the product_name column.
sales_count.sort_values(by="product_name", ascending=True, inplace=True)
print(f"******************______________________***************")
print(sales_count.head(5))

# Add code to write this DataFrame to a file order_summary.csv,
# which should be written in the assignment7 directory.
# Verify that this file is correct.

# just to make it look nice aka Math first pretty later
sales_count.index.names = ["product_id"]
sales_count.rename(columns={"li_id": "line_item_id"}, inplace=True)
sales_count["total"] = sales_count["total"].map(lambda x: f"{x:.2f}")


def log_sales(df):
    order_summary_path = os.path.join(root_path, "assignment7", "order_summary.csv")
    df.to_csv(order_summary_path)


log_sales(sales_count)
