import os

def contains(filename, search):
    with open(filename, "rt") as f:
        return search in f.read()
    


allfiles = os.walk(r"d:\classroom\python")
search = input("Enter search string :")
for (dirname, folders, files)  in allfiles:
    for file in files:
        if file.endswith(".py"):
              filename = dirname + "\\" + file
              if contains(filename, search):
                  print(filename)





