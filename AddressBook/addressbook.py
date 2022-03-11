class AddressBook:

    def __init__(self,firstname,lastname,age,email,phone):
        self.firstname=firstname
        self.lastname=lastname
        self.age=age
        self.email=email
        self.phone=phone

    def __str__(self):
        return f'firstname {0} lastname {1} age {2} email {3} phone {4}'.format(self.firstname,self.lastname,self.age,self.email,self.phone)

    def createtdata(self):
        firstname=input("Enter your firstname: ")
        lastname=input("Enter your lastname: ")
        age=int(input("Enter your age: "))
        email=input("Enter your valid email:")
        phone=input("Enter your phone number: ")

    def insertdata(self):
        try:
            file=open('contact.txt','w')
            self.createtdata()
            file.write(self.firstname)
            file.write(self.lastname)
            file.write(self.age)
            file.write(self.email)
            file.write(self.phone)
        except:
            print("Something went wrong")
        else:
            print("Data added successfully")
        finally:
            file.close()



if __name__=='__main__':
    obj=AddressBook('Pandit','Dandgule',30,'pdandgule@gmail.com',9623639868)
    print(obj.insertdata())