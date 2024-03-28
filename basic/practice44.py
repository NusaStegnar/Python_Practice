"""
Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.
"""

def are_different(num):
    
    if len(num) == len(set(num)):
        return True
    else:
        return False
    
print(are_different([1, 5, 7, 9]))
print(are_different([2, 4, 5, 5, 7, 9]))

