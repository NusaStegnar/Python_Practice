"""
Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).
Sample function and result :
insert_end('Python') -> onononon
insert_end('Exercises') -> eseseses
"""

def making_copies(string):
    length = len(string)

    if length < 2:
        print("Length of a string must be at least 2.")
    else:
        string = list(string)

        end = string[-2:]
        string_end = "".join(end)
    return string_end * 4

result = making_copies("Python")
print(result)

another = making_copies("Exercises")
print(another)