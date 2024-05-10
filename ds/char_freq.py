st = "how are you doing"

chars = []
for c in st:
  if c not in chars:
    print(f"{c} - {st.count(c)}")
    chars.append(c)

    



