"""
Write a Python program to calculate the number of days between two dates.
"""
from datetime import datetime


first_year = int(input("Enter a year: "))
first_month = int(input("Enter a month: "))
first_day = int(input("Enter a day: "))

second_year = int(input("Enter a second year: "))
second_month = int(input("Enter a month: "))
second_day = int(input("Enter a day: "))


d0 = datetime(first_year,first_month,first_day)
d1 = datetime(second_year,second_month,second_day)

if d0 > d1:
    result = d0 - d1
    print(result.days)
if d1 > d0:
    result = d1 - d0
    print(result.days)
