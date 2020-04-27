list = input("Введите список через запятую ")
list = [l.strip() for l in list.split(",")]
for i in range(0, len(list) - 1, 2):
    list[i], list[i + 1] = list[i + 1], list[i]

print(list)