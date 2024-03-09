"""
Write a Python program that accepts a filename from the user and prints the extension of the file.
"""
import sys


filename = input("Enter a filename: ")

filename = filename.split(".")
fname = filename[-1]

print(f"Output: {fname}")