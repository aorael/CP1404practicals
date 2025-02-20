import random

MINIMUM_RANDOM_NUMBER = 1
MAXIMUM_RANDOM_NUMBER = 45


number_of_quick_picks = int(input("Enter number of quick picks: "))

    for row in range(number_of_quick_picks):
        numbers =[]

        while len(numbers) < number_of_quick_picks:
            random_number = random.randint(MINIMUM_RANDOM_NUMBER,MAXIMUM_RANDOM_NUMBER+1)
            if random_number not in numbers:
                numbers.append(random_number)

        numbers.sort()
        print(" ".join(f"{number:2}" for number in numbers))