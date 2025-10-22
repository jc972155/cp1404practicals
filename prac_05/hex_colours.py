"""
Hex Colours
save colours to a dictionary
input name and find hex code
"""

COLOUR_TO_HEX = {"AMBER": "#ffbf00", "BARN RED": "#7c0a02", "CAMEL": "#c19a6b", "DENIM": "#1560bd", "EMINENCE": "#6c3082", "FULVOUS": "#e48400", "GINGER": "#b06500", "GREEN LIZARD": "#a7f432", "HARLEQUIN": "#3fff00", "IRIS": "#5a4fcf", "JASMINE": "#f8de7e"}

for name in COLOUR_TO_HEX.keys():
    print(name)

colour_name = input("Enter a colour: ").upper()
while colour_name != "":
    try:
        print(colour_name, "is", COLOUR_TO_HEX[colour_name])
    except KeyError:
        print("Enter a colour on the list")
    colour_name = input("Enter a colour: ").upper()
print("Program Finished")