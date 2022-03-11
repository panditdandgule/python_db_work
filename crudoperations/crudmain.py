from crudoperations.create import Create
from crudoperations.read import Read
from crudoperations.update import Update
from crudoperations.delete import Delete


if __name__=='__main__':
    createObj=Create()
    readObj =  Read()
    updateObj = Update()
    deleteObj = Delete()
    while True:
        print("Available options:\n1.Create\n2.Read\n3.Update\n4.Delete\n")
        choice=int(input("Choose your option: "))
        if choice == 1:
            createObj.create_data()
        elif choice == 2:
            print(readObj.read_data())
        elif choice == 3:
            updateObj.update_data()
            pass
        elif choice == 4:
            deleteObj.delete_data()
            pass
        else:
            print('Wrong choice, You are going exist.')
        ch=input("Do you want to continue(y|n")

        if ch.lower() in ['no','n']:
            break