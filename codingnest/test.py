import re
s=input("Enter mobile number: ")
m=re.fullmatch("(0|91)?[7-9][0-9]{9}",s)
if m!=None:
    print("Valid mobile number")
else:
    print("Not valid mobile number")