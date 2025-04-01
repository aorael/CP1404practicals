from silver_service_taxi import SilverServiceTaxi

my_taxi = SilverServiceTaxi("Hummer", 200, 4)
print(my_taxi)

taxi2 = SilverServiceTaxi("Taxi 2", 100, 2)
# fuel cant be less than 18 because taxi might stop
# fuel is 100 because to avoid running out of fuel
print(taxi2)

print("-")
def check_by_assert():
    expected_fare = 48.80
    taxi2.drive(18)
    calculated_fare = taxi2.get_fare()
    # print(calculated_fare) # for checking

    assert round(calculated_fare, 2) == expected_fare
    # no AssertionError means the values match

check_by_assert()
