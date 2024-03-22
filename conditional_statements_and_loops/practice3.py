"""
Write a Python program to guess a number between 1 and 9.
Note : User is prompted to enter a guess. 
If the user guesses wrong then the prompt appears again until the guess is correct, 
on successful guess, user will get a "Well guessed!" message, and the program will exit.
"""

import random


target_num  = random.randint(1, 10)


while True:
    guess_num = int(input("Guess a number between 1 and 9: "))
    if guess_num == target_num:
        print("Well guessed!")
        break