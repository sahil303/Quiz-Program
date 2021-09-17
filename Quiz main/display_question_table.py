#How to display records of a Mysql Table from python
import mysql.connector
def display():
    mydb=mysql.connector.connect (
        host="localhost",
        user ="root",
        password="",
        database="QUIZ"
        )
    mycursor=mydb.cursor()

    sql='SELECT * FROM question'
    mycursor.execute(sql)

    myresult=mycursor.fetchall()

    for x in myresult:
        print(x)
