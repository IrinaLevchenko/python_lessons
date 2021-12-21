# months_list = [[12, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
# month_number = int(input('Введите номер месяца:'))
# if month_number in months[0]:
#     print('winter')
# elif month_number in months[1]:
#     print('spring')
# elif month_number in months[2]:
#     print('summer')
# elif month_number in months[3]:
#     print('autumn')

seasons_dict = {1: 'winter', 2: 'winter', 3: 'spring', 4: 'spring',
                5: 'spring', 6: 'summer', 7: 'summer', 8: 'summer',
                9: 'autumn', 10: 'autumn', 11: 'autumn', 12: 'winter'}
month_number = int(input('Введите номер месяца:'))
key = month_number
if key in seasons_dict.keys():
    print(seasons_dict.get(key))
