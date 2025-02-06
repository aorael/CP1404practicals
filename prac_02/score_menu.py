EXCELLENT_THRESHOLD = 90
PASSABLE_THRESHOLD = 50
MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100

MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"

def main():
    score = validate_score()
    print(MENU)
    choice = input("Enter choice: ").upper()
    while choice != "Q":
        if choice == "G":
            score = validate_score()
        elif choice == "P":
            print_result(score)
        elif choice =="S":
            stars = "*" * score
            print(stars)
        print(MENU)
        choice = input("Enter choice: ").upper()
    print("Farewell.")

def validate_score():
    score = int(input("Enter a score: "))
    while score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        print("Invalid score")
        score = int(input("Enter a score: "))
    return score

def print_result(score):
    if score >= EXCELLENT_THRESHOLD:
        print(f"{score} is Excellent")
    elif score >= PASSABLE_THRESHOLD:
        print(f"{score} is Passable")
    else:
        print(f"{score} is Bad")

main()