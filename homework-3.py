with open("h3.txt", "r") as file:
    total = 0
    count = 0
    for line in file:
        lastname, salary = line.split(" ")
        salary = float(salary.strip())
        total += salary
        count += 1
        if salary < 20000:
            print(f"{lastname} зарплата меньше 20000")
    print(f"Средняя зарплата {total/count}")