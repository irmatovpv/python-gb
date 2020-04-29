def int_func(string: str):
    return string.capitalize()

user_input = input("Введите строку. ")

lst = user_input.split(" ")

print(' '.join(map(int_func, lst)))