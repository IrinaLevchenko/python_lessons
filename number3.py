class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income_byn = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'Full name: {self.name} {self.surname}'

    def get_total_income(self):
        return f'Total income: {sum(self._income_byn.values())}'

p = Position('Ira', 'Lev', 'pharmacist', 900, 800)
print(p.get_full_name())
print(p.position)
print(p.get_total_income())
