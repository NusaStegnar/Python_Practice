"""
Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615
"""

n = input("Enter a number: ")
nn = n + n
nnn = n + n + n

n = int(n)
nn = int(nn)
nnn = int(nnn)

result = n + nn + nnn
print(result)