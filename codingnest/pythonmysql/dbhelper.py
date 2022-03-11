import mysql.connector as conn


class DBHelper:
    def __init__(self):
        self.con = conn.connect(host='localhost', user='root', password='root', port='3305', database='pythontest')
        if self.con.is_connected():
            print("Connection successful")
        else:
            print("Connection failed")

        query = 'create table if not exists user(userid int primary key,username varchar(30),phone varchar(12))'
        cur = self.con.cursor()
        cur.execute(query)

        print("Table created successfully..")

    # insert data
    def insert_user(self, userid, username, phone):
        query = "insert into user(userid,username,phone) values({},'{}','{}')".format(userid, username, phone)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        # print("Data saved successfully")

    def fetch_all(self):
        query = "Select *from user"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("UserId: ", row[0])
            print("UserName: ", row[1])
            print("Phone: ", row[2])
            print("")

    def delete_user(self, userid):
        query = "delete from user where userid={}".format(userid)
        cur = self.con.cursor()
        cur.execute(query)
        print("Data delete successfully..")

    def update_user(self, userid, newname, newphone):
        query = "update user set username='{}',phone='{}' where userid={}".format(newname, newphone, userid)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Data updated successfully")
