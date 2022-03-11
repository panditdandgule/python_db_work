from crudoperations import dbconnection as dbconn
class Delete:
    def delete_data(self):
        # Get the SQL connection
        conn=dbconn.get_connection()

        id = int(input('Enter Employee Id = '))

        try:
            # Get record which needs to be deleted
            sql = "Select * From Employee Where Id = %d"
            cursor = conn.cursor()
            cursor.execute(sql %(id))
            item = cursor.fetchone()
            print('Data Fetched for Id = ', id)
            print('ID\t\t Name\t\t\t Age')
            print('-------------------------------------------')
            print(' {}\t\t {} \t\t\t{} '.format(item[0], item[1], item[2]))
            print('-------------------------------------------')
            confirm = input('Are you sure to delete this record (Y/N)?')

            # Delete after confirmation
            if confirm == 'Y':
                deleteQuery = "Delete From Employee Where Id = %d"
                cursor.execute(deleteQuery %(id))
                conn.commit()
                print('Data deleted successfully!')
            else:
                print('Wrong Entry')
        except:
            print('Something wrong, please check')
        finally:
            conn.close()