# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# 31    32         3    5    32        3    5    8    3
# 37    43         2    4    6         8    3    7    1
# 51    86        -1   64   -8
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения
# двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
# первым элементом первой строки второй матрицы и т.д.

# моё решение:
# class Matrix:
#     def __init__(self, list_1, list_2):
#         self.list_1 = list_1  # [[2, -3, 1], [5, 4, -2]]
#         self.list_2 = list_2  # [[4, 2, -5], [-4, 1, 3]]
#
#     def __str__(self):
#         return '\n'.join(['\t'.join([str(j) for j in i]) for i in matrix_result])
#
#     def __add__(self):
#         matrix_new = [[0, 0, 0],
#                       [0, 0, 0]]  # [[6, -1, -4], [1, 5, 1]]
#         for i in range(len(self.list_1)):
#             for j in range(len(self.list_2[i])):
#                 matrix_new[i][j] = self.list_1[i][j] + self.list_2[i][j]
#         return '\n'.join(['\t'.join([str(j) for j in i]) for i in matrix_new])
#                        # [столбец...[...это строки....].................столбец]
#
#
# my_matrix = Matrix([[2, -3, 1], [5, 4, -2]], [[4, 2, -5], [-4, 1, 3]])
# print(my_matrix.__add__())

# решение преподавателя:
from typing import Union, List

a = [[5, 3, 1, 6], [4, 4, 4, 5], [9, 0, 5, 0]]
b = [[1, 1, 1, 2], [2, 2, 2, 2], [3, 3, 3, 1]]


class Matrix:

    def __init__(self, lists: List[Union[list, str]]):
        self.lists = lists

    def __str__(self):
        return '\n'.join(map(str, self.lists))

    def __add__(self, other):
        c = []
        for i in range(len(self.lists)):
            c.append([])
            for j in range(len(self.lists[0])):
                c[i].append(self.lists[i][j] + other.lists[i][j])
            return '\n'.join(map(str, c))


matrix1 = Matrix(a)
matrix2 = Matrix(b)

print(matrix1, '\n')
print(matrix2, '\n')
print(matrix1 + matrix2)
