class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} поехала!')

    def stop(self):
        print(f'Машина {self.name} остановилась!')

    def turn(self, direction):
        self.direction = direction
        print(f'Машина {self.name} повернула {direction}!')

    def show_speed(self, current_speed):
        self.current_speed = current_speed
        print(f'Машина {self.name} едет со скоростью {current_speed}км/ч.')

    def show_attributes(self):
        print(f'Машина {self.name}: скорость {self.speed}, цвет {self.color}, ментовская?{self.is_police}')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self, current_speed):
        self.current_speed = current_speed
        if current_speed > 60:
            print(f'{self.name} едет с превышением скорости! Не выше 60 км/ч!')
        else:
            print(f'Машина {self.name} едет со скоростью {current_speed}км/ч.')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self, current_speed):
        self.current_speed = current_speed
        if current_speed > 40:
            print(f'{self.name} едет с превышением скорости! Не выше 40 км/ч!')
        else:
            print(f'Машина {self.name} едет со скоростью {current_speed}км/ч.')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


ford = Car(230, 'white', 'ford c-max', False)
toyota = TownCar(180, 'blue', 'toyota camry', False)
mustang = SportCar(310, 'red', 'ford mustang', False)
vw = WorkCar(230, 'black', 'vw polo', False)
uaz = PoliceCar(30, 'уродский', 'бобик', True)

ford.turn('налево')
mustang.go()
uaz.stop()
vw.show_speed(50)
toyota.show_speed(80)
mustang.show_speed(300)
uaz.show_attributes()
print(ford.name)
