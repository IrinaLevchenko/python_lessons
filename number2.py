user_seconds = int(input('Введите время в секундах:'))

hour = user_seconds // 3600
seconds = user_seconds % 3600
minutes = seconds // 60
seconds_final = seconds % 60

print(f'''Время {hour}:{minutes}:{seconds_final}''')
# TODO: разобраться как выводить нули 02:01:01
