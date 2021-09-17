#How to modify data of Mysql Table using Python
import mysql.connector
def modify():
    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="QUIZ"
    )

    mycursor = mydb.cursor()
    sid = input("Enter student id: ")
    query = "SELECT * from student where std_id=%s"
    value = (sid,)
    mycursor.execute(query,value)
    myresult=mycursor.fetchall()
    for rec in myresult:
        on = rec[1]
        ou = rec[2]
        op = rec[3]
        print(rec)

    n = input("Enter name:")
    u = input("Enter username:")
    p = input("Enter password:")


    if(n==""):
        n=on
    if(u==""):
        u = ou
    if(p==""):
        p=op

    sql = 'UPDATE student SET student_name=%s, user_name=%s, password = %s WHERE std_id = %s'
    val = (n,u,p,sid,)
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount,"record updated")
