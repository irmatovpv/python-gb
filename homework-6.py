from collections import defaultdict

goods = []
def insert(goods, obj):
        goods.append((len(goods) + 1, obj))


next = True
while(next):
    name = input("Ввидите название: ")
    price = input("Ввидите цена: ")
    amount = input("Ввидите колличество: ")
    unit = input("Ввидите единицы измерения: ")
    insert(goods, {
        'название': name,
        'цена': int(price),
        'количество': int(amount),
        'eд': unit,
    })
    stop = input("Остановится(Y)? ")
    if stop == 'Y':
        next = False

stat = defaultdict(list)
for item in goods:
    for name, value in item[1].items():
        stat[name].append(value)

for name, values in stat.items():
    stat[name] = list(set(values))

print(stat)

