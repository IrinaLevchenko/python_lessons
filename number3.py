poor_workers = []
summary_income = 0
number_of_workers = 0

with open('file_task_3.txt', 'r') as f:
    for line in f:
        if int((line.split(':'))[1]) <= 20000:
            poor_workers.append((line.split(':'))[0])
        summary_income += int((line.split(':'))[1])
        number_of_workers += 1
    average_income = summary_income / number_of_workers

print(f"Доход ниже 20 000руб у сотрудников: {', '.join(poor_workers)}")
print(f"Средний доход сотрудника фирмы: {average_income}")





