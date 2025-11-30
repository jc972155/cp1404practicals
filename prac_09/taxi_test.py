"""
CP1404 Practical
Create an object in the Taxi class
"""

from taxi import Taxi

# Initialise taxi object
my_taxi = Taxi("Prius 1", 100)

# Drive 40km
my_taxi.drive(40)

# Print taxi details and fare
print(my_taxi)
print(my_taxi.get_fare())

# Restart and drive 100km
my_taxi.start_fare()
my_taxi.drive(100)

# Print details and fare
print(my_taxi)
print(my_taxi.get_fare())