
def print_nums(*nums, even = True):
    for n in nums:
        if even and n % 2 == 0:
            print(n)
        elif not even and n % 2 == 1:
            print(n)


print_nums(10,20,45,33,48 )
print_nums(10,20,45,33,48, even = False)



