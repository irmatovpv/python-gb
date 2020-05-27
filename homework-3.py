class WrongType(Exception):
    pass

class MyList:
    def __init__(self):
        self.__list = []
    def append(self, el):
        try:
            el = float(el)
            self.__list.append(el)
        except ValueError:
            raise WrongType

    def print(self):
        print(self.__list)

lst = MyList()
more = True
while more:
    el = input("Введите новый элемент: ")
    if el == "stop":
        lst.print()
        break
    try:
        lst.append(el)
    except WrongType:
        print("Элементом может быть только число")