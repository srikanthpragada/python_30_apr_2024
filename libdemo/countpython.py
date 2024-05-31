import os

allfiles = os.walk(r"d:\classroom\python")
count  = 0
for (dirname, folders, files)  in allfiles:
    for file in files:
        if file.endswith(".py"):
             print( dirname + "\\" + file)
             count += 1

print(f'Count = {count}')


