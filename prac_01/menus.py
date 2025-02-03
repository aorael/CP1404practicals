menu = ["(H)ello", "(G)oodbye", "(Q)uit"]

name = input("Enter name: ")

for option in menu:
    print(option)
choice = input(">>> ").upper()

while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")

    for option in menu:
        print(option)
    choice = input(">>> ").upper()
print("Finished.")

# CHECKING
# declare menu as string > MENU = "(H)ello\n(G)oodbye\n(Q)uit"
MENU = "(H)ello\n(G)oodbye\n(Q)uit"

name = input("Enter name: ")

print(MENU)
choice = input(">>> ").upper()

while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")

    print(MENU)
    choice = input(">>> ").upper()
print("Finished.")