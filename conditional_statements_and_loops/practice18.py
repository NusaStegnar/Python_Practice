"""
Write a Python program to find the median of three values.
Expected Output:

Input first number: 15                                                  
Input second number: 26                                                 
Input third number: 29                                                  
The median is 26.0   
"""

a = float(input("Input first number: "))
b = float(input("Input second number: "))
c = float(input("Input third number: "))


if a > b:
    if a < c:
        median = a
    elif b > c:
        median = b
    else:
        median = c
else:
    if a > c:
        median = a
    elif b < c:
        median = b
    else:
        median = c


print("The median is", median)

