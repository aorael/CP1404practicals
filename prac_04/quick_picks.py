import random

number_of_quick_picks = int(input("Enter number of quick picks: "))

for i in range(number_of_quick_picks):
    random_number = random.randint(1, 45)

    for j in range(6):
        random_number = random.randint(1, 45)
        print(f"{random_number:2}", end=" ")
    print(f"{random_number:2}",sep="")