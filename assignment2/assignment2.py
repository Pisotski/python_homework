import csv
import os
import traceback
import custom_module
from datetime import datetime


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
        with open(path, "r", newline="") as csvfile:
            data = csv.reader(csvfile)
            dictionary["fields"] = next(data)
            dictionary["rows"] = [tuple(row) for row in (data)]
            return dictionary
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


def read_minutes():
    v1 = create_minutes_dictionary("../csv/minutes1.csv")
    v2 = create_minutes_dictionary("../csv/minutes2.csv")
    return v1, v2


minutes1, minutes2 = read_minutes()

# print(minutes1, minutes2)


def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    return set1.union(set2)


minutes_set = create_minutes_set()


def write_output(data):
    with open("minutes4.txt", "w", newline="") as m3:
        writer = csv.writer(m3)
        writer.writerows(data)


def create_minutes_list():
    minutes_list = [list(tuple) for tuple in minutes_set]
    minutes = list(
        map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list)
    )
    return minutes


# write_output(create_minutes_list())
minutes_list = create_minutes_list()


def write_sorted_list():
    minutes_list.sort(key=lambda x: x[1])
    converted_list = list(
        map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), minutes_list)
    )
    print(converted_list)
    # minutes.insert(0, minutes1["fields"])
    try:
        with open("./minutes.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(minutes1["fields"])
            writer.writerows(converted_list)
        return converted_list
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
