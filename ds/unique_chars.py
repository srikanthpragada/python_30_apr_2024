
names = ["java", "python", "c#", "sql", "javascript"]

chars = set()

for n in names:
    chars = chars | set(n)

print(chars)
