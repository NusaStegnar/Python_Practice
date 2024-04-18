"""
Write a program (function!) that takes a list and returns a new list that contains 
all the elements of the first list minus all the duplicates.

Extras:

Write two different functions to do this - one using a loop and constructing a list, and another using sets.
"""

def without_duplicates(x):
    new_list = set(x)
    new_list = list(new_list)
    return new_list


def new_elements(x):
    another_list = []
    for num in x:
        if num in another_list:
            continue
        else:
            another_list.append(num)
    return another_list



result = without_duplicates([3, 7, 1, 14, 7, 9, 47, 37, 43, 76, 24, 6, 3, 9, 14])
print(sorted(result))

another_result = new_elements([3, 7, 1, 14, 7, 9, 47, 37, 43, 76, 24, 6, 3, 9, 14])
print(sorted(another_result))

