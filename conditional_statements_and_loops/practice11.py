"""
Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output 
(all characters in lower case).
"""

list = []

while True:
    l = input()
    if l:
        list.append(l)
    else:
        break

for i in list:
    print(i.lower())