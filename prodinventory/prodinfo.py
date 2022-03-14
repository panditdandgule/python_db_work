class Product:

    def __init__(self,pid,pname,pqty,price,vendor,city):
        self.prodId=pid
        self.prodName=pname
        self.prodQty=pqty
        self.prodPrice=price
        self.prodVendor=vendor
        self.city=city

    def __str__(self):
        return f'''{self.__dict__}'''

    def __repr__(self):
        return str(self)

