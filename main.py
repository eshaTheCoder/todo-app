from todo import Task, TodoManager
from datetime import datetime
manager = TodoManager()
manager.load_from_json()

while True:
    print("\n1. Add  2. Show  3. Done  4. Delete  5. Exit")
    choice = input("Choice:")

    if choice == "1":
        title = input("Title: ")
        desc = input("Desc: ")
        priority = input("Priority: (High/Medium/Low:)") or "Medium"
        while True:
            date_str = input("Due Date (DD-MM-YYYY):")
            try:
                due_date_obj = datetime.strptime(date_str, "%d-%m-%Y")
                break
            except ValueError:
                print("Please enter date following exact format.")
            continue
        manager.add_task(Task(title, desc, due_date_obj, priority))
        manager.save_to_json()
    elif choice == "2":
        manager.show_all()
    elif choice == "3":
        manager.show_all()
        try:
            idx = int(input("Number: ")) - 1
            manager.mark_done(idx)
            manager.save_to_json()
        except ValueError:
            print("Please enter a valid number.")
    elif choice == "4":
        manager.show_all()
        try:
            idx = int(input("Number: ")) - 1
            manager.delete_task(idx)
            manager.save_to_json()
        except ValueError:
            print("Please enter a valid number.")
    elif choice == "5":
        break