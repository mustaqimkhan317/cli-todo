import json
import os

def load_task():
    if not os.path.exists("tasks.json"):
        return []

    with open("tasks.json", "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=2)