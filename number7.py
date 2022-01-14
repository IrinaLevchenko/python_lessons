# Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

# моё решение:
# import json
#
# profit = {}   # фирма:прибыль
# dict_average_profit = {}  # средняя прибыль:значение
# prof = 0
# i = 0
# with open('file_task_7.txt', 'r') as f:
#     for line in f:
#         name, firm, earning, damage = line.split()
#         profit[name] = int(earning) - int(damage)
#         if profit.setdefault(name) >= 0:
#             profit_of_all_firms = prof + profit.setdefault(name)
#             i += 1
#     for key, value in profit.items():
#         print(key, ':', value)
#     if i != 0:
#         profit_average = profit_of_all_firms / i
#         print(f'Прибыль средняя - {profit_average:.2f}')
#     else:
#         print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
#     dict_average_profit = {'average profit': round(profit_average)}
#
# list = [profit, dict_average_profit]
# print(list)
#
# with open('list_task_7.json', 'w') as file:
#     json_list = json.dump(list, file)

# решение преподавателя:
import json

with open('7.json', 'w') as fw:
    with open('7.txt', encoding='utf-8') as f:
        profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f}
        result = [profit, {'average_profit': round(sum([int(i) for i in profit.values() if int(i) > 0]) /
                                                   len([int(i) for i in profit.values() if int(i) > 0]))}]

    json.dump(result, fw, ensure_ascii=False, indent=4)
