def sum_number(user_input):
    numbers = user_input.split(" ")
    sum = 0
    for num in numbers:
        try:
            num = float(num)
        except ValueError:
            break
        sum += num
    return sum

next = True
sum = 0
while next:
    user_input = input("Введите числа разделенные пробелами. Введите симов  'E' чтобы закочить. ")
    if 'E' in user_input:
        next = False
    sum += sum_number(user_input)
    print(f'Cумма чисел: {sum}')
