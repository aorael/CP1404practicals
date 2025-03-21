import datetime
# start_date is converted in datetime format on init method
# cost is converted to float type on init method
# start_date is converted to the initial format for displaying

class Project:
    def __init__(self, name="", start_date="", priority=0, cost=0.0, completion_percentage=0):
        """store the instance variables of projects"""
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = priority
        self.cost = float(cost)
        self.completion_percentage = completion_percentage

    def __str__(self):
        """display the instance variables in a formatted string"""
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: ${self.cost:.2f}, completion: {self.completion_percentage}%"

    def __lt__(self, other):
        """used for sorting according to the priority"""
        return int(self.priority) < int(other.priority)