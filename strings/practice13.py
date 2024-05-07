"""
Write a Python function to reverse a string if its length is a multiple of 4.
"""

def reverse(string):
    length = len(string)

    if length % 4 != 0:
        string = string
    elif length % 4 == 0:
        string = string[::-1]
    return string

result = reverse(input("Enter a string: "))
print(result)
