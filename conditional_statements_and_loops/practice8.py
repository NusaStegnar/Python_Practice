"""
Write a Python program to get the Fibonacci series between 0 and 50.
Note : The Fibonacci Sequence is the series of numbers :
0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it.
Expected Output : 1 1 2 3 5 8 13 21 34
"""
x, y = 0, 1

while y < 50:
    print(y)

    x, y = y, x + y


# OR

fibonacci = [0, 1]

for num in range(8):
    num = fibonacci[-2] + fibonacci[-1]
    fibonacci.append(num)
print(fibonacci)