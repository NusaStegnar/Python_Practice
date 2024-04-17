"""
Write a Python program that accepts a string and calculates the number of digits and letters.
Sample Data : Python 3.2
Expected Output :
Letters 6
Digits 2
"""

text = input("Enter text: ").lower()

num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
alfabeth = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "y", "w", "x", "v", "z"]

numbers = 0
string = 0


for char in text:
    if char in num:
        numbers += 1
    elif char in alfabeth:
        string += 1
    else:
        continue

print(f"Letters: {string} \nDigits: {numbers}")
    



