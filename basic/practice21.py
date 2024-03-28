""""
Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user.
"""

def number(x):
    if x % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")




odd_or_even = number(int(input("Enter a number: ")))
