# Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

# моё решение:
# poor_workers = []
# summary_income = 0
# number_of_workers = 0
#
# with open('file_task_3.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         if int((line.split(':'))[1]) <= 20000:
#             poor_workers.append((line.split(':'))[0])
#         summary_income += int((line.split(':'))[1])
#         number_of_workers += 1
#     average_income = summary_income / number_of_workers
#
# print(f"Доход ниже 20 000руб у сотрудников: {', '.join(poor_workers)}")
# print(f"Средний доход сотрудника фирмы: {average_income}")

# решение преподавателя:
with open('file_task_3.txt', 'r', encoding='utf-8') as f:
    employees_dict = {line.split()[0]: float(line.split()[1]) for line in f}
    print(f'Average salary = {round(sum(employees_dict.values()) / len(employees_dict), 3)}\n'
          f'Employees with salary less than 20k {[e[0] for e in employees_dict.items() if e[1] < 20000]}')
# TODO код не работает! разобраться!