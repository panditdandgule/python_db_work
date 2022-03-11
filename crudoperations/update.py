import pymysql

from crudoperations import dbconnection


class Update:

    def update_data(self):
        # Get the sql connection
        conn = dbconnection.get_connection()

        id = int(input("Enter Employee Id: "))

        try:
            # Fetch the data which need to you updated
            sql = "select *from employee where id=%d"
            cursor = conn.cursor()
            cursor.execute(sql % (id))

            item = cursor.fetchone()

            print('Data Fetched for Id = ', id)
            print('ID\t\t Name\t\t\t Age')
            print('-------------------------------------------')
            print(' {}\t\t {} \t\t\t{} '.format(item[0], item[1], item[2]))
            print('-------------------------------------------')
            print('Enter New Data To Update Employee Record ')

            name = input('Enter New Name = ')
            age = int(input('Enter New Age = '))
            query = "Update Employee Set Name = '%s', Age =%d Where Id =%d"

            # execute the update query
            cursor.execute(query % (name, age, id))
            conn.commit()
            print("Data Updated Successfully")
        except pymysql.DatabaseError as e:
            print("Something went wrong please check ", e)
        finally:
            # close the connection
            conn.close()
