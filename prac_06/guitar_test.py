from guitar import Guitar

"""The Guitar objects: gibson and another_guitar"""
gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
another_guitar = Guitar("Another guitar", 2013, 100)

"""Printing the Guitar objects"""
print(gibson)
print(another_guitar)

"""Testing the methods: get_age and is_vintage"""
print(f"in 2022 the {gibson.name} is: 2022 - {gibson.year} = {gibson.get_age()}")
print(f"{gibson.name} get_age() - expected 100. Got {gibson.get_age()}")
print(f"{another_guitar.name} get_age() - expected 9. Got {another_guitar.get_age()}")
print("-----------------------------------------------------------")
print(f"{gibson.name} is_vintage() - expected True. Got {gibson.is_vintage()}")
print(f"{another_guitar.name} is_vintage() - expected False. Got {another_guitar.is_vintage()}")
print("-----------------------------------------------------------")
