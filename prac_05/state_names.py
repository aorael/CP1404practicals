"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}
print(CODE_TO_NAME)

data = {}
state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        data[state_code] = CODE_TO_NAME[state_code]

        state_code_width = max(len(data) for data in data.keys())
        state_width = max(len(data) for data in data.values())

        for state_code in data:
            print(f"{state_code:{state_code_width}} is {data[state_code]:{state_width}}")
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()
