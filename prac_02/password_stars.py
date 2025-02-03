PASSWORD_LENGTH = 10

password = len(input("Enter password: "))
while len(password) <= PASSWORD_LENGTH:
    print("Invalid password")
    password = input("Enter password: ")

print(password * "*")
