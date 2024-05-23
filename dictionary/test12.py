"""
Write a Python program to get the total length of all values in a given dictionary with string values.
Original dictionary:
{'#FF0000': 'Red', '#800000': 'Maroon', '#FFFF00': 'Yellow', '#808000': 'Olive'}
Total length of all values of the said dictionary with string values:
20
"""

dic = {'#FF0000': 'Red', '#800000': 'Maroon', '#FFFF00': 'Yellow', '#808000': 'Olive'}
sum = 0

for value in dic.values():
    sum += len(value)
print(sum)
