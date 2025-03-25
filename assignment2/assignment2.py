import csv
import os
import traceback
import custom_module


def read_employees():
    employees_data = {}
    try:
        with open("../csv/employees.csv", "r", newline="") as emp:
            data = csv.reader(emp)
            employees_data["fields"] = next(data)
            employees_data["rows"] = [row for row in data]
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(
                f"File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}"
            )
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
    return employees_data


employees = read_employees()


def column_index(field):
    return employees["fields"].index(field)


employee_id_column = column_index("employee_id")


def first_name(row):
    col = column_index("first_name")
    return employees["rows"][row][col]


def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id

    matches = list(filter(employee_match, employees["rows"]))
    return matches


def employee_find_2(employee_id):
    matches = list(
        filter(
            lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]
        )
    )
    return matches


def sort_by_last_name():
    col = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[col])
    return employees["rows"]


sort_by_last_name()


def employee_dict(row):
    dictionary = {}
    for index, value in enumerate(row):
        if not index == employee_id_column:
            dictionary[employees["fields"][index]] = value
    return dictionary


def employee_dict_2(row):
    # dictionary = dict(zip(employees["fields"][1:], row[1:]))
    dictionary = dict(zip(employees["fields"], row))
    dictionary.pop("employee_id", None)
    return dictionary


def all_employees_dict():
    dictionary = {}
    for row in employees["rows"]:
        id = row[employee_id_column]
        dictionary[id] = employee_dict_2(row)
    return dictionary


def get_this_value():
    THISVALUE = os.environ.get("THISVALUE")
    return THISVALUE


def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)


set_that_secret("WATCHMEN")
print(custom_module.secret)


def create_minutes_dictionary(path):
    dictionary = {}
    try:
        with open(path, "r", newline="") as m1:
            data = csv.reader(m1)
            dictionary["fields"] = next(data)
            dictionary["rows"] = [tuple(row) for row in (data)]
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(
                f"File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}"
            )
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
    return dictionary


def read_minutes():
    v1 = create_minutes_dictionary("../csv/minutes1.csv")
    v2 = create_minutes_dictionary("../csv/minutes2.csv")
    return v1, v2
