from random import randint
from car import Car

class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability=0.0):
        """initializes the instance variables"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        return f"{super().__str__()}, reliability = {self.reliability}"

    def drive(self, distance):
        """drive the car with the given distance from user"""
        random_number = randint(0,100)
        # print(f"random num {random_number}") # for checking
        if random_number < self.reliability:
            return f"distance driven: {super().drive(distance)}"
        else:
            return "not driving"