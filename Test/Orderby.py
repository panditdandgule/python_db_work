import sqlite3
import mysql.connector

mydb=mysql.connector.connect(host='localhost',
                             user='root',
                             password='',
                             database='ORG')

print(mydb)

table_name = 'russell3000'

# Create a cursor (an instance) to manipulate your SQL Database
mycursor = mydb.cursor(buffered=True)

# Print a list of all avail databases for given PORT and HOST above
# mycursor.execute('SHOW DATABASES')
# for x in mycursor:
#     print(x)

# # ORDER DATA IN DATABASE ===========================
# Order data retrieved by (params)
params = 'Company_Name'

query = f'SELECT * FROM {table_name} ORDER BY {params}'

mycursor.execute(query)

result = mycursor.fetchall()

print('==================')
for x in result:
    print(x)

# Order data retrieved by (params) in descending order
# Same as above EXCEPT FOR:
descending_query = f'SELECT * FROM {table_name} ORDER BY {params} DESC'