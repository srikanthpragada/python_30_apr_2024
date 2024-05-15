nums = [10, 11, 23, -34, 55, -66]

for n in map(abs, nums):
    print(n)


for n in map (len,['abc','xy', 'p']):
    print(n)    


def removespaces(s):
    return s.replace(' ', '')

for n in map (removespaces,['Java 22','Python 3.12', 'C# 12']):
    print(n)   