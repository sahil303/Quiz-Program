#Menu driven program
import mysql.connector
import insert_into_student_table as adstudent
import modify_student_data as modstd
import delete_student_data as dltstd
import display_student_table as dispstd

def menu():
    ch=0
    while ch!='5':
        print("\t"*5, "Student Managment Program")
        print("\n")
        print("\t"*5,"1. Add student")
        print("\t"*5,"2. Modify student")
        print("\t"*5,"3. Delete student")
        print("\t"*5,"4. Display student")
        print("\t"*5,"5. Exit")
        print("\t","Enter your choice :", end="")
        ch = input()
        if ch=='1' :
            print("Add student")
            adstudent.add()
        elif ch=='2':
            print("Modify student")
            modstd.modify()
        elif ch== '3':
            print("Delete student")
            dltstd.delete()
        elif ch == '4':
            print("Display student")
            dispstd.display()
        else:
            print("Exiting program...")
            break;
        print("\n\n")

