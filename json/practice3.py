"""
Write a Python program to convert Python dictionary object (sort by key) to JSON data. Print the object members with indent level 4.
"""
import json

python_dict = {"4": 2, "1": 7, "3": 4, "2": 9}



json_dict = json.dumps(python_dict, sort_keys=True, indent=4)
print(json_dict)