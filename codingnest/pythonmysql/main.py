from pythonmysql.dbhelper import DBHelper


def main():
    db=DBHelper()

    while True:
        print("*********WELCOME*******")
        print("PRESS 1 to Insert new user")
        print("PRESS 2 to Display all user")
        print("PRESS 3 to Delete  user")
        print("PRESS 4 to Update user")
        print("PRESS 5 to Exit program")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                id = int(input("Enter user id:"))
                username = input("Enter user name:")
                phone = input("Enter user phone number:")
                db.insert_user(id, username, phone)
            elif choice == 2:
                db.fetch_all()
            elif choice == 3:
                id = int(input("Enter which user you want to delete"))
                db.delete_user(userid=id)
            elif choice == 4:
                id = int(input("Enter user id:"))
                username = input("Enter user name:")
                phone = input("Enter user phone number:")
                db.update_user(id, username, phone)
            elif choice == 5:
                print("Do you want to Exit..")
                print("Please enter YES/NO")
                YES = input()
                if (YES == 'yes'or YES=='YES'):
                    break
                else:
                    continue
            else:
                print("Invalid input! please try again..")

        except Exception as e:
            print("Invalid input.. Please Try again..")
            print(e)

main()