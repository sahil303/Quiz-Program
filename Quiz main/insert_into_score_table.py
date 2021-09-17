# Inserting data into Admin Table
import mysql.connector
import datetime
def add(score):
    
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "QUIZ"
    )

    mycursor = mydb.cursor()
    print("Enter your Student ID:",end = "")
    sid = input()
    d = datetime.datetime.now()
    date = d.strftime("%x")
    sql_query = 'INSERT INTO score (date,userid,score) VALUES(%s,%s,%s)'

    val = (date,sid,score)
    mycursor.execute(sql_query,val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted")


