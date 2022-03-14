import sys

from prodimpl import ProductServiceImpl,Product

def take_user_inputs():
    try:
        prodId=int(input("Enter Product Id: "))
        prodName=input("Enter Product Name: ")
        prodQty=int(input("Enter Product Quantity: "))
        prodPrice=float(input("Enter Product Price: "))
        prodVendor=input("Enter Product Vendor Name: ")
        city=input("Enter City Name: ")
        return Product(prodId,prodName,prodQty,prodPrice,prodVendor,city)

    except ValueError:
        print("Please enter valid input..")


if __name__=='__main__':
    prod=ProductServiceImpl()

    while True:
        print("Enter Choice 1 Add Product 2 Display Products 3 Search Product 4 Delete Product 5 Update Product 6 Exit")
        option=int(input("Enter Your choice: "))
        if option==1:
            proddetails=take_user_inputs()
            prod.create_product(proddetails)
        elif option==2:
            prod.display_all_products()
        elif option==3:
            prodid = int(input("Enter Product Id which one you want? "))
            prod.search_product(prodid)
        elif option==4:
            prod.remove_prdoduct()
        elif option==5:
            prod.update_product()
        elif option==6:
            print("Thanks for using this application..")
            sys.exit()
        else:
            print("Invalid option..")

        choice=input("Do you want to continue? (yes|no)")
        if choice.lower() in ["no","n"]:
            break
        else:
            continue
