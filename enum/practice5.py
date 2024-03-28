"""
Write a Python program to get unique enumeration values.
Expected Output:
Afghanistan = 93
Albania = 355
Algeria = 213
Andorra = 376
Angola = 244
"""

import enum

class Country(enum.Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    India = 355
    USA = 213
for result in Country:
    print(result.name, result.value)
