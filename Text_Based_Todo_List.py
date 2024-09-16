from InquirerPy import prompt


def todo_list_run():

    todo_list = []

    def load_task():
        try:
            with open("todolist.txt" , "r") as file:
                tasks = file.readlines()
                return [task.strip() for task in tasks]
        except FileNotFoundError:
            return []
        
    def save_task():
        with open("todolist.txt" , "w") as file:
            for task in todo_list:
                file.write(f"{task}\n")
    
    def add_task():

        add_task_prompt = [{
            "type": "input",
            "name": "task",
            "message": "Enter the task you want to add:"
        }]
        

        task_answer = prompt(add_task_prompt)
        todo_list.append(task_answer["task"])
        print(f"Task added: {task_answer['task']}")
        save_task()                     # It save task to file 

    def delete_task():
        
        if not todo_list:
            print("No tasks to delete.")
            return
        delete_task_prompt = [{
            "type": "list",
            "name": "task_to_delete",
            "message": "Select a task to delete:",
            "choices": todo_list
        }]
        delete_answer = prompt(delete_task_prompt)
        todo_list.remove(delete_answer["task_to_delete"])
        print(f"Task deleted: {delete_answer['task_to_delete']}")
        save_task()

    def view_tasks():

        if not todo_list:
            print("No tasks available.")
        else:
            print("\nCurrent Tasks:")
            for i, task in enumerate(todo_list, start=1):
                print(f"{i}. {task}")


    todo_list.extend(load_task())

    condition = True

    while condition == True :

        program_start = [{

            "type": "list",
            "name": "option",
            "message": "Select an option:",
            "choices": ["Add Task", "Delete Task", "View Task", "Exit"]
        }]

        Q1 = prompt(program_start)


        if (Q1["option"] == "Add Task" ):
            add_task()
        elif (Q1["option"] == "Delete Task" ):
            delete_task()
        elif (Q1["option"] == "View Task" ):
            view_tasks()
        else : 
            condition = False   



todo_list_run()
