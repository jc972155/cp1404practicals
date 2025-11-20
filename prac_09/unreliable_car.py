"""
CP1404 Practical
UnreliableCar class
"""
from car import Car
from random import randint

class UnreliableCar(Car):
    """Represent an Unreliable Car object"""

    def __init__(self, name: str, fuel: int, reliability: float):
        self.name = name
        self.fuel = fuel
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car a given distance if a random number is less than
        the reliability.

        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        if self.reliability > randint(0, 100):
            if distance > self.fuel:
                distance = self.fuel
                self.fuel = 0
            else:
                self.fuel -= distance
            self.odometer += distance
            return distance
        else:
            return 0