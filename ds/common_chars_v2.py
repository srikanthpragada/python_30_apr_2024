
s1 = "abcddead"
s2 = "xyzdef"

chars = []
for c in s1:
    if c in s2 and c not in chars:
        print(c)
        chars.append(c)

