import json
import sys
import os
def load_tasks():
    if os.path.exists('tasks.json'):
        with open('tasks.json') as f:
            file_new = json.load(f)
            return file_new
    else: 
        with open('tasks.json', 'x') as f:
          json.dump([], f)
        return []

    
def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f)
  

def add_task(description):
    tasks = load_tasks()
    highest_Id = 0
    for task in tasks:
        if task["id"] > highest_Id:
            highest_Id = task["id"]
    new_task = {"id": highest_Id + 1, "description": description,
                "status": "todo"}
    tasks.append(new_task)
    print(f"Task added: {description}")
    save_tasks(tasks)


def delete_task(task_id):
    tasks = load_tasks()
    found = False
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            found = True
            save_tasks(tasks)
            break
    if found:
        print(f"Task with ID: {task_id} has been deleted.")
    else:
        print(f"No task found with ID: {task_id}.")

def update_task(task_id, new_description):
    tasks = load_tasks()    
    found = False
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            found = True
            save_tasks(tasks)
            break
    if found:
        print(f"Task ID: {task_id} is updated with new description: {new_description}.")
    else:
        print(f"No task found with ID: {task_id}.")


def mark_done(task_id):
    tasks = load_tasks()
    found = False
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "done"
            found = True
            save_tasks(tasks)
            break
    if found:
        print(f"Task ID: {task_id} has been marked as done.")
    else:
        print(f"No task found with ID: {task_id}.")

def mark_in_progress(task_id):
    tasks = load_tasks()
    found = False
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "in-progress"
            found = True
            save_tasks(tasks)
            break
    if found:
        print(f"Task ID: {task_id} has been marked as in-progress.")
    else:
        print(f"No task found with ID: {task_id}.")

def list_tasks(status=None):
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        for task in tasks:
            if status is None:  
                print(f"{task['id']} -  {task['description']} [{task['status']}]")
            elif task['status'] == status:
                print(f"{task['id']} -  {task['description']} [{task['status']}]")


if len(sys.argv) < 2:
    print("Please provide a single command as an argument.")

elif "add" == sys.argv[1]:
  if len(sys.argv) < 3:
        print("Please provide a task description..")
  else:
        add_task(sys.argv[2])

elif "delete" == sys.argv[1]:
  if len(sys.argv) <= 2 :
    print("Please provide an ID for the task to delete.")
  elif len(sys.argv) == 3:
    delete_task(int(sys.argv[2]))

elif "update" == sys.argv[1]:
    if len(sys.argv) <= 2:
      print("Please provide an ID for the task to update.")
    elif len(sys.argv) == 3:
      print(f"Please provide a new description for the task with ID: {sys.argv[2]}.")
    elif len(sys.argv) == 4:
      update_task(int(sys.argv[2]), sys.argv[3])
    else:
        print("Too many arguments provided for update command.")

elif "mark-done" == sys.argv[1]:
    if len(sys.argv) <= 2:
        print("Please provide an ID for the task to mark as done.")
    elif len(sys.argv) == 3:
        mark_done(int(sys.argv[2]))
    else:
        print("Too many arguments provided for mark-done command.")
elif "mark-in-progress" == sys.argv[1]:
    if len(sys.argv) <= 2:
        print("Please provide an ID for the task to mark as in progress.")
    elif len(sys.argv) == 3:
        mark_in_progress(int(sys.argv[2]))
    else:
        print("Too many arguments provided for mark-in-progress command.")

elif "list" == sys.argv[1]:
    if len(sys.argv) == 2:
        list_tasks()
    elif len(sys.argv) == 3:
        status = sys.argv[2]
        if status in ["todo", "done", "in-progress"]:
            list_tasks(status)
        else:
            print("Invalid status. Please use 'todo', 'done', or 'in-progress'.")
    else:
        print("Too many arguments provided for list command.")

else:
  print("Invalid command. Please use 'add', 'delete', 'update', 'mark-done', or 'mark-in-progress'.")


   


        
            





# if len(sys.argv) < 2:
#     print("Please provide a single command as an argument.")

# elif "add" == sys.argv[1]:
#   if len(sys.argv) < 3:
#         print("Please provide a task description..")
#   else:
#         add_task(sys.argv[2])

# elif "delete" == sys.argv[1]:
#   if len(sys.argv) <= 2 :
#     print("Please provide an ID for the task to delete.")
#   elif len(sys.argv) == 3:
#     delete_task(sys.argv[2])
   

# elif "update" == sys.argv[1]:
#     if len(sys.argv) <= 2:
#       print("Please provide an ID for the task to update.")
#     elif len(sys.argv) == 3:
#       print(f"Please provide a new description for the task with ID: {sys.argv[2]}.")
#     elif len(sys.argv) == 4:
#       update_task(int(sys.argv[2]), sys.argv[3])

# else:
#   print("Invalid command. Please use 'add', 'delete', or 'update'.")
  
    

