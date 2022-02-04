#  Реализовать проект расчёта суммарного расхода ткани на производство одежды.
#  Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
#  К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
#  размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

# моё решение (не использовала абстрактные методы):

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

# решение преподавателя:
# from abc import ABC, abstractmethod
#
#
# class Clothes(ABC):
#     def __init__(self, param):
#         self.param = param
#
#     @property
#     @abstractmethod
#     def consumption(self):
#         pass
#
#     def __add__(self, other):
#         return self.consumption + other.consumption
#
#
# class Coat(Clothes):
#     @property
#     def consumption(self):
#         return round(self.param / 6.5) + 0.5
#
#
# class Costume(Clothes):
#     @property
#     def consumption(self):
#         return (2 * self.param + 0.3) / 100
#
#
# coat = Coat(58)
# costume = Costume(240)
# print(coat + costume)
#
