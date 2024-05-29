"""
Write a Python program to get the frequency of elements in a given list of lists.
Original list of lists:
[[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]
Frequency of the elements in the said list of lists:
{1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}
"""

original_list = [[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]
new_list = []

new_dict = {}

for row in original_list:
    for num in row:
        new_list.append(num)

for n in new_list:
    if n in new_dict.keys():
        new_dict[n] += 1
    else:
        key = n
        value = 1
        new_dict[key] = value
        
print(new_dict)
    