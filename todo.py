import json
import os
from datetime import datetime

class Todo:
    def __init__(self):
        self.tasks = []

    def load_task(self):
        if not os.path.exists("tasks.json"):
            self.tasks = []
            return

        with open("tasks.json", "r") as file:
            self.tasks = json.load(file)

    def take_input(self):
        print("Welcome to the CLI To-do app\n")
        self.display()
        
        while True:
            action = input("Want to add, delete, display tasks or exit? > \n").lower()

            if action == 'add':
                self.add_item()
            elif action == 'delete':
                self.remove_item()
            elif action == 'display':
                self.display()
            elif action == 'exit':
                self.save_tasks()
                print("Thank you, goodbye!")
                break
            else:
                print("Unknown action, Please choose 'add' or 'delete' ")

    def add_item(self):
        title = input("What task would you want to add?? \n")
        
        task = {
            "title": title,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        self.tasks.append(task)
        print(f"Task {task} added")
        self.display()
    
    def remove_item(self):
        ''' 
        1. Print the list
        2. Ask which one to remove
        3. Check exception and remove
        '''
        self.display()
        
        if not self.tasks:
            print("The task list is empty, there is nothing to remove")
            return

        remove = input("Which task you want to remove (1, 2, 3...)\n")

        if not remove.isdigit():
            print("Your input is not a digit")
            return

        index = int(remove) - 1  # Convert to 0-based index

        # Validate index range
        if index < 0 or index >= len(self.tasks):
            print("Invalid index. Please choose an existing task number.")
            return

        removed_task = self.tasks.pop(index)
        print(f"Removed task: {removed_task}")
        self.display()

    
    def display(self):
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task['title']} (added: {task['created_at']})")

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file, indent=2)


def main():
    todo = Todo()
    todo.load_task()
    todo.take_input()
    todo.display()

if __name__ == "__main__":
    main()

'''
--> Done
1. created the structure I wanted
2. the class file
3. properly handle remove 
4. Create a while loop to keep it running
5. git/github
6. store it into database

--> Left
7. find security issues
8. multiple files
9. production grade
10. unit tests

'''