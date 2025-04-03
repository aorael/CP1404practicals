from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

def main():
    """Get user to choose a taxi to be driven"""
    current_taxi = None
    total_bill = 0
    print("Let's drive!")
    menu = "q)uit, c)hoose taxi, d)rive"

    print(menu)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            indexes = display_to_choose()
            current_taxi = get_taxi(current_taxi, indexes)
        elif choice == "d":
            total_bill = drive_taxi(current_taxi, total_bill)
        else:
            print("Invalid option")

        print(f"Bill to date: ${total_bill:.2f}")  # add bill var
        print(menu)
        choice = input(">>> ").lower()

    display_final_result(total_bill)


def display_to_choose():
    """Display all the taxis the user can choose"""
    index = 0
    indexes = []
    print("Taxis available:")
    for taxi in taxis:
        print(f"{index} - {taxi}")
        indexes.append(index)
        index += 1
    return indexes


def get_taxi(current_taxi, indexes):
    """Get user input when choosing the taxi"""
    taxi_chosen = int(input("Choose taxi: "))
    if taxi_chosen not in indexes:
        print("Invalid taxi choice")
    else:
        current_taxi = taxis[taxi_chosen]
        current_taxi.start_fare()  # reset the fare only, not the distance
    # print(indexes) #checking use
    # print(current_taxi) #checking use
    return current_taxi


def drive_taxi(current_taxi, total_bill):
    """Calculate the fare, bill, distance when taxi is driven"""
    if current_taxi == None:
        print("You need to choose a taxi before you can drive")
    else:
        distance_to_drive = int(input("Drive how far? "))
        current_taxi.drive(distance_to_drive)
        fare = current_taxi.get_fare()  # store fare to avoid recalculating if taxi doesnt get switched multiple times
        print(f"Your {current_taxi.name} trip cost you ${fare:.2f}")
        total_bill += fare
    return total_bill

def display_final_result(total_bill):
    """Display the final conclusion including the total bill and the taxis' distance"""
    print(f"Total trip cost: ${total_bill}")
    print("Taxis are now: ")
    for taxi in taxis:
        print(taxi)


main()