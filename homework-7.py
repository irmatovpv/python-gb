class ComplexNumber:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __add__(self, other):
        return ComplexNumber(self._x + other._x, self._y + other._y)

    def __mul__(self, other):
        return ComplexNumber(
            self._x * other._x - self._y * other._y,
            self._x*other._y + other._x* self._y
        )
    def __str__(self):
        return f"({self._x} + i*{self._y})"
a = ComplexNumber(1, 2)
b = ComplexNumber(3, 6)
print(a + b)
print(a * b)