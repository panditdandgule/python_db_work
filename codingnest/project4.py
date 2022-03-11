import re


class PasswordVal:
    def __str__(self):
        return '''Only alphanumeric inputs are accepted in the password field.
                  It should start with the uppercase alphabet.
                  At Least one uppercase alphabet password.
                  The password should be of a specific length.
                  One numeric value must be used in the password.'''

    def validation(self,):
        while True:
            user = input("Enter valid password :")
            if len(user)<8:
                print("Password length should be 8 chars")

            elif user.islower():
                print("At lease one upper case letter")
            elif user.isupper():
                print("Atleast one lowercase letter")
            elif user.isdigit():
                print("you should enter char also")
            elif user.isalnum():
                print("At lease one numeric")
            elif user.isalpha():
                print("One numeric should be used")
            else:
                print("Valid password")
                break



obj = PasswordVal()
print(obj.__str__())
obj.validation()
