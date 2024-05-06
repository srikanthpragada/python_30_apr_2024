n = 29

for i in range( n//2, 1, -1):
    if n % i == 0:
        print(i)
        break 
else:
    print(n)

