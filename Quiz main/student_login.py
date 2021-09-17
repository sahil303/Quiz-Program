import mysql.connector
import run_quiz
def login():
    
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="QUIZ"
        )
    mycursor=mydb.cursor()
    disprec="SELECT*FROM student"
    mycursor.execute(disprec)
    myresult=mycursor.fetchall()
    print("\t"*5, "Welcome to Student Login Program")
    print("\n")
    print("\t"*5, "Enter username:", end="")
    u = input()
    print("\t"*5, "Enter password:", end="")
    p = input()
    for rec in myresult:
        
        if (u == rec[2]):
            if (p == rec[3]):
                print("Login Successsful...")
                run_quiz.run()
                break
            else:
                print("Invalid password")
                break
        
    else:
        print("Invalid Username")


