import sys
import pymysql
from prodservices import ProductServices, Product
import dbconnection


class ProductServiceImpl(ProductServices):

    def create_product(self, proddetails):
        try:
            conn = dbconnection.get_connection()
            cursor = conn.cursor()
            try:
                prodid = proddetails.prodId
            except:
                print("Please enter valid input..")

            query = "SELECT * FROM product WHERE prodid=%d"
            result = cursor.execute(query % (prodid))
            try:
                if prodid > 0 and type(prodid) == int:
                    if result:
                        print("Product Id is already available..")
                        return cursor.fetchone()
                    else:
                        query = "insert into product values (%d,'%s',%d,%f,'%s','%s')"
                        cursor.execute(query % (
                            proddetails.prodId, proddetails.prodName, proddetails.prodQty, proddetails.prodPrice,
                            proddetails.prodVendor, proddetails.city))
                        conn.commit()
                        print("Data Saved Successfully..")
                else:
                    print("Please enter valid product id..")
            except:
                print("Something went wrong while adding data..")
        except pymysql.DatabaseError as e:
            if conn:
                conn.rollback()
            print("There was something went wrong", e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def display_all_products(self):
        try:
            conn = dbconnection.get_connection()
            cursor = conn.cursor()
            cursor.execute("select *from product")
            alldata = cursor.fetchall()

        except pymysql.DatabaseError as e:
            if conn:
                conn.rollback()
            print("There was an error while fetching data", e)
        else:
            print("==" * 40)
            print("ID\t\tName\t\t\tQty\t\t\tPrice\t\t\tVendor\t\tCity")
            print("==" * 40)
            for data in alldata:
                print(data[0], "\t\t", data[1], "\t\t", data[2], "\t\t", data[3], "\t\t", data[4], "\t", data[5])

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def search_product(self, prodid):
        try:

            conn = dbconnection.get_connection()
            cursor = conn.cursor()
            query = "select *from product where prodid=%d"
            cursor.execute(query % (prodid))
            data = cursor.fetchone()
            print("==" * 40)
            print("ID\t\tName\t\t\tQty\t\t\tPrice\t\t\tVendor\t\tCity")
            print("==" * 40)
            print(data[0], "\t\t", data[1], "\t\t", data[2], "\t\t", data[3], "\t\t", data[4], "\t\t", data[5])
            print("==" * 40)

        except pymysql.DatabaseError as e:
            if conn:
                conn.rollback()
            print("There was an error while fetching data ", e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def update_product(self):
        try:
            prodid = int(input("Enter id which id you want to update? "))
            conn = dbconnection.get_connection()
            cursor = conn.cursor()

        except pymysql.DatabaseError as e:
            if conn:
                conn.close()
            print("There was an error while updating data..", e)
        else:
            while True:
                try:
                    print("Enter choice 1 Name 2 Quantity 3 Price 4 Vendor 5 City 6 Exit")
                    choice = int(input("Enter your choice: "))
                except ValueError:
                    print("Please enter valid integer number..")
                if choice == 1:
                    prodname = input("Enter Product Name: ")
                    query = "update product set prodname='%s' where prodid=%d"
                    cursor.execute(query % (prodname, prodid))
                    conn.commit()
                    print("Updated Product Name Successfully..")
                elif choice == 2:
                    quantity = int(input("Enter Product Quantity: "))
                    query = "update product set quantity=%d where prodid=%d"
                    cursor.execute(query % (quantity, prodid))
                    conn.commit()
                    print("Updated product quantity successfully..")
                elif choice == 3:
                    price = float(input("Enter Proudct Price: "))
                    query = "update product set price=%f where prodid=%d"
                    cursor.execute(query % (price, prodid))
                    conn.commit()
                    print("Updated product price successfully..")
                elif choice == 4:
                    vendor = input("Enter vendor name: ")
                    query = "update product set vendor='%s' where prodid=%d"
                    cursor.execute(query % (vendor, prodid))
                    conn.commit()
                    print("Updated vendor name successfully..")
                elif choice == 5:
                    city = input("Enter City Name: ")
                    query = "Update product set city='%s' where prodid=%d"
                    cursor.execute(query % (city, prodid))
                    conn.commit()
                    print("Updated city name successfully..")
                elif choice == 6:
                    print("Your all updates saved successfully")
                    sys.exit()
                else:
                    print("Invalid input.. Please try again..")

                option = input("Do you want to continue update product data? (yes|no)")
                if option.lower() in ["no", "n"]:
                    break
                else:
                    continue

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def remove_prdoduct(self):
        try:
            prodid = int(input("Enter which product you want to delete? "))
            conn = dbconnection.get_connection()
            cursor = conn.cursor()
            query = "delete from product where prodid=%d"
            cursor.execute(query % (prodid))

        except pymysql.DatabaseError as e:
            if conn:
                conn.rollback()
            print("There was an error while deleting data", e)
        else:
            confirm = input("Do you want to delete this (y|n): ")
            sql = "delete  from product where prodid=%d"
            if confirm.lower() == 'y':
                cursor.execute(sql % (prodid))
                conn.commit()
                print("Deleted successfully..")
            elif confirm.lower() == 'n':
                return
                # sys.exit()
            else:
                print("Invalid input..")

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def max_product_price(self):
        try:
            conn = dbconnection.get_connection()
            cursor = conn.cursor()

            query = "select prodid,prodname,prodqty,max(price),city from product"
            cursor.execute(query)
            return cursor.fetchone()
        except pymysql.DatabaseError as e:
            if conn:
                conn.rollback()
            print("There was error while displaying max price..", e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def min_product_price(self):
        try:
            conn = dbconnection.get_connection()
            cursor = conn.cursor()
            query = "select prodid,prodname,prodqty,min(price),city from product"
            cursor.execute(query)
            return cursor.fetchone()
        except pymysql.DatabaseError as e:
            if conn:
                conn.rollback()
            print("There was an error while displaying min price", e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def display_vendors(self,vname):
        try:
            conn=dbconnection.get_connection()
            cursor=conn.cursor()
            query="select * from product where vendor='%s'"
            cursor.execute(query %(vname))
            vendordata=cursor.fetchall()

            print("Following are the",vname,"products")
            print("ID\t\tName\t\t\tQty\t\t\tPrice\t\t\tVendor\t\tCity")
            for data in vendordata:
                print(data[0], "\t\t", data[1], "\t\t", data[2], "\t\t", data[3], "\t\t", data[4], "\t\t", data[5])
        except pymysql.DatabaseError as e:
            if conn:
                conn.rollback()
            print("There was an error while fetching data",e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

