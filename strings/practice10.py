"""
Write a Python program to count the occurrences of each word in a given sentence.
"""

def count(sentence):
    
    new_list = {}

    sentence = sentence.split()
    
    for word in sentence:
        if word in new_list:
            new_list[word] += 1
        else:
            new_list[word] = 1
    return new_list

result = count(input("Enter a sentence: "))
print(result)
