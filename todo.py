from datetime import datetime
from storage import load_task, save_tasks
from tabulate import tabulate

class Todo:
    '''
    Docstring for Todo
    --> Done
    1. created the structure/ responsibilites 
    2. the class file
    3. properly handle remove function
    4. Create a while loop to keep it running
    5. git/github
    6. store it into database

    --> Left
    7. Understand JSON
    8. find security issues
    9. multiple files (Refactoring)
    10. production grade
    11. unit tests
    12. Improve display

    '''
    def __init__(self):
        self.tasks = load_task()

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
                save_tasks(self.tasks)
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
        self.display()
    
    def remove_item(self):
        self.display() # Display the list
        
        # Check whether the list is empty
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
        headers = ['Index', 'Title', 'Date Created']
        
        table = []
        for i, task in enumerate(self.tasks, start=1):
            table.append([
                str(i), task['title'], task['created_at']
            ])
        
        print(tabulate(table, headers, tablefmt="grid"))


def main():
    todo = Todo()
    todo.take_input()
    todo.display()

if __name__ == "__main__":
    main()