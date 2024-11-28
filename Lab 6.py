# Two dictionaries are used to store tasks:
# ▪ One dictionary stores tasks for each day of the week.
# ▪ The other dictionary stores tasks for each month of the year.
# Each dictionary has the days or months as keys, and the tasks are stored as
# lists for each key (day or month).

# Dictionary to store tasks for each day of the week
tasks_by_day = {
    "Monday": [],
    "Tuesday": [],
    "Wednesday": [],
    "Thursday": [],
    "Friday": [],
    "Saturday": [],
    "Sunday": []
}

# Dictionary to store tasks for each month of the year
tasks_by_month = {
    "January": [],
    "February": [],
    "March": [],
    "April": [],
    "May": [],
    "June": [],
    "July": [],
    "August": [],
    "September": [],
    "October": [],
    "November": [],
    "December": []
}

# Mapping numbers to days of the week
day_mapping = {
    "1": "Monday", "2": "Tuesday", "3": "Wednesday", "4": "Thursday",
    "5": "Friday", "6": "Saturday", "7": "Sunday"
}

# Mapping numbers to months of the year
month_mapping = {
    "1": "January", "2": "February", "3": "March", "4": "April",
    "5": "May", "6": "June", "7": "July", "8": "August",
    "9": "September", "10": "October", "11": "November", "12": "December"
}

# Function to display the main menu
def display_menu():
    print("Task Management System")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Exit")

# Function to add a task
def add_task():
    period = input("Do you want to add a task for a day or a month? (day/month): ").strip().lower()
    if period == "day":
        day = input("Enter the day of the week (name or number 1-7): ").strip().capitalize()
        day = day_mapping.get(day, day)  # Convert number to day name if necessary
        if day in tasks_by_day:
            task = input("Enter the task: ").strip()
            tasks_by_day[day].append(task)
            print(f"Task added to {day}.")
        else:
            print("Invalid day.")
    elif period == "month":
        month = input("Enter the month (name or number 1-12): ").strip().capitalize()
        month = month_mapping.get(month, month)  # Convert number to month name if necessary
        if month in tasks_by_month:
            task = input("Enter the task: ").strip()
            tasks_by_month[month].append(task)
            print(f"Task added to {month}.")
        else:
            print("Invalid month.")
    else:
        print("Invalid input.")

# Function to view tasks
def view_tasks():
    period = input("Do you want to view tasks for a day or a month? (day/month): ").strip().lower()
    if period == "day":
        day = input("Enter the day of the week (name or number 1-7): ").strip().capitalize()
        day = day_mapping.get(day, day)  # Convert number to day name if necessary
        if day in tasks_by_day:
            print(f"Tasks for {day}: {tasks_by_day[day]}")
        else:
            print("Invalid day.")
    elif period == "month":
        month = input("Enter the month (name or number 1-12): ").strip().capitalize()
        month = month_mapping.get(month, month)  # Convert number to month name if necessary
        if month in tasks_by_month:
            print(f"Tasks for {month}: {tasks_by_month[month]}")
        else:
            print("Invalid month.")
    else:
        print("Invalid input.")

# Function to delete a task
def delete_task():
    period = input("Do you want to delete a task for a day or a month? (day/month): ").strip().lower()
    if period == "day":
        day = input("Enter the day of the week (name or number 1-7): ").strip().capitalize()
        day = day_mapping.get(day, day)  # Convert number to day name if necessary
        if day in tasks_by_day:
            task = input("Enter the task to delete: ").strip()
            if task in tasks_by_day[day]:
                tasks_by_day[day].remove(task)
                print(f"Task removed from {day}.")
            else:
                print("Task not found.")
        else:
            print("Invalid day.")
    elif period == "month":
        month = input("Enter the month (name or number 1-12): ").strip().capitalize()
        month = month_mapping.get(month, month)  # Convert number to month name if necessary
        if month in tasks_by_month:
            task = input("Enter the task to delete: ").strip()
            if task in tasks_by_month[month]:
                tasks_by_month[month].remove(task)
                print(f"Task removed from {month}.")
            else:
                print("Task not found.")
        else:
            print("Invalid month.")
    else:
        print("Invalid input.")

# Main function to run the program
def main():
    while True:
        display_menu()  # Display the menu
        choice = input("Enter your choice: ").strip()  # Get user choice
        if choice == "1":
            add_task()  # Add a task
        elif choice == "2":
            view_tasks()  # View tasks
        elif choice == "3":
            delete_task()  # Delete a task
        elif choice == "4":
            print("Exiting the program.")  # Exit the program
            break
        else:
            print("Invalid choice. Please try again.")  # Invalid choice

if __name__ == "__main__":
    main()  # Run the main function