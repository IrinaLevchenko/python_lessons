import json

profit = {}   # фирма:прибыль
dict_average_profit = {}  # средняя прибыль:значение
prof = 0
i = 0
with open('file_task_7.txt', 'r') as f:
    for line in f:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            profit_of_all_firms = prof + profit.setdefault(name)
            i += 1
    for key, value in profit.items():
        print(key, ':', value)
    if i != 0:
        profit_average = profit_of_all_firms / i
        print(f'Прибыль средняя - {profit_average:.2f}')
    else:
        print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
    dict_average_profit = {'average profit': round(profit_average)}

list = [profit, dict_average_profit]
print(list)

with open('list_task_7.json', 'w') as file:
    json_list = json.dump(list, file)
