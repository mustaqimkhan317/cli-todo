import json
import os

def load_task(filename):
    if not os.path.exists(filename):
        return []

    with open(filename, "r") as file:
        return json.load(file)

def save_tasks(filename, tasks):
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=2)