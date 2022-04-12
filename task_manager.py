# This program is for a small business that can help it to manage tasks assigned to each member of the team.
# This program will work with two text files, user.txt and tasks.txt. Open each of the files that accompany
# this project and take note of the following:

    # 1. tasks.txt stores a list of all the tasks that the team is working on.
    # Each line includes the following data about a task in this order:
        # The username of the person to whom the task is assigned.
        # The title of the task.
        # A description of the task.
        # The date that the task was assigned to the user.
        # The due date for the task.
        # Either a ‘Yes’ or ‘No’ value that specifies if the task has been completed yet.

    # 2. user.txt stores the username and password for each user that has permission to use your program (task_manager.py).
    # Open the user.txt file that accompanies this project. Note that this text file already contains
    # one default user that has the username, ‘admin’ and the password, ‘adm1n’.
    # The username and password for each user must be written to this file in the following format:
        # First, the username followed by a comma, a space and then the password
        # One username and corresponding password per line

# Your program should allow your users to do the following:
    # Login. The user should be prompted to enter a username and password. A list of valid usernames and passwords
    # are stored in a text file called user.txt. Display an appropriate error message if the
    # user enters a username that is not listed in user.txt or enters a valid username but not a valid password.
    # The user should repeatedly be asked to enter a valid username and password until they provide appropriate credentials.

    # If the user chooses ‘r’ to register a user, the user should be prompted for a new username and password.
    # The user should also be asked to confirm the password. If the value entered to confirm the password
    # matches the value of the password, the username and password should be written to user.txt in the appropriate format.

    # If the user chooses ‘a’ to add a task, the user should be prompted to enter the username of the person
    # the task is assigned to, the title of the task, a description of the task and the due date of the task.
    # The data about the new task should be written to tasks.txt. The date on which the task is assigned should
    # be the current date. Also assume that whenever you add a new task, the value that indicates whether
    # the task has been completed or not is ‘No’.

    # If the user chooses ‘va’ to view all tasks, display the information for each task on the screen in an easy to read format.

    # If the user chooses ‘vm’ to view the tasks that are assigned to them, only display all the tasks that have been assigned
    # to the user that is currently logged-in in a user-friendly, easy to read manner.

# ======================================================================================================================================


# define functions


# menu_option() function:
# depending on the user has logged in display
# the relevant menu. The admin user has 
# options that are not available to the standard user

from itertools import count


def menu_option():
    # display menu option relevant to the logged-in user

    if usernme == "admin":
        print("Please select one of the following options:")
        print("r    -   register user")
        print("a    -   add task")
        print("va   -   view all tasks")
        print("vm   -   view my tasks")
        print("gr   -   generate reports")
        print("ds   -   display statistics")
        print("e    -   exit program")
        user_choice = input("").lower()
    else:
        print("a    -   add task")
        print("va   -   view all tasks")
        print("vm   -   view my tasks")
        print("e    -   exit program")
        user_choice = input("").lower()

    user_decision(user_choice)


# user_decision() function:
# read the user's choice and send them to appropriate
# function based on choice

def user_decision(user_choice):
    if user_choice == "r":
        reg_user()

    if user_choice == "a":
        add_task()

    if user_choice == "va":
        view_all()

    if user_choice == "vm":
        view_mine()

    if user_choice == "gr":
        gen_reports()
    
    if user_choice == "ds":
        disp_stats()

    if user_choice == "e":
        exit()



# reg_user() function:
# if user wants to register a new user, make sure they have admin privileges
# if not display relevant menu option and ask them to select an appropriate option
# else let them register new user

def reg_user():

    f = open('user.txt', 'r')
    if usernme != "admin":
        print("You have selected an invalid choice. Please try again\n")
        menu_option()
    else:
        new_usernme = input("Please enter a new username: ")

        # if the usernmame selected by the user is already found in user.txt
        # ask the user to try a different username
        while new_usernme in usernme_list:
            print("That username has already been taken, please try a different username.\n")
            new_usernme = input("Please enter a new username: ")

        new_passw = input("Please enter the new password: ")
        confirm_passw = input("Please confirm your pasword: ")

        # if password does not match password confirmation, ask user to enter details again
        # else write the new username and password to user.txt

        while new_passw != confirm_passw:
            print("Your password entries do not match. Please try again")
            new_usernme = input("Please enter a new username: ")
            new_passw = input("Please enter the new password: ")
            confirm_passw = input("Please confirm your password: ")

        new_user = (f"\n{new_usernme}, {new_passw}")
        f.close()
        with open('user.txt', 'a') as f:
            f.write(new_user)
        print("\nNew user successfully registered!\n")

    menu_option()


# add_task() function:
# if user wants to add a new task, get the relevant information from the user
# save new info to tasks.txt

def add_task():

    # import the date method to get the current date
    from datetime import date
    from datetime import timedelta

    task_complete = "No"
    task_user = input("Please enter the username who has been assigned the task: ")
    task_title = input("Please enter the name of the task: ")
    task_descrip = input("Please enter a description of the task:\n")
    task_assigned = date.today()
    task_due = task_assigned + timedelta(days=2)

    new_task = (f"\n {task_user}, {task_title}, {task_descrip}, {str(task_assigned)}, {str(task_due)}, {task_complete}")

    with open('tasks.txt', 'a') as g:
        g.write(new_task)
    print("\nNew task successfully added!\n")

    menu_option()


# view_all() function:
# if user wants to view all tasks read tasks.txt
# and display info in easy to read format

def view_all():

    with open('tasks.txt', 'r') as f:
        for line in f:
            print("Task             :   {}".format(line.split(', ')[1]))
            print("Assigned to      :   {}".format(line.split(', ')[0]))
            print("Date Assigned    :   {}".format(line.split(', ')[3]))
            print("Due Date         :   {}".format(line.split(', ')[4]))
            print("Task Completed   :   {}".format(line.split(', ')[5]))
            print("Task Description :   {}".format(line.split(', ')[2]))
            print('\n')

    menu_option()


# view_mine() function:
# if user wants to view tasks assigned specifically to them
# read lines that start with username from tasks.txt and
# display info in easy to read format

def view_mine():

    g = open('temp.txt', 'w+')

    with open('tasks.txt', 'r') as f:

        count = 1
        tasks = []
        for line in f:

            # make sure the line starts with logged in user
            if line.startswith(usernme):
                print(str(count) + ". Task                          :   {}".format(line.split(', ')[1]))
                print("Date Assigned                    :   {}".format(line.split(', ')[0]))
                print("Date Assigned                    :   {}".format(line.split(', ')[3]))
                print("Due Date                         :   {}".format(line.split(', ')[4]))
                print("Task Completed                   :   {}".format(line.split(', ')[5]))
                print("Task Description                 :   {}".format(line.split(', ')[2]))
                print('\n')
            tasks.append(line)
            count += 1
            g.write(str(tasks))

    print("Please select the task you would like to edit by choosing the corresponding number.")
    print("If you would like to return to the main menu, enter '-1':")
    task_choice = int(input(""))

    if task_choice == -1:
        menu_option()

    else:
        for line in g:
            if line.startswith(str(task_choice)):
                print(line.split(', ')[5])

                if line.split(', ')[5] == "No":
                    line.split(', ')[5] = "Yes"
                print(line.split(', ')[5])

        g.close()


# gen_reports() function:

def gen_reports():
    if usernme != "admin":
        print("This is an invalid option. Please select from the following options:\n")
        menu_option()
    else:
        to = open('task_overview.txt', 'w')
        uo = open('user_overview.txt', 'w')
        f1 = open('tasks.txt', 'r')
        f2 = open('user.txt', 'r')

        task_count = 0
        user_count = 0

        for i in f1:
            task_count += 1

        to.write("Total number of tasks generated:\t" + str(task_count) + '\n')
        print("task_overview.txt report succcessfully generated.")

        for i in f2:
            user_count += 1

        uo.write("Total number of users registered:\t" + str(user_count) + '\n')
        uo.write("Total number of tasks generated:\t" + str(task_count) + '\n')


        print("useroverview.txt report successfully generated.")

        to.close()
        uo.close()
        f1.close()
        f2.close()



# if user selects to display stats, make sure they have admin privileges
# if not dispay relevant menu option and ask them to make appropriate choice
# if so display number of registered users and number of tasks

def disp_stats():

    if usernme != "admin":
        print("You have selected an invalid option. Please try again\n")
        menu_option()
    else:

        f = open('user.txt', 'r')
        g = open('tasks.txt', 'r')


        # set counters for number of users and number of tasks to 0

        num_users = 0
        num_tasks = 0

        # for each line in user.txt increment number of users by 1

        for line in f:
            num_users += 1

        # for each line in tasks.txt increment number of tasks by 1

        for line in g:
            num_tasks += 1

        # display results

        print(f"Number of users             :   {num_users}")
        print(f"Number of tasks             :   {num_tasks}")

        # close the files
            
        f.close()
        g.close()



# Exit the program

def exit():
    print("\nApplication closed. #Goodbye.\n")
    quit()



def main():

    with open('user.txt', 'r+') as f:

        # separate the username from the password in the textfile and assign each to a new variable

        # Ask the user for their username and password


        global usernme
        usernme = input("Please enter your username: ")
        passw = input("Please enter your password: ")

        # Use a dictionary to link usernames to passwords from the text file
        # create empty lists for username and password:

        global usernme_list
        usernme_list = []
        passw_list = []

        # separate usernames from passwords:

        for line in f:
            username, password = line.split(',')
            password = password.strip()
            usernme_list.append(username)
            passw_list.append(password)
        data = dict(zip(usernme_list,passw_list))


        # keep asking user for the username and password until the combination is correct:

        while not data.get(usernme) or passw != data[usernme]:
            print("Your username or password is incorrect. Please try again \n")
            usernme = input("Please enter your username: ")
            passw = input("Please enter your password: ")

        menu_option()


# call the main function

main()