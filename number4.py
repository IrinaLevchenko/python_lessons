# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
# уникальные для каждого типа оргтехники.

class Storage:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'Склад {self.name}, адрес {self.address}'


class OfficeEquipment:
    def __init__(self, name, serial_number):
        self.name = name
        self.serial_number = serial_number


class Printer(OfficeEquipment):
    def __init__(self, name, serial_number, print_technology):
        super().__init__(name, serial_number)
        self.print_technology = print_technology

    def __str__(self):
        return f'Принтер: {self.name}, серия: {self.serial_number}, {self.print_technology}'


class Scanner(OfficeEquipment):
    def __init__(self, name, serial_number, scan_resolution):
        super().__init__(name, serial_number)
        self.scan_resolution = scan_resolution

    def __str__(self):
        return f'Сканер: {self.name}, серия: {self.serial_number}, разрешение сканирования {self.scan_resolution}'


class Copier(OfficeEquipment):
    def __init__(self, name, serial_number, scaling):
        super().__init__(name, serial_number)
        self.scaling = scaling

    def __str__(self):
        return f'Ксерокс: {self.name}, серия: {self.serial_number}, максимальное масштабирование {self.scaling}'


storage = Storage('РУП "Фармация"', 'ул. Янки Купалы, 12 г.Брест')
print(storage)
print('*' * 100)

printer = Printer('hp', 'h222301', 'laser printing')
print(printer)
scanner = Scanner('Epson', 's246511', '4800dpi')
print(scanner)
copier = Copier('Xerox', 'f5432131', '400%')
print(copier)
