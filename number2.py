# Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass_asphalt(self, mass_asphalt_1km, road_thickness_cm):
        self.road_thickness_cm = road_thickness_cm
        self.mass_asphalt_1km = mass_asphalt_1km
        print(self._length * self._width * mass_asphalt_1km * road_thickness_cm)


r = Road(5000, 20)
r.mass_asphalt(25, 5)
