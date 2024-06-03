
import re

pwd = input("Enter password :")

if len(pwd) < 8:
    print("Invalid Password. Must be 8 or more chars!")
    exit()

# Uppercase 
if re.search("[A-Z]", pwd) is None:
    print("Invalid Password. Missing Uppercase!")
    exit()

# Special Char 
if re.search("[@#_$]", pwd) is None:
    print("Invalid Password. Missing Special char!")
    exit()    

# Digit 
if re.search("[0-9]", pwd) is None:
    print("Invalid Password. Missing digit!")
    exit()    

print("Valid Password!")