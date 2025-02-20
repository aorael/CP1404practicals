"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"

def main():
    """Loading and displaying the data"""
    data = load_data()
    print(data) # for checking
    display_subject(data)

def display_subject(data):
    """Displaying subject, name, and number of student in a sentence from a list"""
    name_width = max((len(trio[1]) for trio in data))
    number_width = max((len(trio[2]) for trio in data))
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