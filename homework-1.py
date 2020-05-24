from typing import List


class Matrix:
    def __init__(self, matrix: List[List[int]]):
        self._matrix = matrix

    def __str__(self):
        result = ""
        for row in self._matrix:
            result += " ".join(list(map(str, row)))
            result += "\n"
        return result

    def __add__(self, other: "Matrix"):
        assert len(self._matrix) == len(other._matrix)

        matrix = []
        for i in range(len(self._matrix)):
            row = []
            for j in range(len(self._matrix[i])):
                row.append(self._matrix[i][j] + other._matrix[i][j])
            matrix.append(row)
        return Matrix(matrix)

m1 = Matrix([[1,2],[3,4]])
m2 = Matrix([[4,3],[2,1]])
m3 = m1 + m2

print(m1)
print(m2)
print(m3)
