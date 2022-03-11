import pymysql

try:
    con=pymysql.connect(host='localhost',
                        user='root',
                        password='root',
                        port=3305,
                        database='pythontest')

    cursor=con.cursor()
    cursor.execute("select *from employees")
    data=cursor.fetchall()

    for row in data:
        print("Employee Number:",row[0])
        print("Employee Name:",row[1])
        print("Employee Salary:",row[2])
        print("Employee Address:",row[3])
        print()
        print()
except pymysql.DatabaseError as e:
    if con:
        con.rollback()
        print("There was problem with sql",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()