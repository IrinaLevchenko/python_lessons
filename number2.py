class OwnError(Exception):
    def __init__(self, text):
        self.text = text


try:
    num_1 = int(input('Введите числитель: '))
    num_2 = int(input('Введите знаменатель: '))
    if num_2 == 0:
        raise OwnError('Делить на ноль нельзя!')
except OwnError as err:
    print(err)
except ValueError:
    print('Вводите только числа!')
else:
    print(num_1 / num_2)
