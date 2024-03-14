"""
Write a Python program to calculate the distance between the points (x1, y1) and (x2, y2).
"""

import math

x1, x2 = 4, 6
y1, y2 = 0, 6

z1 = x2 - x1
z2 = y2 - y1

formula = (z1 ** 2) + (z2 ** 2)
result =math.sqrt(formula)


print(round(result, 2))


