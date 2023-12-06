def welcome_message():
    user_name = input("Please enter your name: ")
    print(f"Hello {user_name}! Welcome to the To-Do List app. We're happy that you're using our app to manage your time.")

def add_task(todo_list):
    task_add = input("Enter the task, please: ")
    todo_list.append(task_add)
    print("Task added successfully!")

def remove_task(todo_list):
    if not todo_list:
        print("No task to remove.")
    else:
        task_remove = input("Enter the task to remove: ")
        if task_remove in todo_list:
            todo_list.remove(task_remove)
            print("Task removed successfully.")
        else:
            print(f"{task_remove} not found in the to-do list.")

def view_tasks(todo_list):
    if not todo_list:
        print("No tasks to display.")
    else:
        print("Your to-do list:")
        for task in todo_list:
            print(task)

def main():
    welcome_message()
    
    todo_list = []

    while True:
        user_choice = input("Please enter the command ('add', 'remove', 'view', 'exit'): ")

        if user_choice == "add":
            add_task(todo_list)
        elif user_choice == "remove":
            remove_task(todo_list)
        elif user_choice == "view":
            view_tasks(todo_list)
        elif user_choice == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()