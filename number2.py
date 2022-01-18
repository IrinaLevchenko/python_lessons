class Clothes:
    def __init__(self, name):
        self.name = name
        self.total = []

    @property
    def total_fabric(self):
        self.total.append(Coat.fabric_consumption(coat))
        self.total.append(Costume.fabric_consumption(costume))
        total = sum(map(int, self.total))
        return f'Total fabric consumption: {total}'


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    def fabric_consumption(self):
        return self.size / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, height):
        self.height = height

    def fabric_consumption(self):
        return 2 * self.height + 0.3


clothes = Clothes('Outside clothes')
print(clothes.name)

coat = Coat(18)
print(f'Coat fabric consumption: {coat.fabric_consumption()}')

costume = Costume(185)
print(f'Costume fabric consumption: {costume.fabric_consumption()}')

print(clothes.total_fabric)
