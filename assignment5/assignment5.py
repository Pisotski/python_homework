import pandas as pd
import numpy as np

data = [
    {"Employee": "Jones", "Product": "Widget", "Region": "West", "Revenue": 9000},
    {"Employee": "Jones", "Product": "Gizmo", "Region": "West", "Revenue": 4000},
    {"Employee": "Jones", "Product": "Doohickey", "Region": "West", "Revenue": 11000},
    {"Employee": "Jones", "Product": "Widget", "Region": "East", "Revenue": 4000},
    {"Employee": "Jones", "Product": "Gizmo", "Region": "East", "Revenue": 5500},
    {"Employee": "Jones", "Product": "Doohickey", "Region": "East", "Revenue": 2345},
    {"Employee": "Smith", "Product": "Widget", "Region": "West", "Revenue": 9007},
    {"Employee": "Smith", "Product": "Gizmo", "Region": "West", "Revenue": 40003},
    {"Employee": "Smith", "Product": "Doohickey", "Region": "West", "Revenue": 110012},
    {"Employee": "Smith", "Product": "Widget", "Region": "East", "Revenue": 9002},
    {"Employee": "Smith", "Product": "Gizmo", "Region": "East", "Revenue": 15500},
    {"Employee": "Garcia", "Product": "Widget", "Region": "West", "Revenue": 6007},
    {"Employee": "Garcia", "Product": "Gizmo", "Region": "West", "Revenue": 42003},
    {"Employee": "Garcia", "Product": "Doohickey", "Region": "West", "Revenue": 160012},
    {"Employee": "Garcia", "Product": "Gizmo", "Region": "East", "Revenue": 16500},
    {"Employee": "Garcia", "Product": "Doohickey", "Region": "East", "Revenue": 2458},
]
sales = pd.DataFrame(data)

#    Employee    Product Region  Revenue
# 0     Jones     Widget   West     9000
# 1     Jones      Gizmo   West     4000
# 2     Jones  Doohickey   West    11000
# 3     Jones     Widget   East     4000
# 4     Jones      Gizmo   East     5500
# 5     Jones  Doohickey   East     2345
# 6     Smith     Widget   West     9007
# 7     Smith      Gizmo   West    40003
# 8     Smith  Doohickey   West   110012
# 9     Smith     Widget   East     9002
# 10    Smith      Gizmo   East    15500
# 11   Garcia     Widget   West     6007
# 12   Garcia      Gizmo   West    42003
# 13   Garcia  Doohickey   West   160012
# 14   Garcia      Gizmo   East    16500
# 15   Garcia  Doohickey   East     2458

sales_pivot1 = pd.pivot_table(
    sales, index=["Region", "Product"], values="Revenue", aggfunc="sum", fill_value=0
)

#                   Revenue
# Region Product
# East   Doohickey     4803
#        Gizmo        37500
#        Widget       13002
# West   Doohickey   281024
#        Gizmo        86006
#        Widget       24014

sales_pivot2 = pd.pivot_table(
    sales,
    index="Product",
    values="Revenue",
    columns="Region",
    aggfunc="sum",
    fill_value=0,
)

# Region      East    West
# Product
# Doohickey   4803  281024
# Gizmo      37500   86006
# Widget     13002   24014

sales_pivot3 = pd.pivot_table(
    sales,
    index="Product",
    values="Revenue",
    columns=["Region", "Employee"],
    aggfunc="sum",
    fill_value=0,
)

# Region      East                 West
# Employee  Garcia Jones  Smith  Garcia  Jones   Smith
# Product
# Doohickey   2458  2345      0  160012  11000  110012
# Gizmo      16500  5500  15500   42003   4000   40003
# Widget         0  4000   9002    6007   9000    9007

sales_pivot2["Total"] = sales_pivot2["East"] + sales_pivot2["West"]

# Region      East    West   Total
# Product
# Doohickey   4803  281024  285827
# Gizmo      37500   86006  123506
# Widget     13002   24014   37016

per_employee_sales = sales.groupby("Employee").agg({"Revenue": "sum"})
per_employee_sales["Commission Percentage"] = [0.12, 0.09, 0.1]
per_employee_sales["Commission"] = (
    per_employee_sales["Revenue"] * per_employee_sales["Commission Percentage"]
)

#           Revenue  Commission Percentage  Commission
# Employee
# Garcia     226980                   0.12    27237.60
# Jones       35845                   0.09     3226.05
# Smith      183524                   0.10    18352.40

per_employee_sales = sales.groupby("Employee").agg({"Revenue": "sum"})
per_employee_sales["Commission Plan"] = ["A", "A", "B"]

#           Revenue Commission Plan
# Employee
# Garcia     226980               A
# Jones       35845               A
# Smith      183524               B


def calculate_commission(row):
    if row["Revenue"] < 10000:
        return 0
    if row["Commission Plan"] == "A":
        return 1000 + 0.05 * (row["Revenue"] - 10000)
    elif row["Commission Plan"] == "B":
        return 1400 + 0.04 * (row["Revenue"] - 10000)


per_employee_sales["Commission"] = per_employee_sales.apply(
    calculate_commission, axis=1
)
#           Revenue Commission Plan  Commission
# Employee
# Garcia     226980               A    11849.00
# Jones       35845               A     2292.25
# Smith      183524               B     8340.96

data1 = {
    "Name": ["Alice", "Bob", None, "David"],
    "Age": [24, 27, 22, None],
    "Score": [85, None, 88, 76],
}
df1 = pd.DataFrame(data1)

df_missing = df1[df1.isnull().any(axis=1)]
#     Name   Age  Score
# 1    Bob  27.0    NaN
# 2   None  22.0   88.0
# 3  David   NaN   76.0

df_dropped = df1.dropna()
#     Name   Age  Score
# 0  Alice  24.0   85.0

df_filled = df1.fillna({"Age": 0, "Score": df1["Score"].mean()})
#     Name   Age  Score
# 0  Alice  24.0   85.0
# 1    Bob  27.0   83.0
# 2   None  22.0   88.0
# 3  David   0.0   76.0

data2 = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": ["24", "27", "22"],
    "JoinDate": ["2023-01-15", "2022-12-20", "2023-03-01"],
}
df2 = pd.DataFrame(data2)

df2["Age"] = df2["Age"].astype(int)
df2["JoinDate"] = pd.to_datetime(df2["JoinDate"])

# Name                object
# Age                  int64
# JoinDate    datetime64[ns]
# dtype: object

#       Name  Age   JoinDate
# 0    Alice   24 2023-01-15
# 1      Bob   27 2022-12-20
# 2  Charlie   22 2023-03-01

data3 = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Location": ["LA", "LA", "NY"],
    "JoinDate": ["2023-01-15", "2022-12-20", "2023-03-01"],
}
df3 = pd.DataFrame(data3)

# !CAVEAT if value is not either 'LA' or 'NY', map will convert to NaN.
# df3['Location'] = df3['Location'].map({'LA': 'Los Angeles', 'NY': 'New York'})
#       Name     Location    JoinDate
# 0    Alice  Los Angeles  2023-01-15
# 1      Bob  Los Angeles  2022-12-20
# 2  Charlie     New York  2023-03-01

df3["Location"] = df3["Location"].replace({"LA": "Los Angeles", "NY": "New York"})
#       Name     Location    JoinDate
# 0    Alice  Los Angeles  2023-01-15
# 1      Bob  Los Angeles  2022-12-20
# 2  Charlie     New York  2023-03-01

data4 = {
    "Name": ["Tom", "Dick", "Harry", "Mary"],
    "Phone": [3212347890, "(212)555-8888", "752-9103", "8659134568"],
}
df4 = pd.DataFrame(data4)

df4["Correct Phone"] = df4["Phone"].astype(str)


def fix_phone(phone):
    if phone.isnumeric():
        out_string = phone
    else:
        out_string = ""
        for c in phone:
            if c in "0123456789":
                out_string += c
    if len(out_string) == 10:
        return out_string
    return None


df4["Correct Phone"] = df4["Correct Phone"].map(fix_phone)
#     Name          Phone Correct Phone
# 0    Tom     3212347890    3212347890
# 1   Dick  (212)555-8888    2125558888
# 2  Harry       752-9103          None
# 3   Mary     8659134568    8659134568

data5 = {"Name": ["Alice", "Bob", "Charlie"], "Age": [20, 22, 43]}

df5 = pd.DataFrame(data5)

# Increase the age by 1 as a new year has passed
df5["Age"] = df5["Age"] + 1
# df5["Age"] = np.add(df5["Age"], 1)
#       Name  Age
# 0    Alice   21
# 1      Bob   23
# 2  Charlie   44

data6 = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Location": ["LA", "LA", "NY"],
    "Grade": [78, 40, 85],
}
df6 = pd.DataFrame(data6)

df6["Grade"] = pd.cut(df6["Grade"], 3, labels=["bad", "okay", "great"])
#       Name Location  Grade
# 0    Alice       LA  great
# 1      Bob       LA    bad
# 2  Charlie       NY  great

data7 = {
    "Name": ["Alice", "Bob", "Alice", "David"],
    "Age": [24, 27, 24, 32],
    "Score": [85, 92, 85, 76],
}
df7 = pd.DataFrame(data7)
df_cleaned = df7.drop_duplicates()
#     Name  Age  Score
# 0  Alice   24     85
# 1    Bob   27     92
# 3  David   32     76

df_cleaned_by_name = df7.drop_duplicates(subset="Name")
#     Name  Age  Score
# 0  Alice   24     85
# 1    Bob   27     92
# 3  David   32     76

# # Replace outliers in 'Age' (e.g., Age > 100 or Age < 0)
# df['Age'] = df['Age'].apply(lambda x: df['Age'].median() if x > 100 or x < 0 else x)

# print("DataFrame after handling outliers:")
# print(df)
