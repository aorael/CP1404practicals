from taxi import Taxi

class SilverServiceTaxi(Taxi):
    flagfall =4.50
    def __init__(self, name, fuel, fanciness: float):
        """initializes instance variables"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        """display instance variables with the following format"""
        return f"{super().__str__()} plus flagfall of ${SilverServiceTaxi.flagfall:.2f}"

    def get_fare(self):
        """calculate the total fare for a silver taxi"""
        return (super().get_fare()) + self.flagfall