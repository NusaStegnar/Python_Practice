"""
Write a Python program to convert temperatures to and from Celsius and Fahrenheit.
[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
Expected Output :
60°C is 140 in Fahrenheit
45°F is 7 in Celsius
"""

def convert_c(celsius):
    
    fahrnheit = (celsius * 9 / 5) + 32
    return round(fahrnheit)


def convert_f(fahrnheit):
    celsius = (fahrnheit - 32) * 5 / 9
    
    return round(celsius)


conv = convert_c(60)
print(f"60°C is {conv} in Fahrnheit")

conv1 = convert_f(45)
print(f"45°F is {conv1} in Celsius")

# OR

temp = input("Enter the temperature you would like to convert: ")
degree = int(temp[:-1])
symbol = temp[-1]

if symbol.upper() == "C":
   fahrnheit = round((degree * 9 / 5) + 32)
   new_symbol = "Fahrnheit" 
   print(f"{temp} is {fahrnheit} in {new_symbol}") 
elif symbol.upper() == "F":
    celsius = round((degree - 32) * 5 / 9)
    new_symbol = "Celsius" 
    print(f"{temp} is {celsius} in {new_symbol}")