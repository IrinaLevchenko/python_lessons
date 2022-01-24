class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        return f'z_1 + z_2 = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        return f'z_1 * z_2 = {self.a * other.a - self.b * other.b} + {self.a * other.b + self.b * other.a} * i'


z_1 = ComplexNumber(1, 2)
z_2 = ComplexNumber(3, 4)

print(z_1 + z_2)
print(z_1 * z_2)


