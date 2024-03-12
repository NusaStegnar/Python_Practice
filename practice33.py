"""
Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero.
"""

def count_three():

    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    c = int(input("Enter a number: "))

    if a == b or a == c or b == c:
        result = 0
        return(result)
    else:
        result = a + b + c
        return(result)


print(count_three())