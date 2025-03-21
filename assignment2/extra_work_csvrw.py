# Exercise from https://www.w3resource.com/python-exercises/csv/index.php

# 1. Write a Python program to read each
# row from a given csv file and print a list of strings.
import csv

with open("departments.csv", newline="") as file:
    departments = csv.reader(file, delimiter=" ", quotechar="|")
    for row in departments:
        print("".join(row))

# 2. Write a Python program to read a given CSV file ]
# having tab delimiter.

with open("departments.csv", newline="") as csvfile:
    departments = csv.DictReader(csvfile, delimiter="\t", quotechar="|")

    for row in departments:
        print("".join(row))

# 3. Write a Python program to read a given CSV file as a list.
with open("departments.csv", newline="") as csvfile:
    departments = csv.reader(csvfile)
    departments_list = []
    for row in departments:
        departments_list.append(row)
        # departments_list = list(departments)
        # departments_list(row for row in departments)
        print(departments_list)

# 4. Write a Python program to read a given CSV file
# as a dictionary.
with open("countries.csv", newline="") as csvfile:
    countries = csv.DictReader(csvfile)
    for row in countries:
        print(row)

# 5. Write a Python program to read a given CSV files
# with initial spaces after a delimiter and remove those initial spaces.

with open("departments.csv", "r") as csvfile:
    print("with delimiter")
    departments = csv.reader(csvfile, skipinitialspace=False)
    for row in departments:
        print("".join(row))

with open("departments.csv", "r") as csvfile:
    departments = csv.reader(csvfile, skipinitialspace=True)
    print("without delimiter")
    for row in departments:
        print("".join(row))

# 6. Write a Python program that reads a CSV file and remove initial spaces,
# quotes around each entry and the delimiter.

with open("departments.csv", newline="") as csvfile:
    csv.register_dialect(
        "csv_dialect",
        delimiter=" ",
        skipinitialspace=True,
        quotechar="|",
        quoting=csv.QUOTE_ALL,
    )
    departments = csv.reader(csvfile, dialect="csv_dialect")
    for row in departments:
        print("".join(row))

# 7. Write a Python program to read specific columns
# of a given CSV file and print the content of the columns.

with open("departments.csv", newline="") as csvfile:
    departments = csv.reader(csvfile, skipinitialspace=True)
    c = [x[2] for x in departments]
    print(", ".join(c))

with open("departments.csv", newline="") as csvfile:
    departments = csv.DictReader(csvfile, skipinitialspace=True)
    for row in departments:
        print(f"{row['department_id']}, {row['department_name']}")

# 8. Write a Python program that reads each
# row of a given csv file and skip the header
# of the file. Also print the number of rows
# and the field names.

fields = []
rows = []
with open("departments.csv", newline="") as csvfile:
    data = csv.reader(csvfile, delimiter=" ")
    #  Following command skips the first row of the CSV file.
    fields = next(data)
    for row in data:
        print(", ".join(row))
print("\nTotal no. of rows: %d" % (data.line_num))
print("Field names are:")
print(", ".join(field for field in fields))

# 9. Write a Python program to create an object
# for writing and iterate over the rows to print the values.

import sys

with open("temp.csv", "wt") as f:
    writer = csv.writer(f)
    writer.writerow(("id1", "id2", "date"))
    for i in range(3):
        row = (
            i + 1,
            chr(ord("a") + i),
            "01/{:02d}/2019".format(i + 1),
        )
        writer.writerow(row)
print(open("temp.csv", "rt").read())

# 10. Write a Python program to write a Python list of lists to a csv file. After writing the CSV file read the CSV file and display the content.

data = [[10, "a1", 1], [12, "a2", 3], [14, "a3", 5], [16, "a4", 7], [18, "a5", 9]]
with open("temp.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)
with open("temp.csv", newline="") as csvfile:
    data = csv.reader(csvfile, delimiter=" ")
    for row in data:
        print(", ".join(row))

# 11. Write a Python program to write a Python dictionary to a csv file. After writing the CSV file read the CSV file and display the content.

csv_columns = ["id", "Column1", "Column2", "Column3", "Column4", "Column5"]
dict_data = {
    "id": ["1", "2", "3"],
    "Column1": [33, 25, 56],
    "Column2": [35, 30, 30],
    "Column3": [21, 40, 55],
    "Column4": [71, 25, 55],
    "Column5": [10, 10, 40],
}
csv_file = "temp.csv"
try:
    with open(csv_file, "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in dict_data:
            writer.writerow(dict_data)
except IOError:
    print("I/O error")
data = csv.DictReader(open(csv_file))
print("CSV file as a dictionary:\n")
for row in data:
    print(row)
