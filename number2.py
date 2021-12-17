user_seconds = input('Введите время в секундах:')
user_seconds = int(user_seconds)

hour = user_seconds // 3600
seconds = user_seconds % 3600
minutes = seconds // 60
seconds_final = seconds % 60


print(f'''Время {hour}:{minutes}:{seconds_final}''')
