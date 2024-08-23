import sys
from colorama import init, Fore, Style

init(autoreset=True)

tasks = []

def show_menu():
    print(Fore.CYAN + Style.BRIGHT + "\n==============================")
    print(Fore.CYAN + Style.BRIGHT + "   To-Do List Application")
    print(Fore.CYAN + Style.BRIGHT + "==============================")
    print(Fore.YELLOW + Style.BRIGHT + "1. View tasks")
    print(Fore.YELLOW + Style.BRIGHT + "2. Add a task")
    print(Fore.YELLOW + Style.BRIGHT + "3. Remove a task")
    print(Fore.YELLOW + Style.BRIGHT + "4. Mark task as completed")
    print(Fore.RED + Style.BRIGHT + "5. Exit")

def view_tasks():
    print(Fore.CYAN + Style.BRIGHT + "\nYour Tasks:")
    if not tasks:
        print(Fore.RED + "No tasks to display.")
    else:
        for i, task in enumerate(tasks):
            status = Fore.GREEN + "Completed" if task['completed'] else Fore.RED + "Not completed"
            print(Fore.YELLOW + f"{i + 1}. {task['name']} - {status}")

def add_task():
    task_name = input(Fore.CYAN + "\nEnter task name: ")
    tasks.append({"name": task_name, "completed": False})
    print(Fore.GREEN + f"Task '{task_name}' added.")

def remove_task():
    view_tasks()
    try:
        task_index = int(input(Fore.CYAN + "\nEnter task number to remove: ")) - 1
        if 0 <= task_index < len(tasks):
            removed_task = tasks.pop(task_index)
            print(Fore.GREEN + f"Task '{removed_task['name']}' removed.")
        else:
            print(Fore.RED + "Invalid task number.")
    except ValueError:
        print(Fore.RED + "Please enter a valid number.")

def mark_task_completed():
    view_tasks()
    try:
        task_index = int(input(Fore.CYAN + "\nEnter task number to mark as completed: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks[task_index]['completed'] = True
            print(Fore.GREEN + f"Task '{tasks[task_index]['name']}' marked as completed.")
        else:
            print(Fore.RED + "Invalid task number.")
    except ValueError:
        print(Fore.RED + "Please enter a valid number.")

def main():
    while True:
        show_menu()
        choice = input(Fore.CYAN + "\nEnter your choice (1-5): ")

        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            mark_task_completed()
        elif choice == "5":
            print(Fore.RED + "Exiting the To-Do List application.")
            sys.exit()
        else:
            print(Fore.RED + "Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
