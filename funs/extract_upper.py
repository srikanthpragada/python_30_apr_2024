def extract_upper(st):
    us = ''
    for c in st:
        if c.isupper():
             us += c 

    return us 

def extract_upper2(st):
     return "".join(filter(str.isupper, st))


names = ['Java', 'C++', "SQL", "PYthon"]

for n in map(extract_upper2, names):
    print(n)




