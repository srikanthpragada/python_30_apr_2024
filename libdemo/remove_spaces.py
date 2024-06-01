
import re

with  open(r"libdemo\text.txt", "rt") as f:
    contents = f.read() 
    newcontents = re.sub(' +', ' ', contents)
    newcontents = re.sub(r'\n+', '\n', newcontents)

with  open(r"libdemo\text.txt", "wt") as f:
    f.write(newcontents)

