x = 2
y = -7

def my_func(x, y):
    result = 1
    for i in range(-y):
        result /= x
    return result

print(my_func(x, y))
print(x**y)