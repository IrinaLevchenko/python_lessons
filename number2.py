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
