from datetime import datetime, date
DATETIME_STRING_FORMAT = "%Y-%m-%d"


# task_manager_play.py

# def reg_user():

# def add_task():

# def view_all():

# def view_mine():


# options = "Please select one of the following options: \nr - register user \
#     \na - add task \nva - view all tasks \nvm - view my tasks \
#     \ngr - generate reports \nds - display statistics \ne - exit"

# print(options)

"""login loops"""
# username_password = {"admin": "password"}
# print("-"*50)
# print("LOGIN PAGE")
# logged_in = False
# while not logged_in:
#     print("-"*50)
#     curr_user = input("Username: ")
#     if curr_user in username_password.keys():
#         curr_pass = input("Password: ")
#         if username_password[curr_user] == curr_pass:
#             print("-"*50)
#             print("Login Successful!")
#             logged_in = True
#         else:
#             print("Wrong Password")
#     else:
#         print("User does not exist")



"View all tasks from tasks.txt"
# print("-"*50)
# print("View all tasks selected")

# with open('tasks.txt', 'r') as task_file:
#     all_tasks = task_file.readlines()

#     for task in all_tasks:
#         task_info = task.split(';')

#         assigned = task_info[0]
#         title = task_info[1]
#         task_description = task_info[2]
#         date_assigned = task_info[3]
#         due_date = task_info[4]
#         completed = task_info[5].strip("\n")

#         print('-'*50)
#         print(f"Task: \t\t\t{title} \nAssigned to: \t\t{assigned} \
#             \nDate assigned: \t\t{date_assigned} \nDue date: \
#             \t{due_date} \nTask complete? \t\t{completed} \
#             \nTask description: \n {task_description}")


"""view my tasks only"""
# print("-"*50)
# print("View my tasks selected")
# '''Reads the task from task.txt file and prints to the console in the 
#     format of Output 2 presented in the task pdf (i.e. includes spacing
#     and labelling)'''

# curr_user = "bob"
# task_count = 0

# with open('tasks.txt', 'r') as task_file:
#     all_tasks = task_file.readlines()

#     for task in all_tasks:
#         task_info = task.split(';')

#         assigned = task_info[0]
#         title = task_info[1]
#         task_description = task_info[2]
#         date_assigned = task_info[3]
#         due_date = task_info[4]
#         completed = task_info[5].strip("\n")

#         if assigned == curr_user:
#             task_count +=1
#             print('-'*50)
#             print(f"Task: \t\t\t{title} \nAssigned to: \t\t{assigned} \
#                 \nDate assigned: \t\t{date_assigned} \nDue date: \
#                 \t{due_date} \nTask complete? \t\t{completed} \
#                 \nTask description: \n {task_description}")
    
#   # how to print 'no assigned tasks' if none found in for loops
#     if task_count == 0:
#         print('-'*50)
#         print(f"There are no assigned tasks for {curr_user}")

"""Date time output"""

# d = '2019-02-04'
# print(datetime.strptime(d, '%Y-%m-%d').strftime('%d %b %Y'))

"Tabulate dictionary - that's so cool!!"
# from tabulate import tabulate
# with open("tasks.txt", 'r') as task_file:
#     task_data = task_file.read().split("\n")
#     task_data = [task for task in task_data if task != ""]

# task_list = []
# for task_str in task_data:
#     curr_task = {}
#     # Split by semicolon and manually add each component
#     task_components = task_str.split(";")
#     curr_task['username'] = task_components[0]
#     curr_task['title'] = task_components[1]
#     curr_task['description'] = task_components[2]
#     curr_task['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
#     curr_task['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT) 
#     curr_task['completed'] = True if task_components[5] == "Yes" else False
#     task_list.append(curr_task)

# print(tabulate(task_list, headers="keys"))  # CHANGE COL WIDTH???

