with open('file_task_1.txt', 'w') as f:
    first_str = input('Введите тескт: ')
    second_str = input('Ещё введите текст: ')
    third_str = ' '
    f.writelines(f'{first_str}\n{second_str}\n{third_str}')
