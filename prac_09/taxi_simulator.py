"""
CP1404 Practicals
Taxi simulator using Taxi and SilverServiceTaxi instances
"""
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    """Run the taxi simulator"""
    bill_to_date = 0.0
    current_taxi = None
    taxis = [Taxi("Prius", 100),
             SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]

    choice = get_selection()
    while choice != 'q':
        if choice == 'c':
            try:
                current_taxi = select_taxi(taxis)
                print(f"Bill to date: ${bill_to_date:.2f}")
            except (ValueError, IndexError):
                print("Invalid taxi choice")
        elif choice == 'd':
            if current_taxi:
                try:
                    bill_to_date = drive_taxi(current_taxi, bill_to_date)
                    print(f"Bill to date: ${bill_to_date:.2f}")
                except ValueError:
                    print("Invalid distance")
            else:
                print("You need to choose a taxi before you can drive.")
        else:
            print("Invalid option")
        choice = get_selection()
    print(f"Your total trip cost: ${bill_to_date:.2f}")
    print(f"Taxis are now:")
    display_taxis(taxis)


def get_selection():
    """Print the menu and take user input"""
    print("q)uit, c)hoose taxi, d)rive")
    return input(">>> ").lower()


def select_taxi(taxis):
    """Allow the user to choose a taxi fom the available list"""
    print("Taxis available:")
    display_taxis(taxis)
    current_taxi = taxis[int(input("Choose taxi: "))]
    return current_taxi


def drive_taxi(current_taxi, bill_to_date):
    """Drive the selected taxi a given distance."""
    current_taxi.start_fare()
    distance = int(input("Drive how far? "))
    current_taxi.drive(distance)
    bill_to_date += current_taxi.get_fare()
    print(f"Your {current_taxi.name} trip cost you ${current_taxi.get_fare():.2f}")
    return bill_to_date


def display_taxis(taxis):
    """Print each of the taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()
