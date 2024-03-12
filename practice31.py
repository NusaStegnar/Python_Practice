"""
Write a Python program that computes the greatest common divisor (GCD) of two positive integers.
"""

def common_divisor(x, y):
    divisors = []
    divisors_1 = []
    common = []

    for a in range(1, x):
        if x % a == 0:
            divisors.append(a)

    for d in range(1, y):
        if y % d == 0:
            divisors_1.append(d)

    for num in divisors:
        if num in divisors_1:
            common.append(num)

    return(common[-1])


print(common_divisor(12, 17))
print(common_divisor(4, 6))
print(common_divisor(336, 360))

