from mysql.connector import MySQLConnection

class books:

    def __init__(self, bookid, authorid, publisherid, title, ISBN, Genre, Type, PublicationYear, price, condition):
        self.bookid = bookid
        self.authorid = authorid
        self.publisherid = publisherid
        self.title = title
        self.ISBN = ISBN
        self.Genre = Genre
        self.Type = Type
        self.PublicationYear = PublicationYear
        self.price = price
        self.condition = condition


class Publisher(books):
    def __init__(self, bookid, publisherid, country):
        self.bookid = bookid
        self.publisherid = publisherid
        self.country = country


class Author(books):
    def __init__(self, authorid, bookid, firstname, lastname):
        self.authorid = authorid
        self.bookid = bookid
        self.firstname = firstname
        self.lastname = lastname


class BooksInventory(books):
    def __init__(self, bookid, stockcount):
        self.bookid = bookid
        self.stockcount = stockcount


class Customer:
    def __init__(self, customerid, firstname, lastname, emailaddress, mobile, country, otherdetails):
        self.customerid = customerid
        self.firstname = firstname
        self.lastname = lastname
        self.emailaddress = emailaddress
        self.mobile = mobile
        self.country = country
        self.otherdetails = otherdetails


class Orders(Customer):
    def __init__(self, orderid, customerid, orderdate, subtotal, shipping, total):
        self.orderid = orderid
        self.customerid = customerid
        self.orderdate = orderdate
        self.subtotal = subtotal
        self.shipping = shipping
        self.total = total


class Order(books, Orders):
    def __init__(self, item, orderid, bookid, quantity, price):
        self.item = item
        self.orderid = orderid
        self.bookid = bookid
        self.quantity = quantity
        self.price = price

bk=books()