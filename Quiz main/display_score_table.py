#How to display records of a Mysql Table from python
import mysql.connector
import time
def display():
    mydb=mysql.connector.connect (
        host="localhost",
        user ="root",
        password="",
        database="QUIZ"
        )
    mycursor=mydb.cursor()

    sql='SELECT * FROM score'
    mycursor.execute(sql)

    myresult=mycursor.fetchall()

    for x in myresult:
        print("Quiz_id :",x[0],",","Date :",x[1],",","Student_id :",x[2],",","Score :",x[3])
    time.sleep(1)


