tasks = []

def show_menu():
    print("\nTo-Do List Menu:")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Exit")


def view_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        for i, task in enumerate(tasks, 1):
            status = "✅" if task["done"] else "❌"
            print(f"{i}. {task["title"]} [{status}]")


def add_task():
    title = input("Enter task title: ")
    tasks.append({"title": title, "done": False})
    print("Task added!")


def complete_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to mark as done"))
        tasks[task_num - 1]["done"] = True
        print("Task marked as completed!")
    except (IndexError, ValueError):
        print("Invalid task number")


def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to delete"))
        tasks.pop(task_num - 1)
        print("Task deleted!")
    except (IndexError, ValueError):
        print("Invalid task number")


# Main loop
while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
