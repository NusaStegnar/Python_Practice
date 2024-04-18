"""
Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
"""
number = int(input("Enter a number: "))

new_list = []

for num in range(1, number+1):
    if number % num == 0:
        new_list.append(num)
    else:
        continue

print(new_list)