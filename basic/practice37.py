"""
Write a Python program that displays your name, age, and address on three different lines.
"""

def info():

    a = input("Enter your name: ")
    b = input("Enter your age: ")
    c = input("Enter your address: ")

    return f" {a} \n {b} \n {c}"


print(info())