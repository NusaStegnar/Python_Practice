"""
Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string. 
If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
Sample String : 'The lyrics is not that poor!'
'The lyrics is poor!'
Expected Result : 'The lyrics is good!'
'The lyrics is poor!'
"""

def searching(text):

    word_not = text.find("not")
    word_poor = text.find("poor")
    if word_not < word_poor and word_not > 0 and word_poor > 0:
        text = text.replace(text[word_not: word_poor+4], "good")      

    return text

result = searching("The lyrics is not that poor!") 
print(result)

another = searching("The lyrics is poor!")
print(another)