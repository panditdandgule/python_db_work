import pymysql

try:
    con=pymysql.connect(host="localhost",
                    user='root',
                    password='root',
                    port=3305,
                    database='pythontest')
    cursor=con.cursor()
    cursor.execute("create table employees(eno int(10),ename varchar(20),esal float(10),eaddr varchar(20))")
    print("Table created successfully..")

except pymysql.DatabaseError as e:
    if con:
        con.rollback()
        print("There is problem with sql",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
