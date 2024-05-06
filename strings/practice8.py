"""
Write a Python program to change a given string to a newly string where the first and last chars have been exchanged.
"""

def exchange(string):
    text = list(string)
    first = text[0]
    last = text[-1]

    text[0] = last
    text[-1] = first 

    result = "".join(text)
    return result


output = exchange(input("Enter string "))
print(output)