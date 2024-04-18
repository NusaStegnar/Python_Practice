"""
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list 
of only the first and last elements of the given list. For practice, write this code inside a function.
"""


new_list = []

def another_list(a):
    x = a[0]
    y = a[-1]
    new_list.append(x)
    new_list.append(y)
    return new_list

result = another_list(a = [5, 10, 15, 20, 25])
print(result)