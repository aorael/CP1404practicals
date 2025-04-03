from prac_09.unreliable_car import UnreliableCar

#Objects:
car1 = UnreliableCar("Car 1", 50, 30)
car2 = UnreliableCar("Car 2", 100, 60)
car3 = UnreliableCar("Car 3", 200, 70)

print(car1)
print(car2)
print(car3)

print()
print(car1.drive(25))
print(car2.drive(50))
print(car3.drive(150))