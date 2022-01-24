#  Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw.
# Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки, инструмент: {self.title}.')


class Pen(Stationery):
     def draw(self):
        print(f'{self.title}. Подберите цвет стержня! Запуск отрисовки.')


class Pencil(Stationery):
    def draw(self):
        print(f'{self.title} имеет разную ширину грифеля, подберите нужную! Запуск отрисовки.')


class Handle(Stationery):
     def draw(self):
        print(f'{self.title} может просвечивать тескт (или нет), обратите внимание! Запуск отрисовки.')


pen = Pen('Gelpen')
pen.draw()
pencil = Pencil('Hardpencil')
pencil.draw()
marker = Handle('Highlighter')
marker.draw()
