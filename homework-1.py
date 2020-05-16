with open("out.txt", "w") as out:
    while True:
        string = input()
        if not string:
            break
        # out.write(string)
        print(string, file=out)