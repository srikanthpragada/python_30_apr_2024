# Print biggest of 3 numbers

n1 = int(input("Enter number :"))
n2 = int(input("Enter number :"))
n3 = int(input("Enter number :"))

if n1 > n2 and n1 > n3:
    print(n1)
elif n2 > n3:
    print(n2)
else:
    print(n3)

