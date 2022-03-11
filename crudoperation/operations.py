import mysql.connector


def insert_record(name):
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
    sql = "INSERT INTO class(name) VALUES('{}')".format(name)
    mycursor.execute(sql)
    myconnection.commit()


def update_record(roll_no, D):
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
    name = input("Enter new name for the class:")
    sql = "UPDATE class SET name='{}' where roll_no='{}'".format(name, D[roll_no][0])
    mycursor.execute(sql)
    myconnection.commit()


def delete_record(roll_no, D):
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

    sql = "DELETE FROM class WHERE roll_no='{}'".format(D[roll_no][0])
    mycursor.execute(sql)
    myconnection.commit()
    myconnection.close();


def display_record(roll_no, D):
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
    name = input("Enter new name for the class:")
    sql = "UPDATE class SET name='{}' where roll_no='{}'".format(name, D[roll_no][0])
    mycursor.execute(sql)
    myconnection.commit()
