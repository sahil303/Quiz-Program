#Menu driven program

import insert_into_question_table as adq
import modify_question_data as mq
import delete_question_data as dq
import display_question_table as disq

def menu():
    ch=0
    while ch!='5':
        print("\t"*5, "welcome to Qdata Management Program")
        print("\n")
        print("\t"*5,"1. Add Question data")
        print("\t"*5,"2. Modify Question data")
        print("\t"*5,"3. Display question data")
        print("\t"*5,"4. delete question data")
        print("\t"*5,"5. Exit")
        print("\t","Enter your choice :", end="")
        ch = input()
        if ch=='1' :
            print("Add Qdata")
            adq.add()
        elif ch=='2':
            print("Modify Question")
            mq.modify()
        elif ch== '3':
            print("Display Question")
            disq.display()
        elif ch == '4':
            print("Delete Question")
            dq.delete()
        else:
            print("Exiting program...")
            break;
        print("\n\n")

