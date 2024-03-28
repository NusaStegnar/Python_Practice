"""
Write a Python program to test whether a passed letter is a vowel or not.
"""

def letter_check(x):
    vowel = ["a", "e", "i", "o", "u"]
    if x in vowel:
        return "Letter is a vowel"
    return "Letter is not a vowel"
    

print(letter_check(input("Enter a letter: ")))