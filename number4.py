user_text = input('Введите пожелание на Новый год.')
user_text_list = user_text.split( )

for ind, el in enumerate(user_text_list, 1):
    if len(el) > 10:
        print(ind, el[:10])
    else:
        print(ind, el)
