"""
Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String
"""

def making_string(text):
    lenght = len(text)

    if lenght < 2:
        return "Empty String"
    else:
        first = text[0:2]
        last = text[-2:]
        result = first+last
        return result

new_string = making_string("w3resource")
print(new_string)

another = making_string("w3")
print(another)

again = making_string("w")
print(again)
