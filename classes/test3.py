class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("Jane", 34)
p1.myfunc()

p1.age = 40
print(p1.age)

del p1.age
print(p1.age)