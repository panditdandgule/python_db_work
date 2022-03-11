import pymysql

from crudoperations import dbconnection as dbconn


class Read:
    allData = []

    def read_data(self):
        # Get SQL connection
        try:
            conn = dbconn.get_connection()
            cursor = conn.cursor()
            # Excute the sql query
            cursor.execute("select *from employee")
            item=cursor.fetchall()
        except pymysql.DatabaseError as e:
            if conn:
                conn.rollback()
                print("There was something went wrong", e)
        else:
            # print the data
            print('-------------------------------------------')
            print('# ID\t\t Name\t\t\t Age          #')
            print('-------------------------------------------')
            for row in item:

                print(' {}\t\t {} \t\t\t{} '.format(row[0], row[1], row[2]))


        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
