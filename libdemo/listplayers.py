
from datetime import *

f = open(r"libdemo\players.txt", "rt")

players = {}

for line in f.readlines():
    parts = line.strip().split(',')
    if len(parts) < 2:
        continue

    name = parts[0]
    try:
        dob = datetime.strptime(parts[1], '%d-%m-%Y')
    except:
        continue

    players[name] = (datetime.today() - dob).days // 365


for name, age in sorted(players.items(), key=lambda p: p[1], reverse=True):
    print(f"{name:15} {age:2}")
