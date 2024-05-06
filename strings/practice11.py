"""
Write a Python script that takes input from the user and displays that input back in upper and lower cases.
"""

def lower(text):
    text0 = text.upper()
    text1 = text.lower()
    return f"{text0} \n{text1}"



result = lower(input("Enter text: "))
print(result)