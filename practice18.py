"""
Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.
"""

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))


if (a == b == c):
    result = (a + b + c)*3
else:
    result = a + b + c

print(result)