class Cell:
    def __init__(self, cells_number):
        self.cells_number = int(cells_number)

    def __add__(self, other):
        return Cell(self.cells_number + other.cells_number)

    def __sub__(self, other):
        if (self.cells_number - other.cells_number) > 0:
            return Cell(self.cells_number - other.cells_number)
        else:
            return f'Вычитание невозможно!'

    def __mul__(self, other):
        return Cell(self.cells_number * other.cells_number)

    def __truediv__(self, other):
        return Cell(round(self.cells_number / other.cells_number))

    def __str__(self):
        return f'Ячеек в клетке: {self.cells_number}'

    def make_order(self, cells_in_row):
        row = ''
        for _ in range(self.cells_number // cells_in_row):
            row += f'{"*" * cells_in_row}\\n'
        row += f'{"*" * (self.cells_number % cells_in_row)}'
        return row


c_1 = Cell(16)
c_2 = Cell(6)
print(c_1 + c_2)
print(c_1 - c_2)
print(c_1 * c_2)
print(c_1 / c_2)
print(c_1.make_order(5))
