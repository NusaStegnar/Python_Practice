"""
Write a program (using functions!) that asks the user for a long string containing multiple words. 
Print back to the user the same string, except with the words in backwards order.

My name is Michele  ----->>> Michele is name My
"""

def reverse_order(words):

    words = words.split()
    words = words[::-1]
    new_words = " ".join(words)
    return new_words


result = reverse_order(input("Please enter multiple words: "))
print(result)