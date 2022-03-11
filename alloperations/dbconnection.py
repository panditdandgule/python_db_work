import pymysql

db_connection=pymysql.connect(host='localhost',
                              user='root',
                              password='root',
                              port=3305,
                              database='')

print(db_connection)

# creating database_cursor to perform SQL operation
db_cursor = db_connection.cursor()

# executing cursor with execute method and pass SQL query
db_cursor.execute("CREATE DATABASE my_db")

# get list of all databases
db_cursor.execute("SHOW DATABASES")

#print all databases
for db in db_cursor:
    print(db)
