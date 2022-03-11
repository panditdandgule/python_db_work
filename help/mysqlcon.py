import mysql.connector

cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              port='3306',
                              database='student')
mycursor = cnx.cursor()

mycursor.execute("SELECT * FROM student_student")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

cnx.close()