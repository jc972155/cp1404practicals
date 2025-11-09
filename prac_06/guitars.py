"""
CP1404 prac_06
Client code for class Guitar
Estimated: 30min
Actual: 30min
"""

from prac_06.guitar import Guitar


def main():
    """Initialise guitars list and run other functions"""
    guitars = []
    print("My guitars!")
    get_guitar(guitars)
    print_guitars(guitars)


def get_guitar(guitars):
    """Get input from user to create object"""
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitars.append(Guitar(name, year, cost))
        name = input("Name: ")
    print("\n... snip ...\n")


def print_guitars(guitars):
    """Print the list of guitars"""
    for i, guitar in enumerate(guitars, 1):
        print(
            f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{" (vintage)" if guitar.is_vintage() else ""}")


main()
