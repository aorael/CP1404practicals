from guitar import Guitar

def main():
    """storing guitar details in a csv file"""
    filename = "guitars.csv"
    guitars = read_contents(filename)
    guitars.sort()  # this automatically sorts using __lt__ method (by year)
    for guitar in guitars:
        print(guitar)

    get_guitar(guitars)
    overwrite_contents(filename, guitars)

def read_contents(filename):
    """read the contents in a csv file"""
    with open(filename, "r") as in_file:
        guitars = []
        for line in in_file:
            parts = line.strip().split(",")
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)
    return guitars


def overwrite_contents(filename, guitars):
    """overwrite the contents into a csv file"""
    with open(filename, "w") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


def get_guitar(guitars):
    """Get guitar details from user input"""
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost:,.2f} added.")
        name = input("Name: ")

main()