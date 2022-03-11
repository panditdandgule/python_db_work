import mysql.connector
from crudoperation.operations import *

while (1):
    print("------------MENU----------------")
    print("     1)Class")
    print("     2)Section")
    print("     3)Student")
    print("     4)Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("------------MENU----------------")
        print("     1)Add Record")
        print("     2)Update Record")
        print("     3)Delete Record")
        print("     4)Search Record")
        print("     5)Go to Previous Menu")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            name = input("Enter the class name: ")
            insert_record(name)
        elif choice == 2:
            myconnection = mysql.connector.connect(host="localhost",
                                                   user='root',
                                                   password="",
                                                   port="3306",
                                                   database="sunbeam")

            if myconnection.is_connected():
                print("Connection is successful")
            else:
                print("Connection is not successful")
            mycursor = myconnection.cursor()
            sql = "select *from class"
            mycursor.execute(sql)
            data = mycursor.fetchall()
            D = {}
            j = 1
            for i in data:
                D[j] = i
                print(j, ") ", i[1], sep='')

                j += 1
            # print(D)
            roll_no = int(input("Enter your choice:"))
            update_record(roll_no, D)
        elif choice == 3:
            myconnection = mysql.connector.connect(host="localhost",
                                                   user='root',
                                                   password="",
                                                   port="3306",
                                                   database="sunbeam")

            if myconnection.is_connected():
                print("Connection is successful")
            else:
                print("Connection is not successful")
            mycursor = myconnection.cursor()
            sql = "select *from class"
            mycursor.execute(sql)
            data = mycursor.fetchall()
            D = {}
            j = 1
            for i in data:
                D[j] = i
                print(j, ") ", i[1], sep='')

                j += 1
            # print(D)
            roll_no = int(input("Enter your choice:"))
            delete_record(roll_no, D)
            myconnection.close();
        elif choice == 4:
            myconnection = mysql.connector.connect(host="localhost",
                                                   user='root',
                                                   password="",
                                                   port="3306",
                                                   database="sunbeam")

            if myconnection.is_connected():
                print("Connection is successful")
            else:
                print("Connection is not successful")
            mycursor = myconnection.cursor()
            sql = "select *from class"
            mycursor.execute(sql)
            data = mycursor.fetchall()
            D = {}
            j = 1
            for i in data:
                D[j] = i
                print(j, ") ", i[1], sep='')

                j += 1
            # print(D)
            roll_no = int(input("Enter your choice:"))
            display_record(roll_no, D)
            myconnection.close();
        elif choice == 5:
            pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        break
    else:
        print("Invalid option")
        continue
