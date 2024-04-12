tasks = []

while True:
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added successfully!")
    elif choice == '2':
        task = input("Enter the task to remove: ")
        if task in tasks:
            tasks.remove(task)
            print("Task removed successfully!")
        else:
            print("Task not found in the list.")
    elif choice == '3':
        if tasks:
            print("Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
        else:
            print("No tasks found.")
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
