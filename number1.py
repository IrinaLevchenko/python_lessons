# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

# моё решение:
class Data:
    list = []

    def __init__(self, day_month_year):
        self.day_month_year = day_month_year

    @classmethod
    def str_to_int(cls, day_month_year):
        Data.list = [int(el) for el in day_month_year.split('-')]
        return f'День:{Data.list[0]:02}, месяц:{Data.list[1]:02}, год:{Data.list[2]}.'

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

# решение преподавателя:
# class Date:
#     date = None
#     day = None
#     month = None
#     year = None
#
#     def __init__(self, date):
#         self.__class__.date = date
#
#     def __str__(self):
#         return self.date
#
#     @classmethod
#     def to_int(cls):
#         date = [int(s) for s in cls.date.split('-')]
#         cls.day = date[0]
#         cls.month = date[1]
#         cls.year = date[2]
#         print(cls.day, cls.month, cls.year)
#
#     @staticmethod
#     def validate(d):
#         if d.month > 12 or d.month < 1:
#             raise Exception("Месяц должен быть от 1 до 12")
#
#
# d = Date("1-15-2022")
# d.to_int()
# Date.validate(d)