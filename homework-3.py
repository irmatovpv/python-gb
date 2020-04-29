def my_func(a, b, c):
    return sum(sorted([a, b, c], reverse=True)[:2])

print(my_func(1, 5, 11))
