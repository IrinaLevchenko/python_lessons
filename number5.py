class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки, инструмент: {self.title}.')

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'{self.title}. Подберите цвет стержня! Запуск отрисовки.')

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'{self.title} имеет разную ширину грифеля, подберите нужную! Запуск отрисовки.')

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'{self.title} может просвечивать тескт (или нет), обратите внимание! Запуск отрисовки.')

pen = Pen('Gelpen')
pen.draw()
pencil = Pencil('Hardpencil')
pencil.draw()
marker = Handle('Highlighter')
marker.draw()