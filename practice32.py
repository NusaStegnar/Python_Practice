"""
Write a Python program to find the least common multiple (LCM) of two positive integers.
"""

def multiple(x, y):
    common_multiple = []
    common_multiple_1 = []
    common = []

    for a in range(1, (x * y) + 1):
        if (a % x == 0) and (a % y == 0):
            common_multiple.append(a)

    
    return common_multiple[0]


print(multiple(12, 7))
print(multiple(4, 6))
print(multiple(15, 17))