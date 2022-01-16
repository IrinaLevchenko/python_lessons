# Создать текстовый файл (не программно),
# сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.

from itertools import count
with open('file_task_2.txt', 'r', encoding='utf-8') as f:
    ny_wishes = [f'{line}. {" ".join(count.split())} -- {len(count.split())} слов(а) ' for line, count in enumerate(f, 1)]
    print(*ny_wishes, f'Всего строк: {len(ny_wishes)}', sep='\n')



