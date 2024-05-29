"""
Write a Python program to convert Python objects into JSON strings. Print all the values.
"""

import json

python_dict = {"name": "David", "age": 8, "class": "II"}
python_list = ["banana", "apple", "mango"]
python_str = "converting python to json"
python_int = 4895
python_float = 24.972
python_T = True
python_F = False
python_N = None


json_dict = json.dumps(python_dict)
json_list = json.dumps(python_list)
json_str = json.dumps(python_str)
json_int = json.dumps(python_int)
json_float = json.dumps(python_float)
json_T = json.dumps(python_T)
json_F = json.dumps(python_F)
json_N = json.dumps(python_N)


print("json dict: ", json_dict)
print("json list: ", json_list)
print("json str: ", json_str)
print("json int: ", json_int)
print("json float: ", json_float)
print("json true: ", json_T)
print("json false: ", json_F)
print("json null: ", json_N)