import pymysql

from crudoperations import dbconnection as dbconn


class Create:

    def create_data(self):

        # get the sql connection
        conn = dbconn.get_connection()
        id = int(input("Enter Id: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))

        try:

            cursor = conn.cursor()
            query = "insert into employee Values(%d,'%s',%d)"
            # Execute the sql query
            cursor.execute(query % (id, name, age))

            # commit the data
            conn.commit()
            print("Data Saved Successfully")
        except pymysql.DatabaseError as e:
            if conn:
                conn.rollback()
            print("Something went wrong, please check", e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
