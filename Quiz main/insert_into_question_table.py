# Inserting data into Admin Table
import mysql.connector
def add():
    
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "QUIZ"
    )

    ques = input("Enter question :")
    opt1 = input("Enter option 1 :")
    opt2 = input("Enter option 2 :")
    opt3 = input("Enter option 3 :")
    opt4 = input("Enter option 4 :")
    cans = input("Enter correct answer :")

    mycursor = mydb.cursor()

    sql_query = 'INSERT INTO question (question,option1,option2,option3,option4,correct_ans) VALUES(%s,%s,%s,%s,%s,%s)'

    val = (ques,opt1,opt2,opt3,opt4,cans)
    mycursor.execute(sql_query,val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted")

