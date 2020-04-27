year = {
    'зима': [12, 1, 2],
    'весна': [3, 4, 5],
    'лето': [6, 7, 8],
    'осень': [9, 10, 11]
}
number = int(input('Введить номер месяца: '))

for name, numbers in year.items():
    if number in numbers:
        print(f'Время года {name}')
        break