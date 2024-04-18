"""
Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no divisors.). 
"""

divisors = []

def is_prime(x):
    for num in range(1, x+1):
        if x > 1:
            if x % num == 0:
                divisors.append(num)
            else:
                continue

    if len(divisors) > 2:
        return "not prime"
    elif len(divisors) == 2:
        return "prime"


check = is_prime(int(input("Enter a number: ")))
print(f"The number you entered is {check}.")