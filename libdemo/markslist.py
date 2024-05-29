def isName(st):
    for c in st:
        if not (c.isalpha() or c.isspace()):
            return False
        
    return True 



f = open(r"libdemo\marks.txt", "rt")

for line in f.readlines():
    parts = line.strip().split(",")
    if len(parts) < 2:
        continue 

    name = parts[0]
    if not isName(name):
        continue 

    marks_filter = filter(str.isdigit, parts[1:])
    marks_list = list(map(int, marks_filter))
    if len(marks_list) == 0:
        continue 

    total = sum(marks_list)
    print(f"{name:20}  {total:3}  {total/len(marks_list):5.2f}")


f.close()