
nums = []

while True:
    num = int(input("Enter number [0 to stop] :"))
    if num == 0:
        break
    nums.append(num)

nums.sort()

for n in nums:
    print(n, end=' ')
