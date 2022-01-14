class Road:
    _length_m = 20000
    _width_m = 5

    def mass_asphalt(self, mass_asph_1km, road_thickness_cm):
        self.mass_asph_1km = mass_asph_1km
        self.road_thickness_cm = road_thickness_cm
        print(Road._length_m * Road._width_m * mass_asph_1km * road_thickness_cm)


r = Road()
r.mass_asphalt(25, 5)
