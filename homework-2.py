with open("h2.txt", "r") as file:
    lines = file.readlines()
    print("Строк в файле", len(lines))
    i = 1
    for line in lines:
        words_count = len(line.split(' '))
        print(f"В строке с номером {i}, ровно {words_count} слов")