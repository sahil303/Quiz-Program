#Menu driven program
import menu_question as mq
import menu_student as ms
import menu_admin as mad
import display_score_table as ds
def menu():
    ch=0
    while ch!='3':
        print("\t"*5, "Welcome to Admin Panel")
        print("\n")
        print("\t"*5,"1. Question Management Program")
        print("\t"*5,"2. Student Management Program")
        print("\t"*5,"3. Admin Management Program")
        print("\t"*5,"4. Display Score Table")
        print("\t"*5,"5. Exit")
        print("\t","Enter your choice :", end="")
        ch = input()
        if ch=='1' :
            print("Qdata Management Program")
            mq.menu()
        elif ch=='2':
            print("Student Management Program")
            ms.menu()
        elif ch=='3':
            print("Admin Management Program")
            mad.menu()
        elif ch=='4':
            print("Display Score table")
            ds.display()
        else:
            print("Exiting program...")
            break;
        print("\n\n")

