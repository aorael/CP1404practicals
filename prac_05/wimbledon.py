"""
Wimbledon
Estimate: 80 minutes
Actual:   18  minutes 27 min
"""

import csv
filename = "wimbledon.csv"
name_to_number = {}
champions = []
countries = []

def main():
    print("Wimbledon Champions:")
    with open(filename) as in_file:
        reader = csv.reader(in_file)
        next(reader)
        for record in reader:
            # print(record[0], record[1],record[2],record[3], record[4], record[5])
            get_data(record)
        convert_dictionary()
    for champion_name, number_of_wins in name_to_number.items():
        print(f"{champion_name} {number_of_wins}")

    # print(champions) #champion names
    # print(name_to_number) #dictionary = champions : number of wins
    display_countries()


def get_data(record):
    country = record[1]
    if country not in countries:
        countries.append(country)
    champion_name = record[2]
    champions.append(champion_name)


def convert_dictionary():
    for champion_name in champions:
        number_of_wins = name_to_number.get(champion_name, 0) + 1
        name_to_number[champion_name] = number_of_wins


def display_countries():
    number_of_country = len(countries)
    print(f"These {number_of_country} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


main()