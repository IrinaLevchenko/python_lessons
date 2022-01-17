class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1  # [[2, -3, 1], [5, 4, -2]]
        self.list_2 = list_2  # [[4, 2, -5], [-4, 1, 3]]

    def __str__(self):
        return '\n'.join(['\t'.join([str(j) for j in i]) for i in matrix_result])

    def __add__(self):
        matrix_new = [[0, 0, 0],
                         [0, 0, 0]]  # [[6, -1, -4], [1, 5, 1]]
        for i in range(len(self.list_1)):
            for j in range(len(self.list_2[i])):
                matrix_new[i][j] = self.list_1[i][j] + self.list_2[i][j]
        return '\n'.join(['\t'.join([str(j) for j in i]) for i in matrix_new])
                       # [столбец...[...это строки....].................столбец]


my_matrix = Matrix([[2, -3, 1], [5, 4, -2]], [[4, 2, -5], [-4, 1, 3]])
print(my_matrix.__add__())
