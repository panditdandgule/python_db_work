import sqlite3

conn = sqlite3.connect('javatpoint.db')

data = conn.execute("select * from Employees");

for row in data:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("ADDRESS = ", row[2])
    print("SALARY = ", row[3], "\n")

conn.close();