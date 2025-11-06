"""
CP1404 prac_04
Get 5 numbers from user and process them
"""


def main():
    """Get 5 numbers from the user and print processed results"""
    process_numbers(get_numbers())


def get_numbers():
    """Get 5 numbers from the user"""
    numbers = []
    for i in range(5):
        numbers.append(int(input("Number: ")))
    return numbers


def process_numbers(numbers):
    """Process the numbers given by the user"""
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers)}")


main()
