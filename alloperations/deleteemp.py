import pymysql

try:
    con=pymysql.connect(host='localhost',
                        user='root',
                        password='root',
                        port=3305,
                        database='pythontest')

    cursor=con.cursor()
    cutoffsalary=float(input("Enter cutoff salary: "))
    sql="delete from employees where esal>%f"
    cursor.execute(sql %(cutoffsalary))
    print("Record deleted successfully")
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