"""
Write a Python program that prints the calendar for a given month and year.
"""

import calendar

month = int(input("Enter the month: "))
year = int(input("Enter the year: "))

print(calendar.month(year, month))
