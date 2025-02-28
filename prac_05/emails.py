"""
Emails
Estimate: 50 minutes
Actual:   107 minutes
"""

email_to_name = {}

def main():
    """Displaying the name of the user and the email account"""
    email = input("Email: ")
    while email != "":
        name = get_name(email)
        name_confirmation = input(f"Is your name {name} (Y/n)? ").upper()

        if name_confirmation == "Y" or name_confirmation == "":
            email_to_name[email] = name
        else:
            actual_name = input("Name: ")
            email_to_name[email] = actual_name
        email = input("Email: ")

    # print(key_to_value) #check dictionary
    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")

def get_name(email):
    """Converting name from the email user input"""
    username = email.split("@")[0]
    name = " ".join(username.split(".")).title()
    return name


main()
