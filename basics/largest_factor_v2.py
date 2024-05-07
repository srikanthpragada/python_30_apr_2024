n = 29

found = False 
for i in range( n//2, 1, -1):
    if n % i == 0:
        print(i)
        found = True 
        break 



if not found:
    print(n)