"""
Write a Python program to convert Python object to JSON data.
"""

import json

x = {
    "name": "Mike", 
    "age": 18, 
    "country": "Slovenia"
}

y = json.dumps(x)

print(y)