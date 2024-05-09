
squares = []

for n in range(1, 11):
    squares.append(n * n)

print(squares)

# List Comprehension 
squares = [n * n for n in range(1,11) if n % 2 == 0]
print(squares)

