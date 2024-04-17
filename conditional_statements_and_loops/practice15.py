"""
Write a Python program to convert a month name to a number of days.
Expected Output:

List of months: January, February, March, April, May, June, July, August
, September, October, November, December                                
Input the name of Month: February                                       
No. of days: 28/29 days 
"""

month = input("Input the name of Month: ").title()

months_31_days = ["January", "March", "May", "July", "August", "October", "December"]
months_30_days = ["April", "June", "September", "November"]
special = ["February"]

if month in months_31_days:
    print("No. of days: 31 days.")
elif month in months_30_days:
    print("No. of days: 30 days.")
elif month in special:
    print("No. of days: 28/29 days.")