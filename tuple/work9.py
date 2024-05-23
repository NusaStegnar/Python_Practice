"""
Counts the number of occurrences of item 50 from a tuple

tuple1 = (50, 10, 60, 70, 50)
"""

tuple1 = (50, 10, 60, 70, 50)

count = 0

for num in tuple1:
    if num == 50:
        count += 1
    else:
        continue

print(count)

# OR

tuple1 = (50, 10, 60, 70, 50)

print(tuple1.count(50))