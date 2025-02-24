
NAME_TO_CODE = {"Amber": "ffbf00", "Amethyst": "9966cc" ,"Apricot": "fbceb1", "Aqua": "00ffff", "Asparagus": "87a96b", "Black": "000000", "Blond": "faf0be", "Bone": "e3dac9", "Brown": "a52a2a", "Burgundy": "800020"}

print(len(NAME_TO_CODE.keys()))

color_name = input("Enter a color: ").title()
while color_name != "":
    try:
        print(f"{color_name} = #{NAME_TO_CODE[color_name]}")
    except:
        print("The color is not in the dictionary")
    color_name = input("Enter a color: ").title()