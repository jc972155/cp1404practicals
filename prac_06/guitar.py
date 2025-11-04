"""
CP1404 Prac_06
Represent a guitar
Estimated: 40min
Actual:
"""


class Guitar:
    def __init__(self, name="", year=0, cost=0.0):
        """Represent a guitar"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Returns a string with the attributes of the guitar"""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        """Returns the age of the guitar in years"""
        return 2025 - self.year

    def is_vintage(self):
        """Return True if guitar is 50 or more years old"""
        if self.get_age() >= 50:
            return True
        else:
            return False
