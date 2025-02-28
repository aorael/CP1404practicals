"""
Emails
Estimate: 50 minutes
Actual:   107 minutes
"""

key_to_value = {}

def main():
    """Displaying the name of the user and the email account"""
    email = input("Email: ")
    while email != "":
        name = get_name(email)
        name_confirmation = input(f"Is your name {name} (Y/n)? ").upper()

        if name_confirmation == "Y" or name_confirmation == "":
            key_to_value[email] = name
        else:
            actual_name = input("Name: ")
            key_to_value[email] = actual_name
        email = input("Email: ")

    # print(key_to_value) #check dictionary
    print()
    for email, name in key_to_value.items():
        print(f"{name} ({email})")

def get_name(email):
    """Converting name from the email user input"""
    username = email.split("@")[0]
    name = " ".join(username.split(".")).title()
    return name


main()
