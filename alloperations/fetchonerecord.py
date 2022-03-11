import pymysql

try:
    con=pymysql.connect(host='localhost',
                        user='root',
                        password='root',
                        port=3305,
                        database='pythontest')

    cursor=con.cursor()

    cursor.execute("select *from employees")
    row=cursor.fetchone()
    while row is not None:
        print(row)
        row=cursor.fetchone()
except pymysql.DatabaseError as e:
    if con:
        con.rollback()
        print("There was probleme with sql ",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()