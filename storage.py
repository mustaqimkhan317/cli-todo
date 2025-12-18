import json
import os

def load_task(filename):
    if not os.path.exists(filename):
        return []

    try:
        with open(filename, "r") as file:
            return json.load(file)

    except json.JSONDecodeError:
        print("Warning: Task file is corrupted. Starting with an empty list.")
        return []

    except PermissionError:
        print("Error: Permission denied while reading the task file.")
        return []

    except OSError as e:
        print(f"Error: Unable to read task file ({e}).")
        return []

def save_tasks(filename, tasks):
    try:
        with open(filename, "w") as file:
            json.dump(tasks, file, indent=2)

    except PermissionError:
        print("Error: Permission denied while saving tasks.")

    except OSError as e:
        print(f"Error: Unable to save tasks ({e}).")