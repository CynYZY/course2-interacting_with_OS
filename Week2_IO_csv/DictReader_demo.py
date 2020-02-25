import csv
with open("by_department.csv") as bd:
    reader = csv.DictReader(bd)
    for row in reader:
        print(("{} is in {} Department").format(row["name"], row["department"]))