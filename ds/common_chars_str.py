
names = ["abc", "bca", "bbc", "nbc", "abc"]

chars = set(names[0])

for n in names[1:]:
    chars = chars & set(n)

print(chars)
