"""
Write a Python program to solve (x + y) * (x + y).
Test Data : x = 4, y = 3
Expected Output : (4 + 3) ^ 2) = 49
"""

x = 4
y = 3
result = (x * x) + (x * y) + (y * x) + (y * y)
result = (x * x) + 2 * (x * y) + (y * y)

print("({} + {}) ^ 2 = {}".format(x, y, result))