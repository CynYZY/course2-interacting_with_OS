# About CSV 

#### What is parsing?

> Analyzing a file's content to correctly structure the data

### CSV

> Comma Separated Values
>
> 逗号分隔值

- CSV 文件中的每一行都是一个数据记录。 每个记录由一个或多个字段组成，用逗号分隔。 
- CSV 是一种非常简单的数据格式，但是可以有很多差异，例如不同的定界符，换行或引号字符。

 `import csv`

```python
import csv
f = open("csv_file.txt")
csv_f = csv.reader(f)
for row in csv_f:
    name, phone, role = row 
    # unpack
    print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))
```

```python
hosts = [["workstation.local", "192.168.25.46"], ["webserver.cloud", "10.2.5.6"]]
with open("hosts.csv", "w") as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)
```



- `DictReader`

```python
with open("software.csv") as software:
    # "w" is for write-only, in "w" mode, code will have not-readable error
    reader = csv.DictReader(software)
    for row in reader:
        print(("{} has {} users").format(row["name"], row["users"]))
```

```python
'''
"r" Opens a file for reading only.
"r+" Opens a file for both reading and writing.
"rb" Opens a file for reading only in binary format.
"rb+" Opens a file for both reading and writing in binary format.
"w" Opens a file for writing only.
'''
```



- `DictWriter`

```python
users = [{"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"}, 
         {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"},
         {"name": "Charlie Grey", "username": "greyc", "department": "Development"}]
keys = ["name", "username", "department"]
with open("by_department.csv", "w") as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)
```



**关于`quiz_1.py`报错**

```python
import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  with open(filename) as file:
    # Read the rows of the file into a dictionary
    reader = csv.DictReader(file)
    # Process each item of the dictionary
    for row in file:
      return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
  return return_string

#Call the function
print(contents_of_file("flowers.csv"))
```

错误信息

```
Error on line 31:
    print(contents_of_file("flowers.csv"))
Error on line 27:
    return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
TypeError: string indices must be integers
```

原因：`for row in reader:`

修改为

```python
import os
import csv


# Create a file with data in it
def create_file(filename):
    flowers = [{"name": "carnation", "color": "pink", "type": "annual"},
               {"name": "daffodil", "color": "yellow", "type": "perennial"},
               {"name": "iris", "color": "blue", "type": "perennial"},
               {"name": "poinsettia", "color": "red", "type": "perennial"},
               {"name": "sunflower", "color": "yellow", "type": "annual"}]
    keys = ["name", "color", "type"]
    with open(filename, "w") as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerow(flowers)


# Read the file contents and format the information about each row
def contents_of_file(filename):
    return_string = ""

    # Call the function to create the file
    create_file(filename)

    # Open the file
    with open(filename) as file:
        # Read the rows of the file into a dictionary
        reader = csv.DictReader(file)
        # Process each item of the dictionary
        for row in file:
            return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
    return return_string


# Call the function
print(contents_of_file("flowers.csv"))

```

错误信息

```
Traceback (most recent call last):
  File "C:/Users/Cynth/Documents/PythonProjects/csv_demo/quiz_1.py", line 37, in <module>
    print(contents_of_file("flowers.csv"))
  File "C:/Users/Cynth/Documents/PythonProjects/csv_demo/quiz_1.py", line 24, in contents_of_file
    create_file(filename)
  File "C:/Users/Cynth/Documents/PythonProjects/csv_demo/quiz_1.py", line 16, in create_file
    writer.writerow(flowers)
  File "C:\Users\Cynth\AppData\Local\Programs\Python\Python37\lib\csv.py", line 155, in writerow
    return self.writer.writerow(self._dict_to_list(rowdict))
  File "C:\Users\Cynth\AppData\Local\Programs\Python\Python37\lib\csv.py", line 148, in _dict_to_list
    wrong_fields = rowdict.keys() - self.fieldnames
AttributeError: 'list' object has no attribute 'keys'
```

