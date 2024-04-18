"""
Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, 
too high, or exactly right. 

Extras:

Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""

import random


guess = random.randint(1, 9)
count = 0
while guess:
    num = int(input("Enter a number between 1 and 9: "))
    if num > guess:
        print("The number is to high!")
        count += 1
    elif num < guess:
        print("The number is too low!")
        count += 1
    else:
        print("The number is exactly right!")
        count += 1
        print(f"It took you {count} guesses.")
        break
