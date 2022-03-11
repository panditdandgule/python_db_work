import pymysql

try:
    con=pymysql.connect(host='localhost',
                        user='root',
                        password='root',
                        port=3305,
                        database='pythontest')

    cursor=con.cursor()
    cursor.execute("insert into employees values (100,'pandit',10000,'Pune')")
    con.commit()
    print("Record inserted successfully..")
except pymysql.DatabaseError as e:
    if con:
        con.rollback()
        print("There was an error",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()