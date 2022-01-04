from itertools import count

with open('file for number2 task.txt', 'r') as f:
    lines = 0
    for line in f:
        lines += line.count('\n')
        print(f'Количество букв в строке  {lines}: {len(line)}')
print(f'Всего строк: {lines}')

