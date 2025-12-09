task_list = []

print("To-Do List Menu:\n1. View Tasks\n2. Add a task\n3. Remove a Task\n4. Exit")

while True:
    user_choice = input("Enter your choice: ")
    if user_choice == '1':
        if len(task_list) == 0:
            print("No tasks")
        else:
            print(f"Tasks: {task_list}")
    elif user_choice == '2':
        new_task = input("Enter a new task: ")
        if new_task in task_list:
            print("Task already exists")
            task_exist = input("Continue? (y/n): ")
            if task_exist == 'y':
                task_list.append(new_task)
                print("Task added")
        else:
            task_list.append(new_task)
            print("Task added")
    elif user_choice == '3':
        if len(task_list) == 0:
            print("No tasks")
        else:
            print(f"Tasks: {task_list}")
            remove_task = input("Remove task: ")
            if remove_task in task_list:
                for task in task_list:
                    task_list.remove(task)
                    print("Task removed")
            else:
                print("Task does not exist")
    elif user_choice == '4':
        print("Program closed")
        exit()
    else:
        print("Invalid choice")
