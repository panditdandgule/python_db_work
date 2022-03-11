import re
import unittest

phone=input("Enter phone number: ")

if re.findall("[0-9]{10}",phone):
    print("Valid phone number:",phone)
elif re.findall("[^0-9]",phone):
    print("Phone number is not valid",phone)
elif re.findall("[0-9]{1,9}",phone):
    print("Phone number is short required 10 digit number",phone)
else:
    print("Enter valid number")