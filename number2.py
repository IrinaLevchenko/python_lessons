user_seconds = int(input('Введите время в секундах:'))

hours = user_seconds // 3600
seconds = user_seconds % 3600
minutes = seconds // 60
seconds_final= seconds % 60

print(f"{hours:02}:{minutes:02}:{seconds_final:02}")

