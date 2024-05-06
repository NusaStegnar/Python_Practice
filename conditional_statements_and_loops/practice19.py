"""
Write a Python program to calculate the sum and average of n integer numbers (input from the user). Input 0 to finish.
"""
print("To calculate the sum and average of numbers, enter some numbers. Input 0 to finish.")

count = 0
sum = 0
number = 1

while number != 0:
    number = int(input(" "))
    sum += number
    count += 1

if count == 0:
    print("Enter some numbers")
else:
    print(f"Average and the Sum of the above numbers are: {sum / (count - 1)}, {sum}") 