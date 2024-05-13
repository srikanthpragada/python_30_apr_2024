st = "java and javascript are awesome. java is bigger than javascript"

word_freq = {}
words = st.split(" ")

for w in set(words):
   word_freq[w] = words.count(w)


print(word_freq)   
