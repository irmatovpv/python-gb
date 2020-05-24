class Cell:
    def __init__(self, cell_number):
        self.cell_number = cell_number

    def __add__(self, other):
        return Cell(self.cell_number + other.cell_number)

    def __sub__(self, other):
        if self.cell_number <= other.cell_number:
            raise ValueError("Колличество клеток не может быть отрицательно")
        return Cell(self.cell_number - other.cell_number)

    def __mul__(self, other):
        return Cell(self.cell_number * other.cell_number)

    def __truediv__(self, other):
        return Cell(int(self.cell_number / other.cell_number))

    def make_order(self, num):
        rows = self.cell_number // num
        in_last_row = self.cell_number % num
        row = "*" * num
        last_row = "*" * in_last_row
        lines = [row for i in range(rows)]
        lines.append(last_row)

        return "\n\n".join(lines)

c1 = Cell(1)
c2 = Cell(2)
c3 = Cell(3)
c4 = Cell(4)
c5 = Cell(5)

c12 = c1 + c2
c21 = c2 - c1

c34 = c3 * c4
c54 = c5 / c4

print(c12.make_order(5))
print(c21.make_order(5))
print(c34.make_order(5))
print(c54.make_order(5))


c_err = c1 - c2