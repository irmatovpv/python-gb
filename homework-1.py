def func(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

print(func(5, 2))
print(func(5, 0))


