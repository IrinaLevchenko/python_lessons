with open('file_task_5.txt', 'w') as f:
    f.writelines('1 2 3 10 7.6')

with open('file_task_5.txt', 'r') as f:
    sum = 0
    for item in f.read().split():
        sum += float(item)

print(f'Сумма чисел: {sum}')
