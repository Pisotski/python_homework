import pandas as pd

# SELECTING COLUMNS:
# primitives df['column_name'] tuples: df[("Values", "sum")]
# SELECTING ROWS:
# loc - INCLUSIVE. Label-based indexing. You know names of rows, so last one will be returned
# iloc - EXCLUSIVE. Position-based indexing. You don't know label names, works like arrays or lists. Last element will not be included

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [24, 27, 22, 32],
    "Score": [85, 92, 88, 76],
}

df = pd.DataFrame(data)

selected_column = df["Name"]
# print(names)
# OUTPUT:
# 0      Alice
# 1        Bob
# 2    Charlie
# 3      David

first_three_rows = df.loc[0:2]
# print(first_three_rows)
# OUTPUT:
#       Name  Age  Score
# 0    Alice   24     85
# 1      Bob   27     92
# 2  Charlie   22     88
selected_labels_only = df.loc[[0, 2]]
# print(selected_labels_only)
# OUTPUT:
#       Name  Age  Score
# 0    Alice   24     85
# 2  Charlie   22     88

first_three_rows_selected = df.loc[0:2, ["Name", "Age"]]
# print(first_three_rows_selected)
# OUTPUT:
#       Name  Age
# 0    Alice   24
# 1      Bob   27
# 2  Charlie   22

first_two_rows = df.iloc[:2]
# print(first_two_rows)
#     Name  Age  Score
# 0  Alice   24     85
# 1    Bob   27     92

list_sliced = ["a", "b", "c", "d"][0:2]
# OUTPUT:
# ["a","b"]

data2 = {"Category": ["A", "B", "A", "B", "C"], "Values": [10, 20, 30, 40, 50]}
#   Category  Values
# 0        A      10
# 1        B      20
# 2        A      30
# 3        B      40
# 4        C      50

df2 = pd.DataFrame(data2)
summed = df2.groupby("Category").sum()
#           Values
# Category
# A             40
# B             60
# C             50

mean_values = df2.groupby("Category")["Values"].mean()
# Category
# A    20.0
# B    30.0
# C    50.0
result1 = df2.groupby("Category").agg({"Values": "sum"})
# print(result1)

aggregated = df2.groupby("Category").agg({"Values": ["sum", "mean", "count"]})
#          Values
#             sum  mean count
# Category
# A            40  20.0     2
# B            60  30.0     2
# C            50  50.0     1
select_aggregated = aggregated[("Values", "sum")]

# Sample DataFrames
df3 = pd.DataFrame({"ID": [1, 2, 3], "Name": ["Alice", "Bob", "Charlie"]})
df4 = pd.DataFrame({"ID": [1, 2, 4], "Score": [85, 92, 88]})

# Merge on the 'ID' column
merged_df = pd.merge(df3, df4, on="ID", how="inner")
# Inner merge
# print(merged_df)
#    ID   Name  Score
# 0   1  Alice     85
# 1   2    Bob     92

df5 = pd.DataFrame(
    {
        "ID": [1, 2, 3],
        "Date": ["2021-01-01", "2021-01-02", "2021-01-03"],
        "Name": ["Alice", "Bob", "Charlie"],
    }
)

df6 = pd.DataFrame(
    {
        "ID": [1, 2, 3],
        "Date": ["2021-01-01", "2021-01-02", "2021-01-03"],
        "Score": [85, 92, 88],
    }
)

# Merge on both 'ID' and 'Date'
merged_df = pd.merge(df5, df6, on=["ID", "Date"], how="inner")
# print(merged_df)

#    ID        Date     Name  Score
# 0   1  2021-01-01    Alice     85
# 1   2  2021-01-02      Bob     92
# 2   3  2021-01-03  Charlie     88


df7 = pd.DataFrame({"Name": ["Alice", "Bob", "Charlie"]}, index=[1, 2, 3])
df8 = pd.DataFrame({"Score": [85, 92, 88]}, index=[1, 2, 4])

joined_df = df7.join(df8, how="outer")
#       Name  Score
# 1    Alice   85.0
# 2      Bob   92.0
# 3  Charlie    NaN
# 4      NaN   88.0

joined_df["bogus"] = ["x", "y", "z", "w"]
# adds a column
#       Name  Score bogus
# 1    Alice   85.0     x
# 2      Bob   92.0     y
# 3  Charlie    NaN     z
# 4      NaN   88.0     w

joined_df["bogus"] = joined_df["bogus"] + "_value"
# modified values in a column
#       Name  Score    bogus
# 1    Alice   85.0  x_value
# 2      Bob   92.0  y_value
# 3  Charlie    NaN  z_value
# 4      NaN   88.0  w_value

joined_df.drop("bogus", axis=1, inplace=True)
#
# deletes the column.
# You need axis=1 to identify that the drop is for a column, not a row
# inplace=True modifies df inplace=False will return a copy
#
#       Name  Score
# 1    Alice   85.0
# 2      Bob   92.0
# 3  Charlie    NaN
# 4      NaN   88.0

import numpy

data = {"Name": ["A", "B", "C"], "Value": [1, 2, 3]}
new_df = pd.DataFrame(data)
#   Name  Value
# 0    A      1
# 1    B      2
# 2    C      3

new_df["Value"] = new_df["Value"] ** 2  # using an operator
#   Name  Value
# 0    A      1
# 1    B      4
# 2    C      9

new_df["Value"] = numpy.sqrt(new_df["Value"])
# using a numpy function.  You can't use math.sqrt() on a Series.
#   Name  Value
# 0    A    1.0
# 1    B    2.0
# 2    C    3.0

new_df["EvenOdd"] = new_df["Value"].map(lambda x: "Even" if x % 2 == 0 else "Odd")
# the map method for a Series
#   Name  Value EvenOdd
# 0    A    1.0     Odd
# 1    B    2.0    Even
# 2    C    3.0     Odd

new_df["Value"] = new_df["Value"].astype(int)
# type conversion method for a Series
#   Name  Value EvenOdd
# 0    A      1     Odd
# 1    B      2    Even
# 2    C      3     Odd

joined_df.rename(columns={"Score": "Test Score"}, inplace=True)
#       Name  Test Score
# 1    Alice        85.0
# 2      Bob        92.0
# 3  Charlie         NaN
# 4      NaN        88.0

renamed_df = joined_df.set_index("Name")
#          Test Score
# Name
# Alice          85.0
# Bob            92.0
# Charlie         NaN
# NaN            88.0

joined_df.sort_values(by="Test Score", ascending=False, inplace=True)
#       Name  Test Score
# 2      Bob        92.0
# 4      NaN        88.0
# 1    Alice        85.0
# 3  Charlie         NaN

joined_df.reset_index(inplace=True, drop=True)
#       Name  Test Score
# 0      Bob        92.0
# 1      NaN        88.0
# 2    Alice        85.0
# 3  Charlie         NaN
