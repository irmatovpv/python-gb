from random import random

with open("h5-out.txt", "w") as out:
    for i in range(0, 1000):
        num = int(random() * 1000)
        out.write(str(num))
        out.write(" ")

with open("h5-out.txt", "r") as inp:
    data = inp.read()
    num = map(float, data.strip().split(" "))
    print("Сумма: ", sum(num))