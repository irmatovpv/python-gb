from itertools import cycle
input_list = [1, 2, 3]

c = 0
for el in cycle(input_list):
    if c > 10:
        break
    print(el)
    c += 1