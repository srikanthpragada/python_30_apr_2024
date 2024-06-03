
import re

f = open(r"libdemo\customers.txt", "rt")
customers = {}

for line in f.readlines():
    # look for name 
    match = re.search('[a-zA-Z ]+', line)
    if match is None:
        continue 

    name = match.group().strip() 

    # look for mobile number
    match = re.search('[0-9]+', line)
    if match is None:
        continue 

    mobile = match.group()
    customers[name] = mobile 


f.close() 

for name, mobile in sorted(customers.items()):
    print(f"{name:15}  {mobile}")