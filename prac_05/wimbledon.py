"""
Wimbledon.py for prac_05
Estimated: 50mins
actual:
"""

def main():
    matches = create_data()
    winner_to_title = get_winners(matches)
    winning_countries = get_countries(matches)
    print("Wimbledon Champions:")
    for name, number in winner_to_title.items():
        print(name, number)
    print(f"\nThese {len(winning_countries)} countries have won Wimbledon: ")
    print(', '.join(sorted(winning_countries)))


def create_data():
    """Takes data from file and places it into a nested list"""
    matches = []
    with open("wimbledon.csv", "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            matches.append(line.split(','))
    del matches[0]
    return matches

def get_winners(matches):
    """Finds each winner and adds to a dictionary as key. Value is how many times they have won."""
    winner_to_title = {}
    for i in range(len(matches)):
        if matches[i][2] in winner_to_title:
            winner_to_title[matches[i][2]] += 1
        else:
            winner_to_title[matches[i][2]] = 1
    return winner_to_title

def get_countries(matches):
    """Loops through match data and adds each winning country to a set."""
    winning_countries = set()
    for i in range(len(matches)):
        winning_countries.add(matches[i][1])
    return winning_countries

main()
