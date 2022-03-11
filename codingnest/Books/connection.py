import mysql.connector as conn


class Connection:
    def __init__(self):
        self.con = conn.connect(user='root', password='root', host='localhost', port='3305', database='books')
        if self.con.is_connected():
            print("Connection is successful")
        else:
            print("Connection is failed")

        q1 = "create table if not exists books(bookid int primary key AUTO_INCREMENT,foreign key(bookid) references author(authorid),foreign key(bookid) references publisher(publisherid),title varchar(30),isbn varchar(20),gener varchar(20),type varchar(20), publicationyear datetime,price int)"
        q2 = "create table if not exists publisher(publisherid int primary key,foreign key(publisherid) references books(bookid),country varchar(30))"
        q3 = "create table if not exists author(authorid int primary key,foreign key(authorid) references books(bookid),firstname varchar(30),lastname varchar(30))"
        q4 = "create table if not exists booksinventory(bookid int primary key,stockcount int)"
        q5 = "create table if not exists customer(customerid int primary key,firstname varchar(30),lastname varchar(30),emailaddress varchar(30),mobile varchar(12),country varchar(30),otherdetails varchar(60))"
        q6 = "create table if not exists orders(orderid int primary key,foreign key(orderid) references customer(customerid),orderdate datetime,subtotal int,shipping varchar(30),total int)"
        q7 = "create table if not exists orderitem(foreign key(orderid) references books(bookid),foreign key(orderid) references books(bookid),quantity int,price int)"

        cur = self.con.cursor()
        cur.execute(q1)
        cur.execute(q2)
        cur.execute(q3)
        cur.execute(q4)
        cur.execute(q5)
        cur.execute(q6)
        cur.execute(q7)

        # print("Tables created successfully..")
        # showing all tables
        # cur.execute("SHOW TABLES")
        # print("Table names:")
        # for x in cur:
        #   print(x)

    def insert(self, title, isbn, gener, type, publicationyear, price, publisherid, country, authorid, firstname,
               lastname, bookid, stockcount, customerid, emailaddress, mobile, otherdetails, orderid, orderdate,
               subtotal, shipping, total, quantity):
        q1 = "insert into books(title,isbn,gener,type,publicationyear,price) values('{}','{}','{}','{}',{},{})".format(
            title, isbn, gener, type, publicationyear, price)
        q2 = "insert into publisher(publisherid,country) values({},'{}')".format(publisherid, country)
        q3 = "insert into author(authorid,firstname,lastname) values({},'{}','{}')".format(authorid, firstname,
                                                                                           lastname)
        q4 = "insert into booksinventory(bookid,stockcount) values({},{})".format(bookid, stockcount)
        q5 = "insert into customer(customerid,firstname,lastname,emailaddress,mobile,country,otherdetails) values({},'{}','{}','{}','{}','{}','{}')".format(
            customerid, firstname, lastname, emailaddress, mobile, country, otherdetails)
        q6 = "insert into orders(orderid,orderdate,subtotal,shipping,total) values({},{},{},'{}',{})".format(orderid,
                                                                                                             orderdate,
                                                                                                             subtotal,
                                                                                                             shipping,
                                                                                                             total)
        q7 = "insert into orderitem(quantity,price) values({},{})".format(quantity, price)

        cur = self.con.cursor()

        cur.execute(q1)
        cur.execute(q2)
        cur.execute(q3)
        cur.execute(q4)
        cur.execute(q5)
        cur.execute(q6)
        cur.execute(q7)

        self.con.commit()
        print("Data inserted successfully")

    def fetchall(self):
        q1 = "select *from books"
        q2 = "select *from publisher"
        q3 = "select *from author"
        q4 = "select *from booksinventory"
        q5 = "select *from customer"
        q6 = "select *from orders"
        q7 = "select *from oredritem"

        cur = self.con.cursor()

        c1 = cur.execute(q1)
        for row in c1:
            print(row)
        c2 = cur.execute(q2)
        for row in c2:
            print(row)
        c3 = cur.execute(q3)
        for row in c3:
            print(row)
        c4 = cur.execute(q4)
        for row in c4:
            print(row)
        c5 = cur.execute(q5)
        for row in c5:
            print(row)
        c6 = cur.execute(q6)
        for row in c6:
            print(row)
        c7 = cur.execute(q7)
        for row in c7:
            print(row)

    def delete(self,bookid):
        query="delete from books where bookid={}".format(bookid)

    def update(self,bookid,newtitle,newisbn,newgener,newtype,newpublicationyear,newprice):
        query="update books set title='{}',isbn='{}',gener='{}',publicationyear='{}',price={} where bookid={}".format(newtitle,newisbn,newgener,newtype,newpublicationyear,newprice)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Data updated successfully.")
