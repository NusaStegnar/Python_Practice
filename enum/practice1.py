from enum import Enum

"""
Write a Python program to create an Enum object and display a member name and value.
Sample data :
Member name: Albania
Member value: 355
"""

class Country(Enum):
    Albania = 355



print(f"Member name: ", Country.Albania.name, "\nMember value: ", Country.Albania.value)