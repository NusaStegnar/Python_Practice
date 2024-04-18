"""
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""

num = int(input("Enter first number: "))
check = int(input("Enter second number: "))

if num % 2 == 0:
    print(f"{num} number is even.")
if num % 4 == 0:
    print(f"{num} number is multiple of 4.")
elif num % 2 != 0:
    print(f"{num} number is odd.")
elif num % 4 != 0:
    print(f"{num} number is not multiple of 4.")


if check % 2 == 0:
    print(f"{check} number is even.")
if check % 4 == 0:
    print(f"{check} number is multiple of 4.")
elif check % 2 != 0:
    print(f"{check} number is odd.")
elif check % 4 != 0:
    print(f"{check} number is not multiple of 4.")


if num % check == 0:
    print(f"{check} divides evenly into {num}.")
else:
    print(f"{check} does not divide evenly into {num}.")