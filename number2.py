# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class OwnError(Exception):
    def __init__(self, text):
        self.text = text


try:
    divident = int(input('Введите числитель: '))
    divider = int(input('Введите знаменатель: '))
    if divider == 0:
        raise OwnError('Делить на ноль нельзя!')
except OwnError as err:
    print(err)
except ValueError:
    print('Вводите только числа!')
else:
    print(f'Результат: {divident / divider}')
