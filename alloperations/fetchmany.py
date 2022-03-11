import pymysql

try:
    con=pymysql.connect(host='localhost',
                        user='root',
                        password='root',
                        port=3305,
                        database='pythontest')

    cursor=con.cursor()

    cursor.execute("Select *from employees")
    n=int(input("Enter number of records"))
    data=cursor.fetchmany(n)

    for row in data:
        print(row)
except pymysql.DatabaseError as e:
    if con:
        con.rollback()
        print("There was an problem with sql",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
