names = ['Java', 'Python', 'SQL', 'JavaScript', 'C#']

f = open("names.txt", "wt")

for name in names:
    f.write(name + "\n")

f.close() 

