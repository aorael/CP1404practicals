EXCELLENT_THRESHOLD = 90
PASSABLE_THRESHOLD = 50
MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100

MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"

def main():
    print(MENU)
    score = None
    choice = input("Enter choice: ").upper()
    while choice != "Q":
        if choice == "G":
            score = validate_number()
        elif choice == "P":
            score = get_valid_score(score)
            print_result(score)
        elif choice =="S":
            score = get_valid_score(score)
            stars = "*" * score
            print(stars)
        print(MENU)
        choice = input("Enter choice: ").upper()
    print("Finished.")

def validate_number():
    number = int(input("Enter a score: "))
    while number < MINIMUM_SCORE or number > MAXIMUM_SCORE:
        print("Invalid number")
        number = int(input("Enter a score: "))
    return number

def get_valid_score(score):
    if score is None:
        print("Invalid score")
        return validate_number()
    return score

def print_result(score):
    if score >= EXCELLENT_THRESHOLD:
        print(f"{score} is Excellent")
    elif score >= PASSABLE_THRESHOLD:
        print(f"{score} is Passable")
    else:
        print(f"{score} is Bad")

main()