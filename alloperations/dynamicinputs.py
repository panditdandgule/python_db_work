import pymysql

try:
    con=pymysql.connect(host='localhost',
                        user='root',
                        password='root',
                        port=3305,
                        database='pythontest')
    cursor=con.cursor()

    while True:
        eno=int(input("Enter Employee Number:"))
        ename=input("Enter Employee Name:")
        esal=float(input("Enter Employee Salary:"))
        eaddr=input("Enter Employee Address:")
        sql="insert into employees values(%d,'%s',%f,'%s')"
        cursor.execute(sql %(eno,ename,esal,eaddr))
        print("Record inserted successfully")
        option=input("Do you want to insert one more record[Yes|No] :")
        if option=='No':
            con.commit()
            break
except pymysql.DatabaseError as e:
    if con:
        con.rollback()
        print("There was an problem with sql",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
