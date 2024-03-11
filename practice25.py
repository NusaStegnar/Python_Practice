"""
Write a Python program that checks whether a specified value is contained within a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False
"""


# def check_value(x):
#     group_of_values = [1, 5, 8, 3]
#     if x in group_of_values:
#         return True
#     return False


# print(check_value(int(input("Enter a value: "))))

# --- OR ----


def check_value(group_of_values, x):
    for value in group_of_values:
        if value == x:
            return True
    return False


print(check_value([1,5,8,3], 3))
print(check_value([1,5,8,3], -1))