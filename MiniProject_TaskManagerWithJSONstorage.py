import json

TASK_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASK_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(title, deadline):
    tasks = load_tasks()
    tasks.append({"title": title, "status": "Pending", "deadline": deadline})
    save_tasks(tasks)
    print(f"Task '{title}' added.")

def mark_done(title):
    tasks = load_tasks()
    for task in tasks:
        if task["title"] == title:
            task["status"] = "Done"
            print(f"Task '{title}' marked as Done.")
            break
    save_tasks(tasks)

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    for task in tasks:
        print(f"{task['title']} - {task['status']} (Deadline: {task['deadline']})")

# --- Example usage ---
add_task("Finish Day 6", "2026-06-02")
add_task("Push code to GitHub", "2026-06-02")
mark_done("Push code to GitHub")
list_tasks()
