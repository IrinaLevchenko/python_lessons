# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

# моё решение:
# rus_num = ['Один', 'Два', 'Три', 'Четыре']
#
# with open('file_task_4.txt', 'r', encoding='utf-8') as f:
#     numbers = [int((line[-2])) for line in f]
#     content = [rus_num[int(n) - 1] + ' - ' + str(n) for n in numbers]
#     new_file_content = '\n'.join(content)
#
# with open('new_file_task_4.txt', 'w', encoding='utf-8') as f2:
#     f2.write(new_file_content)
#
# print(f'В новый файл записана информация:\n{new_file_content}')

# решение преподавателя первое:
rus_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре" }
with open('new_file_task_4.txt', 'w', encoding='utf-8') as nf:
    with open('file_task_4.txt', 'r', encoding='utf-8') as mf:
        nf.write(str([line.replace(line.split()[0], rus_dict.get(line.split()[0])) for line in mf]))

