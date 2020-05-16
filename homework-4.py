with open("h4.txt", "r") as file:
    with open("h4-out.txt", "w") as out:
        for line in file:
            out_line = line.replace("One", "Один")
            out_line = out_line.replace("Two", "Два")
            out_line = out_line.replace("Three", "Три")
            out_line = out_line.replace("Four", "Четыре")
            out.write(out_line)
