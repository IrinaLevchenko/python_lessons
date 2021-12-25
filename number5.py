def my_sum():
    sum_res = 0
    exit = False
    while not exit:
        numbers = input('Введите числа (для завершения программы введите 000): ').split()
        res = 0
        for el in range(len(numbers)):
            if numbers[el] == '000':
                exit = True
                break
            else:
                res = res + int(numbers[el])
        sum_res += res
        print(f'Сумма последних введённых чисел: {sum_res}')
    print(f'Сумма всех введённых чисел: {sum_res}')


my_sum()
