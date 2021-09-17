#How to delete data of a Mysql Table from Python
import mysql.connector
def delete():
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="QUIZ"
    )
    mycursor = mydb.cursor()
    d = input("Enter the admin id to delete :")
    sql = "DELETE FROM admin WHERE id = %s"
    val=(d,)
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount,"record deleted")

