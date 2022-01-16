# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

#моё решение:
with open('file_task_5.txt', 'w', encoding='utf-8') as f:
    f.write('1 2 3 10 7.6')

with open('file_task_5.txt', 'r') as f:
    print(f'Сумма чисел: {sum(map(float, f.read().split()))}')

# решение преподавателя:
# from random import randint
# with open('5.txt', mode='w+', encoding='utf-8') as f:
#     f.write(" ".join([str(randint(1, 1000)) for _ in range(100000)]))
#     f.seek(0)
#     print(sum(map(int, f.readline().split())))
