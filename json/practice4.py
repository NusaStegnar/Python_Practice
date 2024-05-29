"""
Write a Python program to convert JSON encoded data into Python objects.
"""
import json


json_data = '{"name":"Mario", "nick":"Super", "type":"cartoon"}'

python_data = json.loads(json_data)
print(python_data)