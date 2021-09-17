#Menu driven program
import student_login as slogin
import admin_login as adlogin
import time
ch=0
while ch!='3':
    print("\t"*5, "1. Student")
    print("\t"*5, "2. Admin")
    print("\t"*5, "3. Exit")
    print("\t"*5,"Enter your choice :", end="")
    ch = input()
    if ch=='1':
        print("Student Login")
        print("\n")
        slogin.login()
    elif ch=='2' :
        print("Admin Login")
        print("\n")
        adlogin.login()
    else:
        print("Exiting program...")
        break;
    print("\n\n")
    