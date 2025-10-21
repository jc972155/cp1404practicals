"""
Hex Colours
save colours to a dictionary
input name and find hex code
"""

COLOUR_TO_HEX = {"amber": "#ffbf00", "barn red": "#7c0a02", "Camel": "#c19a6b", "Denim": "#1560bd", "Eminence": "#6c3082", "Fulvous": "#e48400", "Ginger": "#b06500", "Green Lizard": "#a7f432", "Harlequin": "#3fff00", "Iris": "#5a4fcf", "Jasmine": "#f8de7e"}

for name in COLOUR_TO_HEX.keys():
    print(name)

colour_name = input("Enter short state: ").upper()
while colour_name != "":
    try:
        print(colour_name, "is", COLOUR_TO_HEX[state_code])
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()