"""
Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old. 
Note: for this exercise, the expectation is that you explicitly write out the year 
"""

name = input("Enter your name: ")
age = int(input("Enter your age: "))

a = 100 - age

b = 2024 + a

print(f"Hello {name}. In the year {b} you will be 100 years old.")