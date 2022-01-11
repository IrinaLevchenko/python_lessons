#  Пользователь вводит месяц в виде целого числа от 1 до 12.
#  Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
#  Напишите решения через list и через dict.

while True:
    month_number = input('Введите номер месяца:')
    if month_number.isdigit() and 0 < int(month_number) <= 12:
        seasons_dict = {0: 'winter', 1: 'spring', 2:'summer', 3: 'autumn', 4: 'winter'}
        seasons_list = ['зима', 'весна', 'лето', 'осень', 'зима']
        print(f'Из списка сезонов: {seasons_list[int(month_number) // 3]}\n'
              f'Из словаря сезонов: {seasons_dict[int(month_number) // 3]}')
        break
    else:
        print('Ошибка ввода!')
