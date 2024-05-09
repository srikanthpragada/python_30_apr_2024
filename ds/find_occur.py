fs = "how do you do"
ss = "did"

pos = -1

while True:
  pos = fs.find(ss, pos + 1)
  if pos == -1:
    break 
  else:
    print(pos)
