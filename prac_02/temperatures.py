"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

def main():
    MENU = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ - Quit"
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celcius = convert_to_celsius(fahrenheit)
            print(f"Result: {celcius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

def convert_to_fahrenheit(celsius):
    """Converting the temperatures from celsius to fahrenheit"""
    return  5 / 9 * (celsius - 32)

def convert_to_celsius(fahrenheit):
    """Converting the temperatures from fahrenheit to celsius"""
    return fahrenheit * 9.0 / 5 + 32

main()