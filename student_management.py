import os
import platform

global student_list
student_list = ["Clarisse", "Althea", "Eloisa", "Marial"]

def manage_student():

    x = "#" * 30
    y = "=" * 28
    global bye
    bye = "\n {}\n# {} #\n# ===> Brought To You By <===  #\n# ===> code-projects.org <===  #\n# {} #\n {}".format(x, y, y, x)

    print(""" 

  ------------------------------------------------------
 |======================================================| 
 |======== Welcome To Student Management System	========|
 |======================================================|
  ------------------------------------------------------

Enter 1 : To View Student's List 
Enter 2 : To Add New Student 
Enter 3 : To Search Student 
Enter 4 : To Remove Student 

		""")

    try:
        user_input = int(input("Please Select An Above Option: "))
    except ValueError:
        exit("\nHy! That's Not A Number")
    else:
        print("\n")

    if (user_input == 1):
        print("List Students\n")
        for students in student_list:
            print("=> {}".format(students))

    elif (user_input == 2):
        new_student = input("Enter New Student: ")
        if (new_student in student_list):
            print("\nThis Student {} Already In The Database".format(new_student))
        else:
            student_list.append(new_student)
            print("\n=> New Student {} Successfully Add \n".format(new_student))
            for students in student_list:
                print("=> {}".format(students))

    elif (user_input == 3):
        search_student = input("Enter Student Name To Search: ")
        if (search_student in student_list):
            print("\n=> Record Found Of Student {}".format(search_student))
        else:
            print("\n=> No Record Found Of Student {}".format(search_student))

    elif (user_input == 4):
        remove_student = input("Enter Student Name To Remove: ")
        if (remove_student in student_list):
            student_list.remove(remove_student)
            print("\n=> Student {} Successfully Deleted \n".format(remove_student))
            for students in student_list:
                print("=> {}".format(students))
        else:
            print("\n=> No Record Found of This Student {}".format(remove_student))

    elif (user_input < 1 or user_input > 4):
        print("Please Enter Valid Option")

manage_student()

def run_again():  # Making Runable Problem1353
    run_again = input("\nwant To Run Again Y/n: ")
    if (run_again.lower() == 'y'):
        if (platform.system() == "Windows"):
            print(os.system('cls'))
        else:
            print(os.system('clear'))
        manage_student()

    else:
        quit(bye) 

run_again()