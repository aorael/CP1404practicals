
NAME_TO_CODE = {"Magenta": "ff00ff", "White": "ffffff" ,"Black": "000000", "Brown": "a52a2a", "Chocolate": "d2691e", "Pink": "fc0cb", "Gray": "bebebe", "Sage": "bcb88a", "Purple": "a020f0", "Burgundy": "800020"}

# print(len(NAME_TO_CODE.keys())) # number of colors

color_name = input("Enter a color: ").title()
while color_name != "":
    try:
        print(f"#{NAME_TO_CODE[color_name]}")
    except KeyError:
        print("The color is unavailable")
    color_name = input("Enter a color: ").title()