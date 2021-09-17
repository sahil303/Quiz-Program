# Inserting data into Admin Table
import mysql.connector
def add():
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "QUIZ"
    )

    n = input("Enter Name :")
    user_name = input("Enter UserName :")
    passwd = input("Enter Password :")

    mycursor = mydb.cursor()

    sql_query = 'INSERT INTO admin ( name , username , password) VALUES(%s,%s,%s)'

    val = (n, user_name,passwd)
    mycursor.execute(sql_query,val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted")
