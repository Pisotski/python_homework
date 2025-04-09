import pandas as pd

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

print(per_employee_sales)
