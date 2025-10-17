"""
Get valid score
evaluate score
print stars
"""

def main():
    score = get_score()
    print("Menu")
    choice = input("> ").lower()
    while choice != "q":
        if choice == "p":
            print_result(score)
        elif choice == "g":
            get_score()
        elif choice == "s":
            print_stars(score)
        else:
            print("Invalid Choice")
        print("Menu")
        choice = input("> ").lower()
    print("Farewell")

def get_score():
    score = int(input("Enter Score: "))
    while score < 0 or score > 100:
        print("Invalid Score")
        score = int(input("Enter Score: "))
    return score

def print_result(score):
    print(evaluate_score(score))

def print_stars(score):
    for i in range(score):
        print("*")

def evaluate_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()
