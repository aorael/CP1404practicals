"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_THRESHOLD = 90
PASSABLE_THRESHOLD = 50

def main():
    import random

    score = get_number()
    if score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        return "Invalid score"
    else:
        message = get_message(score)
    print(f"{score} is {message}")

    random_score = random.randint(0, 100)
    print(f"The random score is {random_score}")

def get_number():
    number = float(input("Enter score: "))
    return number

def get_message(score):
    if score >= EXCELLENT_THRESHOLD:
        return "Excellent"
    elif score >= PASSABLE_THRESHOLD:
        return "Passable"
    else:
        return "Bad"

main()