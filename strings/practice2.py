"""
Write a Python program to count the number of characters (character frequency) in a string.
Sample String : google.com'
Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
"""

def count_characters(text):
    result = {}
    count = 1
    for char in text:
        if char not in result:
            result[char] = count
        elif char in result:
            result[char] = count + 1
            
    return result

string = count_characters(input("Enter string: "))
print(string)