"""
Take two lists:

	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
Write this in one line of Python using at least one list comprehension. 

Extra:

Randomly generate two lists to test this
"""
import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

new_list = [x for x in set(a) if x in b]

print(new_list)


m = random.sample(range(1, 39), 12)
n = random.sample(range(1, 39), 16)
result = [i for i in set(m) if i in n]

print(result)