import sqlite3

conn = sqlite3.connect("javatpoint.db")
print("Opened database successfully")

conn.execute("INSERT INTO Employees (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, 'Ajeet', 27, 'Delhi', 20000.00 )");

conn.execute("INSERT INTO Employees (ID,NAME,AGE,ADDRESS,SALARY) \
VALUES (2, 'Allen', 22, 'London', 25000.00 )");

conn.execute("INSERT INTO Employees (ID,NAME,AGE,ADDRESS,SALARY) \
VALUES (3, 'Mark', 29, 'CA', 200000.00 )");

conn.execute("INSERT INTO Employees (ID,NAME,AGE,ADDRESS,SALARY) \
VALUES (4, 'Kanchan', 22, 'Ghaziabad ', 65000.00 )");

conn.commit()
print("Records inserted successfully");
conn.close()
