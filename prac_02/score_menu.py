MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"

def main():
    print(MENU)
    choice = input("Enter choice: ").upper()
    while choice != "Q":
        if choice == "G":
            score = float(input("Enter a score: "))
            while score < 0 and score > 100:
                print("Invalid score")
                score = float(input("Enter a score: "))
        elif choice == "P":
            # TODO: copy or import your function to determine the result from score.py
        elif choice =="S":
            # TODO: this should print as many stars as the score
        print(MENU)
        choice = input("Enter choice: ").upper()
    print("Finished.")
main()