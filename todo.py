class Todo:
    def __init__(self):
        self.tasks = []

    def take_input(self):
        print("Welcome to the CLI To-do app\n")
        action = input("Would you like to add or delete a task? > \n")

        if action == 'add':
            self.add_item()
        elif action == 'delete':
            self.remove_item()
        else:
            print("Unknown action, Please choose 'add' or 'delete' ")

    def add_item(self):
        task = input("What task would you want to add?? \n")
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

        remove = input("Which task you want to remove (1, 2, 3...)")

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
        print(self.tasks)



todo = Todo()

todo.take_input()
todo.display()

'''
1. created the structure I wanted
2. the class file
3. properly handle remove 

4. Create a while loop to keep it running
5. store it into database
5. find security issues
6. git/github
7. production grade
8. unit tests

'''