def func(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

a = float(input("Введите первое число. "))
b = float(input("Введите второе число число. "))

c = func(a, b)

if c is None:
    print("Деление на 0")
else:
    print(c)


