"""
Write a Python program to test whether a number is within 100 of 1000 or 2000.
"""



def near_hundred(number):

    return ((abs(1000 - number) <= 100) or (abs(2000 - number) <= 100))

print(near_hundred(number = int(input("Enter an integer: ")))) 


