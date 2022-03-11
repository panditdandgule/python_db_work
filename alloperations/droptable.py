import pymysql

try:
    con=pymysql.connect(host='localhost',
                        user='root',
                        password='root',
                        port=3305,
                        database='pythontest')
    cursor=con.cursor()
    cursor.execute("drop table employees")
    print("Table dropped successfully")
except pymysql.DatabaseError as e:
    if con:
        con.rollback()
        print("There was problem with sql",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()


