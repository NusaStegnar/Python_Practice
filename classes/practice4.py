"""
Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
"""

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


model_x = Vehicle(320, 160)
print(model_x.mileage)