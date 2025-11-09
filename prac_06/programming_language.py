"""
CP1404 Prac_06
Represent a programming language
Estimated 25min, actual 27min
"""


class ProgrammingLanguage:
    """Represent a programming language"""

    def __init__(self, name="", typing="", reflection=False, year=0):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if a program is dynamic"""
        if self.typing == "Dynamic":
            return True
        else:
            return False

    def __str__(self):
        """Return a string with the attributes of the object"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def __repr__(self):
        """Returns the __str__ method"""
        return str(self)
