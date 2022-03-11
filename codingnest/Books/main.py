from Books.connection import Connection

def main():
    obj=Connection()

    while True:
        print("*********WELCOME*******")
        print("PRESS 1 to Insert new book")
        print("PRESS 2 to Display all books")
        print("PRESS 3 to Delete  book")
        print("PRESS 4 to Update book")
        print("PRESS 5 to Exit program")
        choice=int(input("Enter your choice"))

        if choice==1:
            title=input("Enter book title: ")
            isbn=input("Enter ISBN: ")
            gener=input("Enter book generation: ")
            type=input("Enter book type: ")
            publicationyear=input("Enter publication year: ")
            price=int(input("Enter book price: "))
            obj.insert(title,isbn,gener,type,publicationyear,price)
        else:
            pass







if __name__ == '__main__':
    main()