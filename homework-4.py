string = input('Введите вашу строку: ')
words = [l.strip() for l in string.split(" ")]
i = 1
for word in words:
    print(i, word[0:10])
    i += 1
