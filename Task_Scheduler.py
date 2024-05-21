from datetime import datetime, timedelta
import pickle  # For data persistence

# Define a task class
class Task:
    def __init__(self, title, description, due_date, priority):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority

# Function to get user input for a task with error handling
def get_task_details():
    while True:
        try:
            title = input("Enter task title: ")
            description = input("Enter task description (optional): ")
            due_date_str = input("Enter due date (YYYY-MM-DD): ")
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
            priority = int(input("Enter priority (higher number = higher priority): "))
            return Task(title, description, due_date, priority)
        except ValueError:
            print("Invalid input. Please enter valid date format (YYYY-MM-DD) and numerical priority.")

# Function to send notification (replace with actual notification library)
def send_notification(task):
    print(f"**NOTIFICATION** - Task '{task.title}' is due soon!")

# Function to check for upcoming tasks
def check_tasks():
    tasks = load_tasks()  # Load tasks from file
    for task in tasks:
        if task.due_date - datetime.now() < timedelta(days=1):
            send_notification(task)

# Function to load tasks from a file (data persistence)
def load_tasks():
    try:
        with open("tasks.data", "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        print("No tasks found. Add tasks to get started!")
        return []

# Function to save tasks to a file
def save_tasks(tasks):
    with open("tasks.data", "wb") as f:
        pickle.dump(tasks, f)

# Main program loop
tasks = []  # List to hold tasks
while True:
    print("\nTask Scheduler")
    print("1. Add Task")
    print("2. Check Upcoming Tasks")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        task = get_task_details()
        tasks.append(task)
        save_tasks(tasks)  # Save tasks after adding
    elif choice == '2':
        check_tasks()
    elif choice == '3':
        save_tasks(tasks)  # Save tasks before exiting
        break
    else:
        print("Invalid choice!")

print("Exiting Task Scheduler...")
class Car:
    def __init__(self, make, model, year):
        self.make = make  # Brand of the car, e.g., Toyota
        self.model = model  # Model of the car, e.g., Corolla
        self.year = year  # Year of manufacture, e.g., 2022

    def start_engine(self):
        print(f"The {self.year} {self.make} {self.model}'s engine is now running.")

# Creating instances of the Car class
car1 = Car("Toyota", "Corolla", 2022)
car2 = Car("Honda", "Civic", 2021)

# Using the methods defined in the class
car1.start_engine()  # Output: The 2022 Toyota Corolla's engine is now running.
car2.start_engine()  # Output: The 2021 Honda Civic's engine is now running.
