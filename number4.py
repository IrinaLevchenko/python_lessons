rus_num = ['Один', 'Два', 'Три', 'Четыре']

with open('file_task_4.txt', 'r') as f:
    numbers = [int((line[-2])) for line in f]
    content = [rus_num[int(n) - 1] + ' - ' + str(n) for n in numbers]
    new_file_content = '\n'.join(content)

with open('new_file_task_4.txt', 'w') as f2:
    f2.write(new_file_content)

print(f'В новый файл записана информация:\n{new_file_content}')