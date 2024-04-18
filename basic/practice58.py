"""
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence 
is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
"""
new_list = []

def fibonnaci(x):
    if x == 0:
        new_list = []
    elif x == 1:
        new_list = [1]
    elif x == 2:
        new_list = [1, 1]
    elif x > 2:
        new_list = [1, 1]
        for num in range(x-2):
            new_list.append(new_list[-1] + new_list[-2])
        return new_list 

result = fibonnaci(int(input("Enter the number of numbers in the sequence to generate: ")))
print(result)