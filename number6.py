subjects = {}

with open('file_task_6.txt', 'r') as f:
    for line in f:
        data = line.replace('(', ' ').split()
        subjects[data[0][:-1]] = sum(int(i) for i in data if i.isdigit())

print(subjects)
