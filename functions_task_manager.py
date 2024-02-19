'''
All functions for task_manager.py:
print_line(), print_task(), write_task(),
reg_user(), add_task(), view_all(), 
task_complete(), new_task_user(), new_due_date(), view_mine(),
create_task_overview_file(), create_user_overview_file(),
display_statistics()
'''
from datetime import datetime, date
DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Line separator =============================================================
def print_line(symbol="-", length=50):
    """
    The function `print_line` prints a line of a specified length using a 
    specified symbol.
    
    :param symbol: The symbol parameter is a string that represents the 
    character or symbol that will be used to create the line. 
    By default, it is set to "-"
    :param length: The length parameter determines the number of times the 
    symbol character will be printed in the line, defaults to 50.
    """
    print(symbol*length)


# Print Task =================================================================
def print_task(task):
    """
    The code takes a task from a dictionary as input and prints out the 
    details of the task in a formatted manner.
    """
    if task['completed'] == True:
        completed = "Yes"
    else:
        completed = "No"
    print_line()
    disp = f"Task: \t\t {task['title']}\n"
    disp += f"Assigned to: \t {task['username']}\n"
    disp += f"Date Assigned: \t {task['assigned_date'].strftime\
                                 ('%d %b %Y')}\n"
    disp += f"Due Date: \t {task['due_date'].strftime('%d %b %Y')}\n"
    disp += f"Completed: \t {completed}\n"
    disp += f"Task Description: \n {task['description']}\n"
    print(disp)


# Write tasks to text file ===================================================
def write_task(task_list):
    """
    The `write_task` function is responsible for writing the task list to a 
    text file called "tasks.txt". It takes the `task_list` as input and 
    iterates over each task in the list. For each task, it converts the task 
    attributes (username, title, description, due_date, assigned_date, 
    completed) into a string format and appends it to the `task_list_to_write` 
    list. Finally, it writes the contents of `task_list_to_write` to
    the "tasks.txt" file, with each task separated by a new line.
    """
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for task in task_list:
            str_attrs = [
                task['username'],
                task['title'],
                task['description'],
                task['due_date'].strftime(DATETIME_STRING_FORMAT),
                task['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if task['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))


# Register a new user ========================================================
def reg_user(username_password):
    """
    The `reg_user` function prompts the user to enter a new username and 
    password, checks if the username already exists, and if not, adds the 
    username and password to a dictionary and writes them to a file.
    
    :param username_password: The parameter `username_password` is a 
    dictionary that stores the usernames as keys and their corresponding 
    passwords as values.
    """
    while True:
        # Request input of a new username
        new_username = input("New Username: ")
        if new_username in username_password.keys():
            print(f"{new_username} username already exists\n")
        else:
            print(f"{new_username} accepted\n")
            break

    while True:
        # Request input of a new password
        new_password = input("New Password: ")

        # Request input of password confirmation.
        confirm_password = input("Confirm Password: ")

        # Check if the new password and confirmed password are the same.
        if new_password == confirm_password:
            username_password[new_username] = new_password
            
            # If they are the same, add them to the user.txt file,
            with open("user.txt", "a") as out_file:
                out_file.write(f"\n{new_username};{new_password}")
            
            print_line()
            print(f"New user {new_username} added to user.txt")
            break
        # Otherwise you present a relevant message.
        else:
            print("Passwords do no match, try again\n")

   
# Add a task =================================================================
def add_task(username_password, task_list):
    """
    The `add_task` function allows a user to add a new task to a task list, 
    including the username of the person assigned to the task, the title and 
    description of the task, and the due date of the task.
    
    :param username_password: The `username_password` parameter is a dictionary
    that stores the usernames and passwords of users. The keys are the 
    usernames and the values are the corresponding passwords
    :param task_list: The `task_list` parameter is a list that contains 
    dictionaries representing tasks. Each dictionary represents a task.
    """
    # Reopen and read user text file for any new users added
    with open("user.txt", 'r') as user_file:
        user_data = user_file.read().split("\n")

    username_password = {}
    for user in user_data:
        username, password = user.split(';')
        username_password[username] = password

    while True:
        task_username = input("Name of person assigned to task (enter to exit)\
                              \n: ")
        if task_username == "":
            print("Going back to main menu")
            break

        elif task_username not in username_password.keys():
            print("User does not exist. Please enter a valid username\n")
            task_username = False
        
        else:
            task_title = input("Title of Task: ")
            task_description = input("Description of Task: ")
           
            # valid_due_date()  ?!?!?!?!?!?!?!?!?!?!?
            while True:
                try:
                    task_due_date = input("Due date of task (YYYY-MM-DD): ")
                    due_date_time = datetime.strptime(task_due_date, \
                                                      DATETIME_STRING_FORMAT)
                    # Assign current date
                    curr_date = date.today()
                    if due_date_time.strftime('%Y-%m-%d') \
                        < curr_date.strftime('%Y-%m-%d'):
                        print("Due date cannot be in the past\n")
                    else:
                        break
                except ValueError:
                    print("Invalid datetime format\n")

            ''' Add the data to the file task.txt and
                Include 'No' to indicate if the task is complete.'''
            new_task = {
                "username": task_username,
                "title": task_title,
                "description": task_description,
                "due_date": due_date_time,
                "assigned_date": curr_date,
                "completed": False
            }

            task_list.append(new_task)
            write_task(task_list)
            print("Task successfully added.")
            break


# View all tasks =============================================================
def view_all(task_list):
    """
    The function `view_all` takes a list of tasks as input and prints a 
    formatted summary of each task.
    
    :param task_list: The `task_list` parameter is a list of dictionaries, 
    where each dictionary represents a task. 
    """
    for task in task_list:
        print_task(task)


# Mark task as complete ======================================================
def task_complete(task_list, task_edit_index, select_task):
    """
    The function `task_complete` prompts the user to input whether a task is complete or not, updates
    the task's completion status in the task list, and writes the updated task list to a file.
    
    :param task_list: The task_list parameter is a list of dictionaries that represents a collection of
    tasks. Each dictionary in the list represents a single task and contains information such as the
    task's description, due date, and completion status
    :param task_edit_index: The `task_edit_index` parameter is the index of the task in the `task_list`
    that needs to be edited. It is used to access the specific task in the list and update its
    completion status
    :param select_task: The `select_task` parameter is the task that the user has selected to edit or
    mark as complete. It is used to display the task number in the output message
    """
    while True:
        task_complete = input("\nIs this task complete Y/N?: ").upper()
        if task_complete == "Y":
            task_list[task_edit_index].update({'completed':True})
            break
        elif task_complete =="N":
            task_list[task_edit_index].update({'completed':False})
            break
        else:
            print("Not a valid input. Y or N only")
    
    write_task(task_list)
    print(f"Task {select_task} is updated!\n")


# Assign new user to task ====================================================
def new_task_user(username_password, task_list, task_edit_index, select_task):
    """
    The function `new_task_user` updates the assigned user for a specific task 
    in a task list, given the index of the task to edited the selected task.
    
    :param username_password: A dictionary that contains the usernames and 
    passwords of users. The keys are usernames and the values are passwords.
    :param task_list: A list of dictionaries representing tasks. Each
    dictionary contains information about a specific task.
    :param task_edit_index: The index of the task in the `task_list`
    that needs to be edited. It is used to access the specific task in the list
    :param select_task: The `select_task` parameter is the task number the user
    wants to edit
    """
    if task_list[task_edit_index] == ({'completed':True}):
        while True:
            new_username = input("\nNew assigned user: ")
            if new_username in username_password.keys():
                task_list[task_edit_index].update({'username':new_username})

                write_task(task_list)
                print(f"Task {select_task} user updated to {new_username}!\n")
                break

            else:
                print("User does not exist\n")
    else:
        print("Task has already been completed")
            

# Update due date for task ===================================================
def new_due_date(task_list, task_edit_index, select_task):
    """
    The function `new_due_date` allows the user to update the due date of a 
    task in a task list, as long as the task has not already been completed.
    
    :param task_list: A list that contains dictionaries representing tasks.
    :param task_edit_index: The index of the task in the `task_list`.
    It is used to access the specific task in the list and update its due date
    :param select_task: The task that the user has selected to edit.
    """
    if task_list[task_edit_index] == ({'completed':True}):
        while True:
            try:
                new_due_date = input("\nNew due date (YYYY-MM-DD): ")
                new_date_time = datetime.strptime\
                    (new_due_date, DATETIME_STRING_FORMAT)
                # Assign current date
                curr_date = date.today()
                if new_date_time.strftime('%Y-%m-%d') \
                    < curr_date.strftime('%Y-%m-%d'):
                    print("Due date cannot be in the past\n")
                else:
                    break
            except ValueError:
                print("Invalid datetime format\n")

        task_list[task_edit_index].update\
            ({'due_date':new_date_time})

        write_task(task_list)
        print(f"Task {select_task} due date updated to {new_due_date}!\n")
    
    else:
        print("Task has already been completed")
        

# View my tasks ==============================================================  
def view_mine(task_list, curr_user, username_password):
    """
    The `view_mine` function allows a user to view and edit their assigned 
    tasks in a task list.
    
    :param task_list: A list of dictionaries, where each dictionary represents 
    a task.
    :param curr_user: The current logged in user for whom we want to view 
    their assigned tasks
    :param username_password: A dictionary that stores usernames and passwords. 
    It is used to validate the current user and display assigned tasks
    """
    while True:
        task_index = {}
        task_count = 0
        for task in task_list:
            if task['username'] == curr_user:
                task_count += 1
                print(f"Task {task_count}")
                print_task(task)
                task_index[task_count] = task_list.index(task)

        if task_count == 0:
            print('-'*50)
            print(f"There are no assigned tasks for {curr_user}")
            break

        elif task_count > 0:  
            print_line()   
            select_task = (input("Task number to edit or mark as complete \
                                    \n(or -1 to exit): "))
            if select_task == "-1":
                break
                
            elif select_task.isnumeric():
                select_task = int(select_task)
                if select_task in task_index.keys():
                    print_line()
                    print(f"Task {select_task} selected to edit\n")
                    task_edit_index = task_index.get(select_task)
                    
                    while True:
                        edit_task = input("Would you like to: \
                                            \n1. Mark task as complete \
                                            \n2. Change assigned user \
                                            \n3. Change due date \
                                            \n(-1 to exit): ")
                        
                        if edit_task == "-1":
                            break

                        elif edit_task == "1":
                            task_complete(task_list, task_edit_index, \
                                            select_task)
                            break

                        elif edit_task == "2":
                            new_task_user(username_password, task_list, \
                                        task_edit_index, select_task)
                            break 
                                
                        elif edit_task == "3":
                            new_due_date(task_list, task_edit_index, \
                                            select_task)
                            break

                        else:
                            print("Invalid input. -1, 1, 2 or 3 only\n")
                else:
                    print("Task not found")
            else:
                print("Invalid input")


# Create task overview text file =============================================
def create_task_overview_file(task_list):
    ''' Create task_overview.txt
    - total number of tasks generated
    - total number of completed tasks
    - total number of uncompleted tasks
    - total number of overdue tasks
    - percentage of tasks incomplete
    - percentage of tasks overdue
    '''
    # Get total number of tasks
    total_num_tasks = len(task_list)

    # Count number completed and uncompleted
    num_completed = 0
    num_uncompleted = 0
    num_overdue = 0
    for task in task_list:
        if task['completed'] == True:
            num_completed += 1
        else:
            num_uncompleted += 1 
            # Count number overdue if not completed
            if task['due_date'] < datetime.today():
                num_overdue += 1

    # Percentage for incomplete and overdue
    percent_incomplete = (num_uncompleted/total_num_tasks)*100
    percent_overdue = (num_overdue/total_num_tasks)*100

    with open('task_overview.txt', 'w') as file:
        file.write(f"Task Overview - {date.today()}\n\n")
        file.write(f"Total number of tasks: {total_num_tasks}\n")
        file.write(f"Total number of completed tasks: {num_completed}\n")
        file.write(f"Total number of uncompleted tasks: {num_uncompleted}\n")
        file.write(f"Total number of overdue tasks: {num_overdue}\n")
        file.write(f"Percentage of tasks incomplete: "\
                   f"{int(percent_incomplete)}%\n")
        file.write(f"Percentage of tasks overdue: {int(percent_overdue)}%\n")
    
    print_line()
    print("task_overview.txt exported")


# Create user overview text file =============================================
def create_user_overview_file(username_password, task_list):
    '''
    create user_overview.txt
    - total number of users registered 
    - total number of tasks 
    - for each user: total tasks assigned
    - for each user: percentage of tasks assigned to user, complete, incomplete 
      and overdue 
    '''
     # Get total number of tasks
    total_num_tasks = len(task_list)
    # Total number of users registered
    total_users_registered = len(username_password)

    # Open and create new text file
    with open('user_overview.txt', 'w') as file:
        file.write(f"User Overview - {date.today()}\n\n")
        file.write(f"Total number of users registered: "\
                   f"{total_users_registered}\n")
        file.write(f"Total number of tasks: {total_num_tasks}\n")
        
        # For each user: number of tasks complete, incomplete and overdue
        for user in username_password.keys():
            file.write(f"\nUser: {user}\n") 
            user_completed = 0
            user_uncompleted = 0
            user_total_tasks = 0
            user_overdue = 0
            for task in task_list:
                if task['username'] == user:
                    user_total_tasks += 1
                    if task['completed'] == True:
                        user_completed += 1
                    else:
                        user_uncompleted += 1
                        if task['due_date'] < datetime.today():
                            user_overdue += 1
            file.write(f"Tasks assigned: {user_total_tasks}\n")
            
            # Calculate percentage of tasks assigned to user
            percent_tasks_user = (user_total_tasks/total_num_tasks)*100
            file.write(f"Percent of tasks assigned: "\
                       f"{int(percent_tasks_user)}%\n")
            
            # If tasks assigned, calculate percentages and write to txt file
            if user_total_tasks > 0:
                percent_complete_user=(user_completed/user_total_tasks)*100
                percent_incomplete_user=(user_uncompleted/user_total_tasks)*100
                percent_overdue_user=(user_overdue/user_total_tasks)*100
                file.write(f"Percent complete: "\
                           f"{int(percent_complete_user)}%\n")
                file.write(f"Percent incomplete: "\
                           f"{int(percent_incomplete_user)}%\n")
                file.write(f"Percent overdue: {int(percent_overdue_user)}%\n")

    print_line()
    print("user_overview.txt exported")


# Display statistics =========================================================
def display_statistics(curr_user, username_password, task_list):
    '''If the user is an admin they can display statistics about number of
    users and tasks.'''
    if curr_user == "admin":
        num_users = len(username_password.keys())
        num_tasks = len(task_list)

        print("-----------------------------------")
        print(f"Number of users: \t\t {num_users}")
        print(f"Number of tasks: \t\t {num_tasks}")
        print("-----------------------------------")    
        
    else:
        print("You are not authorized, only admin can view statistics")