import pandas as pd

employees = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"],
}

task1_data_frame = pd.DataFrame(employees)
task1_with_salary = task1_data_frame.copy()
task1_with_salary["Salary"] = [70000, 80000, 90000]
task1_older = task1_with_salary.copy()
task1_age = task1_older["Age"]
task1_older["Age"] = task1_age + 1
task1_older.to_csv("employees.csv", index=False)

task2_employees = pd.read_csv("./employees.csv")
additional_employees = pd.DataFrame(
    {
        "Name": ["Eve", "Frank"],
        "Age": [28, 40],
        "City": ["Miami", "Seattle"],
        "Salary": [60000, 95000],
    }
)
additional_employees.to_json("./additional_employees.json", index=False)
json_employees = pd.read_json("./additional_employees.json")
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
first_three = more_employees.head(3)
last_two = more_employees.tail(2)
employee_shape = more_employees.shape
print(more_employees.info())
