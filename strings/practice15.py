"""
Write a Python program to count and display vowels in text.
"""

def count_vowels(text):

    vowels = "aeiouAEIOU"
    count = 0
    empty = []

    for char in text:
        if char in vowels:
            empty.append(char)
            count += 1
        else:
            continue
    return count, empty

count, vowels = count_vowels("Nasa Masa gre k zdravniku.")
print(f"{count} \n{vowels}")

    

   


