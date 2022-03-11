import pymysql

#return the sql connection

def get_connection():
    try:
        connection=pymysql.connect(host='localhost',
                                   user='root',
                                   password='root',
                                   port=3305,
                                   database='emptest')
        print("Database connection successful..")
        return connection
    except pymysql.DatabaseError as e:
        print("While connection soemthing went wrong",e)