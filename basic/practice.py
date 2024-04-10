list = ["carac", "motor"]

lst = []
for char in list[-1]:
    lst.append(char)

if lst[::] == lst[::-1]:
    print(True)
else:
    print(False)

