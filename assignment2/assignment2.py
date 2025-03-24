import csv
import traceback


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
print(employees)
