"""
CP1404 Prac_06
Code to test Guitar class
Estimated: 40min
Actual:
"""

from prac_06.guitar import Guitar


def main():
    """Create objects in class Guitar"""
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar_2 = Guitar("Another Guitar", 2013, 1000.00)

    """Code to test get_age() and is_vintage() from class Guitar"""
    print(f"{gibson.name} get_age() - Expected 103. Got {gibson.get_age()}")
    print(f"{guitar_2.name} get_age() - Expected 12. Got {guitar_2.get_age()}")
    print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage()}")
    print(f"{guitar_2.name} is_vintage() - Expected False. Got {guitar_2.is_vintage()}")


main()
