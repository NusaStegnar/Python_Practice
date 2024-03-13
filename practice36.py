"""
Write a Python program to add two objects if both objects are integers.
"""

# def add_num(a, b):

#     if isinstance(a, int) and isinstance(b, int):
#         return a + b
#     else:
#         return "Inputs must be an integer!"


# print(add_num(4, 7))
# print(add_num("c", 7))
# print(add_num(4, "x"))
# print(add_num(23, 9))
# print(add_num("s", "k"))


# OR


def add_num(a, b):

    if type(a) == int and type(b) == int:
        return a + b
    else:
        return "Inputs must be an integer!"
    

print(add_num(4, 7))
print(add_num("c", 7))
print(add_num(4, "x"))
print(add_num(23, 9))
print(add_num("s", "k"))