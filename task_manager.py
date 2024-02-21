'''Notes: 
1. Use the following username and password to access the admin rights 
username: admin
password: password
Please note all usernames and passwords are case sensitive.
2. Ensure you open the whole folder for this task in VS Code otherwise the 
program will look in your root directory for the text files.
'''

# Importing libraries and functions 
import os
from datetime import datetime, date
import functions_task_manager as func 

DATETIME_STRING_FORMAT = "%Y-%m-%d"
completed = ""

# Create tasks.txt if it doesn't exist and read/store info ===================
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [task for task in task_data if task != ""]

task_list = []
for task_str in task_data:
    curr_task = {}

    # Split by semicolon and manually add each component
    task_components = task_str.split(";")
    curr_task['username'] = task_components[0]
    curr_task['title'] = task_components[1]
    curr_task['description'] = task_components[2]
    curr_task['due_date'] = datetime.strptime(task_components[3], 
                                              DATETIME_STRING_FORMAT)
    curr_task['assigned_date'] = datetime.strptime(task_components[4],
                                                   DATETIME_STRING_FORMAT) 
    curr_task['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_task)

    
# Login Section===============================================================
'''This code reads usernames and password from the user.txt file 
to allow a user to login'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

func.print_line()
print("LOGIN PAGE")

logged_in = False
while not logged_in:
    func.print_line()
    curr_user = input("Username: ")
    if curr_user in username_password.keys():
        curr_pass = input("Password: ")
        if username_password[curr_user] == curr_pass:
            func.print_line()
            print("Login Successful!")
            logged_in = True
        else:
            print("Wrong Password")
    else:
        print("User does not exist")

# MENU OPTIONS ===============================================================
while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    func.print_line()
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my tasks
gr - generate reports
ds - Display statistics
e - Exit
: ''').lower()

# Add a new user to the user.txt file
    if menu == 'r':
        func.print_line()
        print("Registering a User")
        func.print_line()
        
        func.reg_user(username_password)


# Add a task 
    elif menu == 'a':
        func.print_line()
        print("Adding a task")
        func.print_line()
        
        func.add_task(username_password, task_list)
  

# View all tasks
    elif menu == 'va':
        func.print_line()
        print("View all tasks selected")
        
        func.view_all(task_list)


# View my tasks 
    elif menu == 'vm':
        func.print_line()
        print(f"View my tasks for {curr_user} selected\n")
        
        func.view_mine(task_list, curr_user, username_password)


# Generate reports 
    elif menu == 'gr':
        func.print_line()
        print("Generate reports selected")

        func.create_task_overview_file(task_list)
        func.create_user_overview_file(username_password, task_list)


# Display statistics 
    elif menu == 'ds':
        func.print_line()
        print("Display statistics selected")
        func.print_line()

        func.display_statistics(curr_user, username_password, task_list)
        

# Exit task manager
    elif menu == 'e':
        print('-'*50)
        print('Goodbye!!!')
        print('-'*50)
        exit()


# Error message for invalid input for menu option 
    else:
        print('-'*50)
        print("Option not recognized, please Try again")
