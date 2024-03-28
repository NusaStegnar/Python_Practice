"""
Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front. Return the string unchanged if the given string already begins with "Is".
"""


def new_string(x):
    if x.startswith("Is"):
        return x
    else:
        return f"Is{x}"
    

print(new_string(input("Enter a word: ")))
