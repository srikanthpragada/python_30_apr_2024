def iseven(n):
    return n % 2 == 0


nums = [10, 11, 23, 34, 55, 66]

for n in filter(iseven, nums):
    print(n)


for c in filter(str.isupper, "AbCdEf"):
    print(c)

    
