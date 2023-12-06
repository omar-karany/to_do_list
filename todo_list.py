#start the programe welcome and explait it
user_name = input("please enter your name: ")
print(f"hello {user_name} in to do list app. we are happy that you use our app. to manage your time")


#make my empty list to edit it 
todo_list = []


#make while loop to include all commands 
while(True):
#ask user to enter the command to do from "add, remove, view, exit"
  user_choice = input("please enter the command to do 'add, remove, view, exit' ")


#make if condition to do the chosen command and check the input if invalid
  if user_choice == "add":
    task_add= input("enter the task please: ")
    todo_list.append(task_add)
    print("task is added")

  elif user_choice == "remove":
    if not todo_list:
        print("no task to remove")
    else: 
        task_remove = input("enter the task to remove it: ")
        if task_remove in todo_list:
            todo_list.remove(task_remove)
            print("task is removed")
        else: print(f"{task_remove} not in to_do list ")

  elif user_choice == "view":
    if not todo_list:
        print("no task to remove")
    else:  
        print("Your to-do list: ")
        for task in todo_list:
            print(task)
  elif user_choice == "exit":
    print(f"good bye {user_name}")
    break
  else: print("invalid inputs! Please try again.")

