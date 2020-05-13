
def fact(n):
    mul = 1
    for el in range(1, n + 1):
        mul *= el
        yield mul

for el in fact(5):
    print(el)