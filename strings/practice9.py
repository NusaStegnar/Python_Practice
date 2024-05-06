"""
Write a Python program to remove characters that have odd index values in a given string.
"""

def odd(string):
    new_string = []
    lenght = len(string)

    for n in range(lenght+1):
        if n % 2 == 0:
            new_string.append(string[n])
        else:
            continue
    result_string = "".join(new_string)
    return result_string

result = odd(input("Enter a word: "))
print(result)