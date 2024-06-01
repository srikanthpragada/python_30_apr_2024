import re

with open(r"libdemo\trump.txt", "rt") as f:
    contents = f.read()

words = re.findall(r'\w+', contents)

wordcount = []
for w in set(words):
    wordcount.append((w, words.count(w)))


for word, count in sorted(wordcount):
    print(f"{word:10} {count:2}")
