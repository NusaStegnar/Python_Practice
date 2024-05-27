class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, firstname, lastname, graduation_year):
        super().__init__(firstname, lastname)
        self.graduation_year = graduation_year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduation_year)


p1 = Person("john", "doe")
p1.printname()

p2 = Student("mike", "olsen", 2019)
p2.printname()
print(p2.graduation_year)
p2.welcome()