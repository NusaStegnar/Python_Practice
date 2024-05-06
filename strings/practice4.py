"""
Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'
"""

def change_char(text):
    first = text[0]
    new = [first]

    for c in text[1:]:
        if c == first:
            c = "$"
            new.append(c)
        else:
            new.append(c)
    return new


new_text = change_char("restart")
result = "".join(new_text)
print(result)

