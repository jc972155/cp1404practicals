"""
CP1404 prac_04
Quick Picks. Display lines of 6 random numbers
"""

MIN_PICK = 1
MAX_PICK = 45

from random import randint


def main():
    """Ask user how many picks, then display each pick"""
    number_of_picks = int(input("How many quick picks? "))
    picks = pick_numbers(number_of_picks)
    print_picks(picks)


def pick_numbers(number_of_picks):
    """Select 5 unique numbers and store them in a nested list"""
    picks = []
    for i in range(number_of_picks):
        numbers = []
        while len(numbers) < 5:
            next_num = randint(MIN_PICK, MAX_PICK)
            if next_num not in numbers:
                numbers.append(next_num)
        numbers.sort()
        picks.append(numbers)
    return picks


def print_picks(picks):
    """Print each pick aligned to the right, on a new line"""
    for pick in picks:
        for number in pick:
            print(f"{number:>2}", end=" ")
        print()  # Print next pick on a new line


main()
