from itertools import count


with open('file_task_2.txt', 'r') as f:
    lines = 0
    for line in f:
        lines += line.count('\n')
        print(f'Количество букв в строке  {lines}: {len(line)}')

print(f'Всего строк: {lines}')

