"""
Write a Python program to calculate a dog's age in dog years.
Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.
Expected Output:

Input a dog's age in human years: 15                                    
The dog's age in dog's years is 73
"""

year = int(input("Enter dog's age: "))
first_year = 10,5
first_2_years = 2 * 10,5


if year > 2:
    result = ((year - 2) * 4) + 21
elif year <= 2:
    result = year * 10.5

print(result)

