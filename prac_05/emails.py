"""
Emails prac_05
Input email
Take name from email or ask user for name
Store in dictionary
Estimate: 30mins
Actual: 31mins
"""


def main():
    name_to_email = {}
    email = input("Email: ")
    while email != '':
        name = email.split('@')
        name = name[0].split('.')
        name = ' '.join(name).title()
        name_answer = input(f'Is your name {name.title()}? (Y/n): ').lower()
        if name_answer == 'y' or name_answer == '':
            name_to_email[name] = email
        else:
            name = input("Name: ").title()
            name_to_email[name] = email
        email = input("Email: ")
    for name, email in name_to_email.items():
        print(f'{name} ({email})')

main()