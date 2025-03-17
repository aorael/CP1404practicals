from guitar import Guitar

def main():
    filename = "guitars.csv"
    with open(filename, "r") as in_file:
        guitars = []
        for line in in_file:
            parts = line.strip().split(",")
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)

    guitars.sort() #this automatically sorts using __lt__ method (by year)
    for guitar in guitars:
        print(guitar)
main()