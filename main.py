from todo import Todo

def main():
    print("Welcome to the CLI To-do app\n")
    todo = Todo() # Initialize the object
    todo.display() # Display the list 
    todo.take_input()
    todo.display()

if __name__ == "__main__":
    main()