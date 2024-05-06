"""
Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
If the given string already ends with 'ing', add 'ly' instead.
If the string length of the given string is less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'
"""

def add_ing(text):

    lenght = len(text)

    if lenght < 3:
        return text
    else:
        end = text[-3:]
        if end == "ing":
            text += "ly"
            return text
        else:
            text += "ing"
            return text
        

result = add_ing("abc")
print(result)

another = add_ing("string")
print(another)