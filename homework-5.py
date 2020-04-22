revenue = float(input("Введите выручку фирмы: "))
costs = float(input("Введите издержки фирмы: "))
if revenue > costs:
    print("У вас прибыль")
    profit = (revenue - costs)
    print("Ваша рентабельность {}".format(profit / revenue))
    n = int(input("Численность сотрудников фирмы: "))
    print("Прибыль на одного сотрудника {}".format(profit / n))
elif revenue < costs:
    print("У вас убыток")