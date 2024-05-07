"""
Write a Python script to check whether a given key already exists in a dictionary.
"""

dic = {"dog": 3, "mouse": 1, "cat": 7, "bird": 5}
key = "cat"


if key in dic:
    print(True)
else:
    print(False)