my_list = [1, '1', (1, 2), {'1':1}, [1], {1}, False, b'123']

for item in my_list:
    if (type(item) == int):
        print(item, "целое")
    if (type(item) == str):
        print(item, "строка")
    if (type(item) == tuple):
        print(item, "кортеж")
    if (type(item) == dict):
        print(item, "словарь")
    if (type(item) == list):
        print(item, "список")
    if (type(item) == set):
        print(item, "множество")
    if (type(item) == bool):
        print(item, "bool")
    if (type(item) == bytes):
        print(item, "bytes")
