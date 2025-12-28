task = []

while True:
    print('\n---To-Do List Menu---')
    print('1. View Tasks')
    print('2. Add Task')
    print('3. Delete Task')
    print('4. Exit')

    choice = input('Enter your choice (1 to 4): ')
    if choice == '1':
        print('\nYour Tasks:')
        if len(task) == 0:
            print('No task added yet')
        else:
            for tasks in task:
                print("- " + tasks)

    elif choice == '2':
        new_task = input("Enter the new task: ")
        task.append(new_task)
        print('Task Added')

    elif choice == '3':
        remove_task = input("Enter the task to remove: ")
        if remove_task in task:
            task.remove(remove_task)
        else:
            print('Task Not Found')

    elif choice == '4':
        print('Exiting the program. Goodbye!')
        break

    else:
        print('Invalid Choice. please select from (1 to 4)')

