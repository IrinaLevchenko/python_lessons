# Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и
# передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру (например, словарь).

class Storage:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.equip_info = {}
        self.send_away_equip_info = {}

    def __str__(self):
        return f'Склад {self.name}, адрес {self.address}.'

    def add_to_storage(self, other):
        number_of_product = int(input(f'Введите количество товара {other.name}: '))
        self.equip_info.setdefault(other.name, number_of_product)
        print(f'На склад {self.name} получено оборудование: {other.name} серия {other.serial_number},'
              f' количество {number_of_product}шт.\n'
              f'Всего принято на склад: {self.equip_info}')

    def transfer_to_department(self, other):
        number_of_product = int(input(f'Введите количество товара {other.name}: '))
        self.send_away_equip_info.setdefault(other.name, number_of_product)
        print(f'Со склада {self.name} отправлено оборудование {other.name} серия {other.serial_number}.\n' \
              f'Всего будет перемещено: {self.send_away_equip_info}')


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
print('*' * 100)

Storage.add_to_storage(storage, printer)
Storage.add_to_storage(storage, scanner)
Storage.add_to_storage(storage, copier)
print('*' * 100)

Storage.transfer_to_department(storage, printer)
Storage.transfer_to_department(storage, scanner)
Storage.transfer_to_department(storage, copier)
print('*' * 100)