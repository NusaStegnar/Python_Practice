"""
Write a Python program to create a histogram from a given list of integers.
"""

def histogram(integers):
    for num in integers:
        output = ""
        while num > 0:
            output += "#" 
            num -= 1
        print(output)


histogram([2, 9, 5, 8, 4])
