# Реализовать функцию, принимающую два числа и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division(var_1, var_2):
    try:
        var_1, var_2 = int(var_1), int(var_2)
        result = var_1 / var_2
    except ValueError:
        return 'Ошибка ввода данных!'
    except ZeroDivisionError:
        return 'Деление на ноль недопустимо.'
    return round(result, 4)


print(division(input('Введите числитель:'), input('Введите знаменатель:')))
