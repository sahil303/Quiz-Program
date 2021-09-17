

import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="QUIZ"
)
mycursor=mydb.cursor()
sql = "CREATE TABLE score (quizid int(5) NOT NULL AUTO_INCREMENT, date VARCHAR(12) NOT NULL, userid int(5) NOT NULL, score int(3) NOT NULL, PRIMARY KEY (quizid))"
mycursor.execute(sql)
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)