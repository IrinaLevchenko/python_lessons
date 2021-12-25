def division():
    var_1 = int(input('Введите числитель:'))
    var_2 = int(input('Введите знаменатель:'))
    if var_2 != 0:
        return var_1 / var_2
    else:
        print('Деление на ноль недопустимо.')


print(division())


