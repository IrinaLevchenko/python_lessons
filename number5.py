grades_list = [10, 9, 9, 8, 7, 6]
user_grade = int(input('Введите одну оценку (000 - выход): '))
while user_grade != 000:
    for el in range(len(grades_list)):
        if grades_list[el] == user_grade:
            c = grades_list.count(el)
            grades_list.insert(el + c, user_grade)
            break
        elif grades_list[-1] > user_grade:
            grades_list.append(user_grade)
            break
        elif grades_list[0] < user_grade:
            grades_list.insert(0, user_grade)
    print(grades_list)
    user_grade = int(input('Введите одну оценку (000 - выход): '))








