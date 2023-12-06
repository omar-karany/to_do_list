class ToDoListApp:
    def __init__(self, user_name):
        self.user_name = user_name
        self.todo_list = []

    def welcome_message(self):
        print(f"Hello {self.user_name}! Welcome to the To-Do List app. We're happy that you're using our app to manage your time.")

    def add_task(self):
        task_add = input("Enter the task, please: ")
        self.todo_list.append(task_add)
        print("Task added successfully!")

    def remove_task(self):
        if not self.todo_list:
            print("No task to remove.")
        else:
            task_remove = input("Enter the task to remove: ")
            if task_remove in self.todo_list:
                self.todo_list.remove(task_remove)
                print("Task removed successfully.")
            else:
                print(f"{task_remove} not found in the to-do list.")

    def view_tasks(self):
        if not self.todo_list:
            print("No tasks to display.")
        else:
            print("Your to-do list:")
            for task in self.todo_list:
                print(task)

    def start_app(self):
        self.welcome_message()

        while True:
            user_choice = input("Please enter the command ('add', 'remove', 'view', 'exit'): ")

            if user_choice == "add":
                self.add_task()
            elif user_choice == "remove":
                self.remove_task()
            elif user_choice == "view":
                self.view_tasks()
            elif user_choice == "exit":
                print(f"Goodbye, {self.user_name}!")
                break
            else:
                print("Invalid input. Please try again.")

if __name__ == "__main__":
    user_name = input("Please enter your name: ")
    todo_app = ToDoListApp(user_name)
    todo_app.start_app()
