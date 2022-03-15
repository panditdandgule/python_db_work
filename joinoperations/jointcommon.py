import pymysql

from dbconnections import get_connection


def join_common_columns_from_two_tables():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # joining two tables on department
        query = "select employee.eid,employee.ename,employee.salary,departments.did,departments.dname " \
                "from departments join employee on departments.did=employee.did";
        cursor.execute(query)
        print("ID    Name    Salary    Dept_Id    Dept_Name")
        for row in cursor:
            print("%d    %s    %d    %d    %s" % (row[0], row[1], row[2], row[3], row[4]))
    except pymysql.DatabaseError as e:
        if conn:
            conn.rollback()
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


if __name__ == '__main__':
    join_common_columns_from_two_tables()
