import sqlite3

conn = sqlite3.connect("todo.db")
cursor = conn.cursor()

while True:

    opt = int(input("\n1.add task\n2.remove task\n3.display tasks\n4.update task\n5.exit\n\n"))

    # ADD TASK
    if opt == 1:

        new_tasks = input("enter the task: ")

        cursor.execute(
            "INSERT INTO tasks(task) VALUES(?)",
            (new_tasks,)
        )

        conn.commit()

        print(new_tasks, "added successfully")

    # DELETE TASK
    elif opt == 2:

        task_id = int(input("Enter task ID to delete: "))

        cursor.execute(
            "DELETE FROM tasks WHERE id = ?",
            (task_id,)
        )

        conn.commit()

        if cursor.rowcount == 0:
            print("Task not found!")
        else:
            print("Task deleted successfully!")

    # DISPLAY TASKS
    elif opt == 3:

        cursor.execute("SELECT * FROM tasks")
        rows = cursor.fetchall()

        if len(rows) == 0:
            print("No tasks found")
        else:
            for row in rows:
                print(row[0], ".", row[1])

    # UPDATE TASK
    elif opt == 4:

        task_id = int(input("Enter task ID to update: "))
        new_text = input("Enter new task: ")

        cursor.execute(
            "UPDATE tasks SET task = ? WHERE id = ?",
            (new_text, task_id)
        )

        conn.commit()

        if cursor.rowcount == 0:
            print("Task not found!")
        else:
            print("Task updated successfully!")

    # EXIT
    elif opt == 5:
        print("bye bye")
        break

    else:
        print("invalid choice")

conn.close()