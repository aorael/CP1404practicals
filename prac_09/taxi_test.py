from taxi import Taxi

# Q1 Create a new taxi object, my_taxi, with name "Prius 1", 100 units of fuel and price of $1.23
my_taxi = Taxi("Prius 1", 100)

# Q2 Drive the taxi 40 km
my_taxi.drive(40)
# print(my_taxi.fuel) # checking the fuel left

# Q3 Print the taxi's details and the current fare
print(f"Taxi details: {my_taxi}")

# Q4 Restart the meter (start a new fare) and then drive the car 100 km
my_taxi.start_fare()
my_taxi.drive(100)

# Q5 Print the details and the current fare
print(f"Taxi details (2): {my_taxi}")