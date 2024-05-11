st = "java and javascript are awesome"

chars = {}

for c in set(st):
   chars[c] = st.count(c)


for k, v in sorted(chars.items()):
   print(k, v)





    



