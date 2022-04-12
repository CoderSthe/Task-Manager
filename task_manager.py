from itertools import count


def menu_option():

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


def reg_user():

    f = open('user.txt', 'r')
    if usernme != "admin":
        print("You have selected an invalid choice. Please try again\n")
        menu_option()
    else:
        new_usernme = input("Please enter a new username: ")

        while new_usernme in usernme_list:
            print("That username has already been taken, please try a different username.\n")
            new_usernme = input("Please enter a new username: ")

        new_passw = input("Please enter the new password: ")
        confirm_passw = input("Please confirm your pasword: ")

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

def add_task():
    
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

def view_mine():

    g = open('temp.txt', 'w+')

    with open('tasks.txt', 'r') as f:

        count = 1
        tasks = []
        for line in f:

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

def disp_stats():

    if usernme != "admin":
        print("You have selected an invalid option. Please try again\n")
        menu_option()
    else:

        f = open('user.txt', 'r')
        g = open('tasks.txt', 'r')

        num_users = 0
        num_tasks = 0

        for line in f:
            num_users += 1

        for line in g:
            num_tasks += 1

        print(f"Number of users             :   {num_users}")
        print(f"Number of tasks             :   {num_tasks}")

        # close the files
            
        f.close()
        g.close()

def exit():
    print("\nApplication closed. #Goodbye.\n")
    quit()



def main():

    with open('user.txt', 'r+') as f:


        global usernme
        usernme = input("Please enter your username: ")
        passw = input("Please enter your password: ")

        global usernme_list
        usernme_list = []
        passw_list = []

        for line in f:
            username, password = line.split(',')
            password = password.strip()
            usernme_list.append(username)
            passw_list.append(password)
        data = dict(zip(usernme_list,passw_list))

        while not data.get(usernme) or passw != data[usernme]:
            print("Your username or password is incorrect. Please try again \n")
            usernme = input("Please enter your username: ")
            passw = input("Please enter your password: ")

        menu_option()

main()
