# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

# моё решение (длинное и сложное):
# grades_list = [10, 9, 9, 8, 7, 6]
# user_grade = int(input('Введите одну оценку (000 - выход): '))
# while user_grade != 000:
#     for el in range(len(grades_list)):
#         if grades_list[el] == user_grade:
#             c = grades_list.count(el)
#             grades_list.insert(el + c, user_grade)
#             break
#         elif grades_list[-1] > user_grade:
#             grades_list.append(user_grade)
#             break
#         elif grades_list[0] < user_grade:
#             grades_list.insert(0, user_grade)
#     print(grades_list)
#     user_grade = int(input('Введите одну оценку (000 - выход): '))

# решение от преподавателя:
grades_list = [10, 9, 9, 8, 7, 6]
user_grade = int(input('Введите одну оценку для составления рейтинга: '))

i = 0
for n in grades_list:
    if user_grade <= n:
        i += 1
    elif user_grade > n:
        break
grades_list.insert(i, float(user_grade))
print(grades_list)







