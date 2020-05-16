from statistics import mean

out_dict = {}
with open("h7.txt", "r") as inp:
    firms = {}
    for line in inp:
        name, form, revenue, loss = line.split(" ")
        name = name.strip()
        revenue = float(revenue.strip())
        loss = float(loss.strip())
        firms[name] = revenue - loss
print([firms, {'average_profit': mean([value for name, value in firms.items() if value > 0])}])