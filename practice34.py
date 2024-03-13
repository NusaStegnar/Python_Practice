"""
Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20.
"""

def sum_of_two():

    a = int(input("Enter an integer: "))
    b = int(input("Enter another integer: "))

    result = a+b
    if result >= 15 and result <= 20:
        return 20
    return result


print(sum_of_two())
    