"""
Write a Python program to remove a newline in Python.
"""

def newline(string):
    
    new_string = string.replace("\n", "")
    return new_string

result = newline("Nasa masa gre k zdravniku. \nKo pride domov je zelo vesela, \nsaj ji je zdravnik po pregledu dal liziko.")
print(result)