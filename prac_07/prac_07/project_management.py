import sys
from project import Project
from datetime import datetime

DEFAULT_FILE = 'projects.txt'

def load_projects(filename=DEFAULT_FILE):
    projects = []
    try:
        with open(filename, 'r') as in_file:
            in_file.readline()  # skip header
            for line in in_file:
                parts = line.strip().split('\t')
                project = Project(*parts)
                projects.append(project)
    except FileNotFoundError:
        print(f"Warning: {filename} not found, starting with empty list.")
    return projects

def save_projects(projects, filename=DEFAULT_FILE):
    header = "Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n"
    with open(filename, 'w') as out_file:
        out_file.write(header)
        for p in projects:
            date_str = p.start_date.strftime("%d/%m/%Y")
            out_file.write(f"{p.name}\t{date_str}\t{p.priority}\t{p.cost}\t{p.completion}\n")
    print(f"Saved {len(projects)} projects to {filename}")

def display_projects(projects):
    incomplete = [p for p in projects if not p.is_completed()]
    complete = [p for p in projects if p.is_completed()]
    incomplete.sort()
    complete.sort()
    print("Incomplete projects:")
    for p in incomplete:
        print(f"  {p}")
    print("Completed projects:")
    for p in complete:
        print(f"  {p}")

def filter_projects(projects):
    date_str = input("Show projects that start after date (dd/mm/YYYY): ")
    cutoff = datetime.strptime(date_str, "%d/%m/%Y").date()
    filtered = [p for p in projects if p.start_date > cutoff]
    filtered.sort()
    for p in filtered:
        print(f"  {p}")

def add_project(projects):
    name = input("Name: ")
    date_str = input("Start date (dd/mm/YYYY): ")
    priority = input("Priority: ")
    cost = input("Cost estimate: ")
    completion = input("Percent complete: ")
    projects.append(Project(name, date_str, priority, cost, completion))

def update_project(projects):
    for i, p in enumerate(projects):
        print(f"{i} {p}")
    idx = int(input("Project choice: "))
    project = projects[idx]
    print(project)
    new_comp = input("New Percentage: ")
    new_prio = input("New Priority: ")
    project.update(new_completion=new_comp or None,
                   new_priority=new_prio or None)

def main():
    projects = load_projects()
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILE}")
    menu = ("\nMenu:\n"
            "(L)oad projects\n"
            "(S)ave projects\n"
            "(D)isplay projects\n"
            "(F)ilter by date\n"
            "(A)dd new project\n"
            "(U)pdate project\n"
            "(Q)uit\n")
    choice = ''
    while choice.upper() != 'Q':
        print(menu)
        choice = input(">>> ")
        if choice.upper() == 'L':
            projects = load_projects(input("Filename: ") or DEFAULT_FILE)
        elif choice.upper() == 'S':
            save_projects(projects, input("Filename: ") or DEFAULT_FILE)
        elif choice.upper() == 'D':
            display_projects(projects)
        elif choice.upper() == 'F':
            filter_projects(projects)
        elif choice.upper() == 'A':
            add_project(projects)
        elif choice.upper() == 'U':
            update_project(projects)
        elif choice.upper() == 'Q':
            break
        else:
            print("Invalid choice")

    if input(f"Save to {DEFAULT_FILE}? (y/n) ").lower().startswith('y'):
        save_projects(projects, DEFAULT_FILE)
    print("Goodbye!")

if __name__ == "__main__":
    main()