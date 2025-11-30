"""
CP1404
Code to test UnreliableCar class
"""
from unreliable_car import UnreliableCar

# Initialise a new unreliable car
my_car = UnreliableCar("dodgy_car", 100, 50)

# Code to test reliability of car
driven_successfully = 0
for i in range(0, 100):
    if my_car.drive(100) > 0:
        driven_successfully += 1
        my_car.add_fuel(100)
print(f"Car driven {driven_successfully} times")
