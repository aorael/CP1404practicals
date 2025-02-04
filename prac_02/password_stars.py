PASSWORD_LENGTH = 10

def main():
    password = get_password()
    print_asterisks(password)

def print_asterisks(password):
    print(len(password) * "*")

def get_password():
    password = input("Enter password: ")
    while len(password) <= PASSWORD_LENGTH:
        print("Invalid password")
        password = input("Enter password: ")
    return password

main()