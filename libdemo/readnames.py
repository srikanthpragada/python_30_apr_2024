f = open("names.txt", "rt")

for line in sorted(f.readlines()):
    print(line)
    

f.close() 

