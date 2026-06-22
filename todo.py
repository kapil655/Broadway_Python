tasks = []

def add_task():
    new_task = input("Enter the task: ")

    if new_task not in tasks:
        tasks.append(new_task)
        print(new_task, "added successfully")
        print("Total tasks:", len(tasks))
    else:
        print(f"{new_task} already in to-do list")


def remove_task():
    del_index = int(input("Enter task index to delete: "))

    if 0 <= del_index < len(tasks):
        removed = tasks.pop(del_index)
        print("Removed task:", removed)
        print("Remaining tasks:", len(tasks))
    else:
        print("Invalid index!")


def show_task():
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks):
            print(f"{i}. {task}")
        print("Total tasks:", len(tasks))


while True:
    opt = int(input(
        "\n1. Add Task\n2. Remove Task\n3. Display Tasks\n4. Exit\n\nEnter choice: "
    ))

    if opt == 1:
        add_task()

    elif opt == 2:
        remove_task()

    elif opt == 3:
        show_task()

    elif opt == 4:
        print("Bye Bye!")
        break

    else:
        print("Invalid choice")