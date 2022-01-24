#  Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

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

    def show_speed(self):
        print(f'Машина {self.name} едет со скоростью {self.speed}км/ч.')

    def show_attributes(self):
        print(f'Машина {self.name}: скорость {self.speed}, цвет {self.color}, ментовская?{self.is_police}')


class TownCar(Car):
    def show_speed(self):
        if self.speed >= 60:
            print(f'{self.name} едет с превышением скорости! Не выше 60 км/ч!')
        else:
            print(f'Машина {self.name} едет со скоростью {self.speed}км/ч.')


class SportCar(Car):
    """Спортивый автомобиль"""


class WorkCar(Car):
    def show_speed(self):
        if self.speed >= 40:
            print(f'Машина {self.name} едет со скоростью {self.speed}км/ч.')
        else:
            print(f'{self.name} едет с превышением скорости! Не выше 40 км/ч!')


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
vw.show_speed()
toyota.show_speed()
mustang.show_speed()
uaz.show_attributes()
print(ford.name)
