"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)

    limo = Car(100) # Q1
    limo.add_fuel(20) # Q2
    print(f"Amount of fuel in the car is {limo.fuel}") # Q3

    limo.drive(115)
    print(f"Amount of fuel in the car is {limo.fuel} when it is used to drive for 115 km") # Q4

    my_car = Car(my_car.fuel, "My car") # Q6
    limo = Car(limo.fuel, "Limo") # Q6

    print(my_car) # Q7
    print(limo) # Q7

main()