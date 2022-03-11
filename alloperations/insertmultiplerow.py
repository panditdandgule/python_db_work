import pymysql

try:
    con=pymysql.connect(host='localhost',
                        user='root',
                        password='root',
                        port=3305,
                        database='pythontest')
    cursor=con.cursor()
    sql="insert into employees values (:eno,:ename,:esal,:eaddr)"
    records=([(200,'sunny',30000,'Pune'),
              (201,'pandit',40000,'Pune'),
              (202,'bali',25000,'Mumbai')])
    cursor.executemany(sql,records)
    con.commit()
    print("Records inserted successfully.")
except pymysql.DatabaseError as e:
    if con:
        con.rollback()
        print("There was database error",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()