# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

user_text = input('Введите пожелание на Новый год: ').split()
for ind, el in enumerate(user_text, 1):
    print(ind, el[:10])

