"""
guitar, guitar_test, guitars
Estimate: 40 minutes
Actual:   62  minutes
"""

# Starting time = 15:15
# Finishing time = 16:17

class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}): ${self.cost}"

    def get_age(self, current_year = 2022):
        return current_year - self.year

    def is_vintage(self):
         if (2025 - self.year) >= 50:
             return True
         else:
             return False