"""
CP1404 Practicals
Search wikipedia articles and give a summary
Estimated: 40mins
Actual:
"""

import wikipedia
from wikipedia import DisambiguationError, PageError


def main():
    """Allow user to search for wikipedia articles. Print a summary"""
    page = input("Enter a page title: ")
    while page != '':
        try:
            print(wikipedia.summary(page))
            print(wikipedia.page(page).url)
            page = input("Enter a page title: ")
        except DisambiguationError as e:
            print("We need a more specific title. Try one of the following or enter a new search:")
            print(e.options)
            page = input("Enter a page title: ")
        except PageError:
            print(f"Page id '{page}' does not match any pages. Try another id!")
            page = input("Enter a page title: ")
    print("Thank you.")


main()
