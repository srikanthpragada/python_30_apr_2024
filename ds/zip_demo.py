l1 = [1, 2, 3, 4]
l2 = ['abc', 'xyz', 'pqr']


for t in zip(l1, l2, strict=True):
    print(t)

