"""
Write a Python program to convert JSON data to Python object.
"""

import json

x =  '{ "Name":"David", "Class":"I", "Age":6 }'
y = json.loads(x)

print("\nJSON data:")
print(y)
print("\nName:",y["Name"])
print("Class:",y["Class"])
print("Age:",y["Age"]) 