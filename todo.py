import json
from datetime import datetime
class Task:
    def __init__(self, title, desc, due_date_obj, priority="Medium"):
        self.title = title
        self.desc = desc
        self.due_date = due_date_obj
        self.priority = priority
        self.completed = False
        self.created_at = datetime.now().strftime("%Y-%m-%d")

    def is_overdue(self):
        return datetime.now() > self.due_date and not self.completed

    def to_dict(self):
        return {
            "title": self.title,
            "desc": self.desc,
            "due_date": self.due_date.isoformat(),
            "priority": self.priority,
            "completed": self.completed,
            "created_at": self.created_at
        }

        
class TodoManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task): 
        self.tasks.append(task)
        print("Task added")

    def show_all(self):
        if not self.tasks:
            print("No Task Yet")
            return
        
        for i, t in enumerate(self.tasks, 1):
            status = "✅Done" if t.completed == True else "Pending"
            overdue = "OVERDUE!" if t.is_overdue() else ""
            print(f"{i}. {t.title} | {t.priority} |DUE: {t.due_date.date()} | {status}{overdue} ")
            print(f"   DESC: {t.desc}")

    def mark_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            print("Tasks marked done!")
        else:
            print("Invalid Number!")
    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            deleted = self.tasks.pop(index)
            print(f"Deleted: {deleted.title}")
            return deleted
        else:
            print("Invalid Number!")
            return None
    def save_to_json(self):
        with open("tasks.json", "w") as f: 
            json.dump([t.to_dict() for t in self.tasks], f, indent=2)

    def load_from_json(self):
        try:
            with open("tasks.json", "r") as f:
                data = json.load(f)
                for d in data:
                    t = Task(d["title"], d["desc"], datetime.fromisoformat(d["due_date"]), d["priority"])
                    t.due_date = datetime.fromisoformat(d["due_date"])
                    t.completed = d["completed"]
                    t.created_at = d["created_at"]
                    self.tasks.append(t)
        except FileNotFoundError:
            print("No saved tasks found.")
