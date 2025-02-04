"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

def main():
    import random

    score = get_number()
    if score < 0 or score > 100:
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
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()