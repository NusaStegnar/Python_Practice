"""
Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'
"""

def one_from_two(x, y):
    first = x[0:2]
    second = y[0:2]

    new_x = x.replace(first, second)
    new_y = y.replace(second, first)

    result = f"{new_x} {new_y}"
    return result

new_string = one_from_two("abc", "xyz")
print(new_string) 