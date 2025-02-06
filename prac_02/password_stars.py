PASSWORD_LENGTH = 10

def main():
    password = get_password()
    print_asterisks(password)

def print_asterisks(password):
    """Printing asterisks based on the length of password"""
    print(password * "*")

def get_password():
    """Validating the password input by the user"""
    password = len(input("Enter password: "))
    while password <= PASSWORD_LENGTH:
        print("Invalid password")
        password = len(input("Enter password: "))
    return password

main()
