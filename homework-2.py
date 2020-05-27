class DivisionByZero(Exception):
    pass

class Calculator:
    @classmethod
    def div(cls, a, b):
        if b == 0:
            raise DivisionByZero
        return a/b

a = float(input("Введите числитель "))
b = float(input("Введите знаменатель "))

try:
    print(Calculator.div(a,b))
except DivisionByZero:
    print("Деление на 0")
