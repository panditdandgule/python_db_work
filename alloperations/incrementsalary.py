import pymysql

try:
    con=pymysql.connect(host='localhost',
                        user='root',
                        password='root',
                        port=3305,
                        database='pythontest')
    cursor=con.cursor()
    increment=float(input("Enter increment salary"))
    salrange=float(input("Enter Salary Range: "))
    sql="update employees set esal=esal+%f where esal<%f"
    cursor.execute(sql %(increment,salrange))
    print("Record updated successfully")
    con.commit()
except pymysql.DatabaseError as e:
    if con:
        con.rollback()
        print("There was problem with sql",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
