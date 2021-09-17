#How to delete data of Mysql Table using Python
import mysql.connector
def delete():

    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="QUIZ"
    )
    mycursor = mydb.cursor()
    qid = input("Enter the qid to delete :")
    sql = "DELETE FROM question WHERE qid = %s"
    val=(qid,)
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount,"record deleted")
