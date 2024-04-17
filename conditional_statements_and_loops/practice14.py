"""
Write a Python program to check whether an alphabet is a vowel or consonant.
Expected Output:

Input a letter of the alphabet: k                                       
k is a consonant.
"""

letter = input("Enter a letter of the alphabet: ")

vowel = ["a", "e", "i", "o", "u"]

if letter in vowel:
    print(f"Letter {letter} is a vowel.")
else:
    print(f"Letter {letter} is a consonant.")