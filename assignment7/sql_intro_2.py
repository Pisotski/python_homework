# We want to find out how many times each product has been ordered, and what was the total price paid by product.

# Read data into a DataFrame, as described in the lesson. The SQL statement should retrieve
# the line_item_id, quantity, product_id, product_name, and price
# from a JOIN of the line_items table and the product table.
# Hint: Your ON statement would be ON line_items.product_id = products.product_id.

# Print the first 5 lines of the resulting DataFrame. Run the program to make sure this much works.

# Add a column to the DataFrame called "total". This is the quantity times the price. (This is easy: df['total'] = df['quantity'] * df['price'].) Print out the first 5 lines of the DataFrame to make sure this works.

# Add groupby() code to group by the product_id. Use an agg() method that specifies 'count' for the line_item_id column, 'sum' for the total column, and 'first' for the 'product_name'. Print out the first 5 lines of the resulting DataFrame. Run the program to see if it is correct so far.

# Sort the DataFrame by the product_name column.

# Add code to write this DataFrame to a file order_summary.csv, which should be written in the assignment7 directory. Verify that this file is correct.

# As we'll learn in the next lesson, the ordering, grouping, count, and sum operations can be done in SQL, more efficiently than in Pandas.  The key concepts of pandas and SQL overlap very strongly.
