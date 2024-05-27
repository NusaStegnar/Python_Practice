"""
Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number.
Use that function definition to make a function that always doubles the number you send in:
"""

def my_func(n):
    return lambda a: a * n

my_doubler = my_func(2)
my_tripler = my_func(3)
print(my_doubler(11))
print(my_tripler(11))