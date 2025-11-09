"""
CP1404 Prac_06
Client code to use ProgrammingLanguage class
Estimated 25min, Actual 27min
"""

from prac_06.programming_language import ProgrammingLanguage


def main():
    """Create objects in ProgrammingLanguage class"""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    languages = [python, ruby, visual_basic]
    print(languages)

    """Print the dynamically typed languages"""
    print("The dynamically typed languages are: ")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()
