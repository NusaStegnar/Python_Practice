"""
Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number

For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)
"""

number = int(input("Enter number: "))

amount = 0

for n in range(number + 1):
    amount += n
print("Sum is:", amount)


# OR

n = int(input("Enter number: "))
x = sum(range(n + 1))
print("Sum is:", x)