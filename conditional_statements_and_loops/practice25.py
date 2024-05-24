"""
Write a program to print multiplication table of a given number
For example, num = 2 so the output should be

2
4
6
8
10
12
14
16
18
20
"""

number = int(input("Enter number: "))

for n in range(1, 11):
    n *= number
    print(n)
