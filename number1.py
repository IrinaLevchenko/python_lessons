# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv


def salary_worker():
    try:
        salary = (int(work_hours) * int(rate_in_hours)) + float(award)
        print(f'Ваша зарплата: {salary}руб')
    except ValueError:
        print('Введите числа, а не буквы!')


file_name, work_hours, rate_in_hours, award = argv
salary_worker()
