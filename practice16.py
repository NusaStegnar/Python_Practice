"""
Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference.
"""

number = int(input("Enter a number: "))
x = 17


if x > number:
    result = x - number 
    print(abs(result))
else:
    result = (x - number) * 2 
    print(abs(result))