import mysql.connector
from os import system, name
import insert_into_score_table as adscore

def run():
    score=0
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="QUIZ"
        )
    mycursor=mydb.cursor()
    mycursor.execute("SELECT * FROM question")
    myresult=mycursor.fetchall()
    _ = system('cls')
    n = 0
    for x in myresult:
        print("\t"*3,"*"*60)
        print("\t"*4,"Welcome to Techpheonix Quiz Program")
        print("\t"*3,"*"*60)
        print("\t"*3,"     Question", str(n+1)+".",x[1],"\n")
        print("\t"*3,"     Option 1. ", x[2])
        print("\t"*3,"     Option 2. ", x[3])
        print("\t"*3,"     Option 3. ", x[4])
        print("\t"*3,"     Option 4. ", x[5],"\n")
        print("\t"*3,"*"*60)
        print("\t"*3,"   Enter your answer :", end="")
        ans=int(input())
        if(ans==x[6]):
            print("Answer is correct")
            score+=1
        else:
            print("Answer is incorrect")
        print("\n")
        _= system('cls')
        n +=1
    print("\t"*3,"*"*60)
    print("\t"*4,"  You have successfully completed the Quiz\n")
    print("\t"*5,"     Your score is :", score,"/", n)
    adscore.add(score)
    input("Press any key to Exit")
    
    _= system('cls')
