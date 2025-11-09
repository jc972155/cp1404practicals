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
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()
    guitars.sort()
    print_guitars(guitars)


def print_guitars(guitars):
    """Print the guitars"""
    for guitar in guitars:
        print(guitar)


main()
