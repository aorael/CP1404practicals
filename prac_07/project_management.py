
from project import Project
import datetime

menu = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"
default_file = "projects.txt"

def main():
    print("Welcome to Pythonic Project Management")
    projects = load_projects(default_file)

    print(menu)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "L":
            file_name = input("Enter file name to load projects: ")
            try:
                load_projects(file_name)
                print("Projects loaded.")
            except FileNotFoundError:
                print(f"File {file_name} is not found.")

        elif choice == "S":
            file_name = input("Enter file name to save projects: ")
            with open(file_name, "w") as out_file:
                for project in projects:
                    print(f"{project.name} {project.start_date} {project.priority} {project.cost} {project.completion_percentage}", file=out_file)
            print("Projects saved.")

        elif choice == "D":
            incomplete_projects = [project for project in projects if int(project.completion_percentage) < 100]
            completed_projects = [project for project in projects if int(project.completion_percentage) == 100]

            incomplete_projects.sort()
            completed_projects.sort()

            print("Incomplete projects:")
            for project in incomplete_projects:
                print(" ", project)
            print("Completed projects:")
            for project in completed_projects:
                print(" ", project)

        elif choice == "F":  # sort by date
            date_string = get_valid_date("Show projects that start after date (dd/mm/yy): ")
            date_threshold = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            # print(date_string) # FOR CHECKING
            # print(date_threshold) # FOR CHECKING

            filtered_projects = [project for project in projects if project.start_date >= date_threshold]
            filtered_projects.sort(key=lambda x: x.start_date)

            for project in filtered_projects:
                print(project)

        elif choice == "A":
            print("Let's add a new project")
            project_name = get_valid_string("Name: ")
            start_date = get_valid_date("Start date (dd/mm/yy): ")
            priority = get_valid_priority("Priority: ")
            cost = float(get_valid_number("Cost estimate: $"))
            completion_percentage = get_valid_number("Percent complete: ")

            projects.append(Project(project_name, start_date, priority, cost, completion_percentage))

        elif choice == "U":
            for project_index,project in enumerate(projects):
                print(f"{project_index} {project}")

            project_index = int(input("Project choice: "))
            print(projects[project_index])

            new_completion_percentage = get_valid_number("New percentage: ")
            if new_completion_percentage:
                projects[project_index].completion_percentage = int(new_completion_percentage)

            new_priority = input("New priority: ")
            if new_priority:
                projects[project_index].priority = int(new_priority)

        print(menu)
        choice = input(">>> ").upper()

    save_file = input("Would you like to save projects.txt? (Y/n) ").upper()
    if save_file == "Y":
        with open(default_file, "w") as out_file:
            for project in projects:
                print(project, file=out_file)

    print("Thank you for using custom_built project management software.")

def get_valid_priority(prompt):
    """Check user input for priority until the input is valid"""
    try:
        user_input = int(input(prompt))
        return user_input
    except ValueError:
        print("Invalid integer for priority")

def get_valid_date(prompt):
    """Check user input for date until the input is valid"""
    user_input = input(prompt)
    while len(user_input) < 8:
        print("Invalid date")
        user_input = input(prompt)
    return user_input

def get_valid_number(prompt):
    """Check user input for number until the input is valid"""
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("Invalid integer")

def get_valid_string(prompt):
    """Check user input for string until the input is valid"""
    user_input = input(prompt)
    while user_input == "":
        print("Can not be empty")
        user_input = input(prompt)
    return user_input


def load_projects(file_name):
    """Load projects according to the file name"""
    with open(file_name, "r") as in_file:
        next(in_file)
        projects = []
        for line in in_file:
            parts = line.split()

            name = " ".join(parts[:-4])
            start_date = parts[-4]
            priority = parts[-3]
            cost = parts[-2]
            completion_percentage = parts[-1]

            project = Project(name, start_date, priority, cost, completion_percentage)
            projects.append(project)

        project_counter = len(projects)
        print(f"Loaded {project_counter} projects from {projects}")
    return projects


main()

