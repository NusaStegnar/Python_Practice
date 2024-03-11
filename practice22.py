"""
Write a Python program to count the number 4 in a given list.
"""


def count_number(num):
    count = 0
    for n in num:
        if n == 4:
            count += 1
        else:
            count = count
    return count


four = count_number(["a", "f", 4, 9, "h", "j", "P", 3, 7, 4])
print(four)
