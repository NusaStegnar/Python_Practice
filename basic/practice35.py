"""
Write a Python program that returns true if the two given integer values are equal or their sum or difference is 5.
"""

def check_number():
    a = int(input("Enter an integer: "))
    b = int(input("Enter another integer: "))

    sum_result = a + b
    difference_result = a - b

    if a == b or sum_result == 5 or difference_result == 5:
        return True
    else:
        return False
    

print(check_number())