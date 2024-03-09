"""
Write a Python program to get the volume of a sphere with radius six.
"""

import math

pi = math.pi
radius = int(input("Enter a radius: "))

volume = (4/3)*pi*(radius**3)
print(round(volume,2))