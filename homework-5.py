my_list = [7, 5, 3, 3, 2]
number = int(input("Введите целое число: "))
n = len(my_list)
for i in range(n + 1):
    try:
        if my_list[i] < number:
            my_list.insert(i, number)
            break
    except IndexError:
        my_list.append(number)
        break



print(my_list)