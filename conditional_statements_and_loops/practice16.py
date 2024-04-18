"""
Write a Python program to sum two integers. However, if the sum is between 15 and 20 it will return 20.
"""

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))


result = x + y


if result >= 15 and result <= 20:
    print(20)
else:
    print(result)


# OR

def sum(m, n):
    sum = m + n

    if sum in range(15, 20):
        return 20
    else:
        return sum
    
print(sum(19, 3))
print(sum(5, 2))
