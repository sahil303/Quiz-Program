#Menu driven program
import mysql.connector
import insert_into_admin as addadmin
import modify_admin_data as modadd
import delete_admin_data as dltadd
import display_admin_table as disadd

def menu():
    ch=0
    while ch!='5':
        print("\t"*5, "Admin Managment Program")
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
            addadmin.add()
        elif ch=='2':
            print("Modify student")
            modadd.modify()
        elif ch== '3':
            print("Delete student")
            dltadd.delete()
        elif ch == '4':
            print("Display student")
            dispadd.display()
        else:
            print("Exiting program...")
            break;
        print("\n\n")


