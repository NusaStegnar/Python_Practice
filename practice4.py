"""
Write a Python program that calculates the area of a circle based on the radius entered by the user.
"""
import math

radius = float(input("Enter the radius: "))
print(f"r =",radius)
pi = math.pi
area = pi*(radius**2)
print(f"Area = ", area)