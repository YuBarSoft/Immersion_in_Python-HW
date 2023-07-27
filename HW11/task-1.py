# Создайте класс Матрица. Добавьте методы для: вывода на печать, сравнения, сложения, *умножения матриц

class Matrix():
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

    def __eq__(self, other):

        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            return False
        else:
            return True

    def __add__(self, other):
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise ValueError('Матрицы должны быть одного размера')

        result_data = []
        for i in range(len(self.data)):
            row = [self.data[i][j] + other.data[i][j] for j in range(len(self.data[0]))]
            result_data.append(row)

        return Matrix(result_data)

    def __mul__(self, other):
        if len(self.data[0]) != len(other.data):
            raise ValueError('Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы')

        result_data = []
        for i in range(len(self.data)):
            row = []
            for j in range(len(other.data[0])):
                element = sum(self.data[i][k] * other.data[k][j] for k in range(len(self.data[0])))
                row.append(element)
            result_data.append(row)

        return Matrix(result_data)

matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = Matrix([[4, 2, 6], [2, 4, 7], [8, 5, 1]])
matrix3 = Matrix([[2, 1, 6], [3, 4, 5], [4, 6, 2], [3, 5, 7]])

result_add = matrix1 + matrix2
print("Сложение матриц:")
print(result_add)

result_mul = matrix1 * matrix2
print("Умножение матриц:")
print(result_mul)

print('матрица 1:')
print(matrix1)
print('матрица 2:')
print(matrix2)
print(matrix1 == matrix2)
print(matrix3 == matrix2)

