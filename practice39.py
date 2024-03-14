"""
Write a Python program to compute the future value of a specified principal amount, rate of interest, and number of years.
Test Data : amt = 10000, int = 3.5, years = 7
Expected Output : 12722.79
"""

# def future_value(amt, int, years):

#     result = amt * (( 1 + (0.01 * int)) ** years)

#     return result

# print(round(future_value(10000, 3.5, 7), 2))



# OR


amt = 10000
int = 3.5
years = 7

for i in range(7):
    amt += amt * (0.01 * 3.5)

print(round(amt, 2))