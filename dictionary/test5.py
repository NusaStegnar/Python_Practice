"""
Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""

def creating_dic(number):
    dic = {}
    for n in range(1, number+1):
        dic[n] = n*n
    return dic

result = creating_dic(5)
print(result)
