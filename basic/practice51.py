"""
Ask the user for a string and print out whether this string is a palindrome or not. 
(A palindrome is a string that reads the same forwards and backwards.)
"""

words = input("Enter a string: ")

if words[::] == words[::-1]:
    print(f"{words} is palindrome.")
else:
    print(f"{words} is not palindrome.") 