class Guitar:
    VINTAGE_AGE = 50

    def __init__(self, name, year, cost):
        """stores instance variables"""
        self.name = name
        self.year = int(year)
        self.cost = float(cost)

    def __str__(self):
        """prints out the instance variables using the formatted sentence"""
        return f"{self.name} ({self.year}): ${self.cost}"

    def get_age(self, current_year = 2025):
        """count the age of the guitar"""
        return current_year - self.year

    def is_vintage(self):
        """returns boolean value when the age of the guitar is over 50 years old"""
        return self.get_age() >= Guitar.VINTAGE_AGE

    def __lt__(self, other):
        """compare two values if the first value is less than the other value"""
        return self.year < other.year