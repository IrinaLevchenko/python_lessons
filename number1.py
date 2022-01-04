with open('i_created_a_file.txt', 'w') as f:
    first_str = input('Введите тескт: ')
    second_str = input('Ещё введите текст: ')
    third_str = ' '
    f.writelines([first_str, '\n', second_str, '\n', third_str])
