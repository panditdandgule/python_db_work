import pymysql

def get_connection():
    try:
        conn=pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             port=3305,
                             database='prodinventory')
        #print("Database connection was successful..")
        return conn
    except pymysql.DatabaseError as e:
        print("While connecting something went wrong",e)
