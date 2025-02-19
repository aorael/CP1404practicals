"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"

def main():
    data = load_data()
    print(data)
    display_subject(data)

def display_subject(data):
    name_width = max((len(pair[1]) for pair in data))
    number_width = max((len(pair[2]) for pair in data))
    for i in range(len(data)):
        subject = data[i][0]
        name = data[i][1]
        number_of_student = data[i][2]
        print(f"{subject} is taught by {name:{name_width}} and has {number_of_student:>{number_width}} students")


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    # for line in input_file:
        # print(line)  # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        # line = line.strip()  # Remove the \n
        # parts = line.split(',')  # Separate the data into its parts
        # print(parts)  # See what the parts look like (notice the integer is a string)
        # parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        # print(parts)  # See if that worked
        # print("----------")
        # print(line)
    data = ([line.strip().split(",") for line in input_file][:2])
    input_file.close()
    return data

main()