
f = open(r"libdemo\depts.txt", "rt")

depts = {}

for line in f.readlines():
    parts = line.strip().split(",")
    depts[int(parts[0])] = parts[1:]

f.close()

for id, employees in sorted(depts.items()):
    empstring = ",".join(sorted(employees))
    print(f"{id:5} {empstring}")
    

    