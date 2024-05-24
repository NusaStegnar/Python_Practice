"""
Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.

Use the following code for this exercise.

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass
    
    
Expected Output:

Color: White, Vehicle name: School Volvo, Speed: 180, Mileage: 12
Color: White, Vehicle name: Audi Q5, Speed: 240, Mileage: 18
"""

class Vehicle:
    color="White"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass


school_bus = Bus("School Volvo", 180, 12)
print("Color:", school_bus.color, "Vehicle name:", school_bus.name, "Speed:", school_bus.max_speed, "Mileage:", school_bus.mileage)

auto = Car("Audi Q5", 240, 18)
print("Color:", auto.color, "Vehicle name:", auto.name, "Speed:", auto.max_speed, "Mileage:", auto.mileage)