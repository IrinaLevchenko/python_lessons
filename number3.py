class NotDigitError(Exception):
    def __init__(self, text):
        self.text = text


list = []
while True:
    try:
        user_input = input("Введите число, для выхода введите 'stop': ").lower()
        # quit = input('Для выхода введите stop, для продолжения нажмите Enter: ')
        if user_input == 'stop':
            print(f'Список введённых чисел: {list}')
            break
        elif user_input.isdigit():
            list.append(int(user_input))
            print(list)
        elif not user_input.isdigit():
            raise NotDigitError("Вводить можно только числа!")
    except NotDigitError as err:
        print(err)



