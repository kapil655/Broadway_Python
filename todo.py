tasks=[]

while True:

    opt=int(input("\n1.add task\n2.remove tasks\n3.display tasks\n4.exit\n\n"))

    if opt== 1:

        new_tasks=input("enter the task: ")
        if new_tasks not in tasks:
                tasks.append(new_tasks)
                print(new_tasks," added successfully")
                print(new_tasks)
        else:
             print(f"{new_tasks} already in to-do list")

    elif opt == 2:

        del_index = int(input("Enter task index to delete: "))

        if 0 <= del_index < len(tasks):
                removed = tasks.pop(del_index)
                print("Removed task:", removed)
        else:
                print("Invalid index!")
    
    elif opt == 3:
        for i,task in enumerate(tasks):
            print(f"{i}.{task}")

    elif opt == 4:
        print("bye bye ")
        break

    else:
        print("invalid choice")