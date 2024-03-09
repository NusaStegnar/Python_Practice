"""
Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
"""

numbers = input("Enter some numbers seperated with comma: ")
numbers = numbers.split(",")



list = []


for num in numbers:
    if num == "," or num == " ":
        continue
    else:
        list.append(num)
print(f"List: ", list)

ntup = tuple(list)

print("Tuple: ", ntup)


