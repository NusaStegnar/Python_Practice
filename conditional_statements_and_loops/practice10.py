"""
Write a Python program that takes two digits m (row) and n (column) as input and generates a two-dimensional array. 
The element value in the i-th row and j-th column of the array should be i*j.
Note :
i = 0,1.., m-1
j = 0,1, n-1.

Test Data : Rows = 3, Columns = 4
Expected Result : [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]
"""

row_num = int(input("Input number of rows: "))
col_num = int(input("Input number of columns: "))


result = [[0 for col in range(col_num)] for row in range(row_num)]


for row in range(row_num):
    for col in range(col_num):
        result[row][col] = row * col


print(result) 