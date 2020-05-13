from sys import argv

script_name, worked, rate, extra = argv
worked, rate, extra  = float(worked), float(rate), float(extra)
print("Выработка в часах: ", worked)
print("Cтавка в час: ", rate)
print("Премия: ", extra)
print("Зарплата: ", worked * rate + extra)
