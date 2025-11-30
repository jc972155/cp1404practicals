"""
CP1404 Practical
Code to test SilverServiceTaxi class
"""
from silver_service_taxi import SilverServiceTaxi

# Initialise a Silver Service Taxi
new_taxi = SilverServiceTaxi("Hummer", 100, 2)
print(new_taxi)

# Drive Silver Service Taxi
new_taxi.drive(18)
assert new_taxi.get_fare() == 48.80
print(new_taxi.get_fare())
print(new_taxi)
