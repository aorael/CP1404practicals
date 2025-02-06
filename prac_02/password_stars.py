PASSWORD_LENGTH = 10

def main():
    password = get_password()
    print_asterisks(password)

def print_asterisks(password):
    print(password * "*")

def get_password():
    password = len(input("Enter password: "))
    while password <= PASSWORD_LENGTH:
        print("Invalid password")
        password = len(input("Enter password: "))
    return password

main()

