from sys import argv


def salary_worker():
    try:
        salary = (int(work_hours) * int(rate_in_hours)) + int(award)
        print(f'Ваша зарплата: {salary}руб')
    except ValueError:
        print('Введите числа, а не буквы!')


file_name, work_hours, rate_in_hours, award = argv
salary_worker()
