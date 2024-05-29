"""
Write a Python program to compute the sum of digits of each number in a given list.
Original tuple:
[10, 2, 56]
Sum of digits of each number of the said list of integers:
14
Original tuple:
[10, 20, 4, 5, 'b', 70, 'a']
Sum of digits of each number of the said list of integers:
19
Original tuple:
[10, 20, -4, 5, -70]
Sum of digits of each number of the said list of integers:
19
"""

list_1 = [10, 2, 56]
list_2 = [10, 20, 4, 5, 'b', 70, 'a']
list_3 = [10, 20, -4, 5, -70]

sum_all = 0
sum_all_1 = 0
sum_all_2 = 0

for num in list_1:
    for n in str(num):
        if n.isdigit():
            sum_all += int(n)
print(sum_all)


for num in list_2:
    for n in str(num):
        if n.isdigit():
            sum_all_1 += int(n)
print(sum_all_1)


for num in list_3:
    for n in str(num):
        if n.isdigit():
            sum_all_2 += int(n)
print(sum_all_2)