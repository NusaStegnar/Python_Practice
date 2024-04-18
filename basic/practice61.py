"""
Write a function that takes an ordered list of numbers 
(a list where the elements are in order from smallest to largest) and another number. 
The function decides whether or not the given number 
is inside the list and returns (then prints) an appropriate boolean.
"""

def is_in(x, y):
    if y > x[0] and y < x[-1]:
        return True
    else:
        return False
    

def is_inside_list(x, y):
    for num in x:
        if num == y:
            return True
    return False

    
result = is_in((sorted([5, 7, 26, 45, 29, 78, 13, 5, 79, 24, 34, 31, 64, 2, 7, 20])), 18)
print(result)

new_result = is_in((sorted([5, 7, 26, 45, 29, 78, 13, 5, 79, 24, 34, 31, 64, 2, 7, 20])), 102)
print(new_result)

another_result = is_inside_list((sorted([5, 7, 26, 45, 29, 78, 13, 5, 79, 24, 34, 31, 64, 2, 7, 20])), 102)
print(another_result)

yet_another_result = is_inside_list((sorted([5, 7, 26, 45, 29, 78, 13, 5, 79, 24, 34, 31, 64, 2, 7, 20])), 34)
print(yet_another_result)