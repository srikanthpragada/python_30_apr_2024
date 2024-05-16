def set_zero(n):
    print(id(n))
    n = 0
    print(id(n))


a = 10
print(id(a))
set_zero(a)
print(a)
