"""
CP1404 Prac_07
myguitars.py
Read guitars from a CSV file and print them
"""

from guitar import Guitar


def main():
    """Read file of guitars, save as objects, display."""
    guitars = []
    in_file = open('guitars.csv', 'r')
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()

    add_guitar(guitars)
    guitars.sort()
    print_guitars(guitars)


def print_guitars(guitars):
    """Print the guitars"""
    for guitar in guitars:
        print(guitar)


def add_guitar(guitars):
    get_guitar(guitars)
    with open("guitars.csv", "w") as out_file:
        for guitar in guitars:
            out_file.write(f"{guitar.name},{str(guitar.year)},{str(guitar.cost)}\n")


def get_guitar(guitars):
    name = input("Enter new guitar name: ")
    year = int(input("Year of manufacture: "))
    cost = float(input("Cost: "))
    guitars.append(Guitar(name, year, cost))


main()
