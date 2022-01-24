class Data:
    list = []

    def __init__(self, day_month_year):
        self.day_month_year = day_month_year

    @classmethod
    def str_to_int(cls, day_month_year):
        Data.list = [int(el) for el in day_month_year.split('-')]
        return f'Число:{Data.list[0]:02}, месяц:{Data.list[1]:02}, год:{Data.list[2]}.'

    @staticmethod
    def validate_data(day_month_year):
        try:
            Data.str_to_int(day_month_year)
            if 1 <= Data.list[0] <= 31 and 1 <= Data.list[1] <= 12 and 0 < Data.list[2]:
                return f'{Data.list[0]:02}.{Data.list[1]:02}.{Data.list[2]:04}г.'
            else:
                return 'Таких чисел даты не бывает!'
        except ValueError:
            return 'Дату вводят в цифрах!'


print(Data.str_to_int('21-13-2022'))
print(Data.validate_data('21-13-2022'))
print(Data.validate_data('21-1k-2022'))
print(Data.validate_data('1-1-1'))
