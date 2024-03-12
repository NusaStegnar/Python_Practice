"""
Write a Python program that concatenates all elements in a list into a string and returns it.
"""

def concatenate_list(alist):
    new_string = ""
    for letter in alist:
        new_string = new_string + "".join(letter)
    return new_string

print(concatenate_list(["b", "a", "r", "b", "i", "e"]))
